authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

a= author_names = authors.split(',')
def author_last_names(authors = authors):
    print(a)
    print()
    author_last_names =[]
    for name in a:
        first_last = name.split()
        author_last_names.append(first_last[-1])
    return author_last_names
  
print(author_last_names())
