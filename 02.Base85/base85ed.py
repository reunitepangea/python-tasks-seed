"""
Base85 encoder and decoder
"""

from __future__ import annotations
import base64
from beartype import beartype


@beartype
def encode(b:bytes):
    alphabet = b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'
    result = []
    i = 0
    if len(b) == 0:
        return b""
    while i + 4 <= len(b):
        block = b[i:i+4]
        number = block[0]*(pow(256, 3)) + block[1]*(pow(256, 2)) + block[2]*256 + block[3]
        digits = []
        for j in range(5):
            digits.append(number % 85)
            number = number // 85
        digits = digits[::-1]
        for digit in digits:
            result.append(alphabet[digit])
        i += 4
    if i < len(b):
        end = b[i:]
        len_end = len(end)
        end = end + b'\x00'*(4 - len_end)
        number = end[0]*(pow(256, 3)) + end[1]*(pow(256, 2)) + end[2]*256 + end[3]
        digits = []
        for j in range(5):
            digits.append(number % 85)
            number = number // 85
        digits = digits[::-1]
        digits = digits[0:len_end+1]
        for digit in digits:
            result.append(alphabet[digit])
    return bytes(result)


@beartype
def decode(b: bytes):
    result = []
    alphabet = b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'
    i = 0
    digits = []
    for char in b:
        digits.append(alphabet.index(char))
    if len(digits) == 0:
        return b""
    while i + 5 <= len(digits):
        block = digits[i:i+5]
        number = block[0] * (pow(85, 4)) + block[1] * (pow(85, 3)) + block[2] * (pow(85,2)) + block[3]*85 + block[4]
        bbytes = []
        for j in range(4):
            bbytes.append(number % 256)
            number = number // 256
        bbytes = bbytes[::-1]
        for bbyte in bbytes:
            result.append(bbyte)
        i += 5
    if i < len(digits):
        end = digits[i:]
        len_end = len(end)
        if len_end == 1 or len_end == 5:
            raise ValueError
        for j in range(5 - len_end):
            end.append(84)
        number = end[0] * (pow(85, 4)) + end[1] * (pow(85, 3)) + end[2] * (pow(85,2)) + end[3]*85 + end[4]
        bbytes = []
        for j in range(4):
            bbytes.append(number % 256)
            number = number // 256
        bbytes = bbytes[::-1]
        bbbytes = bbytes[:len_end - 1]
        for bbbyte in bbbytes:
            result.append(bbbyte)
    return bytes(result)

