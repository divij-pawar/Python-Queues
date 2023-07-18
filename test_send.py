import sysv_ipc
import time
import sys
KEY = int(input("Enter Queue key to send message to: "))
# Create new queue if queue doesnt exist
# Else use existing queue
mq = sysv_ipc.MessageQueue(KEY, sysv_ipc.IPC_CREAT)
msg = input("Enter Message to be sent: ")

while True:
    try:
        print("Sent "+msg)
        mq.send(msg+" a Type 1 message", type=1)
        time.sleep(1)

    except sysv_ipc.ExistentialError:
        mq = sysv_ipc.MessageQueue(KEY, sysv_ipc.IPC_CREAT)
        continue
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        break