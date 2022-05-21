from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Google Meet',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '-----', []),
        (0x000000, '[M a c O S]', []),
        (0x000000, '-----', []),
        # 2nd row ----------
        (0x0000FA, 'Mute', [Keycode.COMMAND, 'D']),
        (0xFA0000, 'Camera', [Keycode.COMMAND, 'E']),
        (0x00FA00, 'Quit', [Keycode.COMMAND, 'w']),
        # 3rd row ----------
        (0x000000, '-----', []),
        (0x000000, '[L i n u x]', []),
        (0x000000, '-----', []),
        # 4th row ----------
        (0x0000FA, 'Mute', [Keycode.CONTROL, 'd']),
        (0xFA0000, 'Camera', [Keycode.CONTROL, 'e']),
        (0x00FA00, 'Quit', [Keycode.CONTROL, 'w']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}