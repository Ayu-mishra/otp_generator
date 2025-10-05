import time
import random

def generate_otp():
    otp= random.randint(100000, 999999)
    print(f"Your OTP is: {otp}")
    return otp

def verify_otp(sent_otp, valid_for= 30):
    start_time = time.time()

    while True:
        if time.time() - start_time > valid_for:
            print("OTP expaired! Plese request a new one")
            return False
        
        user_otp = input("Enter your OTP: ")
        if not user_otp.isdigit():
            print("Please enter digits only.")
            continue

        if int(user_otp) == sent_otp:
            print("OTP verified successfully")
            return True
        else:
            print("Incorrect OTP. Try again.")
print("----OTP VERIFICATION----")
otp = generate_otp()
verify_otp(otp, valid_for=30)