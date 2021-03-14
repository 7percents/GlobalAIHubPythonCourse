# Final Project
# A 10-question competition, each with only one correct answer worth 10 points, was created. Answers to the questions were received from the user.
# If the user gave more than five correct answers, he/she was deemed successful, otherwise unsuccessful.


# Competition questions and answers
question1 = 'Which famous mathematician proved Fermat\'s last theorem?'
answer1 = 'andrew wiles'

question2 = 'Complete the following sentence: Once you eliminate the impossible, whatever remains, no matter how improbable, must be the ____.'
answer2 = 'truth'

question3 = 'What is the common ancestor of all life on Earth?'
answer3 = 'last universal common ancestor'

question4 = 'What is the meaning of "scientia potentia est"?'
answer4 = 'knowledge is power'

question5 = 'Who was the first person to receive two Nobel Prizes?'
answer5 = 'marie curie'

question6 = 'What is the brightest star in Earth\'s night sky?'
answer6 = 'sirius'

question7 = 'What is the answer to life, the universe, and everything?'
answer7 = 'forty-two'

question8 = 'What is the popular field that includes deep learning and is a subfield of artificial intelligence?'
answer8 = 'machine learning'

question9 = 'Which cosmological model states that the Earth revolves around the Sun?'
answer9 = 'heliocentrism'

question10 = 'Who said "A man provided with paper, pencil, and rubber, and subject to strict discipline, is in effect a universal machine"?'
answer10 = 'alan turing'

questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10]

realqanda = {questions[i]: answers[i] for i in range(len(questions))}    # Qs and As stored in a dictionary
user_qanda = {}

for question in questions:
    user_qanda[question] = input(question)  # get answers from the user

points = 0
for q, a in realqanda.items():
    if user_qanda[q].lower() == realqanda[q]:
        # print('"{}" is the correct answer.'.format(user_qanda[q].lower()))
        points += 10  # calculate the score of the user by giving +10 for each correct answer
    #else:
        # print('"{}" is not the correct answer. The correct answer is "{}".'.format(user_qanda[q].lower(), realqanda[q]))

def check_points(points):
    if points <= 50:
        print('Sorry... You have got {} points. You couldn\'t make it...'.format(points))
    else:
        print('Congrats! You have got {} points. You are successful!'.format(points))

check_points(points)