while True:
 try:
   number = int(input('enter your age'))
   break
 except ValueError:
    print('invalid input')
 else:
    print(f'user input = {number}')
 finally:
    print('finally block......s')
