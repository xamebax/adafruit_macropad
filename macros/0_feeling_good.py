from adafruit_hid.keycode import Keycode

# This doesn't seem to break between MacOS and Linux, phew (^_^)/

app = {
    'name': 'Feeling good',
    'macros': [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xF65C82, ':-)', [':-)']),
        (0xF65C82, ":'-)", [":-)"]),
        (0xF65C82, ':-D', [':-D']),
        # 2nd row ----------
        (0xAA11F0, ':-*', [':-', Keycode.KEYPAD_ASTERISK]),
        (0xAA11F0, 'uWu', ['uWu']),
        (0xAA11F0, '<3', ['<', Keycode.KEYPAD_THREE]),
        # 3rd row ----------
        (0x483A58, ':-3', [':-', Keycode.KEYPAD_THREE]),
        (0x483A58, ':-P', [':-P']),
        (0x483A58, '\o/', '\o/'),
        # 4th row ----------
        (0x56203D, '(@_@)', ["(@_@)",]),
        (0x56203D, 'enter', [Keycode.ENTER]),
        (0x56203D, '(^_^)/', ['(^_^)/']),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
