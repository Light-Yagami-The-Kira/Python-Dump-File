import datetime
import random

def get_busy_room():
    A = open("log.csv", 'r')
    if A.read() == '':
        return []
    a = A.read()[:-1].split('\n')

    a = [k.split(',')[0] for k in a]
    A.close()
    return a

def get_busy_guest_id():
    A = open("log.csv", 'r')
    if A.read() == '':
        return []
    a = A.read()[:-1].split('\n')

    a = [k.split(',')[2] for k in a]
    A.close()
    return a

def check_in():
    guest_name = input("Enter name of the guest: ")
    while True:
        room = input("Select a room from 1 to 1000: ")
        if room.isdigit() and int(room) in range(1,1001):
            break
        else:
            print("Error try again.")
    check_in_date = datetime.datetime.now().strftime("%Y-%m-%d")
    check_out_date = input("Enter checkout date in YYYY-MM-DD or leave blank for no checkout.")

    Q = open('log.csv', 'a')
    Q.write(f'{room},{guest_name},{gen_guest_id()},{check_in_date},{check_out_date}')
    Q.close

def check_out():
    id = input("Enter ID: ")

    if id not in get_busy_guest_id():
        return print('No such id is currently occupying a room.')
    else:
        F = open('log.csv', 'r')
        log = F.read().split('\n')[:-1]
        log = [item.split(',') for item in log]

        for item in log:
            if item[2] == id:
                log.remove(item)

        new_log = [','.join(k) for k in log]
        new_log = '\n'.join(new_log)

        L = open('log.csv', 'w')
        L.write(new_log)
        L.close()
        F.close()


def clearHotel():
    A = open('log.csv', 'w')
    C = open('busy_guest_id.txt', 'w')

    A.write('')
    C.write('')

    print("Cleared.")


def display_log():
    Q = open("log.csv", 'r')
    print(Q.read())
    Q.close()


def check_status():
    F = open('log.csv', 'r')
    log = F.read()
    if log != "":
        log = log.split('\n')
        log = [item.split(',') for item in log]
        for item in log:
            if item[-1] < datetime.datetime.now().strftime("%Y-%m-%d") and item[-1] != '':
                print("[There are some guests whose room service has expired, please check out them.]")
                F.close()
                return
    F.close()

def display_guests_to_be_checked_out():
    F = open('log.csv', 'r')
    log = F.read().split('\n')
    log = [item.split(',') for item in log]
    for item in log:
        if item[-1] < datetime.datetime.now().strftime("%Y-%m-%d") and item[-1] != '':
            print(','.join(item))            
    F.close()
    return

def gen_guest_id():
    while True:
        x = str(random.randint(100000,999999))
        if x not in get_busy_guest_id():
            return x


def wrong_input():
    print("Wrong Input, Try Again")

while True:
    print("\n\n")

    check_status()
    print("1. Check in a guest")
    print("2. Check out a guest")
    print("3. Display The Whole Log")
    print("4. Clear Hotel")
    print("5. Display Record Of guests whose Hotel Room Service Validity has ended and have to be checked out.")
    print("6. Exit")

    UI = input("Enter your menu: ")
    
    switch = {
        '1' : check_in,
        '2' : check_out,
        '3' : display_log,
        '4' : clearHotel,
        '5' : display_guests_to_be_checked_out,
    }

    if UI == '6':
        break
    elif UI in switch:
        switch[UI]()
    else:
        print("Wrong Input.")
