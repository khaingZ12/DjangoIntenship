mylist = []
def exam(name,marks):
    if marks > 100:
        mylist.append(name)
    else:
        print('pass')

exam(name='mg mag', marks= 100)
exam(name='mg hla', marks= 80)
exam(name='mg mya', marks= 100)
print(mylist)