# print("hello world")
# # this is single line comment
# """this is mulit line commnet"""
# '''this is also a multi line comment'''
result =[]
for i in range(int(input())):
        name = input()
        score = float(input())
        result.append([name,score])

result.sort()
# print(result)
# # n = int(input())
# records = []

# for _ in range(n):
#     name = input()
#     score = float(input())
    
#     records.append([name, score])

# # Create a set of unique scores, then convert to list and sort it
# unique_scores = sorted(set(score for name, score in records))
# second_lowest_score = unique_scores[1] # Takes the second lowest score

# # Create a list of name with second lowest score, then sort it
# names = [name for name, score in records if score == second_lowest_score]
# names.sort()

# for name in names:
#     print(name)