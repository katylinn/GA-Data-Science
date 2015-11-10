'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv
with open("chipotle.tsv", mode="rU") as file:
    reader = csv.reader(file, delimiter="\t")
    file_nested_list = [line for line in reader]


'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
header = file_nested_list[0]
data = file_nested_list[1:]


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!  Break the problem into steps and then code each step
'''
        
average_order_price = sum([float(row[4][1:]) for row in data])/1834

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
sodas = []

for row in data:
    if row[2] == "Canned Soda" or row[2] == "Canned Soft Drink":
        if row[3] not in sodas:
            sodas.append(row[3])



'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

topping_counts = [len(row[3].split(",")) for row in data if "Burrito" in row[2]]
average_number_toppings= sum(topping_counts)/float(len(topping_counts))

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
import collections

d = collections.defaultdict(int)
for row in data:
    if "Chips" in row[2]:
        d[row[2]] += int(row[1])

    

'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''

#[your code here]
