from cryptography.fernet import Fernet

#key = Fernet.generate_key()
#cipher_suite = Fernet(key)
#cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
#plain_text = cipher_suite.decrypt(cipher_text)

def generate_key():
    key = Fernet.generate_key()
    return key

def get_cipher_suite(key):
    return Fernet(key)

def encrypt(plain_text, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plain_text)
    return cipher_text

def decrypt(cipher_text, key):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text
'''
key = generate_key()
print "KEY: " + key

message = b"A really secret message. Not for prying eyes."

cipher_text = encrypt(message, key)
print "CIPHER_TEXT: " + cipher_text

plain_text = decrypt(cipher_text, key)
print "PLAIN_TEXT: " + str(plain_text)
'''
