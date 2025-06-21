# list = [] ပြင်လို့ရ
# set = []
# tuple = () ပြင်လို့မရ
# dict = {'key': 'values'}
list = [12,13,1.2,"hello"]
tuple = (12,13,1.2,"hello")
dict = {'name': 'mg mg', 'age': 25}
print(dict)


a = [12,10,5,8,14]
b = [0,1,2,3,4]   #indent
print(a[0])
print(a[1:3])    #range  ဆိုရင် (start, end + 1)


dic = {'name': 'mg mg', 'age': 25}
print(dic['age'])
print(dic.values())


list = ['apple', 'orange', 'car']
# append  ထပ်ထည့်ချင်ရင်သုံး

list.append('bus')
list[1] = 'train'   # နေရာ change  # orange နေရာမှာ train ကိုအစားထိုး
list.insert(2,'ybs')  # ကိုယ်ထည့်ချင်တဲ့နေရာမှာထည့်
list.remove('apple')    # ဖျက်ချင်ရင်သုံး    # ဖျက်မည့်တန်ဖိုးထည့်ပေးရ
print(list)
