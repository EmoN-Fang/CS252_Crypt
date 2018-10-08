def shift_let(letter, n):
    return chr((ord(letter) - ord('a') + n) % 26 + ord('a'))

def Encry(k, p):
    ptext = list(p)
    c = ''.join([shift_let(x, k) for x in ptext]).upper()
    return c

def Decry(k, c):
    ctext = list(c.lower())
    p = ''.join([shift_let(x, -k) for x in ctext])    
    return p

if __name__ == '__main__':
     c = 'OVDTHUFWVZZPISLRLFZHYLAOLYL'     
     print('ciphertext = ' + c)
     for k in range(26):
        print("when k = ",k)
        print('plaintext = ' + Decry(k, c))
