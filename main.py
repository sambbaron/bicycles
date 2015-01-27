
from bicycles import Wheel, Frame, Bicycle, BikeShop, Customer

# Define 3 wheel types
Avenir = Wheel("Avenir", 5, 25)
StaTru = Wheel("Sta Tru", 3, 35)
Aeromax = Wheel("Aeromax", 2, 75)

# Define 3 frame types
Aluminum = Frame("Aluminum", 10, 150)
Carbon = Frame("Carbon", 4, 275)
Steel = Frame("Steel", 15, 75)

# Define 6 bicycle models
Schwinn = Bicycle("Schwinn", Avenir, Aluminum)
Huffy = Bicycle("Huffy", Avenir, Steel)
Vilano = Bicycle("Vilano", StaTru, Carbon)
Diamondback = Bicycle("Diamondback", StaTru, Aluminum)
Kestrel = Bicycle("Kestrel", Aeromax, Carbon)
Windsor = Bicycle("Windsor", Aeromax, Aluminum)

# Create a bike shop with 6 models in stock and 20% markup
CycleWorld = BikeShop("Cycle World", 
                      {Schwinn: 5, Huffy: 10, Vilano: 7, Diamondback: 6, Kestrel: 2, Windsor: 8 },
                      0.20)

# Create 3 customers with funds of $200, $500, and $1000
John = Customer("John", 200)
Sally = Customer("Sally", 500)
Rich = Customer ("Rich", 1000)
customers = [John, Sally, Rich]


# Print each customer with bicycle sale sheet from bike shop making sure customer can afford at least one bicycle
for customer in customers:
  print "{} Current Inventory for {}".format(CycleWorld.shop_name,customer.customer_name)
  CycleWorld.print_inventory(customer.bike_purchase_fund)
  print ""

# Print the bike shop's initial inventory
print "{} Total Starting Inventory".format(CycleWorld.shop_name)
CycleWorld.print_inventory()
print ""

# Each customer purchases a bicycle - print bicycle purchased, cost, and remaining purchase fund
CycleWorld.reset_profit_balance()
bicycle_purchases = {John: Huffy, Sally: Diamondback, Rich: Windsor}
print "Bicycle Purchases"
for customer in bicycle_purchases:
  bicycle_sold = bicycle_purchases[customer]
  customer.purchase_bicycle(bicycle_sold, CycleWorld.bicycle_sales_price(bicycle_sold))
  CycleWorld.sell_bicycle(bicycle_sold)
  print ""

# Print bike shop's ending inventory and total profit on 3 bicycle sales
print "{} Total Ending Inventory".format(CycleWorld.shop_name)
CycleWorld.print_inventory()
print ""
print "{} Total Profit = ${}".format(CycleWorld.shop_name, CycleWorld.profit_balance)
