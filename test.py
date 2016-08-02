Traceback (most recent call last):
  File "/usr/lib/python3.5/threading.py", line 914, in _bootstrap_inner
    self.run()
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/watchdog/observers/api.py", line 199, in run
    self.dispatch_events(self.event_queue, self.timeout)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/watchdog/observers/api.py", line 368, in dispatch_events
    handler.dispatch(event)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/watchdog/events.py", line 322, in dispatch
    self.on_any_event(event)
  File "/home/chillaranand/sandbox/getnikola/nikola/nikola/plugins/command/auto/__init__.py", line 433, in on_any_event
    self.function(event)
  File "/home/chillaranand/sandbox/getnikola/nikola/nikola/plugins/command/auto/__init__.py", line 293, in do_refresh
    refresh_signal.send(path=p)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/blinker/base.py", line 267, in send
    for receiver in self.receivers_for(sender)]
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/blinker/base.py", line 267, in <listcomp>
    for receiver in self.receivers_for(sender)]
  File "/home/chillaranand/sandbox/getnikola/nikola/nikola/plugins/command/auto/__init__.py", line 405, in notify
    self.send(response, response.is_binary)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/ws4py/websocket.py", line 301, in send
    self._write(data)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/ws4py/websocket.py", line 279, in _write
    self.sock.sendall(b)
OSError: [Errno 9] Bad file descriptor



Traceback (most recent call last):
  File "/usr/lib/python3.5/threading.py", line 914, in _bootstrap_inner
    self.run()
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/watchdog/observers/api.py", line 199, in run
    self.dispatch_events(self.event_queue, self.timeout)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/watchdog/observers/api.py", line 368, in dispatch_events
    handler.dispatch(event)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/watchdog/events.py", line 322, in dispatch
    self.on_any_event(event)
  File "/home/chillaranand/sandbox/getnikola/nikola/nikola/plugins/command/auto/__init__.py", line 433, in on_any_event
    self.function(event)
  File "/home/chillaranand/sandbox/getnikola/nikola/nikola/plugins/command/auto/__init__.py", line 293, in do_refresh
    refresh_signal.send(path=p)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/blinker/base.py", line 267, in send
    for receiver in self.receivers_for(sender)]
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/blinker/base.py", line 267, in <listcomp>
    for receiver in self.receivers_for(sender)]
  File "/home/chillaranand/sandbox/getnikola/nikola/nikola/plugins/command/auto/__init__.py", line 405, in notify
    self.send(response, response.is_binary)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/ws4py/websocket.py", line 301, in send
    self._write(data)
  File "/home/chillaranand/.virtualenvs/exp/lib/python3.5/site-packages/ws4py/websocket.py", line 277, in _write
    raise RuntimeError("Cannot send on a terminated websocket")
RuntimeError: Cannot send on a terminated websocket
