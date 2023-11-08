import random


def hangman():
    words = ["tornado", "bottle", "pizza", "dictionary", "zebra", "elephant", "strawberry", "koala"]
    underbars = []
    life = 10

    random_number = random.randint(0,len(words)-1)
    random_word = words[random_number]

    for i in range(len(random_word)):
        underbars.append("_")

    underbars = " ".join(underbars)

    while life>0:
        
        print("Guess the word:"+ underbars)
        underbars = underbars.split()

        guessed_char = input().lower
        
        order = 0
        matched_detector = 0
        
        for i in random_word:
            if i == guessed_char:
                matched_detector =1
                underbars[order] = guessed_char
                order = order + 1
            else:
                order = order +1
        
        if matched_detector == 0:
            
            life = life -1
            
            if life == 9:
                print("9 turns left")
                print("  ---------  ")
                
            elif life == 8:
                print("8 turns left")
                print("  ---------  ")
                print("      O      ")
            
            elif life == 7:
                print("7 turns left")
                print("  ---------  ")
                print("      O      ")
                print("      |      ")
            
            elif life == 6:
                print("6 turns left")
                print("  ---------  ")
                print("      O      ")
                print("      |      ")
                print("     /       ")
            
            elif life == 5:
                print("5 turns left")
                print("  ---------  ")
                print("      O      ")
                print("      |      ")
                print("     / \     ")
            
            elif life == 4:
                print("4 turns left")
                print("  ---------  ")
                print("    \ O      ")
                print("      |      ")
                print("     / \     ")
            
            elif life == 3:
                print("3 turns left")
                print("  ---------  ")
                print("    \ O /    ")
                print("      |      ")
                print("     / \     ")
            
            elif life == 2:
                print("2 turns left")
                print("  ---------  ")
                print("    \ O /|   ")
                print("      |      ")
                print("     / \     ")
            
            elif life == 1:
                print("Last breaths counting. Take care!")
                print("  ---------  ")
                print("    \ O_|/   ")
                print("      |      ")
                print("     / \     ")  
                
            else:
                print("You loose")
                print("You let a kind man die")
                print("  ---------  ")
                print("      O_|    ")
                print("     /|\     ")
                print("     / \     ")
                break
                
        
        underbars = "".join(underbars)
        
        if underbars.isalpha() == True:
            print("Guess the word: "+ underbars)
            print("Victory! You save the man")
            break
    
        underbars = " ".join(underbars)


print("Enter your name: ")
name = input()
print("Welcome "+name)
print("====================================")
print("Try to guess it less than 10 attemps")
hangman()
    
