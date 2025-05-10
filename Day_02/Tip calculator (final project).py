# Project = To calculate total bill for each person with adding tip 

Total_bill = input("what's your total bill : " )

tip_percentage = input("what percentage tip would you like to give 10 ,12 or 15? : ")

total_peers = input("how many people to split the bill ? : ")

tip_to_pay = (float(Total_bill)*float(tip_percentage)/100)/float(total_peers)

bill_for_each = float(Total_bill)/float(total_peers)  

total_bill_for_each = bill_for_each + tip_to_pay

print(round(total_bill_for_each,2))
