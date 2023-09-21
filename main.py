'''
This program simulates an enhanced version of Donders' reaction
time experiment.
'''
#import libraries
import time, sys, random
from os import system, name

#global parameters
SIMPLE_TESTS_COUNT = 5
CHOICE_TESTS_COUNT = 5
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LETTERS = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
MAX_WAIT = 5

#functions
#import function enabling single-character read, depending on host system type
try:
    import msvcrt  #windows
except ImportError:
    import tty  #unix
    import termios

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
else:
    def getch():
        return msvcrt.getch().decode()

#clears console
def clear():
    #windows
    if name == 'nt':
        _ = system('cls')
    #unix
    else:
        _ = system('clear')

#simple reaction time test
def simple(max_delay, count):
    times = []
    #measure time required for long keystrokes
    print("[ Simple Reaction Time Test ]")
    print("When prompted, press \"[SPACE]\" and then \"6\" as fast as you can using ONE FINGER")
    time.sleep(5)
    for itr in range(count):
        print(f"Test {itr+1}/{count}")
        val1 = "-1"
        val2 = "-1"
        end_time = 0
        while (val2 != "6"):
            time.sleep(random.randint(1,max_delay))
            print(f"Press \"[SPACE]\" and then \"6\"!")
            start_time = time.time()
            val1 = getch()
            val2 = getch()
            end_time = time.time() - start_time
            if not str.isspace(val1):
                print("Wrong input! Try again...")
                val2 = "-1"
            elif val2 != "6":
                print("Wrong input! Try again...")
        times.append(end_time)
    #measure time required for medium keystrokes
    clear()
    print("[ Simple Reaction Time Test ]")
    print("When prompted, press \"[SPACE]\" and then \"y\" as fast as you can using ONE FINGER")
    time.sleep(5)
    for itr in range(count):
        print(f"Test {itr+1}/{count}")
        val1 = "-1"
        val2 = "-1"
        end_time = 0
        while (val2 != "y"):
            time.sleep(random.randint(1,max_delay))
            print(f"Press \"[SPACE]\" and then \"y\"!")
            start_time = time.time()
            val1 = getch()
            val2 = getch()
            end_time = time.time() - start_time
            if not str.isspace(val1):
                print("Wrong input! Try again...")
                val2 = "-1"
            elif val2 != "y":
                print("Wrong input! Try again...")
        times.append(end_time)
    return times

#number choice reaction time test
def number_choice(max_delay, count, numbers):
    times = []
    #measure time required for long keystrokes
    print("[ Simple Reaction Time Test ]")
    print("When prompted, press \"[SPACE]\" and then the displayed NUMBER as fast as you can using ONE FINGER")
    time.sleep(5)
    for itr in range(count):
        number = random.choice(numbers)
        print(f"Test {itr+1}/{count}")
        val1 = "-1"
        val2 = "-1"
        end_time = 0
        while (val2 != str(number)):
            time.sleep(random.randint(1,max_delay))
            print(f"Press \"[SPACE]\" and then {number}!")
            start_time = time.time()
            val1 = getch()
            val2 = getch()
            end_time = time.time() - start_time
            if not str.isspace(val1):
                print("Wrong input! Try again...")
                val2 = "-1"
            elif val2 != str(number):
                print("Wrong input! Try again...")
        times.append(end_time)
    return times

#letter choice reaction time test
def letter_choice(max_delay, count, letters):
    times = []
    #measure time required for long keystrokes
    print("[ Simple Reaction Time Test ]")
    print("When prompted, press \"[SPACE]\" and then the displayed LETTER as fast as you can using ONE FINGER")
    time.sleep(5)
    for itr in range(count):
        letter = random.choice(letters)
        print(f"Test {itr+1}/{count}")
        val1 = "-1"
        val2 = "-1"
        end_time = 0
        while (val2 != letter):
            time.sleep(random.randint(1,max_delay))
            print(f"Press \"[SPACE]\" and then {letter}!")
            start_time = time.time()
            val1 = getch()
            val2 = getch()
            end_time = time.time() - start_time
            if not str.isspace(val1):
                print("Wrong input! Try again...")
                val2 = "-1"
            elif val2 != letter:
                print("Wrong input! Try again...")
        times.append(end_time)
    return times

#MAIN
if __name__ == "__main__":
    #print startup messages
    print("Donders' Reaction Experiment+")
    print("Press ENTER to start")

    #wait for any user input + enter
    input()
    clear()
    print("Tests will start in 5 seconds...")
    time.sleep(5)
    clear()

    #run simple reaction time test SIMPLE_TESTS_COUNT times
    simple_tests_results = simple(MAX_WAIT, SIMPLE_TESTS_COUNT)
    clear()
    #run number choice reaction time test CHOICE_TESTS_COUNT times
    number_choice_tests_results = number_choice(MAX_WAIT, CHOICE_TESTS_COUNT, NUMBERS)
    clear()
    #run letter choice reaction time test CHOICE_TESTS_COUNT times
    letter_choice_tests_results = letter_choice(MAX_WAIT, CHOICE_TESTS_COUNT, LETTERS)
    clear()

    #calculations
    avg_keystroke_time = sum(simple_tests_results)/len(simple_tests_results)
    #temp1 = [entry - avg_keystroke_time for entry in number_choice_tests_results]
    #temp2 = [entry - avg_keystroke_time for entry in letter_choice_tests_results]
    #number_choice_tests_results = temp1
    #letter_choice_tests_results = temp2
    #for entry in number_choice_tests_results:
    #    entry -= avg_keystroke_time
    #for entry in letter_choice_tests_results:
    #    entry -= avg_keystroke_time
    avg_number_choice_time = sum(number_choice_tests_results)/len(number_choice_tests_results)
    avg_letter_choice_time = sum(letter_choice_tests_results)/len(letter_choice_tests_results)
    avg_number_desc = avg_number_choice_time - avg_keystroke_time
    avg_letter_desc = avg_letter_choice_time - avg_keystroke_time

    #print calculations
    #simple reaction time
    print("[TEST RESULTS]\n")
    print("[Simple Reaction Test]")
    print("Keystroke times:")
    for entry in simple_tests_results:
        print("{:.4f}".format(entry))
    print("Avg Reaction Time:", avg_keystroke_time, "\n")
    #numbers reaction time
    print("[Number Choice Reaction Test]")
    print("Choice times:")
    for entry in number_choice_tests_results:
        print("{:.4f}".format(entry))
    print("Avg Reaction Time:", avg_number_choice_time)
    print("Avg Decision Time:", avg_number_desc, "\n")
    #letters reaction time
    print("[Letter Choice Reaction Test]")
    print("Choice times:")
    for entry in letter_choice_tests_results:
        print("{:.4f}".format(entry))
    print("Avg Reaction Time:", avg_letter_choice_time)
    print("Avg Decision Time:", avg_letter_desc, "\n")
    #conclusions
    if avg_number_desc < avg_letter_desc:
        print("Decision time for NUMBERS was less than LETTERS")
        print("Diff:", abs(avg_number_desc-avg_letter_desc))
    elif avg_number_desc > avg_letter_desc:
        print("Decision time for LETTERS was less than NUMBERS")
        print("Diff:", abs(avg_number_desc-avg_letter_desc))
    else:
        print("Decision time for LETTERS and NUMBERS was the same")
        print("Diff:", 0)
    print()
