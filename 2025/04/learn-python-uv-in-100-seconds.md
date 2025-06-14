<!--
.. title: Python UV in 100 seconds
.. slug: learn-python-uv-in-100-seconds
.. date: 2025-04-30 23:16:24 UTC+05:30
.. tags: python, uv
.. category: programming
.. link: 
.. description: 
.. type: text
-->

UV is a fast Python package manager that replaces tools like pip, pyenv, virtualenv, etc.

### Install uv

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installing Python

```bash
uv python list

uv python install 3.13
```

This makes it easy to install and manage multiple versions of Python on your system without needing of `pyenv`.


### Using UV with existing requirements.txt

```bash
uv venv --seed -p 3.13

source .venv/bin/activate

uv pip install -r requirements.txt
```

This is way faster than using any other tool to create virtual environments.

### Managing virtual environments

```bash
uv init -p 3.13 --name demo

uv add pandas
```

This creates a new virtual environment named `demo` with Python 3.13 and adds the `pandas` package to it.

### Runs scripts with inline dependencies

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///
import requests

print(requests.get("https://avilpage.com"))
```

```bash
uv run script.py
```

### uvx 

Similar to `pipx`, it can install and run Python applications in isolated environments.

```bash
uv tool install glances

uv tool run glances

# shortcut
uvx glances
```

### Conclusion

UV speeds up Python development by providing a fast package manager, virtual environment management, and inline dependency management. It is a great alternative to traditional tools like pip, pyenv, and virtualenv.