# (1) Returns all customers from customer table
customers = Customers.objects.all()
print("1) All Customers:", customers)

# ----------------------------------------------------------
# (2) Returns first customer in table
firstCustomer = ustomer.objects.first()
print("2) First Customer:", firstCustomer)

# ----------------------------------------------------------
# (3) Returns last customer in table
lastCustomer = customer.objects.last()
print("3) Last Customer:", lastCustomer)

# ----------------------------------------------------------
# (4) Returns single customer by name
# (Assumes field name="Peter Piper")
try:
    customerByName = Customer.objects.get(name='Peter Piper')
    print("4) Customer by Name:", customerByName)
except Customer.DoesNotExist:
    print("4) Customer 'Peter Piper' does not exist.")

# ----------------------------------------------------------
# (5) Returns single customer by id
try:
    customerById = Customer.objects.get(id=4)
    print("5) Customer by ID:", customerById)
except Customer.DoesNotExist:
    print("5) Customer with ID=4 does not exist.")

# ----------------------------------------------------------
# (6) Returns all orders related to customer
if firstCustomer:
    customerOrders = firstCustomer.order_set.all()
    print("6) Orders for firstCustomer:", customerOrders)

# ----------------------------------------------------------
# (7) Returns order’s customer name (query parent model values)
firstOrder = Order.objects.first()
if firstOrder:
    parentName = firstOrder.customer.name
    print("7) Parent Customer Name for First Order:", parentName)

# ----------------------------------------------------------
# (8) Returns products from products table with category = "Out Door"
products = Product.objects.filter(category="Out Door")
print("8) Products with category 'Out Door':", products)

# ----------------------------------------------------------
# (9) Order/Sort objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

print("9A) Products from least to greatest:", leastToGreatest)
print("9B) Products from greatest to least:", greatestToLeast)

# ----------------------------------------------------------
# (10) Returns all products with tag "Sports" (Many-to-many field)
productsFiltered = Product.objects.filter(tags__name="Sports")
print("10) Products with tag 'Sports':", productsFiltered)

# ----------------------------------------------------------
# (11) Bonus Question:
# Q: If the customer has more than 1 "Ball", how do we store that?
# A: We DO NOT store totals in DB. We calculate dynamically.

if firstCustomer:
    ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()
    print("11) Total 'Ball' orders:", ballOrders)

# Returns total count for each product the customer ordered
allOrders = {}
if firstCustomer:
    for order in firstCustomer.order_set.all():
        productName = order.product.name
        if productName in allOrders:
            allOrders[productName] += 1
        else:
            allOrders[productName] = 1

print("11B) Count for each product ordered:", allOrders)
# Example output: {'Ball': 2, 'BBQ Grill': 1}

# ----------------------------------------------------------
# RELATED SET EXAMPLES (Important Django ORM concept)
from django.db import models

class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name} → Parent: {self.parent.name}"