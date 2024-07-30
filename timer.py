import time

def countdown(t, message):
  
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  
        time.sleep(1)
        t -= 1
    print("\n" + message)  



duration = int(input("Enter countdown duration in seconds: "))
custom_message = input("Enter your custom message: ")

countdown(duration, custom_message)
