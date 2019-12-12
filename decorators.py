def my_fun(asd):
    def are():
        print('this is function 1')
        asd()
    return are

def func1():
    print('this is two')

var = my_fun(func1)
var()

