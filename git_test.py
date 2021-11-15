import os

def main():
    greetUser()

def uselessFunc():
    if 1 + 1 == 2:
        return
    return

def greetUser():
    userName = os.getlogin()
    print(f'Hello, {userName}')

main()