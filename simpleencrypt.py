def encrypt(sentence):
    
    result = []
    
    for letter in sentence:
        l = ord(letter) - 33
        result.append(l)
    
    print('this is the encrypted message')    
    for numbers in result:
        print(numbers),

    decrypt(result)

def decrypt(result):
    end_string = ""
    for numbers in result:

        l = int(numbers)
        l = l + 33
        l = chr(l)
        end_string = end_string + str(l)
        
    print(end_string)

def main():
    s = input("input the sentence to encrypt: ")
    encrypt(s)

if __name__ == '__main__':
    main()
