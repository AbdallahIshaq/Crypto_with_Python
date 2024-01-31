key=int(input("enter the Key:"))
plaintext=input("Enter plaintext:").lower()
alpha="abcdefghijklmnopqrstuvwxyz"
op=key*2-2
def encryption(key,plaintext,op):
    tranpostext=""
    global ciphertex
    ciphertex=""
    for row in range(key):
        index=0
        if row==0:
            while index<len(plaintext):
                tranpostext+=plaintext[index]
                index+=op
        elif row==key-1:
            index=row
            while index <len(plaintext):
                tranpostext+=plaintext[index]
                index+=op
        else:
            l_index=row
            r_index=op-row
            while l_index<len(plaintext):
                tr+=plaintext[l_index]
                if r_index<len(plaintext):
                    tranpostext+=plaintext[r_index]
                l_index+=op
                r_index+=op
    for x in tranpostext:
        ciphertex+=alpha[( alpha.index(x)+key)%26]
    return ciphertex
def Dencryption(key,Ciphertex,op):
    tranpostext=""
    text=""
    for x in Ciphertex:
        text +=alpha[( alpha.index(x)-key)%26]
    for row in range(key):
        if row==key-1:
            index=row
            while index <len(text):
                tranpostext+=plaintext[index]
                index+=op
        elif row==0:
            index=0
            while index<len(text):
                tranpostext+=plaintext[index]
                index+=op
    return tranpostext
print(encryption(key,plaintext,op))
print(Dencryption(key,ciphertex,op))
