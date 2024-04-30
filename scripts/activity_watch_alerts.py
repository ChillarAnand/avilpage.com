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
    os.system(f"osascript -e 'display notification \"{hours} hours {minutes} minutes\" with title \"Screen Time\"'")


if __name__ == "__main__":
    main()
