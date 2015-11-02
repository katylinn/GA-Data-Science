## Class 2 Homework: Command Line Chipotle

#### Command Line Tasks

##### Q1
Each column is an item in an order.  For Example, a "Side of Chips" or a "Chicken Burrito".  Each order can contain multiple items, so there is an *order_id* column to identify all the contents of an order.  
**Rest of the Columns**\
*quantity* - integer number of identical items in the same order\
*item_name* - string that describes the item (probably very similar to what is listed on the menu)\
*choice_description* - List of modifiers or choices for the item.  For Example, an Izze drink  comes in many flavors, but the drink requested in order 1 is Clemintine Flavored.\
*item_price* - Subtotal for the row ($)


```sh
$ head chipotle.tsv
```
order_id | quantity|	item_name|	choice_description|	item_price
--- | --- | ---|--- | --- | 
1|	1|	Chips and Fresh Tomato Salsa	|NULL|	$2.39|
1|	1|	Izze|	[Clementine]|	$3.39 
1|	1|	Nantucket Nectar|	[Apple]|	$3.39 
1|	1|	Chips and Tomatillo-Green Chili Salsa|	NULL	|$2.39 
2|	2|	Chicken Bowl|	[Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]]|	$16.98 
3|	1|	Chicken Bowl|	[Fresh Tomato Salsa (Mild), [Rice, Cheese, Sour Cream, Guacamole, Lettuce]]|	$10.98 
3|	1|	Side of Chips|	NULL|	$1.69 
4|	1|	Steak Burrito|	[Tomatillo Red Chili Salsa, [Fajita Vegetables, Black Beans, Pinto Beans, Cheese, Sour Cream, Guacamole, Lettuce]|$11.75 
4|	1|	Steak Soft Tacos|	[Tomatillo Green Chili Salsa, [Pinto Beans, Cheese, Sour Cream, Lettuce]]	|$9.25 
```sh
$ tail chipotle.tsv
```
order_id | quantity|	item_name|	choice_description|	item_price
--- | --- | ---|--- | --- | 
1831|	1|	Carnitas Bowl|	[Fresh Tomato Salsa, [Fajita Vegetables, Rice, Black Beans, Cheese, Sour Cream, Lettuce]]|	$9.25 
1831|	1|	Chips|	NULL|	$2.15 
1831|	1|	Bottled Water|	NULL|	$1.50 
1832|	1|	Chicken Soft Tacos	[Fresh Tomato Salsa, [Rice, Cheese, Sour Cream]]|	$8.75 
1832|	1|	Chips and Guacamole|	NULL|	$4.45 
1833|	1|	Steak Burrito|	[Fresh Tomato Salsa, [Rice, Black Beans, Sour Cream, Cheese, Lettuce, Guacamole]]|	$11.75 
1833|	1|	Steak Burrito|	[Fresh Tomato Salsa, [Rice, Sour Cream, Cheese, Lettuce, Guacamole]]|	$11.75 
1834|	1|	Chicken Salad Bowl|	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Guacamole, Lettuce]]|	$11.25 
1834|	1|	Chicken Salad Bowl|	[Fresh Tomato Salsa, [Fajita Vegetables, Lettuce]]|	$8.75 
1834|	1|	Chicken Salad Bowl|	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Lettuce]]|	$8.75 

##### Q2
Given the readout of the tail above, There appear to be 1834.  One easy check to make sure the list is actually sorted:
```sh
$ sort -n  chipotle.tsv
```
That output appears to confirm the conclusion above.  However, here is still some chance that there is a chunk of order_ids missing from the middle

##### Q3
There are **4623** lines in chipotle.tsv
```sh
$ wc -l chipotle.tsv
```

##### Q4

```sh
$ grep -c "Steak Burrito" chipotle.tsv 
368
$ grep -c "1\tSteak Burrito" chipotle.tsv 
352
$ grep -c "2\tSteak Burrito" chipotle.tsv 
14
$ grep -c "3\tSteak Burrito" chipotle.tsv 
2
$ python -c "print(352*1 + 14*2 + 2*3)"
386
```
There are 368 orders that contain at least 1 steak burrito.  However, there are several orders that contain more than one, so there are actually 386 Steak Burritos total.
```sh
$ grep -c "Chicken Burrito" chipotle.tsv 
553
$ grep -c "1\tChicken Burrito" chipotle.tsv 
521
$ grep -c "2\tChicken Burrito" chipotle.tsv 
28
$ grep -c "3\tChicken Burrito" chipotle.tsv 
2
$ grep -c "4\tChicken Burrito" chipotle.tsv 
2
$ python -c "print(521*1 + 28*2 + 2*3+ 2*4)"
591
```
Calculating with logic similar to above, there are 591 Chicken Burritos.  Therefore, we know that the Chicken Burrito is more popular (591>386)

##### Q5
Chicken Burritos with Pinto Beans
```sh
$ grep "1\tChicken Burrito" chipotle.tsv | grep -c "Pinto Beans"
102
$ grep "2\tChicken Burrito" chipotle.tsv | grep -c "Pinto Beans"
3
$ grep "3\tChicken Burrito" chipotle.tsv | grep -c "Pinto Beans"
0
$ grep "4\tChicken Burrito" chipotle.tsv | grep -c "Pinto Beans"
0
$ python -c "print(102+3*2)"
108
```
Chicken Burritos with Black Beans
```sh
$ grep "1\tChicken Burrito" chipotle.tsv | grep -c "Black Beans"
261
$ grep "2\tChicken Burrito" chipotle.tsv | grep -c "Black Beans"
19
$ grep "3\tChicken Burrito" chipotle.tsv | grep -c "Black Beans"
0
$ grep "4\tChicken Burrito" chipotle.tsv | grep -c "Black Beans"
2
$ python -c "print(261+19*2+4*2)"
307
```
Chicken Burritos are more often ordered with black beans (108 < 307)

