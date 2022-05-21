from adafruit_hid.keycode import Keycode

app = {
    'name' : 'X - D',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xD60270, 'xD', ['xD']),
        (0x551BBA, 'XD', ['XD']),
        (0x0038A8, 'xd', ['xd']),
        # 2nd row ----------
        (0xD60270, 'x-D', ['x-D']),
        (0x551BBA, 'X-D', ['X-D']),
        (0x0038A8, 'x-d', ['x-d']),
        # 3rd row ----------
        (0xD60270, 'xDDDD', ['xDDDD']),
        (0x551BBA, 'XDDDD', ['XDDDD']),
        (0x0038A8, 'xdddd', ['xddd']),
        # # 4th row ----------
        (0xD60270, '', ['']),
        (0x551BBA, 'enter', [Keycode.ENTER]),
        (0x0038A8, '', ['']),
        # # Encoder button ---
        (0x000000, '', [])
    ]
}
