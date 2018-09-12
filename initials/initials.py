def get_initials(fullname):
    initials = ""
    for x in range(len(fullname)):
        if x==0:
            initials += str.upper(fullname[x])
        if fullname[x] == " ":
            initials += str.upper(fullname[x+1])
    return initials

def main():
    Name = input("What is your full name?:\n")
    print(get_initials(Name))

if __name__ == '__main__':
    main()