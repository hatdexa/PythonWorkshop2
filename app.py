

from banking_pkg import account


def atm_menu(name):   
    print("str")
print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input ("Enter PIN: ")
balance = '0'
print(name, "has been registered with a starting balance of $" + balance)


while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name:")
    pin_to_validate = input("Enter PIN: ")

    if name == name_to_validate and pin_to_validate:
        print("Login successful!")
        break
    if name != name_to_validate and pin != pin_to_validate:
        continue
    print("Invalid credentials!")



while True:
    print("          === Automated Teller Machine ===          ")
    print("User:" + name)
    
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

    option = input("Choose an option: ")
    
    if option =="1":
        account.show_balance(balance)
    
    elif option =="2":
        account.deposite(balance)
        
    
    elif option =="3":
        account.withdraw(balance)

    elif option =="4":
        account.logout(name)

        break
        
        
 