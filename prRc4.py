import sys
def KSA(key):
    keylength = len(key)
    S = range(256)
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap
    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

def convert_key(s):
    return [ord(c) for c in s]

def codigo(plaintext,key):
    key = convert_key(key)
    keystream = RC4(key)    
    d=""
    for c in plaintext:
        d=d+("%02X-" % (ord(c) ^ keystream.next()))
    return d[:len(d)-1]