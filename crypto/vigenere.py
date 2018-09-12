from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    NewList = []
    rot = list(rot)
    y = 0
    for x in range(len(text)):
        if y > (len(rot) - 1):
            y = 0
        #print(y)
        if text[x].isalpha():
            NewList.append(rotate_character(text[x], alphabet_position(rot[y])))
            y += 1
        else:
            NewList.append(text[x])
    return ''.join(NewList)

def main():
    text = str(input('Type a Message:\n'))
    rot = str(input('Encryption key:\n'))
    print(encrypt(text,rot))

if __name__ == "__main__":
    main()    