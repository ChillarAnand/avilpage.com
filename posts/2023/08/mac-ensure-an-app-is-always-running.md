<!--
.. title: Periodically Launch an App in Background
.. slug: periodically-launch-app-background
.. date: 2023-08-23 19:03:49 UTC+05:30
.. tags: macbook, command-line, automation
.. category: 
.. link: 
.. description: How to ensure an app runs always in background. Even if it is closed, it should be launched periodically.
.. type: text
-->

I recently started using Outlook app on my Mac. If the app is closed, it won't send any notifications. When I accidentally close the app, until I re-open it, I won't get any notifications.

I want to ensure that it starts periodically so that I don't miss any notifications for meetings.

After trying out various methods, I ended up using `open` command with `cron` to launch the app every 15 minutes.

```bash
$ crontab -e
```

```bash
*/15 * * * * /usr/bin/open -a "Microsoft Outlook"
```

This will launch the app every 15 minutes. This is inconvenient as it will bring Outlook to foreground every 15 minutes. 

To avoid this, I passed `-g` option to run it in background.

```bash
$ crontab -e
```

```bash
*/15 * * * * /usr/bin/open -g -a "Microsoft Outlook"
```

This silently launches the app in background without causing any disturbance. Since the app is running the background, it will send notifications for any meetings.

This will ensure that I don't miss any meetings, even if I close outlook accidentally.
