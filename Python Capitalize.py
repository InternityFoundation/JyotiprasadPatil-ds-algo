def solve(s):
    n = len(s)
    lst = list(s)
    lst[0] = lst[0].upper()
    for i in range(n):
        if lst[i] == " ":
            lst[i+1] = lst[i+1].upper()
    str1 = ""
    return str1.join(lst)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()