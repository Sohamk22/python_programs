#fizz_bizz
#using the for loop for the input numbers, we can define the range by changing the range for the loop
#simple if else conditions for printing Fizz Bizz
# % sign is used to find the remainder and '==' is used to compare the result

for number in range(1, 61):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
