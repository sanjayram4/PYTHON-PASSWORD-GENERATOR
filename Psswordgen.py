
#python password generator and save data base

import random
class PassswordGenerator:
    def __init__(self):
        self.store = {}
    def pass_gen(self):
        passwords = "1234567890!@#$%^&*()qwertyuiopasdfghjklzxcvbnmQWERTYUIOPSDFGHJKLZXCVBNM"
        user_size = int(input("Enter Password size eg(6 / 8 / 12 / 16) : "))
        temp_pass = ""
        for i in range(user_size):
            ran_pass = random.choice(passwords)
            temp_pass += ran_pass
        print("Your Password : ",temp_pass)
        user_store_pass = input("You store this password (yes / no) : ")
        if user_store_pass.lower() == "yes":
            user_email = input("Enter Your E-mail : ")
            self.store[user_email] = temp_pass
            print("Your Password Will Sucessfully Stored !!!")
        else:
            print("The Password is Gone.")
        temp_pass = ""
    def show_pass(self):
        for k,v in self.store.items():
            print(f"E-mail : {k}\nPassword : {v}")
passsword_gen = PassswordGenerator()
while True:
    print("1.Password Generator and store 2.Show Password")
    user_choice = input("Enter Your Choice : ")
    if user_choice == "1":
        passsword_gen.pass_gen()
    elif user_choice == "2":
        passsword_gen.show_pass()
    else:
        print("Enter Correct Option")