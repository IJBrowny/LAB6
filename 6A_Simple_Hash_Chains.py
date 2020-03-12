
import hashlib

mystring = input('Enter the text to hash: ')

hash1 = hashlib.md5(mystring.encode()).hexdigest()
hash2 = "c89aa2ffb9edcc6604005196b5f0e0e4"
print(hash1)

while hash1 != hash2:
    hash1 = hashlib.md5(hash1.encode()).hexdigest()  # calculate next hash
    print(hash1)

print("done")
