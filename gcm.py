# based on tutorial https://asecuritysite.com/encryption/aes_gcm
from Crypto.Cipher import AES
import hashlib
import sys
import binascii

plaintext='Data to be encrypted'
password='IRIS123!'

def encrypt(plaintext, key):
  encobj = AES.new(key, AES.MODE_GCM)
  ciphertext,authTag=encobj.encrypt_and_digest(plaintext)
  return(ciphertext,authTag,encobj.nonce)

def decrypt(ciphertext,key):
  (ciphertext,  authTag, nonce) = ciphertext
  encobj = AES.new(key, AES.MODE_GCM, nonce)
  return(encobj.decrypt_and_verify(ciphertext, authTag))

key = hashlib.sha256(password.encode()).digest()

print("GCM Mode: Stream cipher and authenticated")
print("\nMessage:\t",plaintext)
print("Key:\t\t",password)


ciphertext = encrypt(plaintext.encode(),key)

print("Cipher:\t\t",binascii.hexlify(ciphertext[0]))
print("Auth Msg:\t",binascii.hexlify(ciphertext[1]))
print("Nonce:\t\t",binascii.hexlify(ciphertext[2]))


res= decrypt(ciphertext,key)


print ("\n\nDecrypted:\t",res.decode())