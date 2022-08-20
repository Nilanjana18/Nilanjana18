print("Hello..Dear....")
print("Welcome to this tech quiz....")
print("you will be given a total of 5 questions and for each correct answer you will be awarded 1 marks each.")
print('Keep in mind youhave only one attemt..')
playing=input("So, Are you ready for the Quiz? ")

if  playing.lower() != "yes":
    quit()
print("So, Let's Start the Quiz")
score=0

print("And here comes your first question...")
ques1=input("What is the full form of AI?")
if ques1.lower() == "artificial intelligence":
    print("Correct Answer..")
    score=score+1
else:
    print("Incorrect Answer..")

print("Second question...")
ques2 = input("What does GPU Astands for?")
if ques2.lower() == "graphics processing unit":
    print("Correct Answer..")
    score = score+1
else:
    print("Incorrect Answer..")

print("Time for your third question")
ques3 = input("How many types of Ml(Machine Learning) are there?")
if ques3.lower() == "two":
    print("Correct Answer..")
    score = score+1
else:
    print("Incorrect Answer..")

print("We have almost reached to the end of our game.")
print("here comes your fourth question...")
ques4 = input("Is Ardruino a microcontroller board?")
if ques4.lower() == "yes":
    print("Correct Answer..")
    score = score+1
else:
    print("Incorrect Answer..")

print("So, Finally it's time for the last question of the day..")
ques5 = input("What is python in computer science?")
if ques5.lower() == "a programming language":
    print("Correct Answer..")
    score = score+1
else:
    print("Incorrect Answer..")

print("You got " + str(score) + " answers correct!" )
print("Your points sre : " + str(score) + " out of 5." )

#so this is a quiz game .........(beginner project based on the use of if conditional statements in python...)
