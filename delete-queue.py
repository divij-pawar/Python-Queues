import sysv_ipc

KEY = 100
mq = sysv_ipc.MessageQueue(KEY, sysv_ipc.IPC_CREAT)

mq.remove()
print("Emptied queue with key", KEY)
#########