from os import system, name
from time import sleep

def print_Benin_Flag(h = 6):
    l = int(h * 1.5)

    green = '\u001b[48;2;0;135;81m'
    yellow = '\u001b[48;2;252;209;22m'
    red = '\u001b[48;2;232;17;45m'
    reset = '\u001b[0m'

    for line in range(h):
        if line < h // 2:
            print(f'{green}{'  ' * (l // 3)}{yellow}{'  ' * (l * 2 // 3)}{reset}')
        else: 
            print(f'{green}{'  ' * (l // 3)}{red}{'  ' * (l * 2 // 3)}{reset}')


def pattern(n = 11, m = 9, steps=7):
    color = '\u001b[48;2;0;135;81m'
    reset = '\u001b[0m'
    countpixels = -1

    for i in range(m):
        if i <= m // 2: countpixels += 2
        else: countpixels -= 2
        if steps - countpixels // 2 * 2 >= 0:
            print(f'{'  ' * (m // 2 - countpixels // 2)}', f'{color}{'  ' * countpixels}{reset}{'  ' * (steps - countpixels // 2 * 2)}' * n, sep='', end='')
    
        else:
            print(f'{'  ' * (m // 2 - countpixels // 2)}', f'{color}{'  ' * (countpixels // 2 * 2 + n + steps * (n - 1))}{reset}', sep='', end='')
        print()


def loop_animated(m = 13, step = 2):
    reset = '\u001b[0m'
    
    for c in range(3):
        color = '\u001b[48;2;0;135;81m'

        countpixels = -1
        for i in range(m):
            if i <= m // 2: countpixels += 2
            else: countpixels -= 2
            print(f'{'  ' * (m // 2 - countpixels // 2 + step)}{color}{'  ' * countpixels}{reset}')
        sleep(1)
        print(f'\u001b[{0};{0}H')
        system('clear')
        
        color = '\u001b[48;2;252;209;22m'

        for i in range(m):
            print(f'{'  ' * step}{color}{'  ' * m}{reset}')
        sleep(1)
        print(f'\u001b[{0};{0}H')
        system('clear')        

        color = '\u001b[48;2;232;17;45m'

        countpixels = -1
        for i in range(m):
            countpixels += 2
            print(f'{'  ' * (m // 2 - countpixels // 2 + step)}{color}{'  ' * countpixels}{reset}')    
        sleep(1)
        print(f'\u001b[{0};{0}H')
        system('clear')    


def graphics_group_print():
    red = '\u001b[41m'
    blue = '\u001b[44m'
    white = '\u001b[37m'
    reset = '\u001b[0m'

    with open('sequence.txt') as f:
        nums = [float(x) for x in f]

    group1 = []
    group2 = []

    for n in nums:
        if 0 < n < 5: group1.append(n)
        elif -5 < n < 0: group2.append(n)

    print(f'{red}{' ' * (len(group1) - 6)}{white}{len(group1) / (len(group1) + len(group2)) * 100:.2f}%{reset}')
    print(f'{blue}{' ' * (len(group2) - 6)}{white}{len(group2) / (len(group1) + len(group2)) * 100:.2f}%{reset}')


def function_print(n):
    white = '\u001b[47m'
    black = '\u001b[40m'
    reset = '\u001b[0m'

    result = []

    for y in range(n - 1, -1, -1):
        x = int(y ** 0.5)
        line = (
            f'{white}{"  " * x}'
            f'{black}{"  " if x >= 0 else ""}'
            f'{white}{"  " * (n - x - 1)}{reset}'
        )
        result.append(line)

    print(*result, sep='\n')


# print_Benin_Flag(14)

# pattern(10, 13, 9)

# sleep(4)

# loop_animated(13, 22)

# graphics_group_print()

function_print(18)

