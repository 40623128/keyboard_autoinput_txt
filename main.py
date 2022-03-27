from pymouse import PyMouse
from pykeyboard import PyKeyboard
import keyboard
import time
import random

Average_typing_speed = 10 #Average typing speed 100 letter per second
path = 'input.txt' #Change to the name of the file


k = PyKeyboard()
time_step = 2/Average_typing_speed
f = open(path, 'r')
all_text = f.read()
word_number = len(all_text)
while True:
    if keyboard.read_key() == "shift":
        for i in range(word_number):
            time.sleep(random.random()*time_step)
            if all_text[i] == "A":
                k.press_key('A')
                k.release_key ('A')
            elif all_text[i] == "B":
                k.press_key('B')
                k.release_key ('B')
            elif all_text[i] == "C":
                k.press_key('C')
                k.release_key ('C')
            elif all_text[i] == "D":
                k.press_key('D')
                k.release_key ('D')
            elif all_text[i] == "E":
                k.press_key('E')
                k.release_key ('E')
            elif all_text[i] == "F":
                k.press_key('F')
                k.release_key ('F')
            elif all_text[i] == "G":
                k.press_key('G')
                k.release_key ('G')
            elif all_text[i] == "H":
                k.press_key('H')
                k.release_key ('H')
            elif all_text[i] == "I":
                k.press_key('I')
                k.release_key ('I')
            elif all_text[i] == "J":
                k.press_key('J')
                k.release_key ('J')
            elif all_text[i] == "K":
                k.press_key('K')
                k.release_key ('K')
            elif all_text[i] == "L":
                k.press_key('L')
                k.release_key ('L')
            elif all_text[i] == "M":
                k.press_key('M')
                k.release_key ('M')
            elif all_text[i] == "N":
                k.press_key('N')
                k.release_key ('N')
            elif all_text[i] == "O":
                k.press_key('O')
                k.release_key ('O')
            elif all_text[i] == "P":
                k.press_key('P')
                k.release_key ('P')
            elif all_text[i] == "Q":
                k.press_key('Q')
                k.release_key ('Q')
            elif all_text[i] == "R":
                k.press_key('R')
                k.release_key ('R')
            elif all_text[i] == "S":
                k.press_key('S')
                k.release_key ('S')
            elif all_text[i] == "T":
                k.press_key('T')
                k.release_key ('T')
            elif all_text[i] == "U":
                k.press_key('U')
                k.release_key ('U')
            elif all_text[i] == "V":
                k.press_key('V')
                k.release_key ('V')
            elif all_text[i] == "W":
                k.press_key('W')
                k.release_key ('W')
            elif all_text[i] == "X":
                k.press_key('X')
                k.release_key ('X')
            elif all_text[i] == "Y":
                k.press_key('Y')
                k.release_key ('Y')
            elif all_text[i] == "Z":
                k.press_key('Z')
                k.release_key ('Z')
            elif all_text[i] == "a":
                k.press_key('a')
                k.release_key ('a')
            elif all_text[i] == "b":
                k.press_key('b')
                k.release_key ('b')
            elif all_text[i] == "c":
                k.press_key('c')
                k.release_key ('c')
            elif all_text[i] == "d":
                k.press_key('d')
                k.release_key ('d')
            elif all_text[i] == "e":
                k.press_key('e')
                k.release_key ('e')
            elif all_text[i] == "f":
                k.press_key('f')
                k.release_key ('f')
            elif all_text[i] == "g":
                k.press_key('g')
                k.release_key ('g')
            elif all_text[i] == "h":
                k.press_key('h')
                k.release_key ('h')
            elif all_text[i] == "i":
                k.press_key('i')
                k.release_key ('i')
            elif all_text[i] == "j":
                k.press_key('j')
                k.release_key ('j')
            elif all_text[i] == "k":
                k.press_key('k')
                k.release_key ('k')
            elif all_text[i] == "l":
                k.press_key('l')
                k.release_key ('l')
            elif all_text[i] == "m":
                k.press_key('m')
                k.release_key ('m')
            elif all_text[i] == "n":
                k.press_key('n')
                k.release_key ('n')
            elif all_text[i] == "o":
                k.press_key('o')
                k.release_key ('o')
            elif all_text[i] == "p":
                k.press_key('p')
                k.release_key ('p')
            elif all_text[i] == "q":
                k.press_key('q')
                k.release_key ('q')
            elif all_text[i] == "r":
                k.press_key('r')
                k.release_key ('r')
            elif all_text[i] == "s":
                k.press_key('s')
                k.release_key ('s')
            elif all_text[i] == "t":
                k.press_key('t')
                k.release_key ('t')
            elif all_text[i] == "u":
                k.press_key('u')
                k.release_key ('u')
            elif all_text[i] == "v":
                k.press_key('v')
                k.release_key ('v')
            elif all_text[i] == "w":
                k.press_key('w')
                k.release_key ('w')
            elif all_text[i] == "x":
                k.press_key('x')
                k.release_key ('x')
            elif all_text[i] == "y":
                k.press_key('y')
                k.release_key ('y')
            elif all_text[i] == "z":
                k.press_key('z')
                k.release_key ('z')
            elif all_text[i] == " ":
                k.press_key(k.space_key)
                k.release_key (k.space_key)
            elif all_text[i] == ",":
                k.press_key(',')
                k.release_key (',')
            elif all_text[i] == ".":
                k.press_key('.')
                k.release_key ('.')
            elif all_text[i] == "(":
                k.press_key('(')
                k.release_key ('(')
            elif all_text[i] == ")":
                k.press_key(')')
                k.release_key (')')
            elif all_text[i] == "-":
                k.press_key('-')
                k.release_key ('-')
            else:
                print("Button",all_text[i],"is not pressed")
        f.close()
        break
