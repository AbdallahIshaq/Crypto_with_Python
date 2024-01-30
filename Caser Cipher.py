plaintext="cryptoisfun"
plaintextreverce="fubswrlvixq"
key=3
alpha="aabcdefghijklmnopqrstuvwxyz"
#process
def caser_encryption(plaintext,key):
    ciphertext=""
    for x in plaintext:
        ciphertext+=alpha[( alpha.index(x)+key)%26]

    return ciphertext#return value not valuable
def caser_decripyion(plaintext,key):
    ciphertext=""
    for x in plaintext:
        ciphertext+=alpha[( alpha.index(x)-key)%26]

    return ciphertext#return value not valuable


#output
print(caser_encryption(plaintext,key))
print(caser_decripyion(plaintextreverce,key))
