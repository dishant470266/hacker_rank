# def average_num(l1,l2):
#     new_list = []
#     for i in zip(l1,l2):
#         new_list.append(sum(i)/len(i))
#     return new_list
# print(average_num([1,2,3] ,[4,5,6]))

#============================================

new_list = lambda *args : [sum(i)/len(i) for i in zip(*args)]
print(new_list([1,2,3],[4,5,6]))