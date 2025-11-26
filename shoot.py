from pynput import keyboard, mouse
import time

kb, ms = keyboard.Controller(), mouse.Controller()

def press_key(k): kb.press(k); kb.release(k)
def type_text(text):
    for c in text: kb.press(c); kb.release(c)
def click(btn): ms.press(btn); ms.release(btn)
def hold_click(btn, d): ms.press(btn); time.sleep(d); ms.release(btn)

positions = [
    "setpos_exact 1796.174316 -409.890259 -351.968750;setang_exact 0.000000 93.447632 0.000000",
    "setpos_exact 1925.711182 -405.424194 -351.968750;setang_exact 0.000000 93.009583 0.000000",
    "setpos_exact 2052.659912 -399.622925 -351.968750;setang_exact 0.000000 92.613708 0.000000",
    "setpos_exact 2180.494141 -411.235474 -351.968750;setang_exact 0.000000 91.293640 0.000000",
]

def setpos_block(line):
    press_key('`'); time.sleep(1.5)
    type_text(line); time.sleep(1.5)
    press_key(keyboard.Key.enter); time.sleep(1.5)
    press_key('`'); time.sleep(1.5)
    click(mouse.Button.middle); time.sleep(1.5)
    press_key('o'); time.sleep(1.5)
    press_key('g'); time.sleep(1.5)

def do_action():
    press_key('`'); time.sleep(0.1)
    type_text("exec shoot"); time.sleep(0.1)
    press_key(keyboard.Key.enter); time.sleep(0.1)
    type_text("bot_kick"); time.sleep(0.1)
    press_key(keyboard.Key.enter)
    press_key('`'); time.sleep(0.5)
    for _ in range(4):
        press_key('.'); time.sleep(0.5)

    for pos in positions:
        setpos_block(pos)

    press_key('`'); time.sleep(1.5)
    type_text("setpos_exact 2327.276855 -395.690308 -351.968750;setang_exact 0.000000 93.684540 0.000000"); time.sleep(1.5)
    press_key(keyboard.Key.enter); time.sleep(1.5)
    type_text("give weapon_ak47"); time.sleep(1.5)
    press_key(keyboard.Key.enter); time.sleep(1.5)
    press_key('`'); time.sleep(1.5)

    click(mouse.Button.x2); time.sleep(1)      # mouse5 (bind mouse5 toggle bot_mimic 1 0)
    press_key('1'); time.sleep(1.5)

    time.sleep(5)
    press_key(keyboard.Key.f4); time.sleep(1) #capframex recording starts. Make sure you set capframex hotkey to f4 for recording

    for _ in range(4):
        hold_click(mouse.Button.left, 3.5); time.sleep(2)

    click(mouse.Button.x2); time.sleep(1)      # mouse5 toggles of bot_mimic to 0
    press_key(keyboard.Key.f4)                # f4 end (capframex recording ends)

def on_press(key):
    if key == keyboard.Key.f6:
        print("F6 → executing"); do_action()
    if key == keyboard.Key.f8:
        print("F8 → terminating"); return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
