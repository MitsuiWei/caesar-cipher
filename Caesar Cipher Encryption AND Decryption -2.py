alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#將加密和解密的fun合併之後有兩種判斷方向的方式
def caesar(start_text, shift_amount):
  end_text = ""
  for letter in start_text:
    position = alphabet.index(letter)
    if direction == "encode":
       new_position = position + shift_amount
    elif direction == "decode":
       new_position = position - shift_amount
    end_text = end_text + alphabet[new_position]
  if direction == "encode":
    print(f"The encoded text is {end_text}")
  elif direction == "decode":
    print(f"The decoded text is {end_text}")
  
  
caesar(start_text=text, shift_amount=shift)
