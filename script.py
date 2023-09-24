last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#2 1d arrays
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

#should be combined arrays from above
gradebook = [['physics', 98], ['calculus',97], ['poetry', 85], ['history', 88]]

gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])

gradebook[5][1] = 98

gradebook[2].pop(1)
gradebook[2].append('pass')

full_gradebook = gradebook + last_semester_gradebook

print(gradebook)
print(full_gradebook)
