if __name__ == '__main__':
    s = input()
    n = False
    for i in s:
        if i.isalnum():
            n = True
            print(n)
            break
    if n != True:
        print(n)
    n = False
    for i in s:
        if i.isalpha():
            n = True
            print(n)
            break
    if n != True:
        print(n)
    n = False
    for i in s:
        if i.isdigit():
            n = True
            print(n)
            break
    if n != True:
        print(n)
    n = False
    for i in s:
        if i.islower():
            n = True
            print(n)
            break
    if n != True:
        print(n)
    n = False
    for i in s:
        if i.isupper():
            n = True
            print(n)
            break
    if n != True:
        print(n)
