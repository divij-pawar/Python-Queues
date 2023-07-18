import sysv_ipc
import time
import os

KEY = int(input("Enter Queue key to monitor: "))
mq = sysv_ipc.MessageQueue(KEY, sysv_ipc.IPC_CREAT)

while True:
    try:
        # Clear the console output
        os.system('clear')  # For Linux/Mac
        # os.system('cls')  # For Windows
        print(f"Queue key {KEY}")
        # Get the total count of messages in the queue
        total_messages = mq.current_messages
        print(f"Queue has {total_messages} msgs")
        time.sleep(1)

    except sysv_ipc.ExistentialError:
        mq = sysv_ipc.MessageQueue(KEY, sysv_ipc.IPC_CREAT)
        continue
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        break
