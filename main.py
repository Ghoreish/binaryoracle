import random


def guess_next(history: list):
    total_len = len(history)
    for i in range(1, total_len):
        selected = history[i: total_len]
        start = i - 1
        end = total_len - 1
        while start >= 0:
            if selected == history[start: end]:
                print(selected, history[start: end + 1])
                print(history)
                return history[end]
            start -= 1
            end -= 1
    return None



history = []
guess = random.randint(0, 1)
while True:
    print('Is your number {}? (1/0)(yes/no)'.format(str(guess)))
    inp = input('> ')
    if inp == '1':
        history.append(guess)
    elif inp == '0':
        history.append((guess + 1) % 2)
    else:
        print('Wrong input BRO!!!')
        continue

    next = guess_next(history)
    print(next)
    if next != None:
        guess = next
    else:
        guess = random.randint(0, 1)

