from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    NewList = []
    for x in text:
        #print(x)
        NewList.append(rotate_character(x,rot))
    return ''.join(NewList)

#print(encrypt('Hello, World!',5))

def main():
    text = str(input('Type a Message:\n'))
    rot = int(input('Rotate by:\n'))
    print(encrypt(text,rot))

if __name__ == "__main__":
    main()