import tkinter as tk
from tkinter import messagebox


class CaesarCipher:
    def __init__(self, shift: int):
        if not isinstance(shift, int):
            raise ValueError("Shift value must be an integer.")
        self.shift = shift % 26  # Ensure shift stays within 0-25

    def encrypt(self, text: str) -> str:
        if not isinstance(text, str):
            raise ValueError("Text to encrypt must be a string.")
        return self._caesar_cipher(text, self.shift)

    def decrypt(self, text: str) -> str:
        if not isinstance(text, str):
            raise ValueError("Text to decrypt must be a string.")
        return self._caesar_cipher(text, -self.shift)

    def _caesar_cipher(self, text: str, shift: int) -> str:
        encrypted_text = []
        for char in text:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                encrypted_text.append(shifted_char)
            else:
                encrypted_text.append(char)  # Non-alphabetic characters remain unchanged
        return ''.join(encrypted_text)


class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Encryptor/Decryptor")

        # Labels and Entry fields
        self.label_text = tk.Label(root, text="Enter text:")
        self.label_text.pack()

        self.entry_text = tk.Entry(root, width=50)
        self.entry_text.pack(padx=50)

        self.label_shift = tk.Label(root, text="Enter shift value:")
        self.label_shift.pack()

        self.entry_shift = tk.Entry(root, width=10)
        self.entry_shift.pack()

        # Frame for buttons to place them side by side
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Encrypt and Decrypt buttons (side by side)
        self.button_encrypt = tk.Button(self.button_frame, text="Encrypt", command=self.encrypt_text)
        self.button_encrypt.pack(side=tk.LEFT, padx=10)

        self.button_decrypt = tk.Button(self.button_frame, text="Decrypt", command=self.decrypt_text)
        self.button_decrypt.pack(side=tk.LEFT, padx=10)

        # Result label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def encrypt_text(self):
        try:
            shift_value = int(self.entry_shift.get())
            text = self.entry_text.get()

            caesar_cipher = CaesarCipher(shift_value)
            encrypted_text = caesar_cipher.encrypt(text)

            self.result_label.config(text=f"Encrypted text: {encrypted_text}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid shift value.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt_text(self):
        try:
            shift_value = int(self.entry_shift.get())
            text = self.entry_text.get()

            caesar_cipher = CaesarCipher(shift_value)
            decrypted_text = caesar_cipher.decrypt(text)

            self.result_label.config(text=f"Decrypted text: {decrypted_text}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid shift value.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Create the main window and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
