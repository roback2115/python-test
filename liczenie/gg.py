# User's answers for the 30 questions
user_answers_full = [
    'C', 'C', 'B', 'C', 'B',
    'A', 'A', 'A', 'C', 'A',
    'B', 'A', 'C', 'B', 'B',
    'A', 'A', 'B', 'C', 'C',
    'D', 'A', 'A', 'B', 'D',
    'B', 'A', 'B', 'B', 'B'
]

# Correct answers for the 30 questions
correct_answers_full = [
    'B', 'A', 'B', 'B', 'B',
    'B', 'A', 'A', 'B', 'B',
    'B', 'B', 'B', 'B', 'B',
    'B', 'A', 'B', 'A', 'B',
    'B', 'A', 'B', 'B', 'A',
    'A', 'A', 'B', 'A', 'A',
    'B', 'B'
]

# Calculate the number of correct answers
correct_count_full = sum([1 for user, correct in zip(user_answers_full, correct_answers_full) if user == correct])

# Total number of questions
total_questions_full = len(correct_answers_full)

# Calculate the percentage
percentage_full = (correct_count_full / total_questions_full) * 100
print(correct_count_full, percentage_full)
