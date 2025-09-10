import random
import string

chars =" " +string.punctuation + string.ascii_letters + string.digits
chars=list(chars)
key = chars.copy()

random.shuffle(key)
if __name__=="__main__":
    print(chars)

def encrypt(message):
    cipher=""
    for i in message:
        if i in chars:
            index=chars.index(i)
            cipher+=key[index]
    return cipher


def decrypt(cipher1):
    message=""
    for i in cipher1:
        if i in key:
            index=key.index(i)
            message+=chars[index]

    return message



def take_input():
    print("Welcome to the Encryption-Decryption Program!")
    print("----------------------------")
    message=input("Enter Your Mmesage : ")
    choice=input("Input 1 for encryption and 2 for decryption :")
    if choice=='1':
        print(f"Encrpted message is : {encrypt(message)}")
    elif choice=='2':
        print(f"Decrypted message is : {decrypt(message)}")
    else:
        print("Invalid Input")

    if input("Do you want to continue ? (y/n) : ").lower()=='y':
        take_input()
    else:
        print("Thank you for using the program. Goodbye!")
    


