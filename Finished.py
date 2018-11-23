import re

def initialPrompt():
    print ("Welcome to The Hungry Snake!")
    print ("We are open from 10 AM to 10 PM")


def stats(orders, burgersOrdered):
    print ( "\n\n*** Summary Statistics *** ")
    if (len(orders) == 0):
        print ( "No summary statistics available since no orders were placed")
        return

    if (len(orders) < 50):
        print ( "There was no fiftieth customer")
    else:
        print ( "The name of the fiftieth customer is %s\n" % orders[49][0])

    print ( "The client with the longest name is %s" % max([order[0] for order in orders], key=len))

    # orders = [[customerName, hour, totalCost]]
    topClients =  sorted(orders, key = lambda x: int(x[2]), reverse = True)

    if (len(topClients) >= 3):
        print ( "The best customers (from most to least) are %s: %.2f, %s: %.2f and %s: %.2f" % (topClients[0][0],topClients[0][2], topClients[1][0], topClients[1][2], topClients[2][0], topClients[2][2])) 
    else:
        print ( "There are fewer than 3 clients. Here they are: ")
        print ( [item[0] for item in topClients])
        
    topSellingBurgers = sorted(burgersOrdered.items(), key = lambda x: int(x[1]), reverse=True)[0:3]
    print ( "The best selling burgers (from most to least) are %s: %d, %s: %d, and %s: %d" % (topSellingBurgers[0][0],topSellingBurgers[0][1], topSellingBurgers[1][0],topSellingBurgers[1][1], topSellingBurgers[2][0], topSellingBurgers[2][1])) 

    if (len(topClients) >= 2):
        print ( "The client with the second-to-lowest bill is %s: %.2f" % (topClients[-2][0], topClients[-2][2]))

    clientsByHour = {'10 AM': 0, '11 AM' : 0, '12 PM' : 0, '1 PM' : 0, '2 PM' : 0, '3 PM' : 0, '4 PM' : 0, '5 PM' : 0, '6 PM' : 0
            , '7 PM' : 0, '8 PM' : 0, '9 PM' : 0}
    salesByHour= {'10 AM': 0.0, '11 AM' : 0.0, '12 PM' : 0.0, '1 PM' : 0.0, '2 PM' : 0.0, '3 PM' : 0.0, '4 PM' : 0.0, '5 PM' : 0.0, '6 PM' : 0.0
            , '7 PM' : 0.0, '8 PM' : 0.0, '9 PM' : 0.0}

    for order in orders:
        clientsByHour[order[1]] += 1
        salesByHour[order[1]] += order[2]

    maxClientHour = max(clientsByHour, key=clientsByHour.get)
    maxSalesHour = max(salesByHour, key=salesByHour.get)

    print ( "%s was the hour with the most clients (%d)" % ( maxClientHour, clientsByHour[maxClientHour] ))

    print ( "%s was the hour with the most sales ($%.2f)" % ( maxSalesHour, salesByHour[maxSalesHour] ))

    print ( "Total sales of the day = $%.2f" % sum([order[2] for order in orders]))  
        

def printMenu (burgers):
    menu = "\t*** MENU ***'\n" 
    count = 1
    for burgerName, burgerPrice in burgers.items():
        menu += '\t\t%d) %s Burger: %.2f\n' % (count, burgerName, burgerPrice)
        count += 1 

    print ( menu )


def start():
    # orders = [[customerName, hour, totalCost]]
    orders = []
    burgersOrdered = {'Glue' : 0, 'Glass' : 0, 'Peanut' : 0, 'Paper' : 0, 'Pen' : 0, 'Water' : 0}
    burgers = {'Glue' : 1.00, 'Glass' : 2.00, 'Peanut' : 2.00, 'Paper' : 4.00, 'Pen' : 5.00, 'Water' : 9.00}
    hours = ['10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM', '9 PM']
    initialPrompt()

    customerNumber = 0;
    customerName = ""
    currentHour = 0;

    while (True):
        print ( ("Welcome customer number: %d\nIt is currently the hour of %s") % (customerNumber + 1, hours[currentHour]))

        while (True):
            timePrompt = str (input("\tTo advance to the next hour, please type 'shift'; else, press any key: ") )

            if (timePrompt == 'shift'):
                currentHour += 1 
                if (currentHour >= len(hours)):
                    print ("The restaurant is now closed")
                    break;
                else:
                    print (("The time is now %s") % (hours[currentHour]) )
            else:
                break;

        customerName = str( input("\tPlease enter customer name or leave blank to stop orders: ") )
        if (customerName == ''):
            break;


        orders.append([customerName, hours[currentHour], 0.0])
        
        while (True):
            printMenu (burgers)
            print ("\tPlease enter which burger you'd like (1-6) or leave blank to finish order")
            burger = str( input("\tBurger selection: ") )
            if ( re.match("^[1-6]{1}$", burger) ):
                quantity = str( input("\tQuantity: "))
                if (re.match("^[0-9]+$", quantity) ): 
                    burger = int(burger)
                    burgersOrdered[list(burgers.keys())[burger-1]] += int(quantity)
                    orders[customerNumber][2] += (float(quantity) * burgers[list(burgers.keys())[burger-1]] )

                else:
                    print ("Invalid input, cancelled selection")

            if (burger == ''):
                print ( "Total order for this customer equals %.2f" % orders[customerNumber][2])
                break

        customerNumber += 1 


    stats(orders, burgersOrdered)
    

start()
print ( )
