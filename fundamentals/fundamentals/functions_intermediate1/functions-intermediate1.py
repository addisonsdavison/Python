# Update Values in Dictionaries and Lists
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

# x = [ [5,2,3], [10,8,9] ] 
# for i,t in enumerate(x):
#     for j,v in enumerate(t):
#         if v == 10:
#             x[i][j] = 15
# print(x)


# Change the last_name of the first student from 'Jordan' to 'Bryant'

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# for i,student in enumerate(students):
#     l_name = student["last_name"]
#     # print(l_name)
#     if l_name == "Jordan":
#         students[i]["last_name"] = "Bryant"
# print(students)


# In the sports_directory, change 'Messi' to 'Andres'

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# for k,v in sports_directory.items():
#     # print(k,v)
#     for i,player in enumerate(v):
#         if player == "Messi":
#             sports_directory[k][i] = "Andres"
# print(sports_directory)





# Change the value 20 in z to 30

# z = [ {'x': 10, 'y': 20} ]

# for i,j in enumerate(z):
#     for key,value in j.items():
#         if value == 20:
#             z[i][key] = 30
# print(z)


