# number = [6,50,4]
# print(min(number))
# print(max(number))
#================================
number = [6,50,4]
def greastest_diff(l):
    return max(l) - min(l)
print(greastest_diff(number))