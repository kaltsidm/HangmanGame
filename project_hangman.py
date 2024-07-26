word_list = ['bugatsa', 'pastitsio', 'kadaifi', 'spanakopita', 'papoutsakia', 'mousakas']
import random
word = random.choice(word_list)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#print('The choosen word is: ', word)
blank_word = '_'*len(word)
listword = list(blank_word)

print("Let's play the hangman!!!")
print('You will have 6 lives. You can make 6 mistakes maximum. So be careful!!!')
lives = 6
print('Are you ready?')
x = input('Yes/No: ').lower()
if x == 'yes':
  while '_' in listword and lives>0:
    x = input('Choose a letter: ').lower()
    if x in word:
      if x in listword:
        print(f'you already put character {x} in your word. Choose another one')
      indices = [i for i, char in enumerate(word) if char == x]
      for index in indices:
        listword[index] = x
    else:
      lives -=1
      print(stages[lives-len(stages)])
    string = ''.join(listword)
    print(string)
  if lives == 0:
    print('You lost!')
    print('The word was: ', word)
  else:
    print('You won!')
    print('Congrats!!! You found the word: ', string)
else:
  print('Ok, no problem. Come next time!')