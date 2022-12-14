# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
A macro/hotkey program for Adafruit MACROPAD. Macro setups are stored in the
/macros folder (configurable below), load up just the ones you're likely to
use. Plug into computer's USB port, use dial to select an application macro
set, press MACROPAD keys to send key sequences and other USB protocols.
"""

# pylint: disable=import-error, unused-import, too-few-public-methods

import os
import time
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

# START Keyboard layout -----------------------------------------------------
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_base import KeyboardLayoutBase

# Note: this KeyboardLayout was generated using https://github.com/Neradoc/Circuitpython_Keyboard_Layouts
# and a modified XML file downloaded from https://kbdlayout.info/KBDDV/download/xml
# the XML above is for a US Dvorak layout; the layout below is for a Polish Programmer's Dvorak layout.
# TODO: there are no keycodes available for characters:
# - " (34/0x22)
# - ' (39/0x27)
# - $ (36/0x24)
# - 'ą' (261/0x105) and other Polish and Norwegian characters (no alt layer)
class KeyboardLayout(KeyboardLayoutBase):
    SHIFT_FLAG = 0x80
    ASCII_TO_KEYCODE = (
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2a'  # BACKSPACE
        b'\x2b'  # '\t'
        b'\x28'  # '\n'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x29'  # ESC
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2c'  # ' '
        b'\x2d'  # '!'
        b'\x00'
        b'\x2e'  # '#'
        b'\x00'
        b'\x9e'  # '%'
        b'\x1e'  # '&'
        b'\x00'
        b'\x22'  # '('
        b'\x25'  # ')'
        b'\x24'  # '*'
        b'\x26'  # '+'
        b'\x1a'  # ','
        b'\x34'  # '-'
        b'\x08'  # '.'
        b'\x2f'  # '/'
        b'\xa4'  # '0'
        b'\xa2'  # '1'
        b'\xa5'  # '2'
        b'\xa1'  # '3'
        b'\xa6'  # '4'
        b'\xa0'  # '5'
        b'\xa7'  # '6'
        b'\x9f'  # '7'
        b'\xad'  # '8'
        b'\xa3'  # '9'
        b'\x94'  # ':'
        b'\x14'  # ';'
        b'\x9a'  # '<'
        b'\x23'  # '='
        b'\x88'  # '>'
        b'\xaf'  # '?'
        b'\x30'  # '@'
        b'\x84'  # 'A'
        b'\x91'  # 'B'
        b'\x8c'  # 'C'
        b'\x8b'  # 'D'
        b'\x87'  # 'E'
        b'\x9c'  # 'F'
        b'\x98'  # 'G'
        b'\x8d'  # 'H'
        b'\x8a'  # 'I'
        b'\x86'  # 'J'
        b'\x99'  # 'K'
        b'\x93'  # 'L'
        b'\x90'  # 'M'
        b'\x8f'  # 'N'
        b'\x96'  # 'O'
        b'\x95'  # 'P'
        b'\x9b'  # 'Q'
        b'\x92'  # 'R'
        b'\xb3'  # 'S'
        b'\x8e'  # 'T'
        b'\x89'  # 'U'
        b'\xb7'  # 'V'
        b'\xb6'  # 'W'
        b'\x85'  # 'X'
        b'\x97'  # 'Y'
        b'\xb8'  # 'Z'
        b'\x1f'  # '['
        b'\x31'  # '\\'
        b'\x27'  # ']'
        b'\xb0'  # '^'
        b'\xb4'  # '_'
        b'\xae'  # '`'
        b'\x04'  # 'a'
        b'\x11'  # 'b'
        b'\x0c'  # 'c'
        b'\x0b'  # 'd'
        b'\x07'  # 'e'
        b'\x1c'  # 'f'
        b'\x18'  # 'g'
        b'\x0d'  # 'h'
        b'\x0a'  # 'i'
        b'\x06'  # 'j'
        b'\x19'  # 'k'
        b'\x13'  # 'l'
        b'\x10'  # 'm'
        b'\x0f'  # 'n'
        b'\x16'  # 'o'
        b'\x15'  # 'p'
        b'\x1b'  # 'q'
        b'\x12'  # 'r'
        b'\x33'  # 's'
        b'\x0e'  # 't'
        b'\x09'  # 'u'
        b'\x37'  # 'v'
        b'\x36'  # 'w'
        b'\x05'  # 'x'
        b'\x17'  # 'y'
        b'\x38'  # 'z'
        b'\x20'  # '{'
        b'\xb1'  # '|'
        b'\x21'  # '}'
        b'\xb5'  # '~'
        b'\x00'
    )
    NEED_ALTGR = ''
    HIGHER_ASCII = {
    }
    COMBINED_KEYS = {
    }

class Keycode:
    A = 0x04
    B = 0x11
    C = 0x0c
    D = 0x0b
    E = 0x07
    F = 0x1c
    G = 0x18
    H = 0x0d
    I = 0x0a
    J = 0x06
    K = 0x19
    L = 0x13
    M = 0x10
    N = 0x0f
    O = 0x16
    P = 0x15
    Q = 0x1b
    R = 0x12
    S = 0x33
    T = 0x0e
    U = 0x09
    V = 0x37
    W = 0x36
    X = 0x05
    Y = 0x17
    Z = 0x38
    ALT = 0xe2
    END = 0x4d
    F1 = 0x3a
    F2 = 0x3b
    F3 = 0x3c
    F4 = 0x3d
    F5 = 0x3e
    F6 = 0x3f
    F7 = 0x40
    F8 = 0x41
    F9 = 0x42
    F10 = 0x43
    F11 = 0x44
    F12 = 0x45
    F13 = 0x68
    F14 = 0x69
    F15 = 0x6a
    F16 = 0x6b
    F17 = 0x6c
    F18 = 0x6d
    F19 = 0x6e
    F20 = 0x6f
    F21 = 0x70
    F22 = 0x71
    F23 = 0x72
    F24 = 0x73
    GUI = 0xe3
    ONE = 0x1e
    SIX = 0x23
    TAB = 0x2b
    TWO = 0x1f
    FIVE = 0x22
    FOUR = 0x21
    HOME = 0x4a
    NINE = 0x26
    ZERO = 0x27
    ALTGR = 0xe6
    COMMA = 0x1a
    EIGHT = 0x25
    ENTER = 0x28
    MINUS = 0x34
    PAUSE = 0x48
    QUOTE = 0x14
    SEVEN = 0x24
    SHIFT = 0xe1
    SPACE = 0x2c
    THREE = 0x20
    APPLICATION = 0x65
    BACKSLASH = 0x31
    BACKSPACE = 0x2a
    CAPS_LOCK = 0x39
    COMMAND = 0xe3
    CONTROL = 0xe0
    DELETE = 0x4c
    DOWN_ARROW = 0x51
    EQUALS = 0x30
    ESCAPE = 0x29
    FORWARD_SLASH = 0x2f
    GRAVE_ACCENT = 0x35
    INSERT = 0x49
    KEYPAD_ASTERISK = 0x55
    KEYPAD_EIGHT = 0x60
    KEYPAD_FIVE = 0x5d
    KEYPAD_FORWARD_SLASH = 0x54
    KEYPAD_FOUR = 0x5c
    KEYPAD_MINUS = 0x56
    KEYPAD_NINE = 0x61
    KEYPAD_NUMLOCK = 0x53
    KEYPAD_ONE = 0x59
    KEYPAD_PERIOD = 0x63
    KEYPAD_PLUS = 0x57
    KEYPAD_SEVEN = 0x5f
    KEYPAD_SIX = 0x5e
    KEYPAD_THREE = 0x5b
    KEYPAD_TWO = 0x5a
    KEYPAD_ZERO = 0x62
    LEFT_ALT = 0xe2
    LEFT_ARROW = 0x50
    LEFT_BRACKET = 0x2d
    LEFT_CONTROL = 0xe0
    LEFT_GUI = 0xe3
    LEFT_SHIFT = 0xe1
    OEM_102 = 0x64
    OPTION = 0xe2
    PAGE_DOWN = 0x4e
    PAGE_UP = 0x4b
    PERIOD = 0x08
    PRINT_SCREEN = 0x46
    RETURN = 0x28
    RIGHT_ALT = 0xe6
    RIGHT_ARROW = 0x4f
    RIGHT_BRACKET = 0x2e
    RIGHT_CONTROL = 0xe4
    RIGHT_GUI = 0xe7
    RIGHT_SHIFT = 0xe5
    SCROLL_LOCK = 0x47
    SEMICOLON = 0x1d
    SPACEBAR = 0x2c
    UP_ARROW = 0x52
    WINDOWS = 0xe3

    @classmethod
    def modifier_bit(cls, keycode):
        """Return the modifer bit to be set in an HID keycode report if this is a
        modifier key; otherwise return 0."""
        return (
            1 << (keycode - 0xE0) if cls.LEFT_CONTROL <= keycode <= cls.RIGHT_GUI else 0
        )

# END Keyboard layout -----------------------------------------------------

# CONFIGURABLES ------------------------

MACRO_FOLDER = '/macros'

# CLASSES AND FUNCTIONS ----------------

class App:
    """ Class representing a host-side application, for which we have a set
        of macro sequences. Project code was originally more complex and
        this was helpful, but maybe it's excessive now?"""
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']

    def switch(self):
        """ Activate application settings; update OLED labels and LED
            colors. """
        group[13].text = self.name   # Application name
        for i in range(12):
            if i < len(self.macros): # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
                group[i].text = self.macros[i][1]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
                group[i].text = ''
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()


