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
def simple(count):
    times = []
    #measure time required for long keystrokes
    print("[ Simple Reaction Time Test ]")
    print("When prompted, press \"1\" and then \"0\" as fast as you can using ONE FINGER")
    time.sleep(5)
    for itr in range(count):
        print(f"Test {itr+1}/{count}")
        val1 = "-1"
        val2 = "-1"
        end_time = 0
        while (val2 != "0"):
            time.sleep(1)
            print(f"Press \"1\" and then \"0\"!")
            start_time = time.time()
            val1 = getch()
            val2 = getch()
            end_time = time.time() - start_time
            if val1 != "1":
                print("Wrong input! Try again...")
                val2 = "-1"
            elif val2 != "0":
                print("Wrong input! Try again...")
        times.append(end_time)
    #measure time required for medium keystrokes
    clear()
    print("[ Simple Reaction Time Test ]")
    print("When prompted, press \"3\" and then \"8\" as fast as you can using ONE FINGER")
    time.sleep(5)
    for itr in range(count):
        print(f"Test {itr+1}/{count}")
        val1 = "-1"
        val2 = "-1"
        end_time = 0
        while (val2 != "8"):
            time.sleep(1)
            print(f"Press \"3\" and then \"8\"!")
            start_time = time.time()
            val1 = getch()
            val2 = getch()
            end_time = time.time() - start_time
            if val1 != "3":
                print("Wrong input! Try again...")
                val2 = "-1"
            elif val2 != "8":
                print("Wrong input! Try again...")
        times.append(end_time)
    #measure time required for short keystrokes
    clear()
    print("[ Simple Reaction Time Test ]")
    print("When prompted, press \"5\" and then \"6\" as fast as you can using ONE FINGER")
    time.sleep(5)
    for itr in range(count):
        print(f"Test {itr+1}/{count}")
        val1 = "-1"
        val2 = "-1"
        end_time = 0
        while (val2 != "6"):
            time.sleep(1)
            print(f"Press \"5\" and then \"6\"!")
            start_time = time.time()
            val1 = getch()
            val2 = getch()
            end_time = time.time() - start_time
            if val1 != "5":
                print("Wrong input! Try again...")
                val2 = "-1"
            elif val2 != "6":
                print("Wrong input! Try again...")
        times.append(end_time)
    return times

#number choice reaction time test
def number_choice(max_delay, count, numbers):
    times = []
    print("[ Choice Reaction Time Test (NUMBERS) ]")
    print(f"Press the displayed NUMBER as fast as you can...")
    time.sleep(5)
    for itr in range(count):
        number = random.choice(numbers)
        print(f"Test {itr+1}/{count}")
        val = -1
        end_time = 0
        while (val != number):
            time.sleep(random.randint(1,max_delay))
            print(f"Press {number}")
            start_time = time.time()
            val = getch()
            end_time = time.time() - start_time
            if val != str(number):
                print("Wrong input! Try again...")
            else:
                val = int(val)
        times.append(end_time)
    return times

#letter choice reaction time test
def letter_choice(max_delay, count, letters):
    times = []
    print("[ Choice Reaction Time Test (LETTERS) ]")
    print(f"Press the displayed LETTER as fast as you can...")
    time.sleep(5)
    for itr in range(count):
        letter = random.choice(letters)
        print(f"Test {itr+1}/{count}")
        val = -1
        end_time = 0
        while (val != letter):
            time.sleep(random.randint(1,max_delay))
            print(f"Press {letter}")
            start_time = time.time()
            val = getch()
            end_time = time.time() - start_time
            if val != letter:
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
    simple_tests_results = simple(SIMPLE_TESTS_COUNT)
    clear()
    #run number choice reaction time test CHOICE_TESTS_COUNT times
    number_choice_tests_results = number_choice(MAX_WAIT, CHOICE_TESTS_COUNT, NUMBERS)
    clear()
    #run letter choice reaction time test CHOICE_TESTS_COUNT times
    letter_choice_tests_results = letter_choice(MAX_WAIT, CHOICE_TESTS_COUNT, LETTERS)
    clear()

    #calculations
    avg_keystroke_time = sum(simple_tests_results)/len(simple_tests_results)
    temp1 = [entry - avg_keystroke_time for entry in number_choice_tests_results]
    temp2 = [entry - avg_keystroke_time for entry in letter_choice_tests_results]
    number_choice_tests_results = temp1
    letter_choice_tests_results = temp2
    #for entry in number_choice_tests_results:
    #    entry -= avg_keystroke_time
    #for entry in letter_choice_tests_results:
    #    entry -= avg_keystroke_time
    avg_number_choice_time = sum(number_choice_tests_results)/len(number_choice_tests_results)
    avg_letter_choice_time = sum(letter_choice_tests_results)/len(letter_choice_tests_results)

    #print calculations
    #simple reaction time
    print("[TEST RESULTS]\n")
    print("[Simple Reaction Test]")
    print("Keystroke times:")
    for entry in simple_tests_results:
        print("{:.4f}".format(entry))
    print("Avg:", avg_keystroke_time, "\n")
    #numbers reaction time
    print("[Number Choice Reaction Test]")
    print("Choice times:")
    for entry in number_choice_tests_results:
        print("{:.4f}".format(entry))
    print("Avg:", avg_number_choice_time, "\n")
    #letters reaction time
    print("[Letter Choice Reaction Test]")
    print("Choice times:")
    for entry in letter_choice_tests_results:
        print("{:.4f}".format(entry))
    print("Avg:", avg_letter_choice_time, "\n")
    #conclusions
    if avg_number_choice_time < avg_letter_choice_time:
        print("Decision time for NUMBERS was less than LETTERS")
        print("Diff:", abs(avg_number_choice_time-avg_letter_choice_time))
    elif avg_number_choice_time > avg_letter_choice_time:
        print("Decision time for LETTERS was less than NUMBERS")
        print("Diff:", abs(avg_number_choice_time-avg_letter_choice_time))
    else:
        print("Decision time for LETTERS and NUMBERS was the same")
        print("Diff:", 0)
    print()