Its a little disconcerting that 108+307 is far fewer than the 591 Chicken Burritos we calculated in the previous question.  It turns out there are several Chicken Burritos with no Beans
```sh
$ grep "1\tChicken Burrito" chipotle.tsv | grep -v -c "Beans"
178
$ grep "2\tChicken Burrito" chipotle.tsv | grep -v -c "Beans"
6
$ grep "3\tChicken Burrito" chipotle.tsv | grep -v -c "Beans"
2
$ grep "4\tChicken Burrito" chipotle.tsv | grep -v -c "Beans"
0
$ python -c "print(178+6*2+2*3)"
196
```
And we also double counted some Burritos with both types of beans (-v flag performs the inverse operation, finding lines without "Beans")

```sh
$ grep "Chicken Burrito" chipotle.tsv | grep "Pinto Beans" | grep -c "Black Beans"
20
```

So we can feel better that 108+307+196-20=591, which is what we found in previous question.

##### Q6
```sh
$ find . -regex ".*\.[ct]sv"
./data/airlines.csv
./data/bank-additional.csv
./data/bikeshare.csv
./data/chipotle.tsv
./data/drinks.csv
./data/hitters.csv
./data/imdb_1000.csv
./data/sms.tsv
./data/titanic.csv
./data/ufo.csv
./data/vehicles_test.csv
./data/vehicles_train.csv
./data/yelp.csv
```

##### Q7
The grep command searches recursively across all the files in the repo, and sends the result to the wc command, which counts 48 lines
```sh
$ grep -r -i "dictionary" . | wc -l
48
```
It is, in fact, approximate, since grep would not count multiple occurences within the same line.

##### Q8
Finding something "interesting" in a data set alwasy feels like a fool's errand, but I did play around with the commands from the advanced section to look at the most common ways to "fix up" the various dishes, ie, the most common collections of toppings from the *choice_description* column.  

Note: This method assumes that a given collection of ingredients only ever appears in a single order.  Ie, if [X, Y, Z] exists in the set, then [Y, X, Z] does not, nor does any other permutation of the same ingredients.  I believe this assumption holds, but only from my own manual inspection. 

Top Preparations for Chicken Burritos:
```sh
$ grep "Chicken Burrito" chipotle.tsv | cut -f4 | sort | uniq -c |sort -r|head -n 5
  16 [Fresh Tomato Salsa, [Rice, Black Beans, Cheese, Sour Cream, Lettuce]]
  13 [Fresh Tomato Salsa, [Rice, Black Beans, Cheese, Sour Cream]]
  12 [Fresh Tomato Salsa, [Rice, Black Beans, Cheese, Sour Cream, Guacamole, Lettuce]]
  10 [Fresh Tomato Salsa, [Rice, Cheese, Sour Cream, Lettuce]]
  10 [Fresh Tomato Salsa, [Rice, Black Beans, Cheese, Lettuce]]
```
Top Preparations for Steak Burritos:
```sh
$ grep "Steak Burrito" chipotle.tsv | cut -f4 | sort | uniq -c |sort -r|head -n 5
  12 [Fresh Tomato Salsa (Mild), [Pinto Beans, Rice, Cheese, Sour Cream]]
   6 [Tomatillo Green Chili Salsa, [Fajita Vegetables, Rice, Cheese, Sour Cream, Lettuce]]
   6 [Roasted Chili Corn Salsa (Medium), [Rice, Fajita Veggies, Cheese, Sour Cream, Lettuce]]
   5 [[Roasted Chili Corn Salsa (Medium), Tomatillo-Red Chili Salsa (Hot)], [Black Beans, Rice, Cheese, Sour Cream, Lettuce]]
   5 [Roasted Chili Corn Salsa (Medium), [Rice, Black Beans, Sour Cream]]
```
Top Preparations for Chicken Bowls:
```sh
$ grep "Chicken Bowl" chipotle.tsv | cut -f4 | sort | uniq -c |sort -r|head -n 5
  17 [Fresh Tomato Salsa, [Fajita Vegetables, Rice]]
  14 [Fresh Tomato Salsa, [Rice, Black Beans, Cheese, Sour Cream, Lettuce]]
  14 [Fresh Tomato Salsa, [Rice, Black Beans, Cheese, Sour Cream, Guacamole, Lettuce]]
  13 [Fresh Tomato Salsa, [Rice, Cheese, Sour Cream, Lettuce]]
  13 [Fresh Tomato Salsa, [Rice, Cheese, Lettuce]]
```

Top Preparations for Steak Bowls:
```sh
$ grep "Steak Bowl" chipotle.tsv | cut -f4 | sort | uniq -c |sort -r|head -n 5
   5 [Roasted Chili Corn Salsa, [Rice, Pinto Beans, Sour Cream, Cheese, Guacamole]]
   5 [Fresh Tomato Salsa, [Rice, Black Beans, Cheese, Sour Cream, Guacamole]]
   5 [Fresh Tomato Salsa (Mild), [Rice, Cheese, Sour Cream, Lettuce]]
   3 [Tomatillo Red Chili Salsa, [Rice, Black Beans, Cheese]]
   3 [Tomatillo Red Chili Salsa, [Rice, Black Beans, Cheese, Sour Cream, Lettuce]]
```
Most Popular Soda:
(Canned Soft Drink or Canned Soda)
```sh
$ grep "Canned" chipotle.tsv | cut -f4 | sort | uniq -c |sort -r|head -n 5
 110 [Diet Coke]
 102 [Coke]
  72 [Sprite]
  31 [Lemonade]
  26 [Coca Cola]
```






