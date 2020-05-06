def toMathSans(text):
    # convert alphabetic characters to Math Sans, for nick escaping
    result = ''
    for c in text:
        o = ord(c)
        if o >= 0x0061 and o <= 0x007a:
            result += chr(o - 0x0061 + 0x1d5ba)
        elif o >= 0x0041 and o <= 0x005a:
            result += chr(o - 0x0041 + 0x1d5a0)
        else:
            result += c
    return result
