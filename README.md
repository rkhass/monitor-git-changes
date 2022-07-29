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
5. Copy cron file and past to `crontab -e`
6. Enjoy!
