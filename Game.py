
def main_func():
    print("Hello! Play with me I will think of 3 digit number that has no repeating digits.")
    print ("You have to guess a three digit number and I'll give you clues. ")
    print("1.Close: You've guessed a correct number but in the wrong position")
    print("2.Match: You've guessed a correct number in the correct position")
    print("3.Nope: You haven't guess any of the numbers correctly")
    print("Let's start!")
    my_number=456
    def Match_number(num,gus):
        num=str(num)
        gus=str(gus)
        for int_char in num:
            for digit in gus:
                matches=sum(digit==int_char for digit,int_char in zip(gus,num))
        if(matches>=1):
            print("%d Matches"%matches)
            print("-------------------")
        else:
            close_number(my_number,guess)

    def close_number(num,gus):
        num=str(num)
        gus=str(gus)
        close=0
        for int_char in num:
            for digit in gus:
                if digit==int_char:
                    close=close+1
        if(close>=1):
            print("%d Close"%close)
            print("-------------------")
        else:
            none_number(my_number,guess)

    def none_number(num,gus):
        print("Nope")
        print("-------------------")

    guess = input("What is your guess? ")
    Match_number(my_number,guess)
    main_func()
main_func()
