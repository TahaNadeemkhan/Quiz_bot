
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    
    
questions = [
    [
    "Which of the following data types is mutable in Python?", "Integer","String","list", "Tuple", 3
],
[
    'Which planet is known as the "Red Planet"? ', "Venus","Mars","Jupiter","Saturn", 2
],
[
    'Who wrote the famous play "Romeo and Juliet"?', "William Shakespeare","Charles Dickens","Jane Austen","Mark Twain", 1
],
[
    "What is the tallest mountain in the world? ", "Mount Everest", "K2", "Mount Kilimanjaro", "Mount Fuji", 1
],
[
    "What is the largest organ in the human body?", "Brain", "Liver", "Heart", "Skin", 4
],
]


levels =  [5000, 10000, 40000, 80000, 160000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rupees {levels[i]}")
    l = f"Question for Rupees {levels[i]}"
    text_to_speak = f"{l}"
    speak(text_to_speak)
    print(f"{question[0]}")
    M = f"{question[0]}"
    text_to_speak = f"{M}"
    speak(text_to_speak)
    N = f"option a. {question[1]}     option b. {question[2]}"
    o = f"option c. {question[3]}     option d. {question[4]}"
    text_to_speak = f"{N}"
    speak(text_to_speak)
    print(f"a.{question[1]}     b.{question[2]}")
    text_to_speak = f"{o}"
    speak(text_to_speak)
    print(f"c. {question[3]}     d.{question[4]}")
    p = "Enter your answer"
    text_to_speak = f"{p}"
    speak(text_to_speak)
    reply = int(input("Enter your answer, (1-4): \n"))
    if(reply == question[-1]):
        print(f"Congratulations! You've just won {levels[i]} rupees")
        x = f"Congratulations! You've just won {levels[i]} rupees"
        text_to_speak = f"{x}"
        speak(text_to_speak)
        print("Here is your next question")      
    else:
        print("Wrong Answer!")
        x = "Sorry! Your Answer is incorrect, Better luck next time."
        print("Thanks for playing")
        text_to_speak = f"{x}"
        speak(text_to_speak)
        break
    if(i == 1):
        money == 10000
        warning = ("Do you want to continue this game? Your current amount is 10000, reply as Yes or No: ")
        print(warning)
        text_to_speak = {warning}
        speak(text_to_speak)
        warning = input("Y or N?: \n")
        if(warning == 'y'):
            print("Your next question is on your screen: ")
            t = "Your next question is on your screen: "
            text_to_speak = {t}
            speak(text_to_speak)
        else:
            print(f"Thanks for playing,Your total prize is {levels[i]}")
            t = f"Thanks for playing,Your total prize is {levels[i]}"
            text_to_speak = {t}
            speak(text_to_speak)
            break
    elif(i == 4):
        money == 160000
        print(f"Thanks for playing,Your total prize is {levels[i]}")
        t = f"Thanks for playing,Your total prize is {levels[i]}"
        text_to_speak = {t}
        speak(text_to_speak)
        break
           
   
        

            
    
        

        



