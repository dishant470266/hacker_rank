def outer_func():
    def inner_func():
        print('inner function')
    return inner_func

var = outer_func()
var()