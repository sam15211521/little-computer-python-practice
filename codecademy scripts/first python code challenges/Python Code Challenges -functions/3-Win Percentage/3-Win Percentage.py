#calculates % of games won from total games and wone games

# Write your win_percentage function here:
def win_percentage(win, loss):
    return win/(win+loss)*100

# Uncomment these function calls to test your win_percentage function:
#def square_root(num):
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100