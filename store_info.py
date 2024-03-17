# Problem statement: Take user input for first)name last_name, agae, dob, add_street1, addre_street2, city, country, pin_code. And store it in CSV file.
# Logic:
#1. Take user input for all values
#2. Store in a variable in CSV format
#3. Open the file
#4.  Wrtie the stored information
#5. Close the file


# Take user input

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
date_of_birth = input("Enter your date of birth: ")
address_street1 = input("Enter your street 1 address: ")
address_street2 = input("Enter your street 2 address: ")
city = input("Enter your city:")
country = input("Enter your country:")
pin_code = input("Enter your pin code:")

# Store it in CSV format
info=(first_name+","+last_name+","+age+","+date_of_birth+","+address_street1+","+address_street2+","+city+","+country+","+pin_code)
print(info)

#Open a file
f1 = open("c:\python\information.csv", 'w')
f1.write(info)

#write the stored info
#close the file
f1.close()




