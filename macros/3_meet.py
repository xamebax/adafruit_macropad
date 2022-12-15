from adafruit_hid.keycode import Keycode

# TODO: Figure out how to use locally defined keycodes instead of whatever this is.
#       It might have something to do with when the keys are unpressed.

app = {
    'name': 'Google Meet',
    'macros': [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '[M a c O S]', []),
        (0x000000, '', []),
        (0x00FA00, 'Chat', [Keycode.CONTROL, Keycode.COMMAND, 0x0c]),  # 'C'
        # 2nd row ----------
        (0x0000FA, 'Mute', [Keycode.COMMAND, 0x0b]),  # 'D'
        (0xFA0000, 'Camera', [Keycode.COMMAND, 0x07]),  # 'E'
        (0x00FA00, 'Quit', [Keycode.COMMAND, 0x36]),  # 'w'
        # 3rd row ----------
        (0x000000, '[L i n u x]', []),
        (0x000000, '', []),
        (0x00FA00, 'Chat', [Keycode.CONTROL,
         Keycode.ALT, 0x0c]),  # 'C'
        # 4th row ----------
        (0x0000FA, 'Mute', [Keycode.CONTROL, 0x0b]),
        (0xFA0000, 'Camera', [Keycode.CONTROL, 0x07]),
        (0x00FA00, 'Quit', [Keycode.CONTROL, 0x36]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
