import random
number = random.randint(1, 100)
continue_playing = "yes"
win = False
while continue_playing == "yes":
	for i in range(9, -1, -1):
		guess = int(input("Enter your guess: "))
		if guess == number:
			print("You win! The number was ", number)
			win = True
			break
		elif guess > number:
			print("Your guess is too high.")
			print("You have", i, "guesses remaining")
		else:
			print("Your guess is too low.")
			print("You have", i, "guesses remaining")
	if win:
		print("You win!")
	else:
		print("You lose!")
		print("The number was ", number)
	continue_playing = input("Enter \"Yes\" to continue playing: ")
print("Thank you for playing!")

