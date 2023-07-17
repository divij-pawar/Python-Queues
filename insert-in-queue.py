
import pandas as pd
import time
import os
import sysv_ipc
import threading
import json
from dotenv import load_dotenv
load_dotenv()


class ImportTrade():
    def __init__(self):
        self.SLEEP_TIME = int(os.getenv('sleep_time'))
        databases =  os.getenv('databases').split(',')
        for database in databases:
            # Start the notification listener thread
            notification_thread = threading.Thread(target=self.TradeBookExtraction, args=(f'{os.getcwd()}/tradefiles/{database}.csv', database))
            notification_thread.start()
            # Join the notification listener thread with the main thread (optional)
            #notification_thread.join()
     
    def TradeBookExtraction(self,file, database) -> None:
        try:
            data = pd.read_csv(file, index_col='inID')
            data.columns = data.columns.str.strip().str.replace(' ', '').str.lower()
            data = data.fillna('')
            time.sleep(self.SLEEP_TIME)
            self.TradeBook(data, database)
        except Exception as e:
            print(e)

    def df_to_queue(self,df, database) -> None:
        mq_key = 100
        mq = sysv_ipc.MessageQueue(mq_key, sysv_ipc.IPC_CREAT)

        try:
            for _, row in df.iterrows():  
                json_string =row.to_json()
                mq.send(json_string, block=False, type=1)
                print(f"Writing queue for {database}")
                time.sleep(self.SLEEP_TIME)

        except Exception as e:
            print(e)

if __name__ == '__main__':
    ImportTrade() 