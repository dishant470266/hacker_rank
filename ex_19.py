student  = [
    {'name':'disja','score': 90 , 'age' : 20},
    {'name':'raj','score': 70 , 'age' : 19},
    {'name':'vijay','score': 60 , 'age' : 18}
]
print(max(student , key = lambda item : item.get('score')))