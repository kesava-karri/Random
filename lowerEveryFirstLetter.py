def lowerEveryFirstLetter(sentence):
  """
  Input: FIVE THINGS YOU’RE DOING WRONG IN CSGO
  Output: Five Things You’re Doing Wrong In Csgo
  """
  sen = sentence.split()

  # Converting the words into required format using list comprehension
  # (only first letter Capital in every word)

  temp = [word[:1] + word[1:].lower() for word in sen]
  
  # Iterating through the list of strings and concatenating the words
  lowered_sen = ''
  for lowered_word in temp:
    lowered_sen = lowered_sen +' '+ lowered_word
  return lowered_sen

your_sentence = "FIVE THINGS YOU’RE DOING WRONG IN CSGO"
print(lowerEveryFirstLetter(your_sentence))