# INITIALIZATION -----------------------

macropad = MacroPad()
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False

# We use the US Dvorak keyboard layout here
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)

# Set up displayio group with all the labels
group = displayio.Group()
for key_index in range(12):
    x = key_index % 3
    y = key_index // 3
    group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                             anchored_position=((macropad.display.width - 1) * x / 2,
                                                macropad.display.height - 1 -
                                                (3 - y) * 12),
                             anchor_point=(x / 2, 1.0)))
group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))
group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(macropad.display.width//2, -2),
                         anchor_point=(0.5, 0.0)))
macropad.display.show(group)

# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print("ERROR in", filename)
            import traceback
            traceback.print_exception(err, err, err.__traceback__)

if not apps:
    group[13].text = 'NO MACRO FILES FOUND'
    macropad.display.refresh()
    while True:
        pass

last_position = None
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0
apps[app_index].switch()

# MAIN LOOP ----------------------------

while True:
    position = macropad.encoder
    if position != last_position:
        app_index = position % len(apps)
        apps[app_index].switch()
        last_position = position

    # Handle encoder button. If state has changed, and if there's a
    # corresponding macro, set up variables to act on this just like
    # the keypad keys, as if it were a 13th key/macro.
    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch
        if len(apps[app_index].macros) < 13:
            continue    # No 13th macro, just resume main loop
        key_number = 12 # else process below as 13th macro
        pressed = encoder_switch
    else:
        event = macropad.keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            continue # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed

    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop.

    sequence = apps[app_index].macros[key_number][2]
    if pressed:
        # 'sequence' is an arbitrary-length list, each item is one of:
        # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
        # Negative integer: (absolute value) key released
        # Float (e.g. 0.25): delay in seconds
        # String (e.g. "Foo"): corresponding keys pressed & released
        # List []: one or more Consumer Control codes (can also do float delay)
        # Dict {}: mouse buttons/motion (might extend in future)
        if key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = 0xFFFFFF
            macropad.pixels.show()
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.press(item)
                else:
                    macropad.keyboard.release(-item)
            elif isinstance(item, float):
                time.sleep(item)
            elif isinstance(item, str):
                layout.write(item)
            elif isinstance(item, list):
                for code in item:
                    if isinstance(code, int):
                        macropad.consumer_control.release()
                        macropad.consumer_control.press(code)
                    if isinstance(code, float):
                        time.sleep(code)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.press(item['buttons'])
                    else:
                        macropad.mouse.release(-item['buttons'])
                macropad.mouse.move(item['x'] if 'x' in item else 0,
                                    item['y'] if 'y' in item else 0,
                                    item['wheel'] if 'wheel' in item else 0)
                if 'tone' in item:
                    if item['tone'] > 0:
                        macropad.stop_tone()
                        macropad.start_tone(item['tone'])
                    else:
                        macropad.stop_tone()
                elif 'play' in item:
                    macropad.play_file(item['play'])
    else:
        # Release any still-pressed keys, consumer codes, mouse buttons
        # Keys and mouse buttons are individually released this way (rather
        # than release_all()) because pad supports multi-key rollover, e.g.
        # could have a meta key or right-mouse held down by one macro and
        # press/release keys/buttons with others. Navigate popups, etc.
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.release(item)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.release(item['buttons'])
                elif 'tone' in item:
                    macropad.stop_tone()
        macropad.consumer_control.release()
        if key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
            macropad.pixels.show()
