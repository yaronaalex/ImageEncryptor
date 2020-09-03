from cryptography.fernet import Fernet

def textToPixelArray(text):
    #key = Fernet.generate_key()
    key = b'a2SZqYyRBsh9Ffb4xox24BYBy2REYeqvdqXicy8lzDc='
    
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(text)
    
    arr = bytearray(cipher_text)
    
    r = []
    g = []
    b = []
    j = 0

    for byte in arr:
        if j is 0:
            r.append(byte)
        if j is 1:
            g.append(byte)
        if j is 2:
            b.append(byte)
        j = j + 1
        if j is 3:
            j = 0
    
    if(len(g) < len(r)):
        g.append(0)
    if(len(b) < len(r)):
        b.append(0)
    
    rgb = (r, g, b)
       
    return rgb

def decrypt(encryptedArray):
    key = b'a2SZqYyRBsh9Ffb4xox24BYBy2REYeqvdqXicy8lzDc='
    x = bytes(encryptedArray)
    cipher_suite = Fernet(key)
    clean_text = cipher_suite.decrypt(x)
    print(clean_text)
    return