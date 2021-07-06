letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {letter: point for letter, point in zip(letters, points)}

letters_to_points[" "] = 0
#print(letters_to_points)

#function socres a word
def score_word(word):
  point_total = 0
  for letter in word.upper():
    point = letters_to_points.get(letter, 0)
    point_total += point
  return point_total

#these are the players and their words
PtW = player_to_words = {'player1' : ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['eraser', 'belly', 'husky'], 'Prof Reader': ['zap', 'coma', 'period']}

#function finds the current point value of all the players
def points_of_player():
    player_to_points = {}
    for player, words in player_to_words.items():
      player_points = 0
      for word in words:
        player_points += score_word(word)
      player_to_points[player] =player_points
    print(player_to_points)
    
#function adds a new word to a player's score
    # works on the global part
newPtW = {}
def play_word(player, word):
    old = PtW[player] #temp value
    old.append(word)
    PtW[player] = old #updates PtW
    print (PtW)       #prints new word values for all
    print () 
    points_of_player() #calls PoP to pring current 
    
    
    
    
    
#here is the playing of the code 
play_word('player1', 'sam')
print('###')
play_word('wordNerd', 'hello')

#points_of_player()
    