class Myfamily:
    address = 'Yangon'
    def parent():
        print('This is Parent Function')

a = Myfamily
print(a.address)
print(a.parent())


class DailyTask:
    def complete():
        print('Swimming')

    def delete():
        print('Driver')


# Error handling
n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero")