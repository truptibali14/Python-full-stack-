n = int(input("Enter number of scores: "))
scores = []
for i in range(n):
    score = int(input("Enter score {i+1}: "))
    scores.append(score)
total = sum(scores)
average = total / len(scores)
count_above_avg = 0
for s in scores:
    if s > average:
        count_above_avg += 1
print("\n----- Score Analysis -----")
print("Scores:", scores)
print("Total Score:", total)
print("Average Score:", average)
print("Count of Scores Above Average:", count_above_avg)
