# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT
from adafruit_hid.keycode import Keycode

app = {
    'name' : 'CS:GO shortcuts',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x272E6F, 'TODO', ['TODO']),
        (0x272E6F, 'TODO', ['TODO']),
        (0x272E6F, 'TODO', ['TODO']),
        # 2nd row ----------
        (0xF99D1C, 'TODO', ['TODO']),
        (0xF99D1C, 'TODO', ['TODO']),
        (0xF99D1C, 'TODO', ['TODO']),
        # 3rd row ----------
        (0xFFF5E3, 'TODO', ['TODO']),
        (0xFFF5E3, 'TODO', ['TODO']),
        (0xFFF5E3, 'TODO', ['TODO']),
        # 4th row ----------
        (0x272E6F, 'TODO', ['']),
        (0x272E6F, '', ['']),
        (0x272E6F, 'TODO', ['']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
