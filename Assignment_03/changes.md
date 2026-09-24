Assignment 03 - CHANGES 
Name: Than Min Aung 
Student ID: 6705140064

1. What I Changed
Change 1 - Product Tuples
Original problem

In the original program, products were stored as tuples:

("Laptop", 1200.0, "electronics")

This means the program had to remember that index 0 was the name, index 1 was the price, and index 2 was the category.
My change

I created a Product class with clear attributes:

Product(name, price, category)

The class also contains methods for handling product tax.
OOP concept

Classes and encapsulation.

The product's information and behaviour are now kept together in one object.
How I verified it

I ran:

python Assignment_3.py

The self-test compared the new output with the original GOLDEN_OUTPUT and confirmed that the behaviour was unchanged.
Change 2 - Order Items
Original problem

The original program stored order items as tuples such as:

(0, 1)

The first value represented the product index and the second value represented the quantity.
My change

I created an OrderItem class.

An OrderItem contains:

    a Product

    a quantity

It also has methods such as line_total() and tax().
OOP concept

Composition.

An OrderItem has a Product.
How I verified it

I checked that every product and quantity from the original orders was kept unchanged. I then ran the self-test and confirmed that every receipt line was the same.
Change 3 - Order Class
Original problem

The original program represented an entire order using a tuple:

("Alice", "gold", [(0, 1), (1, 2), (2, 3)])

This made the order difficult to understand and maintain.
My change

I created an Order class.

An Order contains:

    one Customer

    multiple OrderItem objects

The Order class is responsible for calculations such as:

subtotal()
discount()
tax()
total()
points()

OOP concept

Composition and encapsulation.

The order has a customer and has many order items.
How I verified it

I compared the original orders with the objects created by build_orders(). I then ran the self-test and confirmed that the four receipts and grand total remained unchanged.
Change 4 - Membership If/Else Statements
Original problem

The original program used repeated if/elif statements to calculate membership discounts:

if t == "none":
    ...
elif t == "silver":
    ...
elif t == "gold":
    ...
elif t == "platinum":
    ...

The same type of logic was repeated when calculating points.
My change

I created a base Customer class and different subclasses:

Customer
    |
    +-- SilverCustomer
    +-- GoldCustomer
    +-- PlatinumCustomer

Each membership class has its own discount_rate() and points_multiplier() methods.
OOP concept

Inheritance and polymorphism.

The Order class does not need to check the customer's tier. It simply asks the customer for the discount rate and points multiplier.
How I verified it

I checked the original rules:

    Silver: 2% or 5%

    Gold: 5% or 10%

    Platinum: 10% or 15%

    None: 0%

I also checked the points multipliers:

    None: x1

    Silver: x2

    Gold: x3

    Platinum: x5

After checking these values, I ran the self-test.
Change 5 - Calculation and Printing
Original problem

The original calc() function performed calculations and printed the receipt at the same time.

This mixed two different responsibilities together.
My change

I separated the calculations into individual methods:

subtotal()
discount()
tax()
total()
points()

These methods return numbers instead of printing.

I also created:

receipt()

to build the receipt text.

Finally, refactored_main() handles printing.
OOP concept

Separation of concerns.

Calculation and output are now separate responsibilities.
How I verified it

I checked that the calculation methods do not contain print() statements.

I then ran the program and confirmed that the final output matched the original output exactly.
Change 6 - Magic Numbers
Original problem

The original program contained numbers directly inside calculations, for example:

0.07
0.03
10
100

These numbers do not clearly explain what they mean.
My change

I replaced them with named constants:

TAX_RATE = 0.07
FOOD_TAX_RATE = 0.0
DISCOUNT_THRESHOLD = 100
BULK_QTY_THRESHOLD = 10
BULK_DISCOUNT_RATE = 0.03
POINTS_DIVISOR = 10

I also created named constants for the different membership discount rates and point multipliers.
OOP concept

Clean code and meaningful names.

The code is easier to read because the names explain the business rules.
How I verified it

I compared every constant with the original business rules to make sure I did not change any values.

I then ran the self-test.
Change 7 - Global Variable
Original problem

The original calc() function contained:

global TAXRATE

The function did not actually need to modify the global variable.
My change

The refactored program uses named constants instead of unnecessary global state.

For example:

TAX_RATE = 0.07

OOP concept

Encapsulation and reducing global state.

This makes the code safer and easier to understand.
How I verified it

I checked that the tax calculation still produced:

    7% for electronics

    7% for stationery

    0% for food

I then ran the self-test.
Change 8 - Product Tax Responsibility
Original problem

The original calc() function decided the tax based on the product category:

if cat == "food":
    ...
else:
    ...

This meant the main calculation function had to know details about products.
My change

