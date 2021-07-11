# Write your movie_review function here:
# gives rating based on how much i liked it
# <5 "Avoid at all costs"
# <9 "This one was fun"
# else "Outstanding"

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating <9:
        return "This one was fun."
    else:
        return "Outstanding!"


# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(5))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."