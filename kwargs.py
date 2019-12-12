def func(l, **kwagrs):
    if kwagrs.get('reverse_str') == True:
      return[name[::-1].title() for name in l ]
    else:
        return(name.title() for name in l)
names = ['disaha','raj']
print(func(names,reverse_str = True))