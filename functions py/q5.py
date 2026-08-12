import random
words=("Python","Cobol","C++","Java","Visual Studio","MySql","Fortran")
wordu=random.choice(words)
correct=word
correct=correct.lower()
jumble=""
while word:
    position=random.randrange(len(word))
    jumble=jumble+word[position]
    word=word[:position]+word[(position+1):]
    print("Welcome to Word Jumble Game! Unscrable the letters to make a word.")
    print("(Note. Press the enter key at prompt to quit.)")
    print("The jumble word is:",jumble)
    guess=input("\nPlease enter again your guess:")
    while (guess!=correct) and (guess!=""):
        print("Sorry, %s is not exactly the jumble word"%jumble)
        guess=input("Please enter again your guess:")
        guess=guess.lower()
    if guess==correct:
        print("That's it! You've guessed it!\n")
    print("Thanks for playing")