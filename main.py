import RPi.GPIO as GPIO
import random
import time


def check_sequence(in_sequence, button):

    # Marks the validity of the user's input for each button press
    correct = True

    # The number of button presses
    cnt = 0

    # Check for user input.
    # The user's input matches the machine generated one and the value of the
    # cnt at the end is len(in_sequence), or
    # the user has made a mistake halfway through and correct no longer is true.
    while correct and cnt < len(in_sequence):

        for i in range (0, len(button)):

            # Was the i-th button pressed?
            if GPIO.input(button[i]) == False:
                if in_sequence[cnt] == i:
                    correct = True
                    time.sleep(0.2)
                else:
                    correct = False

                cnt = cnt + 1

    return correct


def main():
    ############################## Initialization ##############################
    GPIO.setmode(GPIO.BOARD)

    # Initialize leds
    led = [13, 11]

    for i in range(0, len(led)):
        GPIO.setup(led[i], GPIO.OUT)

    # Initialize buttons
    button = [5, 3]
    reset_button = 15

    for i in range(0, len(button)):
        GPIO.setup(button[i], GPIO.IN)

    GPIO.setup(reset_button, GPIO.IN)

    ################################## main ####################################
    correct_round = True
    sequence = []

    while correct_round:

        ############################## Celebrate ###############################
        for k in range(0, 2):
            for i in range(0, len(led)):
                GPIO.output(led[i], 1)

            time.sleep(0.7)

            for i in range(0, len(led)):
                GPIO.output(led[i], 0)

            time.sleep(0.7)

        ########################## Generate new blink ##########################
        random_number = random.uniform(0, len(led) - 1)
        sequence.append(int(round(random_number)))
        print sequence

        for i in range(0, len(sequence)):
            GPIO.output(led[sequence[i]], 1)
            time.sleep(0.6)
            GPIO.output(led[sequence[i]], 0)
            if i < len(sequence) - 1:
                time.sleep(0.6)

        correct_round = check_sequence(sequence, button)

    GPIO.cleanup()



if __name__ == '__main__':
    main()
