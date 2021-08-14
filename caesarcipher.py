alphabet = 'abcdefghijklmnopqrstuvwxyz'

string_input = raw_input('Enter your message to encrypt: ')
key = input('Enter encryption key: ')

n = len(string_input)

string_output = ""

for i in range(n):
    character = string_input[i]
    location = alphabet.find(character)
    new_location = (location + key) % 26
    string_output += alphabet[new_location]

print 'Encrypted message [ ' + (string_output) + ' ]'

print 'key =' + str(key)

print 'decrypt doesnt work properly because of modulus operator'

string_decrypt = ""
string_output = string_decrypt

for i in range(n):
    character = string_input[i]
    location = alphabet.find(character)    
    new_location = (location - key) % 26
    string_decrypt += alphabet[new_location]
  
print 'Decrypted message [ ' + (string_decrypt) + ' ]'
