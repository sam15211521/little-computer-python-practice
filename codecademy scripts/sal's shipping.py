weight = int(input("Please enter weight of your package: "))

#ground shipping cost
g_price = 20
print("Price for ground shipping:")
if weight <=2:
    g_price += 1.5*weight
    print(str(g_price)+"$")
elif weight > 2 and weight <= 6:
    g_price += 3.00*weight
    print(str(g_price)+"$")
elif weight > 6 and weight <= 10:
    g_price += 4.00*weight
    print(str(g_price)+"$")  
elif  weight > 10:
    g_price += 4.75*weight
    print(str(g_price) +"$") 

#Ground Shipping Premium
print("Price for Ground Premium:")
print("125$")
#Drone shipping 
g_p_price = 0
print("Price for Drone:")
if weight<=2:
    g_p_price += 4.5*weight
    print(str(g_p_price)+"$")
elif weight > 2 and weight <= 6:
    g_p_price += 9.0*weight
    print(str(g_p_price)+"$")
elif weight > 6 and weight <= 10:
    g_p_price += 12.00*weight
    print(str(g_p_price)+"$")  
elif  weight > 10:
    g_p_price += 14.25*weight
    print(str(g_p_price) +"$") 

#comparison of prices
if g_price < g_p_price and g_price < 125:
    print("shipping by ground is cheepest")
elif g_p_price < g_price and g_p_price < 125:
    print("shipping by drone is cheepest")
else:
    print("shipping by ground premium is cheepest")
