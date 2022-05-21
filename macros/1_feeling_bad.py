from adafruit_hid.keycode import Keycode

# Note to self:
# since the only already available dvorak keyboard layout (in code.py)
# is a US Dvorak layout for 104 keys, things get really weird on my
# Polish Programmers Dvorak. Example: A kiss, ':*', is represented
# by a " and the variable taking the asterisk from the keypad
# (which won't change with the layout). A simple smiley is `"-8`.
# TODO: Create your own layout that is Polish Programmers Dvorak
#       so you don't have to hack like this.

# This doesn't seem to break between MacOS and Linux, phew (^_^)/

# (´_ゝ`) - indifferent
# (凸ಠ益ಠ)凸 - middle finger
# (╯°□°）╯︵ ┻━┻ - table flip

app = {
    'name' : 'Feeling bad',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x9598C6, ':-(', ['"-5']),
        (0x9598C6, ":'-(", ["'-5"]),
        (0x9598C6, '(;_;)', ["5'_'8"]),
        # 2nd row ----------
        (0x5E64D4, ':-/', ['"-/']),
        (0x5E64D4, 'O_o', ['O_o']),
        (0x5E64D4, "indif", [Keycode.KEYPAD_ASTERISK,
         "feeling indifferent", Keycode.KEYPAD_ASTERISK]),
        # 3rd row ----------
        (0x333BD7, ':$', ['"`']),
        (0x333BD7, '(; -_-)', ["5' -_-8"]),
        (0x333BD7, '</3', ['</', Keycode.KEYPAD_THREE]),
        # 4th row ----------
        (0x1A21A3, 'tblfl', [
         Keycode.KEYPAD_ASTERISK, "table flip", Keycode.KEYPAD_ASTERISK]),
        (0x1A21A3, 'enter', [Keycode.ENTER]),
        (0x1A21A3, 'midfin', [Keycode.KEYPAD_ASTERISK,
         "middle finger", Keycode.KEYPAD_ASTERISK]),
        # Encoder button ---
        # Deep inside I am still an IRC-raised teenager, sorry.
        (0x000000, '8===D', [Keycode.KEYPAD_EIGHT, '666D'])
    ]
}
