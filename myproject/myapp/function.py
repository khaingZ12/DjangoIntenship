# def function_name(parameters):
    # statement             #body statement
    # return       #function return

#types of python function arguments
# default argument
# keyword arguments (named arguments)
# positional arguments
# variable arguments *args and **kwargs

a = 20
b = 30

def add_number():
    ans = a + b
    print(ans)
   
add_number()


# i = int(input('Enter i Number'))
# x = int(input('Enter x Number'))
# def add():
    # ans = i + x
    # print(ans)

# add()


# i = int(input('Enter i Number'))
# x = int(input('Enter x Number'))
# def multiple():
    # ans = i * x  
    # print(ans)

# multiple()


def add_no(a,b):
    ans = int(a) + int(b)
    print(ans)

add_no(a=20,b=10)
add_no(a=20,b=20)


def variable(*args):
    print(*args)

variable('mg mg', '12054')


def keyvari(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

keyvari(first= 'Data', mid = 'for', last = 'python')


def acc_login(**kwargs):
    for x,y in kwargs.items():      # value ကိုလိုချင်ရင် .values() ကိုထည့်
        print(x,y)

acc_login(username = 'mg mag', password = '12345')

