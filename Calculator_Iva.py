##This is the program for calculating the Iva and the total price, including Iva based on the prices entered as codes##




#here,we enter the customer's details and the value of their order#
client_name=input("please,enter the client name: ")

bill=int(input("enter total bill amount:"))

#here,in this script,we determine the range of values applicable to IVA#
Iva=float(input("enter the aplicable Iva: "))*bill

charge_range=int(input("enter the value to which IVA will be applied: "))

#in this part of the code , we put the conditionals#
if bill >= charge_range:
    print(f"considering that the applicable IVA rate is {Iva} because your bill is  {bill}  ,therefor,your total account balance is:{bill+Iva}  MR/MS {client_name} ")

else:
    print(f"your total account balance is:{bill}  MR/MS {client_name} ")


#The result provided by the conditional statements will determine the value displayed in the console#