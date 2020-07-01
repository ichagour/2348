
portion = input().split()
name = portion[0]
while name != '-1':
    try:
        age = int(portion[1]) + 1
    except Exception as ex:
        age = 0

    print('{} {}'.format(name, age))
    portion = input().split()
    name = portion[0]