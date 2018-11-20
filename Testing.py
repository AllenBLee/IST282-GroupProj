menu = 'MENU\n' 'pen burger: $5.00 - - glue burger: $1.00\n' 'glass burger: $2.00 - - paper burger: $4.00\n' 'peanut burger: $2.00 - - water burger: $9.00\n'
print (menu)
transaction = []

pen_burger = float (5.00)
glue_burger = float (1.00)
glass_burger = float (2.00)
paper_burger = float (4.00)
peanut_burger = float (2.00)
water_burger = float (9.00)
start = int (0)#10AM
finish = int (2)#10PM
order_number = (1)#less than 101
total_cost = float (0.0)


while start < finish and order_number != 3:                                    
	
	print ("Welcome,", + order_number)
	first_name = input("What's your first name?: ")
	transaction.append(first_name)
	last_name = input("What's your last name?: ")
	transaction.append(last_name)
	order = input ("What do you want?: ")
	transaction.append(order)
	quantity = float(input ("How many?: "))
	transaction.append(quantity)
		
	if order == "pen burger":
		total_cost = quantity * (5.00)
	if order == "glue burger":
		total_cost = quantity * (1.00)
	if order == "glass burger":
		total_cost = quantity * (2.00)
	if order == "paper burger":
		total_cost = quantity * (4.00)
	if order == "peanut burger":
		total_cost = quantity * (2.00)
	if order == "water burger":
		total_cost = quantity * (9.00)
	
	transaction.append(total_cost)
	order_number = order_number + 1
	start = start + 1
	
	first_name = transaction[0]
	last_name = transaction[1]
	order = transaction[2]
	quantity = transaction[3]
	total_cost = transaction[4]
	
	print (transaction)
	

	
#(00:00, firstname, lastname, burgertype, quantity, $cost)
