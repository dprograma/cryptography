'''Polygraphic Cipher using Python'''


class Cryptographer:
    diction = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, msg, k):
        self.message = msg
        self.key = k

    def encrypt(self):
        encrypted_msg = ""
        s = 0
        for i in self.message:
            idx = Cryptographer.diction.find(i)
            if idx != -1:
                idx = idx + Cryptographer.diction.find(self.key[s])
                idx = idx % len(Cryptographer.diction)
                encrypted_msg += Cryptographer.diction[idx]
                s += 1
                if s == len(self.key):
                    s = 0
            else:
                encrypted_msg += i
        return encrypted_msg

    def decrypt(self):
        decrypted_msg = ""
        s = 0
        for i in self.message:
            idx = Cryptographer.diction.find(i)
            if idx != -1:
                idx = idx - Cryptographer.diction.find(self.key[s])
                idx = idx % len(Cryptographer.diction)
                decrypted_msg += Cryptographer.diction[idx]
                s += 1
                if s == len(self.key):
                    s = 0
            else: 
                decrypted_msg += i
        return decrypted_msg.lower()

    def display_cryto(self):
        self.message = self.message.upper()
        self.key = self.key.upper()

        user_input = input("Enter \"e\" for Encryption and \"d\" for Decryption. (e\d)").lower()
        if user_input == "e":
            print("Encryted Message: \n")
            print(self.encrypt())
        elif user_input == "d":
            print("Decryted Message: \n")
            print(self.decrypt())


while True:
    message = input("Enter plaintext: \n")
    key = input("Enter keystream: \n")
    ncrypt = Cryptographer(message, key)
    ncrypt.display_cryto()
