def parameter_echo_decorator(func):
    def decorate(*args,**kwargs):
        print('call to ',func,args,kwargs)
        return func(*args,*kwargs)
    return decorate

def repeat_decorator(a,b):
    def decorator(func):
        def decorate(*args):
            print(b)
            for i in range(a):
                func(*args)
        return decorate
    return decorator
@parameter_echo_decorator
def do_that(a,b):
    return a+b


@repeat_decorator(5,'a')
def print_that():
    print('that')




print(do_that(5,8))
print_that()