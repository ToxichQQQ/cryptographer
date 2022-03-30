import hashlib


text = input('Ввведите сообщение для шифрования: ')

text_sha1 = hashlib.sha1(text.encode('utf-8'))
result = text_sha1.hexdigest()

print(result)
input('Press ENTER to exit')