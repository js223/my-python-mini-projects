import random

def password_generator():
    
    uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
    numbers = ['1','2','3','4','5','6','7','8','9','10']
    special_characters = ['!','@','#','$','%','^','&','*']
    
    all_lists = [uppercase, lowercase, numbers, special_characters]
    
    password = ""
    
    password_length = int(input("how many letters do you want to have?"))
    
    n = 0
    
    if password_length>50:
        while password_length>50:
            print("Too long to create. Please type again")
            password_length = int(input("how many letters do you want to have?"))
            
    for i in range(0,password_length):
        chosen_list = random.choice(all_lists)
        random_letter = random.choice(chosen_list)
        password = password +str(random_letter)
            
    print(password)

password_decision = input("Do you want to create your password? (y/n)")
if password_decision == 'y':
    password_generator()
    