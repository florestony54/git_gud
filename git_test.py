def main():
    with open('test.txt', 'r') as file:
        data = file.readlines()
    print(f'Hello, {data[0]}')

def uselessFunc():
    if 1 + 1 == 2:
        return
    return

main()