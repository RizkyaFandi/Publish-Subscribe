import threading

user = [[2, 3, 4], [3, 4], [1, 2, 4], [1, 2]]
userMessage = [["available"], ["available"], ["available"], ["available"]]


def subscribe(userid, target):
    if target in user[userid-1]:
        print("You already subscribe to user " + str(target) + "\n\n")
    else:
        user[userid-1].append(target)

    print("You have subscribe to user " + str(target))


def appending(target, message):
    userMessage[target-1].append(message)


def publish(userid, message):
    for target in user[userid-1]:
        t = threading.Thread(target=appending, args=(target, message))
        t.start()

    print("Message sent to your subscribers!\n\n")


def menuapp(login):
    while True:
        print("------ You have login as user " + str(login) + " ------")
        print("\nWhat will you do?\n\t1.publish\n\t2.subscribe\n\t3.view message\n\t4.log out\n\t5.exit")
        decision = int(input())
        if decision == 1:
            print("Write your message here:")
            message = input()
            publish(login, message)
        elif decision == 2:
            print("Which user you want to subscribe?")
            identity = int(input())
            subscribe(login, identity)
        elif decision == 3:
            for m in userMessage[login-1]:
                print(m)
        elif decision == 4:
            loginapp()
        else:
            exit()


def loginapp():
    print("select account\n\t1.user1\n\t2.user2\n\t3.user3\n\t4.user4")
    login = int(input())
    menuapp(login)


loginapp()
