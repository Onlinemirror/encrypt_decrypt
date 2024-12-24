Code Explanation
Interface with Tkinter:

Uses Text to enter text and display the result.
Buttons to encrypt, decrypt, save and load keys.
Event Handling:

Each button calls the associated function:
encrypt_text: encrypts the text entered by the user.
decrypt_text: decrypts the text.
save_key: saves the current key to the file key.key.
load_key: loads the key from a file.
Generating and Working with Keys:

The key is created when the program starts.
The user can save it to a file and load it later.
Error Messages:

If the user enters an empty field or incorrect data, a message is displayed via the messagebox.
