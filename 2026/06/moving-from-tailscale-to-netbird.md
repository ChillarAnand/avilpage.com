<!--
.. title: Moving from TailScale to NetBird
.. slug: moving-from-tailscale-to-netbird
.. date: 2026-06-27 11:13:54 UTC+05:30
.. tags: networking, self-hosting
.. category: networking
.. link: 
.. description: Why I moved from TailScale to NetBird for self-hosting my VPN solution.
.. type: text
-->

### Why?

I have been using [TailScale](/tags/tailscale.html) from 4 years. 
Recently, I wanted to self-host HeadScale(open source TailScale server) on my own server. 

During self hosting, I realised that HeadScale is not a drop-in replacement for TailScale.

App connectors are main reason I was using TailScale and HeadScale [doesn't support app-connectors](https://github.com/juanfont/headscale/issues/1651).

### NetBird

[NetBird](https://github.com/netbirdio/netbird) is completely open source and has a self-hosted server. 
Setting up split DNS tunneling and routing is easier with NetBird.

It has a clean web UI to manage network/policies which is way better than TailScale's web UI.

It also has a cool control center to visualize the network and connected devices.

![netbird](/images/netbird.png)

It still doesn't have support for light theme yet. 
Since I am not accustomed to dark theme, I am using [Stylus](https://github.com/openstyles/stylus) extension
and changing the theme to light theme.

```css
html { filter: invert(1) hue-rotate(180deg); background: #fff; }
img, svg, video, canvas, [style*="background-image"] { filter: invert(1) hue-rotate(180deg); }
```

### Conclusion

NetBird can be self-hosted in few minutes and migration is much smoother than I expected. 