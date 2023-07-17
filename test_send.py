import sysv_ipc
import time
import sys
key = 100
# Create new queue if queue doesnt exist
# Else use existing queue
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
msg = input("Enter Message to be sent: ")
print("Sent "+msg)
mq.send(msg+"Type1", type=1)

mq.send(msg+"Type2", type=2)
