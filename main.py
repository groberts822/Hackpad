import time
import board
import digitalio
import usb_hid
import adafruit_hid.keyboard
import adafruit_hid.keycode
import adafruit_ssd1306

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

keys = [
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
]

buttons = []
for pin in keys:
    b = digitalio.DigitalInOut(pin)
    b.switch_to_input(pull=digitalio.Pull.UP)
    buttons.append(b)

clk = digitalio.DigitalInOut(board.D6)
dt = digitalio.DigitalInOut(board.D7)
clk.switch_to_input(pull=digitalio.Pull.UP)
dt.switch_to_input(pull=digitalio.Pull.UP)

i2c = board.I2C()
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.text("Hackpad Ready", 0, 0, 1)
display.show()

last_clk = clk.value
volume = 50

while True:
    for i, button in enumerate(buttons):
        if not button.value:
            kbd.press(Keycode.F13 + i)
            time.sleep(0.15)
            kbd.release_all()

    current_clk = clk.value
    if current_clk != last_clk:
        if not dt.value:
            volume = min(100, volume + 2)
            kbd.send(Keycode.VOLUME_INCREMENT)
        else:
            volume = max(0, volume - 2)
            kbd.send(Keycode.VOLUME_DECREMENT)

        display.fill(0)
        display.text("Volume:", 0, 0, 1)
        display.text(str(volume), 0, 16, 1)
        display.show()

    last_clk = current_clk
    time.sleep(0.01)