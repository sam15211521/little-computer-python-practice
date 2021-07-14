#accepts a dict where the keys are last names and values are first names of people
#need to calculate the number of people who have the same first letter in their last name

# Write your count_first_letter function here:

def count_first_letter(names):
    count_dic = {}
    for name, people in names.items():
        if name[0] not in count_dic:
            count_dic[name[0]] =len(people)
        else:
            count_dic[name[0]] +=len(people)
    return count_dic

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}