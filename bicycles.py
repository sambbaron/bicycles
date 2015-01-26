
class Bicycle(object):
  """A bicycle with:
  model_name - string - Bicycle model name
  weight - integer - Bicycle weight in pounds
  cost - integer - Bicycle production cost in whole dollars"""
  
  def __init__(self, model_name, weight, cost):
      self.model_name = model_name
      self.weight = weight
      self.cost = cost

class BikeShop(object):
  """A bike shop with:
  shop_name - string - Bike shop name
  bicycle_inventory - dictionary - Bicycle model (key) and inventory count (value) as integer
  bicycle_markup - float - Percentage increase over bicycle cost for sale price
  profit_balance - integer - Total profit made on bicycle sales"""
  
  def __init__(self, shop_name, bicycle_inventory = {}, bicycle_markup = 0.0):
    self.shop_name = shop_name
    self.bicycle_inventory = bicycle_inventory
    self.bicycle_markup = bicycle_markup
    
  profit_balance = 0
  
  def bicycle_sales_price(self, bicycle):
    """Return sale price for bicycle"""
    return int(bicycle.cost + round(bicycle.cost * self.bicycle_markup,0))
    
  def sell_bicycle(self, bicycle):
    """Sell bicycle using markup over cost, return profit margin, and add to profit balance"""
    # Test whether bicycle is in inventory
    if self.bicycle_inventory[bicycle] > 0:
      # Calculate bicycle profit margin, rounded to a whole dollar
      bicycle_profit = self.bicycle_sales_price(bicycle) - bicycle.cost
      # Return bicycle profit margin
#       return bicycle_profit
      # Add profit to profit balance
      self.profit_balance += bicycle_profit
      # Remove bicycle from inventory stock
      self.bicycle_inventory[bicycle] -= 1
      # Confirmation message
      print "{} has successfully sold a {} for ${}.".format(self.shop_name, bicycle.model_name, bicycle_profit)
    else:
      print "{} bicycle is not in stock to sell.".format(bicycle)
      
  def reset_profit_balance(self):
    """ Reset bicycle profit balance to zero """
    self.profit_balance = 0
    
  def print_inventory(self, sale_price_limit = 9999):
    """ Print inventory with bicycle names, counts, and sale prices with optional price limit """
    print "Name    Count    Sale Price"
    for bicycle in self.bicycle_inventory:
      # Calculate sale price and test whether under limit
      bicycle_sale_price = self.bicycle_sales_price(bicycle)
      if bicycle_sale_price < sale_price_limit:
        print "{}    {}    ${}".format(bicycle.model_name, self.bicycle_inventory[bicycle], bicycle_sale_price)
      
class Customer(object):
  """A bicycle customer with:
  customer_name - string - Customer name
  bike_purchase_fund - integer - Customer funds used for purchasing a bicycle, rounded to whole dollars
  customer_bicycle - bicycle class - Bicycle owned by customer"""
  
  def __init__(self, customer_name, bike_purchase_fund, bicycle = None):
    self.customer_name = customer_name
    self.bike_purchase_fund = bike_purchase_fund
    self.bicycle = bicycle

  def purchase_bicycle(self, bicycle, bicycle_cost):
    """Customer purchases bicycle and reduces purchase fund"""
    self.bicycle = bicycle
    self.bike_purchase_fund -= bicycle_cost
    # Confirmation message
    print "Congratulations {}, you purchased a {} for ${}.  You have ${} remaining of your bike purchase fund.".format(self.customer_name, bicycle.model_name, bicycle_cost, self.bike_purchase_fund)
    