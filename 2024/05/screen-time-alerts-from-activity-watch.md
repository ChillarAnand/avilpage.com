<!--
.. title: Screen Time Alerts from Activity Watch
.. slug: screen-time-alerts-from-activity-watch
.. date: 2024-05-01 06:59:27 UTC+05:30
.. tags: python, productivity
.. category: programming
.. link: 
.. description: How to show screen time alerts from activity watch data?
.. type: text
-->

### Introduction

![Activity Watch](/images/activity-watch-alerts.png)

Activity Watch[^activity_watch] is a cross-platform open-source time-tracking tool that helps us to track time spent on applications and websites.

At the moment, Activity Watch doesn't have any feature to show screen time alerts. In this post, we will see how to show screen time alerts using Activity Watch.


### Python Script

Activity Watch provides an API to interact with the Activity Watch server. We can use the API to get the screen time data and show alerts.

```python
import json
import os
from datetime import datetime

import requests


def get_nonafk_events(timeperiods=None):
    headers = {"Content-type": "application/json", "charset": "utf-8"}
    query = """afk_events = query_bucket(find_bucket('aw-watcher-afk_'));
window_events = query_bucket(find_bucket('aw-watcher-window_'));
window_events = filter_period_intersect(window_events, filter_keyvals(afk_events, 'status', ['not-afk']));
RETURN = merge_events_by_keys(window_events, ['app', 'title']);""".split("\n")
    data = {
        "timeperiods": timeperiods,
        "query": query,
    }
    r = requests.post(
        "http://localhost:5600/api/0/query/",
        data=bytes(json.dumps(data), "utf-8"),
        headers=headers,
        params={},
    )
    return json.loads(r.text)[0]


def main():
    now = datetime.now()
    timeperiods = [
        "/".join([now.replace(hour=0, minute=0, second=0).isoformat(), now.isoformat()])
    ]
    events = get_nonafk_events(timeperiods)

    total_time_secs = sum([event["duration"] for event in events])
    total_time_mins = total_time_secs / 60
    print(f"Total time: {total_time_mins} seconds")
    hours, minutes = divmod(total_time_mins, 60)
    minutes = round(minutes)
    print(f"Screen Time: {hours} hours {minutes} minutes")

    # show mac notification
    os.system(f"osascript -e 'display notification \"{hours} hours {minutes} minutes\" with title \"Screen TIme\"'")


if __name__ == "__main__":
    main()
```

This script[^github] will show the screen time alerts using the Activity Watch API. We can run this script using the below command.

```bash
$ python screen_time_alerts.py
```

![Screen Time Alerts](/images/activity-watch-alerts2.png)

We can set up a cron job to run this script every hour to show screen time alerts.

```bash
$ crontab -e
0 * * * * python screen_time_alerts.py
```

We can also modify the script to show alerts only when the screen time exceeds a certain limit.

### Conclusion

Since Actvity Watch is open-source and provides an API, we can extend its functionality to show screen time alerts. We can also use the API to create custom reports and dashboards.


[^activity_watch]: [Activity Watch](https://activitywatch.net/)
[^github]: [Screen Time Alerts Script](https://github.com/ChillarAnand/avilpage.com/blob/master/scripts/activity_watch_alerts.py)
