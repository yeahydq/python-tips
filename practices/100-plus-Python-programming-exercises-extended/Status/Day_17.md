

</details>

# Question 65

### **Question**

>***Please write assert statements to verify that every number in the list [2,4,6,8] is even.***


----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Use "assert expression" to make assertion.***

----------------------

**Main author's Solution: Python 2**
```python
li = [2,4,6,8]
for i in li:
    assert i%2==0
```
----------------
**My Solution: Python 3**
```python
data = [2,4,5,6]
for i in data:
    assert i%2 == 0, "{} is not an even number".format(i)
```
---------------------



</details>

# Question 66

### **Question**

>***Please write a program which accepts basic mathematic expression from console and print the evaluation result.***

>***Example:
If the following n is given as input to the program:***
```
35 + 3
```
>***Then, the output of the program should be:***
```
38
```

----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Use eval() to evaluate an expression.***

----------------------

**Main author's Solution: Python 2**
```python
expression = raw_input()
print eval(expression)
```
----------------
**My Solution: Python 3**
```python
expression = input()
ans = eval(expression)
print(ans)
```
---------------------


</details>

# Question 67

### **Question**

>***Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.***

----------------------
### Hints:
<details>  <summary>Show the answer</summary>

>***Use if/elif to deal with conditions.***

----------------------

**Main author's Solution: Python 2**
```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print bin_search(li,11)
print bin_search(li,12)

```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------



</details>

# Question 68

### **Question**

>***Please generate a random float where the value is between 10 and 100 using Python module.***

----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Use random.random() to generate a random float in [0,1].***

----------------------

**Main author's Solution: Python 2**
```python
import random
print random.random()*100
```
----------------
**My Solution: Python 3**
```python
import random
rand_num = random.uniform(10,100)
print(rand_num)
```
---------------------




</details>

# Question 69

### **Question**

>***Please generate a random float where the value is between 5 and 95 using Python module.***


----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Use random.random() to generate a random float in [0,1].***

----------------------

**Main author's Solution: Python 2**
```python
import random
print random.random()*100-5
```
----------------
**My Solution: Python 3**
```python
import random
rand_num = random.uniform(5,95)
print(rand_num)
```
---------------------


[***go to previous day***](Documentation/../Day_16.md "Day 16")

[***go to next day***](Documentation/../Day_18.md "Day 18")

[***Discussion***](../../../../../issues)