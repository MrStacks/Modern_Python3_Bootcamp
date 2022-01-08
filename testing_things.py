again = ''
while again.lower() not in ('y','yes','n','no')
again.input("Would you like to play again? ")
if again.lower() in ('y','yes'):
	guesses = 5
    current_quote_num += 1
    print("Great! Here we go again!")
    break
else: print("OK GOODBYE!")
	quit()	