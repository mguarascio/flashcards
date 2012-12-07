import random
import sys

if len(sys.argv) < 2:
    print "filename is a required parameter!"
    sys.exit()

filename = sys.argv[1]
"""'state_capitals.txt'"""
questions = {}

with open(filename) as f:
    for line in f:
        qalist = line.strip().split(',')
        questions[qalist[0]] = qalist[1]
f.closed

while True:
    question = random.choice(questions.keys())
    answer = questions[question]
    answerGiven = raw_input(question + ":\n")

    if answerGiven == "exit":
        print "GOODBYE..."
        break
    elif answer == answerGiven:
        print "Correct!\n"
    else:
        print "Incorrect. The answer is: ", answer, "\n"
