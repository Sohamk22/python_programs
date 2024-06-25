z_table = {
    -3.4: 0.0003,
    -3.3: 0.0005,
    -3.2: 0.0007,
    -3.1: 0.0010,

    3.1: 0.9990,
    3.2: 0.9993,
    3.3: 0.9995,
    3.4: 0.9997
}

while True:
    z_num = float(input("Enter the Z number"))

    if z_num in z_table:
        probability = z_table[z_num]
        print(f"Probability for Z-score {z_num} is: {probability:.4f}")
    else:
        print("Z-score is outside the range of the provided table (-3.4 to 3.4).") 

        print("Thank you")