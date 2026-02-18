def guess_with_while():
    guessLimit= 3
    guessCount= 0
    word= "random"
    while(guessCount<guessLimit):
        userInput= input("Enter the word: ")
        if(userInput==word):
            print("yes, you win!")
            break
        else:
            guessCount+=1
            print("you have",guessLimit-guessCount,"guesses left")
    print("Better luck next Time")
    
def for_exs():
    dishes= ['burger', 'pizza', 'momos']
    for i in range(len(dishes)):
        print(dishes[i])
        
def math_pow(num, pow):
    result= 1
    while(pow):
        result*= num
        pow-= 1
    return result
    
# guess_with_while()
# for_exs()
math_pow(3, 4)
