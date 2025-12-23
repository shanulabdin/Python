# def convertToFahrenheit(c):
#     return (c * 9/5) + 32

# print(convertToFahrenheit(0))
# print(convertToFahrenheit(25))
# print(convertToFahrenheit(100))



# def isEligibleForFreeShipping(totalAmount):
#     return totalAmount >= 500

# print(isEligibleForFreeShipping(400))
# print(isEligibleForFreeShipping(500))
# print(isEligibleForFreeShipping(900))



# ---------- Task 3: Movie Ticket Price ----------

def ticketPrice(age):
    regular_price = 100
    
    if age < 12:
        return regular_price * 0.5      # 50% discount
    elif age >= 60:
        return regular_price * 0.7      # 30% discount
    else:
        return regular_price      

print(ticketPrice(8))    
print(ticketPrice(30))   
print(ticketPrice(65)) 

# #  Task 4: Sales Commission Calculator 
# def calculateCommission(salesAmount):
#     if salesAmount < 1000:
#         return salesAmount * 0.05
#     elif salesAmount <= 5000:
#         return salesAmount * 0.1
#     else:
#         return salesAmount * 0.15

# print('---')
# print(calculateCommission(500))
# print(calculateCommission(3000))
# print(calculateCommission(8000))
# print('---')


# #  Task 5: Electricity Bill Calculator 
# def calculateBill(units):
#     if units <= 100:
#         return units * 5
#     elif units <= 200:
#         return 100 * 5 + (units - 100) * 7
#     else:
#         return 100 * 5 + 100 * 7 + (units - 200) * 10

# print("task5 tests")
# print(calculateBill(50))
# print(calculateBill(150))
# print(calculateBill(250))



# #  Task 6: Salary Bonus Calculator 
# def calculateBonus(salary):
#     if salary < 30000:
#         return salary * 0.05
#     elif salary <= 70000:
#         return salary * 0.1
#     else:
#         return salary * 0.15

# print("task6 tests")
# print(calculateBonus(25000))
# print(calculateBonus(50000))
# print(calculateBonus(90000))
