#try
#except
while True:
 try:
   age = int(input('enter your age'))
   break
 except ValueError:
    print('invalid input')

if age >= 18:
    print('you play this game')
else:
    print('you can/t play this game')