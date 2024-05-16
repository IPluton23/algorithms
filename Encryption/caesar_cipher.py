# Simple Caesar encryption

print("Enter a text to be encrypted:")
plaintext = input()

ciphertext = "" # Value for encrypted message

print("Enter shift value:")

# Checks if shift value is number if not asks to input value again
while True:
    try:
        shift = int(input())
        break
    except ValueError:
        print("Incorrect value. Please enter a number:")


plaintext = plaintext.upper()

# Shifting letters and assigning them to ciphertext
for letter in plaintext:
    # This piece is ensuring that ciphertext will be alphabet letter not some ASCII signs after Z value
    if ord(letter) + shift > ord('Z'):
        new_shift = (ord(letter) + shift) - (ord('Z') + 1)
        ciphertext += chr(ord('A') + new_shift)
    else:
        ciphertext += chr(ord(letter) + shift)

print("Your encrypted message is: \n" + ciphertext)