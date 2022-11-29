from __future__ import print_function
import qwiic_i2c
import qwiic_button
import sys
import random
import time

def run_whack():
    print("\nConfig Buttons")
    my_button0 = qwiic_button.QwiicButton()
    my_button1 = qwiic_button.QwiicButton(0x5F)
    my_button2 = qwiic_button.QwiicButton(0x5E)
    my_button3 = qwiic_button.QwiicButton(0x5D)

    if my_button0.begin() == False:
        print("\nThe Qwiic Button 0 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    if my_button1.begin() == False:
        print("\nThe Qwiic Button 1 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    if my_button2.begin() == False:
        print("\nThe Qwiic Button 2 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    if my_button3.begin() == False:
        print("\nThe Qwiic Button 3 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return

    print("\nButton's ready!")

    out = []
    brightness = 100

    nxt1 = 0.0
    pushTime = time.time() + random.randrange(1, 4.0)
    popTime = pushTime + random.randrange(1, 3.0)
    prev = -1
    while True:
        # Generate next mole to pop up
        num = random.randint(0,4)
        while num == prev:
            num = random.randint(0,4)
        if len(out) < 2:
            popTime = pushTime + random.randrange(1, 4.0) 
            if pushTime < time.time():
                pushTime = time.time() + random.randrange(1, 3.0)
                out.append(num)
        
        # Bring mole down if it wasn't whacked
        if popTime < time.time():
            out.pop(0)

        # Visualize moles
        arr = [0, 0, 0, 0, 0]
        for x in out:
            arr[x] = 1
        
        # Check if button 0 is pressed
        if 0 in out:
            # print("\nButton 1 is pressed!")
            my_button0.LED_on(brightness)
        else:
            my_button0.LED_off()

        # Check if button1 is pressed
        if 1 in out:
            # print("\nButton 1 is pressed!")
            my_button1.LED_on(brightness)
        else:
            my_button0.LED_off()

        # Check if button2 is pressed
        if 2 in out:
            # print("\nButton 1 is pressed!")
            my_button2.LED_on(brightness)
        else:
            my_button0.LED_off()

        # Check if button3 is pressed
        if 3 in out:
            # print("\nButton 1 is pressed!")
            my_button3.LED_on(brightness)
        else:
            my_button0.LED_off()

        time.sleep(0.02)    # Don't hammer too hard on the I2C bus

        prev = num
        
        print(arr)

        # Check for whack
        # press = int(input())
        # if press in out:
        #     out.pop(out.index(press))
        #     print("Whack!")

if __name__ == '__main__':
    try:
        run_whack()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 7")
        sys.exit(0)
