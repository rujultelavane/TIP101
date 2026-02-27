#we are currently in our first python file

'''def print_num(num):
    print(num)

print_num(4)
print_num(5)
print_num(6)

def hello_world():
    print("Hello world!")

hello_world()'''


######## PROBLEM SET 1 ########

#1.
def hello_world():
    print("Hello world!")
hello_world()

#2.
def todays_mood():
    mood = "😎"
    print("Today's mood: " + mood)

todays_mood()

#3.
def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu("🍕")

#4.
def add(a, b):
    return a + b

sum1 = add(13, 27)
print(add(sum1, sum1))

#5.
def product(a, b):
    return a*b
print(product(22, 7))

#6. 
def classify_age(age):
    if(age<18):
        return "child"
    else: 
        return "adult"

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)

#7
def what_time_is_it(hour):
    if(hour==2):
        return "taco time 🌮"
    if (hour==12):
        return "peanut butter jelly time 🥪"
    else:
        return "nap time 😴"

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)

#8.
def blackjack(score):
    if score==21:
        print("Blackjack!")
    if score>21:
        print("Bust!")
    if 17<=score<21:
        print("Nice hand!")
    if score<17:
        print("Hit me!")

blackjack(21)
blackjack(24)
blackjack(19)
blackjack(10)

#9.
def get_first(lst):
    return lst[0]

lst = [3,1,6,7,5]
print(get_first(lst))

#10.
def get_last(lst):
    return lst[len(lst)-1]

print(get_last(lst))

#11.
def counter(stop):
    for i in range(stop+1):
        print (i)

counter(7)

#12.
def sum_ten():
    sum = 0
    for i in range(11):
        sum += i
    return sum

output = sum_ten()
print(output)

#13.
def sum_positive_range(stop):
    sum=0
    for i in range(stop+1):
        sum+=i
    return sum
sum = sum_positive_range(6)
print(sum)

#14.
def sum_range(start, stop):
    sum=0
    for i in range(start, stop+1):
        sum+=i
    return sum
sum = sum_range(3, 9)
print(sum)

#15.
def print_negatives(lst):
    sum=0
    found_neg = False
    for i in lst:
        if i<0:
            found_neg = True
            print(i)
    if found_neg == False:
        print("None")

print_negatives([3,-2,2,1,-5])
print_negatives([1,2,3,4,5])


######## PROBLEM SET 2 ########
#1.
def greet_user(name):
    print("Hello "+name)

greet_user("Michael")

#2.
def difference(a, b):
    return b-a
diff = difference(8, 3)
print(diff)

#3.
def concatenate_list(nums):
    ans = []
    