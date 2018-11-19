menu = 'MENU\n' 'pen burger: $5.00 - - glue burger: $1.00\n' 'glass burger: $2.00 - - paper burger: $4.00\n' 'peanut burger: $2.00 - - water burger: $9.00\n'
print (menu)

transaction = []

start = int (0)
finish = int (2)
order_number = (1)
while start < finish:
	
	print ("Welcome,", + order_number)
	name = input("What's your name?: ")
	transaction.append(name)
	order = input ("What do you want?: ")
	transaction.append(order)
	quantity = input ("How many?: ")
	transaction.append(quantity)
	order_number = order_number + 1
	start = start + 1
	for users in transaction:
		print(users)
	
