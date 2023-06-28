# find_factorial

def find_factorial():
    number = int(input("please enter any number "))
    if number <0:
        
        print ("please enter a positiv numbeer ")
        
    if number == 0:
        pass
    if number == 1:
        print ("your Numbers factorial is 1 ")
    n = number
    k = 1
    while k < n :
        
        number *= k
        k += 1  
    print (number)
find_factorial()





#[1 - 100] pir numbers 

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)




# password matches 

sec_pass = "abcd"
pas = input("please enter your password ")
if sec_pass == pas:
    print ("sucsses")
else :
    print ("password error ")




 # print_pattern

n = int (input())
k = 1
while k<=n:
    j = 1
    while j <= k:
        print (j,end='')
        j+=1
    print()

    k+=1




# # find_common_elements

def f_c_e(ls1, ls2):
    comm_el = []
    for elem in ls1:
        if elem in ls2:
            comm_el.append(elem)
    return comm_el
ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 777, 8, 9, 0, 1]
ls2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 989]

print(f_c_e(ls1, ls2))




# find_prime_factors

ls = []
num = int(input ())
for k in range(2, num):
    for i in range(2, k):
        if k % i == 0:
            break
    else:
        ls.append(k)
print (ls)




# calculetor 

while True:
    a = int (input ("please enter the first element "))
    b = int (input ("please enter the second element "))
    x = str (input ("please choose one of the following option + - * /   for Exit ! "))
    if x == '+':
        c = a+b
        print (c)
    elif x == '-':
        print (a - b)
    elif x == '*' :
        print (a*b)
    elif x == '/':
        print (a/b)
    elif x ==  '!':
        break




# merges()

def merge(ls1, ls2):
    ls = []
    i, j = 0, 0

    while i < len(ls1) and j < len(ls2):
        if ls1[i] <= ls2[j]:
            ls.append(ls1[i])
            i += 1
        else:
            ls.append(ls2[j])
            j += 1

    while i < len(ls1):
        ls.append(ls1[i])
        i += 1

    while j < len(ls2):
        ls.append(ls2[j])
        j += 1

    return ls

print(merge([1,2,3,4,5,6],[4,5,6,7,8,9,12,13,90]))




#  numbers_to_wordes

def teen_numbers(x):
    x = str(x)
    if x == '1':
        xstr = 'eleven'
    elif x == '0':
        xstr = 'ten'
    elif x == '2':
        xstr = 'twelve'
    elif x == '3':
        xstr = 'thirteen'
    elif x == '4':
        xstr = 'fourteen'
    elif x == '5':
        xstr = 'fifteen'    
    elif x == '6':
        xstr = 'sixteen'
    elif x == '7':
        xstr = 'seventeen'
    elif x == '8':
        xstr = 'eighteen'
    elif x == '9':
        xstr = 'nineteen'

    return xstr


def numberToWord(x):
    if x == 1:
        xstr = 'one'
    elif x == 0:
        xstr = ''
    elif x == 2:
        xstr = 'two'
    elif x == 3:
        xstr = 'tre'
    elif x == 4:
        xstr = 'four'
    elif x == 5:
        xstr = 'five'    
    elif x == 6:
        xstr = 'six'
    elif x == 7:
        xstr = 'seven'
    elif x == 8:
        xstr = 'eight'
    elif x == 9:
        xstr = 'nine'
    else:
        xstr = ''

    return xstr



        
        


def int_str(str):
    num = list(str)
    for el in num:
        elem = int(el)
        index = num.index(el)
        num[index] = elem
    if (len(num) < 4):
        for i in range(0, 4):
            if i > len(num) - 1:
                num.insert(len(num) - i, 0)
        

    i = len(num) - 1
    res = []
    teen_prefix = ''
    if len(num) > 1:
        if num[len(num)  - 2] > 1:
            teen_prefix = 'ty'
    prefix = [' thousend ', ' hundred ', teen_prefix, ' ']
    print(num)
    while (i >= 0):
        currentText = ''
        currentText = numberToWord(num[i])
        number_representation = ''
        if (i == len(num) - 1) and num[len(num) - 2] == 1:
            number_representation =  teen_numbers(num[i]) 
        elif  num[i] != 0 and((i < len(num) - 2 and num[len(num) - 2] == 1 ) or (num[len(num) - 2] != 1)):
            print (num [i])
            number_representation = ' ' + currentText + prefix[i]
        res.append(number_representation)
        i -= 1
    res.reverse()
    j = 0
    result = ''
    while j < len(res):
        result += res[j]
        j += 1
        
    return result

numberToWord(2)
print(int_str(''))




# is_sorted

def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True
print (is_sorted([1,2,3,4,5]))



# power_of

def power_of(n):
  def power():
    c =n**n
    return c
  
  return power
  
print (power_of(3)())




# global x

x = 10
print (x)
def my_function():
    x = 20 
    print (x)

my_function()




# outer_function

def outer_function(x):
    def inner_function(fac):
        return x * fac

    res = inner_function(5) 
    print(res)

outer_function(10)   




# increment_counter

counte = 0
def increment_counter():
    global counte
    counte +=1
    print (counte)

increment_counter()
increment_counter()
print (counte)





# calculate_area

def calculate_area(rad):
    area = rad**2 * 3.14
    print (area)
calculate_area(2)