I moved the tax responsibility into the Product class.

The product now has:

tax_rate()

and:

tax_for(quantity)

The OrderItem can ask its product to calculate the appropriate tax.
OOP concept

Encapsulation and responsibility.

The product now knows how its own tax is determined.
How I verified it

I checked that food products remain tax-free and electronics and stationery products use the 7% tax rate.

I then ran the self-test to confirm that the receipt tax amounts did not change.
Change 9 - Constructor Validation
Original problem

The original program used tuples and did not validate object state.

For example, there was no object constructor checking whether a quantity was valid.
My change

I added validation to constructors.

For example:

if quantity < 1:
    raise ValueError("Quantity must be at least 1.")

The Product constructor also checks the product name, price, and category.
OOP concept

Encapsulation and validation.

Objects should not be allowed to contain obviously invalid state.
How I verified it

I checked that all original data is valid and can still be used normally.

I also reviewed the validation conditions to make sure they do not change any of the original valid data.
2. Short Reflection

The change that improved the code the most was replacing the repeated membership if/elif statements with inheritance and polymorphism. In the original program, the membership rules were repeated in different parts of the code, which made the program harder to maintain. In the refactored version, each customer type is responsible for its own discount and points rules. Separating the calculations from receipt printing also made the code easier to understand and test. Keeping the behaviour exactly the same was the most important challenge because even a small change to the receipt format, rounding, or calculation could cause the self-test to fail. I used the original GOLDEN_OUTPUT and the supplied self-test to verify that the refactored program still produced exactly the same output.
3. Prompt Log - Level 2
Prompt 1
My prompt to the AI

"Can you refactor this messy store program into a clean object-oriented design while keeping the exact same output?"
What the AI suggested

The AI suggested creating classes for the main parts of the store, including:

    Product

    OrderItem

    Customer

    Order

It also suggested using composition so that an Order contains a Customer and multiple OrderItems.
What I did

I accepted the overall idea and implemented the classes. I adjusted the design to match the assignment requirements.
How I checked it

I read through the code and checked the relationships between the classes. I then ran the self-test.
Prompt 2
My prompt to the AI

"How can I replace the tier if/elif statements with inheritance and polymorphism?"
What the AI suggested

The AI suggested creating a base Customer class and subclasses for Silver, Gold, and Platinum customers.

Each subclass could provide its own discount and points behaviour.
What I did

I accepted the design and created:

Customer
SilverCustomer
GoldCustomer
PlatinumCustomer

I implemented discount_rate() and points_multiplier() in the customer classes.
How I checked it

I compared the discount rates and point multipliers with the original program and ran the self-test.
Prompt 3
My prompt to the AI

"How should I separate calculations from receipt printing?"
What the AI suggested

The AI suggested using separate methods for:

subtotal
discount
tax
total
points

It also suggested keeping receipt generation separate from the calculations.
What I did

I implemented these methods in the Order class and created a separate receipt() method.
How I checked it

I checked that the calculation methods return values and do not print anything. I then ran the self-test and checked that the receipt output remained unchanged.
Prompt 4
My prompt to the AI

"How can I remove magic numbers and the unnecessary global variable?"
What the AI suggested

The AI suggested replacing values such as 0.07, 0.03, 10, and 100 with named constants.

Examples included:

TAX_RATE
BULK_DISCOUNT_RATE
POINTS_DIVISOR
DISCOUNT_THRESHOLD

It also suggested removing the unnecessary global TAXRATE.
What I did

I accepted the suggestion and created named constants. I also removed the unnecessary global declaration from the refactored code.
How I checked it

I compared all constant values with the original business rules and ran the self-test.
Prompt 5
My prompt to the AI

"How can Product handle its own tax calculation?"
What the AI suggested

The AI suggested giving the Product class methods to determine its tax rate and calculate tax.
What I did

I added:

tax_rate()
tax_for(quantity)

to the Product class.
How I checked it

I verified that food products have 0% tax and electronics and stationery products have 7% tax. I then ran the self-test.
Prompt 6
My prompt to the AI

"Can you check why my refactored program gives a NameError for build_orders?"
What the AI suggested

The AI explained that build_orders() was missing or was not defined before refactored_main() used it.

It provided a corrected version where build_orders() is defined before refactored_main().
What I did

I accepted the correction and placed the build_orders() function before refactored_main().
How I checked it

I ran:

python Assignment_3.py

The program then ran the refactored code and the self-test confirmed that the behaviour was unchanged.
Ownership Statement

By submitting this assignment, I confirm that I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.

I verified the AI-assisted changes by reading the code, comparing the business rules with the original program, checking the calculations, and running the supplied self-test.original program, and running the supplied self-test to confirm that the behaviour remained unchanged.
