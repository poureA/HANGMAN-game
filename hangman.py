#importing random module
import random as rn
import os
import time
#creating a class 
class Hangman(object) :
    ''' hangman game '''
    def play(self)->str :
        '''return messages about your guesses'''
        os.system('cls')
        print('* welcome to the hangman game *\nim thinking about a word ...')
        with open('F:\\projects\\\hunter_game\\words.txt','r') as file :
            words = file.read().split()
        secret_word = rn.choice(words)
        print(secret_word)
        time.sleep(2)
        if len(secret_word)<=4:
            counter = 6
        else :
            counter = len(secret_word)+2
        os.system('cls')
        print(f'that is a {len(secret_word)} letters long')
        print(f'you have {counter} guesses \nso lets go !')
        r = ''
        right_letters = list()
        right_guess = list()
        alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
        while guess:=input('guess a letter :') :
                if counter >0 :
                    if guess.isalpha() :
                        if len(guess) == 1 :
                            if guess in secret_word :
                                if guess in alpha :
                                    counter -= 1
                                    if counter == 0 :
                                        os.system('cls')
                                        print(f'sorry you lost the game\nsecret word was {secret_word}')
                                        break
                                    os.system('cls')
                                    print('thats right :) !')
                                    alpha.remove(guess)
                                    right_letters.append(guess)
                                    for i in secret_word :
                                        if i in right_letters :
                                            r+=i
                                            continue
                                        r+='-'
                                    right_guess.append(r)
                                    if secret_word in right_guess :
                                        score = counter * len(set(list(secret_word)))
                                        spc = ' '*5
                                        os.system('cls')
                                        print(f'***congrats you won***\n{spc}""{secret_word}"\nyour score :{score}')
                                        break
                                    print(f'secret word : {r}\nyou have {counter} more guesses')
                                    print(f'available letters : {",".join(alpha)}')
                                    r = ''
                                else :
                                    os.system('cls')
                                    counter -= 1
                                    if counter == 0 :
                                        os.system('cls')
                                        print(f'sorry you lost the game\nsecret word was {secret_word}')
                                        break
                                    for i in secret_word :
                                        if i in right_letters :
                                            r+=i
                                            continue
                                        r+='-'
                                    print('you can guess a letter just one time not more\nsorry you lost a chance to guess')
                                    print(f'secter word : {r}')
                                    print(f'you have {counter} more guesses')
                                    print(f'available letters : {",".join(alpha)}')
                                    r = ''
                            else :
                                counter -= 1
                                if counter == 0 :
                                    os.system('cls')
                                    print(f'sorry you lost the game\nsecret word was {secret_word}')
                                    break
                                for i in secret_word :
                                    if i in right_letters :
                                        r+=i
                                        continue
                                    r+='-'
                                os.system('cls')
                                print(f'sorry thats wrong :( \nyou have {counter} more guesses\nsecret word : {r}')
                                print(f'available letters : {",".join(alpha)}')
                                r = ''
                        else :
                            if guess == secret_word :
                                score = counter * len(set(list(secret_word)))
                                spc = ' '*5
                                os.system('cls')
                                print(f'***congrats you won***\n{spc}""{secret_word}"\nyour score :{score}')
                                break
                            else :
                                counter -= 1
                                if counter == 0 :
                                    os.system('cls')
                                    print(f'sorry you lost the game\nsecret word was {secret_word}')
                                    break
                                for i in secret_word :
                                    if i in right_letters :
                                        r+=i
                                        continue
                                    r+='-'
                                os.system('cls')
                                print(f'wrong guess for full word !\nyou have {counter}more guesses\nsecret word : {r}')
                                print(f'available letters : {",".join(alpha)}')
                                r = '' 
                    else :
                        counter -= 1
                        if counter == 0 :
                                    os.system('cls')
                                    print(f'sorry you lost the game\nsecret word was {secret_word}')
                                    break
                        os.system('cls')
                        print(f'please enter a letter ! you have {counter} more guesses')
                        if counter == 0 :
                            print(f'sorry you lost the game\nsecret word was {secret_word}')
                            break
                else :
                    os.system('cls')
                    print(f'sorry you lost the game\nsecret word was {secret_word}')
                    break
        print('thank you for playing')        
        return
while ask:=input('wanna play ?') :
        if ask[0]=='y' or ask[0] == 'Y' :
            sample = Hangman()
            sample.play()
        else :
            break
