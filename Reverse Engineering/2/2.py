flag = "G8KEY{Tw1N_Sh1fT_C1ph3r}"  # Your predefined flag
enc_data = ""  # Store Unicode output

for i in range(0, len(flag), 2):
    if i + 1 < len(flag):
        combined = (ord(flag[i]) << 8) | ord(flag[i + 1])  # Pack two characters
    else:
        combined = (ord(flag[i]) << 8) | 0  # Zero-padding if odd length

    enc_data += chr(combined)  # Convert to Unicode character

# Save encrypted Unicode string to a file
with open("flag.enc", "w", encoding="utf-8") as f:
    f.write(enc_data)

print("Encrypted flag saved as 'flag.enc'!")
