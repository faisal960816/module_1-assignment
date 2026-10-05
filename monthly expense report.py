# monthly expense report
name= input("enter your name :")
monthly_income = float(input("enter your income:"))
rent=int(input("enter your rent:"))
food_expense=int(input("enter your food expense:"))
travel_expense=int(input("enter your travel expense:"))
entertainment_expense=int(input("enter your entertainment expense:"))
other_expense=int(input("enter your other expense:"))
total_expense=(rent+food_expense+travel_expense+entertainment_expense+other_expense)
remaning_money=monthly_income-total_expense
saving_persentage=(total_expense/monthly_income)*100
daily_expense=total_expense/30
weekly_expense=total_expense/4
saving_target=int(input("enter your saving target:"))
print(f"""my name is:{name}\n
my salary is:{monthly_income}\n
total expense is:{total_expense}\n
my saving money is::{remaning_money}\n
my saving persentage is:{saving_persentage}\n
my daily expense is:{daily_expense}\n
my weekly expense is:{weekly_expense}\n
my saving target is:{saving_target}\n""")


 
