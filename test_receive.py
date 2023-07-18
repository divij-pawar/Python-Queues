import sysv_ipc

KEY = int(input("Enter Queue key to receive messages from: "))
mq = sysv_ipc.MessageQueue(KEY, sysv_ipc.IPC_CREAT)

while True:
    try:
        s,_ = mq.receive(block=False, type=1)
        s = s.decode()
        print("Received "+s)
    except sysv_ipc.BusyError:
        # No message of the specified type is available, wait or retry
        continue
    except KeyboardInterrupt:
        # Handle Ctrl+C to exit the loop gracefully
        break