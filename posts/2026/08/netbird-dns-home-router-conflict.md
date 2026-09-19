<!--
.. title: Tracing NetBird split-DNS connectivity issue
.. slug: netbird-dns-home-router-conflict
.. date: 2026-08-05 09:30:00 UTC+05:30
.. tags: netbird, dns, macos, networking, vpn, draft
.. category: 
.. link: 
.. description: How a home router's DHCP-injected DNS search domain silently shadowed NetBird's split-DNS resolver on macOS.
.. type: text
-->

### Context

I run a self-hosted [NetBird](https://netbird.io) mesh VPN for internal access. Except for one user, it worked perfectly for all remote users.

### Symptoms

- `netbird status` showed the client Connected, P2P tunnel established to the peer.
- Internal hostnames (`talos.joinmidi.com`, `*.athenahealth.com`, etc) failed to resolve.
- Worked perfectly on office WiFi. Broke every time on home WiFi.

### Investigation

Since the daemon reported healthy connectivity, the problem had to be DNS, not the tunnel itself. We collected diagnostics from her machine:

```
netbird status --detail >> ns.txt
scutil --dns >> scutil.txt
cat /etc/resolv.conf >> resolv.txt
```

`scutil --dns` was the key file. macOS uses split-DNS: NetBird installs *supplemental resolvers* scoped to specific domains (like `netbird.selfhosted`, `talos.joinmidi.com`) pointing at NetBird's internal DNS server, while the default/catch-all resolver stays on the regular LAN DNS.

On her machine, the default resolver was `192.168.113.1` (her home router) — and that router had also pushed a DHCP search domain matching NetBird's own domain, `netbird.selfhosted`. That collision meant macOS's resolver scoping picked the router's DNS as authoritative for those internal hostnames instead of NetBird's resolver. The router had no idea about those internal hosts, so lookups failed.

At the office, the network's DHCP didn't push that search domain, so no collision, no failure.

### Why only her, and not the hundreds of other remote users

DHCP option 119 (domain search list) is optional — most consumer routers don't set it at all. Some ISP-supplied gateways do, either as a default or as part of DNS-forcing/parental-control features. Only her home router happened to inject a search domain that collided with NetBird's own `.selfhosted` suffix. Everyone else's routers simply didn't send that option, so there was nothing to collide with.

### Why System Settings → WiFi → DNS couldn't fix it

The GUI only lets you *add* DNS servers on top of what DHCP provides — it doesn't let you remove or override the DHCP-injected search domain and its priority. The entry from the router shows up greyed out and isn't deletable from there.

### Fix

Couldn't touch the router (personal home network, not IT-managed). Fixed it locally by forcing macOS to override the search domain and DNS resolver order for that network service, independent of DHCP:

```
networksetup -setsearchdomains Wi-Fi <correct-domain>
networksetup -setdnsservers Wi-Fi <netbird-dns-ip> <fallback-dns-ip>
```

This pins the resolver config so the router's DHCP-supplied search domain no longer wins the scoping fight.

### Takeaway

If a VPN with split-DNS works on one network and not another, don't just check the tunnel — check `scutil --dns` for resolver order and search domain collisions. DHCP can silently inject config that shadows your VPN's DNS scope, and it'll only bite on networks whose router happens to send that option.
