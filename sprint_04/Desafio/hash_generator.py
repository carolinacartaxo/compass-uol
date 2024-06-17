import hashlib

while True:
    user_input = input("Digite uma string para transformar em hash: ")
    hash_object = hashlib.sha1(user_input.encode())
    hex_dig = hash_object.hexdigest()
    print(f"SHA-1 hash: {hex_dig}")
