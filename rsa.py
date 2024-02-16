from Crypto.Util.number import *    
p = getPrime(1024)
q = getPrime(1024)
n = p * q              
phi = (p-1) * (q-1)    
e = (2**16)+1          
d = pow(e, -1, phi)
PT = bytes_to_long(b'rsa is cool')
CT = pow(PT, e, n)
decrypted = long_to_bytes(pow(CT, d, n))
print(f"plaintext: {PT}\nciphertext: {CT}\ndecrypted: {decrypted}")
