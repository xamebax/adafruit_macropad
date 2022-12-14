from adafruit_hid.keycode import Keycode

# This doesn't seem to break between MacOS and Linux, phew (^_^)/

# (´_ゝ`) - indifferent
# (凸ಠ益ಠ)凸 - middle finger
# (╯°□°）╯︵ ┻━┻ - table flip

app = {
    'name': 'Feeling bad',
    'macros': [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x9598C6, ':-(', [':-(']),
        (0x9598C6, ":'-(", [":'-("]),
        (0x9598C6, '(;_;)', ["(;_;)"]),
        # 2nd row ----------
        (0x5E64D4, ':-/', [':-/']),
        (0x5E64D4, 'O_o', ['O_o']),
        (0x5E64D4, "indif", [Keycode.KEYPAD_ASTERISK,
         "feeling indifferent", Keycode.KEYPAD_ASTERISK]),
        # 3rd row ----------
        (0x333BD7, ':$', [':$']),
        (0x333BD7, '(; -_-)', ["(; -_-)"]),
        (0x333BD7, '</3', ['</', Keycode.KEYPAD_THREE]),
        # 4th row ----------
        (0x1A21A3, 'tblfl', [
         Keycode.KEYPAD_ASTERISK, "table flip", Keycode.KEYPAD_ASTERISK]),
        (0x1A21A3, 'enter', [Keycode.ENTER]),
        (0x1A21A3, 'midfin', [Keycode.KEYPAD_ASTERISK,
         "middle finger", Keycode.KEYPAD_ASTERISK]),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
