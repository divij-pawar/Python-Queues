import sysv_ipc

KEY = int(input("Enter Queue key delete: "))
mq = sysv_ipc.MessageQueue(KEY, sysv_ipc.IPC_CREAT)

mq.remove()
print("Emptied queue with key", KEY)
#########