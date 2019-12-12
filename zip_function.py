# user_id = ['user1','user2','user3']
# names = ['rohit','mohit','jay']

# print (list(zip(user_id,names)))
#=========================================
#zip_unpacking  

# l =[(1,2), (3,4) ,(5,6) ,(7,8)]
# l1,l2 = list(zip(*l))
# print(l1)
# print(l2)
#================================

l1 = [ 1,2,3,5] 
l2 = [5,5,6,8]
new_list = []
for i in zip(l1,l2):
    new_list.append(max(i))
print(new_list)
