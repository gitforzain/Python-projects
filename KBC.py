total_score = 0

q1 = "What is the capital city of France?"
print(q1)

ans1 = ["a: London", "b: Berlin", "c: Paris", "d: Rome"]
for i in ans1:
    print(i)
answer = input("Enter your answer: ")
if answer == "c":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")
print()

q2 = "Who wrote the famous play \"Romeo and Juliet\"?"
print(q2)
ans2 = ["a: William Shakespeare", "b: Jane Austen","c: Jane Austen","d: Charles Dickens"]
for i in ans2:
    print(i)
answer = input("Enter your answer: ")
if answer == "a":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")
print()

q3 = "What is the largest planet in our solar system?"
print(q3)
ans3 = ["a: Jupiter", "b: Saturn", "c: Uranus", "d: Neptune"]
for i in ans3:
    print(i)
answer = input("Enter your answer: ")
if answer == "a":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")
print()

q4 = "What is the chemical symbol for gold?"
print(q4)
ans4 = ["a: Ag", "b: Au", "c: Cu", "d: Fe"]
for i in ans4:
    print(i)
answer = input("Enter your answer: ")
if answer == "b":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")
print()


q5 = "What is the largest mammal in the world?"
print(q5)
ans5 = ["a: Elephant", "b: Blue Whale", "c: Giraffe" , "d: Hippopotamus"]
for i in ans5:
    print(i)
answer = input("Enter your answer: ")
if answer == "b":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")
print()

q6 = "What is the smallest country in the world?"
print(q6)
ans6 = ["a: Vatican City", "b: Monaco", "c: San Marino", "d: Liechtenstein"]
for i in ans6:
    print(i)
answer = input("Enter your answer: ")
if answer == "a":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")
print()

q7 = "What is the largest ocean in the world?"
print(q7)
ans7 = ["a: Atlantic Ocean", "b: Indian Ocean", "c: Pacific Ocean", "d: Arctic Ocean"]
for i in ans7:
    print(i)
answer = input("Enter your answer: ")
if answer == "c":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")
print()

q8 = "What is the currency of Japan?"
print(q8)
ans8 = ["a: Yen", "b: Dollar", "c: Euro", "d: Pound"]
for i in ans8:
    print(i)
answer = input("Enter your answer: ")
if answer == "a":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")
print()
  
q9 = "What is the tallest mountain in the world?"
print(q9)
ans9 = ["a: Mount Everest", "b: K2", "c: Kangchenjunga", "d: Lhotse"]
for i in ans9:
    print(i)
answer = input("Enter your answer: ")
if answer == "a":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")
print()
  
q10 = "What is the largest desert in the world?"
print(q10)
ans10 = ["a: Sahara Desert", "b: Gobi Desert", "c: Arabian Desert", "d: Antarctic Desert"]
for i in ans10:
    print(i)
answer = input("Enter your answer: ")
if answer == "a":
    # print("Correct answer")
    total_score += 1
# else:
#     print("Incorrect answer")

# print(f"Total score: {total_score}")
print()

scores = total_score
print("Your total score is:",scores)

if total_score > 7:
    print("You got total" ,total_score, "score and You are Pass")
else:
    print("You got total" ,total_score, "score and You are fail")