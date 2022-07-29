# monitor-git-changes
Tool to monitor uncommitted changes or unfinished work in repo to keep it always tidy.

## How to use?
1. Install packages
```shell
pip instal -r requirements.txt
```
2. Set up the telegram bot
   1. Generate a token https://t.me/BotFather (`TELEGRAM_TOKEN`)
   2. Add this bot to a chat you want and open 
   https://api.telegram.org/bot<YourBOTToken>/getUpdates, 
   where you can find chat id (`TELEGRAM_CHAT_ID`)
   3. Put `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` numbers to `.env` file 
3. List repositories and write location in `.env` file
```text
LOCATION_NAME = LocalMacBook
REPOS_TO_MONITOR = PathToRepo1, PathToRepo2 
```
4. Customize your cron file (`cron.file`). Example: 
```bash
# path to the Python:
PY_ENV = /home/username/py38/bin/python3.8
# Path to the monitor repo:
MONITOR_REPO = /home/username/github/monitor-git-changes

# 9,13,17 - means running 3 times at 9, 13, 17 o'clock
0 9,13,17 * * * cd $MONITOR_REPO && $PY_ENV main.py >> ~/log_monitor 2>&1
```
5. Copy cron file and past to `crontab -e`
6. Enjoy!
