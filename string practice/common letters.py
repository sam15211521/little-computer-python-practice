def common_letters(string_one, string_two):
  common =[]
  for letter in string_one:
    if letter in string_two:
      if letter in common:
        continue
      else:
        common.append(letter)
  return common

#returns the common letters in two strings, only if the letter is not already in common.