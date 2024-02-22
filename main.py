#Task_1
#https://edabit.com/challenge/9hQogtkbZSSJ8tYsG
word = input("Enter  the  word:")

def reverser(word):
    reverse = word[::-1]
    text = reverse.swapcase()
    return text

print(reverser(word))

#Task_2
#https://edabit.com/challenge/S9KCN5kqoDbhNdKh5
lst = [
  "22222222",
  "22222222",
]

def count_characters(lst):
    i = 0
    for sign in lst:
        for sign1 in sign:
           if sign[0]==sign[1]:
              i+=1
    return i


print(count_characters(lst))


#Task_3
# https://edabit.com/challenge/HpqLxNqqRvMQoz8ME
string = "String"
string1 = ""
def double_char(string, string1):
    for letter in string:
        string1 += letter*2
    print(string1)


double_char(string, string1)

#Task_4
#https://edabit.com/challenge/rQkriLJBc9CbfRbJb
string = "eDaBiT"
lst = []
def index_of_caps(string, lst):
    for item in string:
        if item == item.upper():
            lst.append(string.index(item))
    print(lst)


(index_of_caps(string, lst))

#Task_5
#https://edabit.com/challenge/4Agr8CTY7x2rAhh5n
word = "hello"

def alphabet_soup(word):
    lst = list(word)
    sort = sorted(lst)
    string = ''.join(sort)
    print(string)

alphabet_soup(word)

#Task_6
#https://edabit.com/challenge/m9bcZKy4niMmsg3JX
lst = ["Adam", "Sarah", "Malcolm"]
lst1 =[]
def society_name(lst, lst1):
    for item in lst:
        lst1.append(item[0])
        lst1.sort
    j = "".join(lst1)
    print(j)

society_name(lst, lst1)


#Task_7
#https://edabit.com/challenge/vTGXrd5ntYRk3t6Ma
string = "Algorism"

def is_isogram(string):
    case = string.casefold()
    for x in case:
        if case.count(x)==1:
            return True
        else:
            return False


print(is_isogram(string))

#Task_8
#https://edabit.com/challenge/EFwDXErjDywXp56WG
word = "abc"

def is_in_order(word):
    b = list(word)
    a = sorted(b)
    if a==b:
        return True
    else:
        return False

print(is_in_order(word))

#Task_9
#https://edabit.com/challenge/MvgCxPkSgtQ8hQjwx
word = "I have never seen a thin person drinking Diet Coke."
vowel = "aeiuo"

def remove_vowels(word, vowel):
    string = ""
    for x in word:
        if x not in vowel:
            string = string +x
    return string

print(remove_vowels(word, vowel))

#Task_10
#https://edabit.com/challenge/763oGpb5JvctX5tAc
word = "cristian"
word1 = "Cristina"

def is_anagram(word, word1):
    r = set(word1).issuperset((set(word)))
    return r

print(is_anagram(word, word1))







