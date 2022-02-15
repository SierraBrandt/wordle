import random

with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    word = random.choice(words).lower()

#print(word)
correct = False
wordleCurrentRow = 0
tries = 0
rows, cols = (6, 5)
wordle = [[ "■" for i in range(cols) ] for j in range(rows) ]

while not correct:

  for x in wordle:
    print(*x, sep='')

  
  if tries >= 6:
    print("You lost, the word was " + word)
    break

  userGuess = input("\nplease guess a word: ").lower()

  
  if(len(userGuess) == 5):
    tries += 1
    if(userGuess == word):
      for col in range(cols): 
        wordle[wordleCurrentRow][col] = word[col]
      for x in wordle:
        print(*x, sep='')
      correct = True
    for col in range(cols): 
      if word[col] == userGuess[col]:
          wordle[wordleCurrentRow][col] = word[col]
      elif userGuess[col] in word and word[col] != userGuess[col]:
        print(userGuess[col] + " is in the word but not the correct spot") 
  else:
    print("Please guess a word with 5 letters")



  wordleCurrentRow += 1

if tries < 6:
  print("Correct, the word was " + word + ". You got it in " + str(tries) + " tries.")
  
