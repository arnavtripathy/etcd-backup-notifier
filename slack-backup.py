import slack
from datetime import datetime as dt
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import os
# Slack token needs to be present in the .env file. This script should be running as cronjob

env_path= '/home/ubuntu/.env'

try:
        load_dotenv(dotenv_path=env_path)
        run=subprocess.check_output(["bash","/home/ubuntu/etcd-backup-automation/run.sh"])
        date=subprocess.check_output(["date"])
        client=slack.WebClient(token=os.environ['SLACK_TOKEN'])


        if b"ETag" in run:
               
                client.chat_postMessage(channel='#channel-name', text="Backup was a success today "+date.decode("utf-8"))
        else:
                
                client.chat_postMessage(channel='#channel-name', text="Backup was a failure "+date.decode("utf-8"))
except Exception as err:
        print(str(err))
        send_crash_alert()
