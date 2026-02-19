#1. make sure you select your settings first
#2. restart your computer after selecting required settings
#3. load up game into main menu dont press anything
#4. bind your capframex hotkey to f4 keep capframex open before running script\
#5. set capframex timer to 105 - 107 seconds.
#6. make sure it is consistent across all your runs
#7. select number of runs by changing the variable
#8. press F6 to start script or press f8 to terminate
#9. first two cold runs are done to build shaders and to ensure warm caching
#10. then number of runs are done and all your results are saved to capframex
#by default number of trials = 5, make sure you change the load time if your pc is slower

import time
from pynput.keyboard import Controller, Key, Listener

keyboard = Controller()

running = False
terminate = False  

COMMAND = "map_workshop 3240880604 de_dust2"
LOOPS = 5   # benchmark loops (with F4 bound to capframeX and seconds to 107)

def press_key(key):
    keyboard.press(key)
    keyboard.release(key)

def type_text(text, char_delay=0.01):
    for ch in text:
        if terminate:
            return
        keyboard.press(ch)
        keyboard.release(ch)
        time.sleep(char_delay)

def run_sequence():
    global running, terminate

    print(f"[+] Starting sequence: 2 warmup runs (no capframeX record) + {LOOPS} benchmark loops with CapFrameX record.")
    time.sleep(3)

    # Compulsory warmup runs without logging capframex
    for i in range(1):
        if terminate: break
        print(f" Warmup {i+1}/2 (no F4) ")

        press_key('`')
        time.sleep(1.0);  
        if terminate: break

        

        type_text(COMMAND)
        time.sleep(1.0);  
        if terminate: break

        press_key(Key.enter)
        time.sleep(1.0);  
        if terminate: break

        press_key('`')
        time.sleep(10.0); 
        if terminate: break

        time.sleep(120.0)  
        press_key('`')
        time.sleep(1) 
        press_key('`')
        time.sleep(1.0); 

    #  Benchmark loops pressing F4 
    for i in range(LOOPS):
        if terminate: break
        print(f"Benchmark {i+1}/{LOOPS}")

        press_key('`')
        time.sleep(1.0);  
        if terminate: break

        type_text(COMMAND)
        time.sleep(1.0);  
        if terminate: break

        press_key(Key.enter)
        time.sleep(1.0);  
        if terminate: break

        press_key('`')
        time.sleep(10.0); 
        if terminate: break

        press_key(Key.f4)
        time.sleep(120.0); 
        press_key('`')
        time.sleep(1.0); 
        if terminate: break

        press_key('`')

    print("Finished sequence.")
    running = False
    terminate = False


def on_press(key):
    global running, terminate

    # Start
    if key == Key.f6 and not running:
        running = True
        terminate = False
        print("F6: Starting.")
        run_sequence()

    # Stop
    if key == Key.f8 and running:
        terminate = True
        print("[!] F8 pressed: stopping after current step.")


print("Press F6 to start the sequence (warmup x2 + benchmark loops).")
print("Press F8 to terminate safely.")

with Listener(on_press=on_press) as listener:
    listener.join()
