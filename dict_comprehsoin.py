#num = {1:1,2:4,3:6}

# square = {f" {num}":num**2 for num in range(1,11)}
# for k,v in square.items():
#     print(f"{k}:{v}")

#===============================================

name = 'dishu'

word_count = {i:name.count(i) for i in name}
print(word_count)
