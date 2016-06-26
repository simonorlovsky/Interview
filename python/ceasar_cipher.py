def cipher(string, offset):
    cipher = []
    for i in range(len(string)):
        cipher.append(chr((ord(string[i])+offset)))
    return ''.join(cipher)

def main():
    print cipher("hello", 1)

main()
