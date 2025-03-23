# Take encrypted flag input from the user
enc_data = input("Enter the encrypted flag: ")

flag = ""  # Store the decrypted flag

# Process each Unicode character and extract two original characters
for char in enc_data:
    combined = ord(char)  # Get the Unicode value
    high = (combined >> 8) & 0xFF  # Extract the first character (high byte)
    low = combined & 0xFF  # Extract the second character (low byte)
    
    flag += chr(high)  # Add first character
    if low != 0:  # If second character exists (not zero-padded)
        flag += chr(low)

print("Decrypted flag:", flag)
