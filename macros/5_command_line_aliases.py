from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Command line aliases',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x066006, 'TODO', ['TODO']),
        (0x066006, 'TODO', ['TODO']),
        (0x066006, 'TODO', ['TODO']),
        # 2nd row ----------
        (0x066006, 'TODO', ['TODO']),
        (0x066006, 'TODO', ['TODO']),
        (0x066006, 'TODO', ['TODO']),
        # 3rd row ----------
        (0x066006, 'TODO', ['TODO']),
        (0x066006, 'TODO', ['TODO']),
        (0x066006, 'TODO', ['TODO']),
        # 4th row ----------
        (0x066006, 'TODO', ['']),
        (0x066006, '', ['']),
        (0x066006, 'TODO', ['']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
