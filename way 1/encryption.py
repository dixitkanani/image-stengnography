# Import necessary libraries
from PIL import Image
import stepic
import cryptocode

# Open the image within which the secret message is to be stored:
img = Image.open("1.jpg")
key=input("Enter key to edit(Security Key) : ")
text=input("Enter text to hide : ")
encoded = cryptocode.encrypt(text,key)

# Convert the message into UTF-8 format:
encoded = encoded.encode()
# Pass the image and message into the encode() function.
# This function returns a new image within which the message is hidden:
encoded_img = stepic.encode(img, encoded)
# Specify the name and extension for the new image generated:
encoded_img.save("new1.png")

print("Encryption Completed!")