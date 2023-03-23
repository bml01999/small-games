print("Welcome to my computer quiz! ")

playing = input("Do you want to play?(y/n)   ")

if playing.upper() != "Y":
    quit()

print("Okay! lets get started. :) ")
score = 0
answer = input ("What does CPU stand for?  ")
if answer == "central processing unit":
    print("Wow! that's correct.")
    score += 1
else:
    print("Oops, try again!")

answer = input ("What does GPU stand for?  ")
if answer == "graphics processing unit":
    print("Wow! that's correct.")
    score += 1
else:
    print("Oops, try again!")

answer = input ("What does RAM stand for?  ")
if answer == "random access memory":
    print("Wow! that's correct.")
    score += 1
else:
    print("Oops, try again!")

answer = input ("What does ROM stand for?  ")
if answer == "read only memory":
    print("Wow! that's correct.")
    score += 1
else:
    print("Oops, try again!")

answer = input ("What does PSU stand for?  ")
if answer == "power supply":
    print("Wow! that's correct.")
    score += 1
else:
    print("Oops, try again!")

print("You got " + str(score) + " questions correct!!")

print("you got " + str((score/5)*100)+ "%")