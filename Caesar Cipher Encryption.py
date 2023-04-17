alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter) 
    #將明文的位置對應字母標當中找出來，:ex:hello -> 7,4,11,11,14
    new_position = position + shift
    #已知輸入的字母的位置，再加上偏移值等於加密過後的字母位置
    new_letter = alphabet[new_position]
    #有了新的字母位置，將新的字母取出來
    cipher_text = cipher_text + new_letter 
    #將加密過後的字母組裝成密文
  print(f'The encoded text is {cipher_text}')
 
encrypt(plain_text=text, shift_amount=shift)
