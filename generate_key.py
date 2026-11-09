import random

def generate_key(decnum = '') -> str:
    if len(decnum) != 3 or decnum.isdigit() == False or decnum[0] == '0':
        return ''
    else:
        key = ''
        letters = [chr(ord('A') + i) for i in range(26)] + [str(j) for j in range(10)]
        for i in range(5):
            key += random.choice(letters)

        for i in range(4, 1, -1):
            candidate = list(key[-i-1:-1])
            for char in enumerate(candidate):
                n, s = char
                if s.isdigit():
                    candidate[n] = str((int(s) + int(decnum[4 - i]) * (-1) ** i) % 10)
                else:
                    candidate[n] = chr((ord(s) - ord('A') + int(decnum[4 - i]) * (-1) ** i) % 26 + ord('A'))
            key += '-' + ''.join(candidate)
        return key

if __name__ == '__main__':
    print(generate_key('123'))
 