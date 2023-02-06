

from audioop import add
from cgi import print_arguments


def show_balance(balance):
    print("Current balance $: ", float(balance))


def deposite(balance):
    amount = input ("Enter amount to deposite: ")
    balance = 0
    balance = balance + float(amount)
    print("Current balance $:", balance)
    return(balance)
   
    



def withdraw(balance):
    amount = input ("Enter amount to withdraw: ")
    balance = 100000
    balance = balance - float(amount)
    print("Current balance $:", balance)
    return(balance)
   


def logout(name):
    print("Goodbye ", name + "!")
