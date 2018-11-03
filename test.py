import os
import time,thread

def display_screen(interval):
    x = 0
    while True:
        os.system('clear')
        print ("\n\n\n\n")
        line_remain = (x / 2) % 10

        for y in range(line_remain):
            print(" "),

        remain = x % 4
        if remain == 0:
            print("-")
        elif remain == 1:
            print("\\")
        elif remain == 2:
            print("|")
        elif remain == 3:
            print("/")
        x = x + 1
        time.sleep(interval)

def wait_for_input():
    while True:
        if 'y' == raw_input():
            os.system('clear');
            print("stop")
            exit()

thread.start_new_thread(display_screen, (0.2,))
wait_for_input()
