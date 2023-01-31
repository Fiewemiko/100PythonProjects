import random
from replit import clear

cialo = [' ',' ',' ',' ',' ',' ']

list_of_word=['dupa','noga','super','pies','komplikacja']
slowo = random.choice(list_of_word)
display= ['_' for i in range(len(slowo))]
lives = 6
koniec_gry = False

def szubienica():
    print("+------++\n"
          " |     ||\n"
          " |     ||\n"
          " "+cialo[0]+"     ||\n"
          ""+cialo[2]+cialo[1]+cialo[3]+"    ||\n"
          " "+ cialo[4]+cialo[5]+"    ||\n"
          "       ||\n"
          "=======++"
          )

def litera_usera():

    while True:
        literka = input('Wpisz literkę: ')
        if len(literka) == 1:
            if literka.isalpha():
                break
            else:
                print('Proszę wpisz jedną literkę z aflabetu łacińskiego ')
        else:
            print('Proszę wpis JEDNĄ literkę')
    return literka

print('Zaczynamy grę w wisielca, zgadnij słowo!: ')

while not koniec_gry:


    litera = litera_usera()
    clear()
    if litera in display:
        print("already taken")

    for position in range(len(slowo)):
        letter = slowo[position]
        if letter == litera:
            display[position] = letter

    if str(litera) not in slowo:
        lives -= 1
        print(f"you guessed {litera} that not in the word, zostało ci {lives} żyć")
        if lives == 5:
            cialo[0]='O'
            szubienica()
        elif lives == 4:
            cialo[1] = '|'
            szubienica()
        elif lives == 3:
            cialo[2] = '/'
            szubienica()
        elif lives == 2:
            cialo[3] = '\.'
            szubienica()
        elif lives == 1:
            cialo[4] = '/'
            szubienica()

        if lives ==0:
            cialo[5] = '\.'
            szubienica()
            print("przegrales")
            koniec_gry = True

    print(f"{' '.join(display)}")

    if '_' not in display:
        print('Wygrałes!')
        koniec_gry = True
