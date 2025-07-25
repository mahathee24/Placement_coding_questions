import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw_one():
    for i in range(7):
        if i == 6:
            print("*")
        else:
            print("  *  ")

def draw_two():
    for i in range(7):
        if i == 0 or i == 6:
            print(" *** ")
        elif i == 1:
            print("*   *")
        elif i == 2:
            print("    *")
        elif i == 3:
            print("   * ")
        elif i == 4:
            print("  *  ")
        elif i == 5:
            print(" *   ")

def draw_three():
    for i in range(7):
        if i == 0 or i == 6 or i == 3:
            print(" *** ")
        elif i == 1 or i == 5:
            print("*   *")
        else:
            print("    *")

while True:
    clear()
    draw_one()
    time.sleep(1)

    clear()
    draw_two()
    time.sleep(1)

    clear()
    draw_three()
    time.sleep(1)