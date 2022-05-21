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

app = {
    'name' : 'Feeling good',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xF65C82, ':-)', ['"-8']),
        (0xF65C82, ":'-)", ["'-8"]),
        (0xF65C82, ':-D', ['"-D']),
        # 2nd row ----------
        (0xAA11F0, ':-*', ['"-', Keycode.KEYPAD_ASTERISK]),
        (0xAA11F0, 'uWu', ['uWu']),
        (0xAA11F0, '<3', ['<', Keycode.KEYPAD_THREE]),
        # 3rd row ----------
        (0x483A58, ':-3', ['"-', Keycode.KEYPAD_THREE]),
        (0x483A58, ':-P', ['"-P']),
        (0x483A58, '\o/', '\o/'),
        # 4th row ----------
        (0x56203D, '(@_@)', ["5=_=8",]),
        (0x56203D, 'enter', [Keycode.ENTER]),
        (0x56203D, '(^_^)/', ['5+_+8/']),
        # Encoder button ---
        # Deep inside I am still an IRC-raised teenager, sorry.
        (0x000000, '8===D', [Keycode.KEYPAD_EIGHT, '666D'])
    ]
}
