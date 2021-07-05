letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {letter: point for letter, point in zip(letters, points)}

letters_to_points[" "] = 0
#print(letters_to_points) 
def score_word(word):
  point_total = 0
  for letter in word.upper():
    point = letters_to_points.get(letter, 0)
    point_total += point
  return point_total
print(score_word("BROWNIE"))

PtW = player_to_words = {'player1' : ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['eraser', 'belly', 'husky'], 'Prof Reader': ['zap', 'coma', 'period']}
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] =player_points
print(player_to_points)



#If you want extended practice, try to implement some of these ideas with the Python you’ve learned:

#play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
#update_point_totals() — turn your nested loops into a function that you can call any time a word is played
#make your letter_to_points dictionary able to handle lowercase inputs as well
