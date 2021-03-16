import time
import sys
#delays
a = 2
b = 0.08
#c = 0.08

def intro():
	print("\nFuture seems so dark...\n")
	time.sleep(a)
	print("Although you did really well...\n")
	time.sleep(a)
	print("Heightened anxiety of choosing a career...\n")
	time.sleep(a)
	print("While you only have a tunneled vision...\n")
	time.sleep(a)
	print("It's true ....YOU'RE A KID!!!!\n")
	time.sleep(a)
	print("Nobody seems to notice that...\n")
	time.sleep(a)
	print("You do some soul searching and you have 2 choices it seems...\n")
	time.sleep(a)
	print("Choice #1: PCM")
	time.sleep(a)
	print("Choice #2: Humanities")
	time.sleep(a)
	first_choice = input("\nWhich one would you pick??? : (1/2) \n")

	if first_choice == '1':
		choice1()
	elif first_choice == '2':
		choice2()

def choice1():
	print("Godspeed!! You've chosen the right future..\n")
	s1 = "Umm..I like Calculus"
	for character in s1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	s2 = "WOW ..what are these monkeys doing here...oh I have to calculate this.."
	for character in s2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	s3 = "Why are they teaching Chemistry with this much useless theory??.."
	for character in s3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	print("After 2 hard years......life throws another set of choices to you!!\n")
	print("Choice #1: ENGINEERING\n")
	print("Choice #2: Designing\n")
	second_choice = input("\nWhich one would you pick??? : (1/2) \n")

	if second_choice == '1':
		choice1_1()
	elif second_choice == '2':
		choice1_2()


def choice1_1():
	s4 = "What the heck!!"
	for character in s4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	s5 = "Where am I???"
	for character in s5:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	s6 = "I hate calculus"
	for character in s6:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	s7 = "I gotta find my PASSION or i'll waste this precious life...FUCK CORPORATE.."
	for character in s7:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	s8 = "Let's start this toy business..."
	for character in s8:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	print("YOU WIN!!")
	

def choice1_2():
	s9 = "Feels great to be a freelance designer!!"
	for character in s9:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	s10 = "Instagram is the future..."
	for character in s10:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(b)
	print()
	time.sleep(a)
	print("GAME OVER!! YOU DIDN'T LOSE... BUT YOU SURE AS HELL DIDN'T WIN\n")
	
def choice2():
	print("Nice choice your love for abstract knowledge is going to get strong...\n")
	time.sleep(a)
	print("You will also have plenty of time for reading and doing things you actually love\n")
	time.sleep(a)
	print("After months of reading authors from the likes of Jane Austen, Agatha Christie, George R. Martin and many more\nyou have decided to get your own book published..\n")
	time.sleep(a)
	print("You are a renowned writer ...YOU WIN!!!")





##welcome message

print("				**********************")
print("				**********************")
print("				**    CHOICES OF    **")
print("				**     AN INTJ      **")
print("				**********************")
print("				**********************")
print()
print()
time.sleep(a)



#set_1

print("DAD : Congratulations beta....You know i've got big plans for you..")
time.sleep(a)
print("      So which college do you have in mind???\n ")
time.sleep(a)

print("YOU : Thanks pops, it was hard to manage...uh.. about college i haven't given any thoughts to that..\n")
time.sleep(a)

print("DAD : Hmmm...what branch then??\n")
time.sleep(a)

print("YOU : I am sorry dad...but i am not sure about whether Arts or Commerce\n")
time.sleep(a)


time.sleep(a)

print("DAD : Beta!! You have scored a full of 10 points in your boards!!!\n      It's clear that you will go to the best engineering institute...\n      besides engineering is the only field after which you get wide variety of career opporunities....\n      no other field offers you that..\n")
time.sleep(a)

print("YOU : Alright dad i'll think about it...\n")
time.sleep(a)

print("DAD : You better do your thinking quick...it's your future\n")
time.sleep(a)
# set_1 complete

#start game?

startGame = input("START GAME ? (Y/N):  \n")


if startGame == 'y' or 'Y':
	intro()
elif startGame == 'n' or 'N':
	print("Maybe next time...")
