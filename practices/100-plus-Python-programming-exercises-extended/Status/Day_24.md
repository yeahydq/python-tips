
</details>

# Question 100

### **Question**

>***You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.***

>***If the following string is given as input to the program:***
>```
>4
>bcdef
>abcdefg
>bcde
>bcdef
>```
>***Then, the output of the program should be:***
>```
>3
>2 1 1
>```

### Hints:
<details>  <summary>Show the answer</summary>

> ***Make a list to get the input order and a dictionary to count the word frequency***

----------------------
**My Solution: Python 3**
```python
n = int(input())

word_list = []
word_dict = {}

for i in range(n):
    word = input()
    if word not in word_dict:
        word_list.append(word)
    word_dict[word] = word_dict.get(word, 0) + 1

print(len(word_list))
for word in word_list:
    print(word_dict[word], end=' ')
```
---------------------


</details>

# Question 101

### **Question**

>***You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.***

>***If the following string is given as input to the program:***
>```
>aabbbccde
>```
>***Then, the output of the program should be:***
>```
>b 3
>a 2
>c 2
>```

### Hints:
<details>  <summary>Show the answer</summary>

> ***Count frequency with dictionary and sort by Value from dictionary Items***

----------------------

**My Solution: Python 3**
```python
word = input()
dct = {}
for i in word:
    dct[i] = dct.get(i,0) + 1

dct = sorted(dct.items(),key=lambda x: (-x[1],x[0]))
for i in dct[:3]:
    print(i[0],i[1])
```
---------------------



</details>

# Question 102
### **Question**

>***Write a Python program that accepts a string and calculate the number of digits and letters.***

**Input**
>```
>Hello321Bye360
>```

**Output**
>```
>Digit - 6
>Letter - 8
>```
----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Use isdigit() and isalpha() function***

----------------------

**Solution:**
```python
word = input()
digit,letter = 0,0
for char in word:
    digit+=char.isdigit()
    letter+=char.isalpha()

print('Digit -',digit)
print('Letter -',letter)
```
----------------



</details>

# Question 103

### **Question**

>***Given a number N.Find Sum of 1 to N Using Recursion***

**Input**
>```
>5
>```

**Output**
>```
>15
>```

----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Make a recursive function to get the sum***

----------------------

**Solution:**
```python
def rec(n):
    if n == 0:
        return n
    return rec(n-1) + n


n = int(input())
sum = rec(n)
print(sum)
```
----------------

</details>

[***go to previous day***](Documentation/../Day_22.md "Day 23")

[***Discussion***](../../../../../issues)

# To Be Continue...