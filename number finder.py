print("hi, please think of a number, between any ending point to 0, then enter the ending point.\
then the computer will ask you certain question, if this is the number, if the number is less than your number press l, then press l\
if the number is more than your number, than press m, if it is the number press = ")

tries = 0


end = float(input("ending point:"))

start = 0


  
midvalue = (end + start)//2



while True:
    midvalue = (end + start)//2
    guess = input(f"is the number less(l), or more(m) or the number {midvalue}(=)")
    midvalue = (end + start)//2
    tries += 1
   
    


    while guess:

        if guess == 'l':
            end = midvalue
            midvalue = (end + start)//2
            guess = input(f"is the number less(l), or more(m) or the number {midvalue}(=)")
            tries += 1
            if guess == '=':
                print(f"the computer guessed the number {midvalue}, in {tries} tries")
                quit()

        if guess == 'm':
            start = midvalue
            midvalue = (end + start)//2
            guess = input(f"is the number less(l), or more(m) or the number {midvalue}(=)")
            tries += 1
            if guess == '=':
                print(f"the computer guessed the number {midvalue}, in {tries} tries")
                quit()
        
        
        if guess == '=':
            print(f"the computer guessed the number {midvalue}, in {tries} tries")
            quit()        
