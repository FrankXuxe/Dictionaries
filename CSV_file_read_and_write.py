import csv

customers = open('customers.csv', 'r')

customer_file = csv.reader(customers, delimiter= ',')

next(customer_file)

for record in customer_file:
    print(record)
    print('First Name: ', record[1])
    print('Last Name: ', record[2])
    input()

