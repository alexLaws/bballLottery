from random import randint
from time import sleep

diceOutcomes = {
    (1, 2, 3): 'World B Freed',
    (1, 2, 4): 'World B Freed',
    (1, 2, 5): 'World B Freed',
    (1, 2, 6): 'World B Freed',
    (1, 3, 4): 'World B Freed',
    (1, 3, 5): 'World B Freed',
    (1, 3, 6): 'New York Sbarros',
    (1, 4, 5): 'New York Sbarros',
    (1, 4, 6): 'New York Sbarros',
    (1, 5, 6): 'New York Sbarros',
    (2, 3, 4): 'A Washington Basketball Team',
    (2, 3, 5): 'A Washington Basketball Team',
    (2, 3, 6): 'A Washington Basketball Team',
    (2, 4, 5): 'A Washington Basketball Team',
    (2, 4, 6): 'Sweat Kennel U (Goes To Jack if 5th or 6th)',
    (2, 5, 6): 'Sweat Kennel U (Goes To Jack if 5th or 6th)',
    (3, 4, 5): 'Sweat Kennel U (Goes To Jack if 5th or 6th)',
    (3, 4, 6): 'Linsanity 2.0',
    (3, 5, 6): 'Linsanity 2.0',
    (4, 5, 6): 'Bizzy Bimbos XXX',
}


draft = ['',
         '',
         '',
         '',
         '',
         '',
         'Leaping Luka\'s',
         'Stay Off The Reed',
         'A Bug\'s Life',
         'Swaet Kennel U (From nuqDaq ‘oH tach’e)',
         'A Washington Basketball team (From Barrett\'s Bad Boys)',
         'Heat Culture']


def getDice():
    a = randint(1, 6)
    while True:
        b = randint(1, 6)
        if b != a:
            break
    while True:
        c = randint(1, 6)
        if c not in [a, b]:
            break
    rolls = sorted([a, b, c])
    # print((rolls[0], rolls[1], rolls[2]))
    return diceOutcomes[(rolls[0], rolls[1], rolls[2])]


def pickGoesTo():
    team = getDice()
    # print(team)
    if team not in draft:
        return team
    else:
        return False


def ordinal(n):
    return "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])


print("The Lottery is starting!")
input("Are you ready to begin?")
input("Congrats to our defending champion, Heat Culture")
print("ping pong balls bouncing....")
sleep(15)

pick = 1

while pick < 7:
    team = pickGoesTo()
    if team is not False:
        draft[pick - 1] = team
        pick += 1
        if pick < 7:
            print('Pick {} is decided!'.format(pick-1))
        sleep(1)

print("The draft order is set!")
input("First the non-Lottery teams:")

for i in range(12, 6, -1):
    input("{} pick: {}".format(ordinal(i), draft[i - 1]))

sleep(2)

input("Now the Lottery teams!")

for i in range(6, 3, -1):
    input("{} pick: {}".format(ordinal(i), draft[i - 1]))

input("Now the top 3!")
input("{} pick: {}".format(ordinal(3), draft[2]))
input("{} pick: {}".format(ordinal(2), draft[1]))
print("And that means the first pick goes to:")
input("{} pick: {}".format(ordinal(1), draft[0]))
