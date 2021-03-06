import random
from itertools import repeat
import time as t
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

#Functions

def num_maker(counter):
    xy = counter
    num = Label(d, anchor=CENTER, font=('Arial', 25), text=("%02d" % (xy,)))
    counter = xy - 1
    i = ("%02d" % (counter,))
    z = int(i[1]) * 78
    if int(i[1]) > 4:
        z += 63
    x_pos = z + 55
    y_pos = int(i[0]) * 64 + 62
    num.place(x=x_pos, y=y_pos)

def m10maker(n):
    maker = True
    qwerty = 0
    if qwerty > int((n - 1)/10) - 1:
        return
    while maker == True:
        if qwerty == int((n - 1)/10) - 1:
            maker = False
        qwerty += 1
        multiples_of_10.append((qwerty * 10)-1) 

def getplayersnames(p,t,an,num):
    for counter in range(int(p)):
        n = num[an]
        the =  simpledialog.askstring('Name', 'Who is your ' + n + ' player? ')
        t.insert(an, the)
        an = an + 1
        list_of_players = ', '.join(t)
    ans1 = messagebox.askyesno('Players', 'These are the players playing:\n' + list_of_players + '\nAre these the only people playing(y/n)?')
    if ans1 == False:
        play = simpledialog.askstring('Players' ,'How many more players are playing?')
        getplayersnames(play,t,an,num)
    if ans1 == True:
        messagebox.askquestion('Part 2: Players Cards' ,'Now for the player\'s cards. Are you ready to continue')
    else:
        play = simpledialog.askstring('Players' ,'How many more players are playing?')
        getplayersnames(play,t,an,num)

def makecards(clen, cnums, p, n):
   for a in range(p):
        num90 = list(range(1, n))
        for counter in range(clen):
            cardnum = random.choice(num90)
            num90.remove(cardnum)
            cnums[a].append(cardnum)

def getnumbers(num90, finnums, a, names, cards, fincards, an, nums, an2, finnames, an3):
    z = [ ]
    while len(num90) > 0:
        chosen_number = random.choice(num90)
        num90.remove(chosen_number)
        finnums.append(chosen_number)
        cd.config(text=str(chosen_number))
        num_maker(chosen_number)
        t.sleep(1)
        an = 0
        an2 = 0
        for counter in range(len(names)):
            an3 = 0
            plural = ' numbers'
            if chosen_number in cards[counter]:
                an += 1
                fincards[counter].append(chosen_number)
                cards[counter].remove(chosen_number)
                if len(cards[counter]) == 0:
                    an2 += 1
                    an3 += 1
                    messagebox.askquestion(names[counter], (names[counter] + ' has finished their numbers and is ' + nums[0] + '\n Are you ready to continue?'))
                    finnames.append(names[counter])
                if an3 != 1:
                    if len(cards[counter]) == 1:
                        plural = ' number'
                    messagebox.askquestion(names[counter], (names[counter] + ', you have ' + str(chosen_number) + ' in your card, and have ' + str(len(cards[counter])) + plural + ' left to finish' + '\n Are you ready to continue?'))
                t.sleep(0.5)
        if an2 >= 1:
            z.append(an2)
            nums.remove(nums[0])
        a = a + 1
        messagebox.askquestion('Ready', 'Are you ready to continue?')
    return [z, finnames]

#Variables/Lists
winner = 'winners are'
finnumbers = [ ]
z = [ ]
the_players = [ ]
finplayers = [ ]
donenums = [ ]
any_use = 0
anyuse = 0
anyuses = 0
any_uses = 0
numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eigth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'twenty-fourth', 'twenty-fifth', 'twenty-sixth', 'twenty-seventh', 'twenty-eigth', 'twenty-ninth', 'thirtieth', 'thirty-first', 'thirty-second']
global multiples_of_10
multiples_of_10 = [ ]
posTextList = [ ]

#Screens and Setup
main = Tk()
main.geometry('+90+10')
display = Canvas(main, width=510, height=500)
display.pack()

board = Toplevel(main)
board.geometry('+600+10')
d = Canvas(board, width=920, height=700)
d.pack()

introDisp = Toplevel(main)
introDisp.geometry('+90+620')
introCanvas = Canvas(introDisp, width=900, height=400)
introCanvas.pack()

main.attributes("-topmost", True)
board.attributes("-topmost", True)
introDisp.attributes("-topmost", True)

#Intro
introText = '''Welcome to DigiBingo(2 - 30 players)!
DigiBingo:
    1. Asks for details
    2. Makes each player a card of numbers
    3. Chooses a random number not chosen already 
    and shows which people have that number
    4. Displays the winner and the position of players
Click on the screen above to get started.'''
introLabel = Label(introCanvas, font=('Arial', 14), text=introText, justify=LEFT)
introLabel.pack()
main.attributes("-topmost", False)
board.attributes("-topmost", False)
introDisp.attributes("-topmost", False)

#Get player's names and Setup
player = simpledialog.askstring('Part 1: Players', 'How many players are playing DigiBingo?')
getplayersnames(player,the_players,any_use,numbers)
n = 91
numbers_to_n = list(range(1, n))
m10maker(n)

#Make the cards
cardnums = [[] for counter in repeat(None, len(the_players))]
cardlen = 15
makecards(int(cardlen), cardnums, len(the_players), n)
for a in range(len(the_players)):
    l = ', '.join(map(str, cardnums[a]))
    messagebox.askquestion(the_players[a], (the_players[a] + ', your numbers are: ' + l + '\n Are you ready to continue?'))
messagebox.askquestion('Ready', 'Are you ready to continue?')

#Setup
display.create_text(255, 25, text='The chosen number is:', font=('Arial', 20))
cd = Label(display, text='', font=('Arial', 285))
cd.place(x=255, y=250, anchor='center')

#Calling the numbers
fincardnums = [[] for counter in repeat(None, len(the_players))]
y = getnumbers(numbers_to_n, finnumbers, any_use, the_players, cardnums, fincardnums, anyuse, numbers, anyuses, finplayers, any_uses)
z = y[0]
finplayers = y[1]

#Who wins?
display.delete("all")
cd.destroy()
if z[0] == 1:
    winner = 'winner is'
smt = Label(display, text=('The ' + winner + '...'), font=('Arial', 20))
smt.place(y=30, x=30)
t.sleep(0.5)
sm = Label(display, text=(', '.join(finplayers[:z[0]])), font=('Arial', 20))
sm.place(x=240, y=30)
numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31th', '32th']
for counter in range(len(z)):
    posTextList.append(f"{numbers[counter]}: {', '.join(finplayers[:z[0]])}")
    for counter in range(z[0]):
        finplayers.remove(finplayers[0])
    z.remove(z[0])
h = Label(display, text='\n'.join(posTextList), font=('Arial', 20), justify=LEFT)
h.place(y=60, x=30)
main.mainloop()