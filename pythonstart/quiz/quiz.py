#importing class from other component
from questions import Question 

#list of questions fasciliatates reuseability. 
questions_list = [
    "What's the smallest prime number?\n(a) 2\n(b) 5\n(c) 1\n(d) 3",
    "What's the capital of France?\n(a) Madrid\n(b) Rome\n(c) Paris\n(d) Berlin",
    "Which planet is known as the Red Planet?\n(a) Earth\n(b) Mars\n(c) Jupiter\n(d) Venus",
    "What's the largest mammal?\n(a) Elephant\n(b) Giraffe\n(c) Blue Whale\n(d) Whale Shark",
    "What's the square root of 16?\n(a) 2\n(b) 3\n(c) 4\n(d) 8",
    "What gas do plants absorb from the atmosphere?\n(a) Oxygen\n(b) Nitrogen\n(c) Carbon Dioxide\n(d) Helium",
    "What's the boiling point of water at sea level?\n(a) 90°C\n(b) 100°C\n(c) 120°C\n(d) 80°C",
    "Who wrote 'Romeo and Juliet'?\n(a) Charles Dickens\n(b) William Wordsworth\n(c) William Shakespeare\n(d) Jane Austen"
]

answers = ["a", "c", "b", "c", "c", "c", "b", "c"]

#use questions list and answer list to creat the questions. use a loop to allow for dynamic / quick change of questions. 
questions = [Question(questions_list[i], answers[i]) for i in range(len(questions_list))]

#function that loops through and prints the questions for user to give answers through input. 
def run_test(questions):
    #score set to 0 and increased if question is answered cortrectly. 
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("you got " + str(score) + "/" + str(len(questions_list)) )
    #final score message
    
run_test(questions)
#call function 