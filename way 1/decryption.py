# Import necessary libraries
from PIL import Image
import stepic
import cryptocode

# Open the image from which the secret message is to be extracted:
image = Image.open("new1.png")

# Pass the above image into the decode() function.
# This function returns the secret message in the form of a string:
decoded_msg = stepic.decode(image)

print("Decryption Completed!")
# Display the message
print("Decoded Key :", decoded_msg)
key=input("Enter key to edit(Security Key) : ")
## And then to decode it:
decoded = cryptocode.decrypt(decoded_msg, key)
print("Decoded message :", decoded)
