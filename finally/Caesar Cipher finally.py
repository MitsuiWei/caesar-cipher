alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet: 
      #判斷輸入內容是否存在於alphabet，如果存在再進行加解密處理
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      #如果不存在於alphabet，就直接放入字串當中不做任何處理
      end_text = end_text + char
  
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)
#從外部引入其他檔案
continue_start = True
while continue_start:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 25
    #避免使用者輸入大於50的數字，使用取餘數的方式處理
    #ex:102%25 = 2
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == 'no':
      continue_start = False
      print('Bye')