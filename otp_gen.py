import random

def generate_otp(length=4):
    otp = ""
    for i in range(length):
        otp += str(random.randint(0, 9))
    return otp


otp = generate_otp()
print("Your OTP:", otp)

