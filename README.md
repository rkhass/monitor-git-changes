# monitor-git-changes
Tool to monitor uncommitted changes or unfinished work in repo to keep it always tidy.

## How to use?
1. Install packages
```shell
pip instal -r requirements.txt
```
2. Set up the telegram bot
3. List repositories in `.env` file
```text
PATH_TO_REPO = PathToRepo1, PathToRepo2 
```
4. Customize your cron file (`cron.file`). Example: 
```bash
# path to the Python:
PY_ENV = py38/bin/python3.8
# Path to the main monitor script:
MONITOR_SCRIPT = Users/username/github/monitor-git-changes/main.py

# 9,13,17 - means running 3 times at 9, 13, 17 o'clock
0 9,13,17 * * * $PY_ENV $MONITOR_SCRIPT
```
5. Enjoy!