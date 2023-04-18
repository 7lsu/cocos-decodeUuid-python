# from cocos engine uuid decode
def base64_to_uuid(base64_text):
    BASE64_KEYS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    BASE64_VALUES = [64] * 123
    for i in range(64):
        BASE64_VALUES[ord(BASE64_KEYS[i])] = i

    Base64Values = BASE64_VALUES

    HexChars = list('0123456789abcdef')

    _t = ['', '', '', '']
    UuidTemplate = _t + _t + ['-'] + _t + ['-'] + _t + ['-'] + _t + [
        '-'
    ] + _t + _t + _t
    Indices = [i for i, x in enumerate(UuidTemplate) if x != '-']

    if len(base64_text) != 22:
        return base64_text
    UuidTemplate[0] = base64_text[0]
    UuidTemplate[1] = base64_text[1]
    j = 2
    for i in range(2, 22, 2):
        lhs = Base64Values[ord(base64_text[i])]
        rhs = Base64Values[ord(base64_text[i + 1])]
        UuidTemplate[Indices[j]] = HexChars[lhs >> 2]
        UuidTemplate[Indices[j + 1]] = HexChars[((lhs & 3) << 2) | (rhs >> 4)]
        UuidTemplate[Indices[j + 2]] = HexChars[rhs & 0xf]
        j += 3
    return ''.join(UuidTemplate)
