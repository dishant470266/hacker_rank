# with open('file1.txt') as f:
#     data = f.read()
#     print(data)

# with open('file1.txt' , 'w') as f:
#     f.write('hello')

with open('file1.txt','r') as rf:
    with open('file2.txt','w') as wf:
        wf.write(rf.read())
