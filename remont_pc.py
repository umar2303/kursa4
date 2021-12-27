import sqlite3

users = {'client': 'pa$$w0rd123', 'repair': 'pa$$w0rd123', 'supplier': '$upplier123', 'worker': 'worker123'}
def login():
    global users
    acc_type = input('To start the program, please enter the account type: ').lower()
    if acc_type == 'client':
        password = input('Enter the password: ')
        while True:
            if password == users[acc_type]:
                print('Authorization has been successfully completed!')
                print('Hello, dear customer!')
                client_menu()
                break
            
            password = input('Invalid password, please repeat: ')
                
    else:
        print("Sorry, but we didn't find this type of account, please repeat.")
        login()
  
def client_menu():
    menu_page = int(input('Please enter the menu number to work with the program: \n 1. Show all services, \n if you are done, then enter 6: '))
    while True:
        if menu_page == 1:
            print('2. Give it for repair \n 3. Replacement of the component \n 4. Service \n 5. Check status \n 6. Exit')
            return client_menu()
            break
            
        elif menu_page == 2:
            clnt_menu_2 = int(input('Please select the category of technic for repair: \n 1) Personal Computer \n 2) Laptop \n 3) Tablet \n '))
            if clnt_menu_2 == 1:
                remont_price(1.5)
                break
        elif menu_page == 3:
            pass
        elif menu_page == 4:
            pass
        elif menu_page == 5:
            pass
        elif menu_page == 6:
            print('You are out of the menu.')
            break
        menu_page = int(input('Invalid menu number, please repeat: '))

def remont_price(kf):
    rep_type = int(input(f'What repairs are required: \n 1) Repair the display - {kf * 50}$ \n 2)Repair the keyboard - {kf * 25}$ \n 3)Repair the insides (Motherboard, processor, etc.)  - {kf * 40}$ '))
    return client_menu()
login()