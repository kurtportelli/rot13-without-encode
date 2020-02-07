def rot13(message):
    cipher_key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r',
                  'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
                  'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
                  'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
                  'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l',
                  'z': 'm'}
    result = ''
    for c in message:
        if c in cipher_key:
            result += cipher_key[c]
        elif c.lower() in cipher_key:
            result += cipher_key[c.lower()].upper()
        else:
            result += c
    return result
