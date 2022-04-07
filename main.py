from pymouse import PyMouse
from pykeyboard import PyKeyboard
import keyboard
import time
import random

Average_typing_speed = 10 #Average typing speed 100 letter per second
path = 'input.txt' #Change to the name of the file


k = PyKeyboard()
time_step = 2/Average_typing_speed
f = open(path, 'r', encoding='UTF-8')
all_text = f.read()
word_number = len(all_text)
while True:
    if keyboard.read_key() == "shift":
        for i in range(word_number):
            #time.sleep(random.random()*time_step)
            check_list = all_text[i]
            if all_text[i] == check_list:
                k.press_key(check_list)
                k.release_key (check_list)
        f.close()
        break
