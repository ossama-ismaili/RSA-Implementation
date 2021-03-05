import rsa

s = input("Enter a message to encrypt: ")
print("Plain message: ", s)

enc = rsa.encrypt_string(s)
print("Encrypted message: ", enc.encode("utf-8"))

dec = rsa.decrypt_string(enc)
print("Decrypted message: ", dec)