alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#將加密和解密的fun合併之後有兩種判斷方向的方式
def caesar(start_text, shift_amount):
  end_text = ""
  if direction == "decode":
      shift_amount = shift_amount * -1
  #方法一:
  #判斷語句在for外面，因為如果在for裡面會造成出錯
  #shift_amount跑第一次迴圈時會正常，因為shift_amount輸入會是正數，正數乘上-1就變成負數，實現相減的功能 ex:5*-1 = -5
  #但如果跑第二次迴圈，此時的shift_amount是剛剛紀錄的值(-5)，再乘上-1就變成正數
  
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text = end_text + alphabet[new_position]
  if direction == "encode":
    print(f"The encoded text is {end_text}")
  elif direction == "decode":
    print(f"The decoded text is {end_text}")
  
  
caesar(start_text=text, shift_amount=shift)
