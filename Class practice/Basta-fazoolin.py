class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return 'The ' +self.name +' menu is available from ' +str(self.start_time) +' to ' + str(self.end_time) 

  #calculates the bill, only give in integers
  def calculate_bill(self, purchased_items):
    bill =0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

class Franchise:
  def __init__(self, store_name, address, menus):
    self.name = store_name
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return 'The address of the ' + self.name + ' is ' + self.address

 #finds avaliable menues based on time for a store
  def available_menus(self, time):
    avalable_menus =[]
    for men in self.menus:
      if time >= men.start_time and time <= men.end_time:
        avalable_menus.append(men)
    return avalable_menus
  
class Business:
  def __init__(self, name, franchises_list):
    Business.name = name
    Business.franchises_list = franchises_list
    

#here are the dictanaries of items with their prices

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

#here we initialize the objects of class Menu
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
early_bird_menu = Menu('Early Bird', early_bird, 1500,1800)
dinner_menu = Menu('Dinner', dinner, 1700, 2300)
kids_menu = Menu('Kids', kids, 1100, 2100)

# here is an array of our menus
menus =[brunch_menu, early_bird_menu, dinner_menu, kids_menu]

#here are the diffrent Franchises of this buisness:
flagship_store = Franchise('Flagship', '1232 West End Road', menus)
new_installment = Franchise('New Installment','12 East Mulberry Street', menus)

#initiating the objects for Businesses

Basta_Fazoolin_with_my_Heart = Business('Basta Fazoolin\'\ with my Heart', ['flagship_store', 'new_installment'])

Takea_Arepa = Business('Takea\'\a Arepa', ['Arepa\'\s Place'])


###
###
###

#menu for Takea' Arepa
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Takea\'\a Arepa', arepas_items, 1000, 2000)
#franchises of Takea' Arepa
arepas_place = Franchise('Arepa\'\s Place', '189 Fitzgerald Avenue', arepas_menu)



#

#print(dinner.items)
#print(kids.name)
print(brunch_menu)
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print()
print(early_bird_menu)
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

print(flagship_store)
print(new_installment)
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))
print()
print(arepas_place)