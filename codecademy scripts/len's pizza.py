#list of toppings and prices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices =[2, 6, 1, 3, 2, 7, 2]
pap=pizza_and_prices=[[2, "Pepperoni"], [6, "pinapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
# research
n2ds= num_2_dollar_slice = prices.count(2)

num_pizzas = len(toppings)
print("We sell", num_pizzas," diffrent kindes of pizza!")
# sorting and finidng the cheepest pizza
pap.sort()
cp = cheepest_pizza = pap[0][1]
print ("The cheepist pizza is", cp, "at",pap[0][0],"$")
print(pap) 
#shouting customer
pricest_pizza = pap[-1]
pap.pop()
pap.insert(4, [2.5, "peppers"])
print(pap)
three_cheapest = pap[:3]
print(three_cheapest)
