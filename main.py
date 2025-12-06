## inputs we need from the users 
# total rent 
# total food 
# Total food for snacking 
# Electricity units spend 
# charge per unit 
# person living in room/flat

## output 
# total amount you've to pay is 

rent=int(input("Enter Your hostel/flat rent = "))
food=int(input("Enter the amount of food ordered = "))
Electricity_spend =int(input("Enter the amount of electricity = "))
charge_per_unit= int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of person living in room /flat = "))


Total_bill = Electricity_spend * charge_per_unit

output =(food+rent+Total_bill)// persons

print("each person will pay = ", output)