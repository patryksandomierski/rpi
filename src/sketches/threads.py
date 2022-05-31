import threading

a = 1
lcd = "hi"


def thread_1():
    global a
    print(a)
    a += 1


def thread_2():
    global a
    print(a)


first_thread = threading.Thread(target = thread_1)
second_thread = threading.Thread(target = thread_2)


def main():
    print("hello")
    first_thread.start()
    second_thread.start()


if __name__ == '__main__':
    main()
