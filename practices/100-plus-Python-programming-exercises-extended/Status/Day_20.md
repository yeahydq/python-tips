

</details>

# Question 80

### **Question**

>***Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].***


----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Use list comprehension to delete a bunch of element from a list.***

----------------------

**Main author's Solution: Python 2**
```python
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print li
```
----------------
**My Solution: Python 3**
```python
def isEven(n):
    return n%2!=0

li = [5,6,77,45,22,12,24]
lst = list(filter(isEven,li))
print(lst)
```
**OR**
```python
li = [5,6,77,45,22,12,24]
lst = list(filter(lambda n:n%2!=0,li))
print(lst)
```
---------------------



</details>

# Question 81

### **Question**

>***By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].***

----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Use list comprehension to delete a bunch of element from a list.***

----------------------

**Main author's Solution: Python 2**
```python
li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print li
```
----------------
**My Solution: Python 3**
```python
li = [12,24,35,70,88,120,155]
li = [x for x in li if x % 35!=0]
print(li)
```
---------------------


</details>

# Question 82

### **Question**

>***By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].***

----------------------
### Hints:
<details>  <summary>Show the answer</summary>

>***Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.***

----------------------

**Main author's Solution: Python 2**
```python

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print li
```
----------------
**My Solution: Python 3**
```python
li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i%2 != 0]
print(li)
```
---------------------



</details>

# Question 83

### **Question**

>***By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].***

----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.***

----------------------

**Main author's Solution: Python 2**
```python

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i<3 or 4<i]
print li

```
----------------
**My Solution: Python 3**
```python
#to be written
li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i<3 or 4<i]
print(li)
```
---------------------




</details>

# Question 84

### **Question**

> ***By using list comprehension, please write a program generate a 3\*5\*8 3D array whose each element is 0.***


----------------------
### Hints:
<details>  <summary>Show the answer</summary>

> ***Use list comprehension to make an array.***

----------------------

**Solution:**
```python
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print array
```
----------------

</details>

[***go to previous day***](Documentation/../Day_19.md "Day 19")

[***go to next day***](Documentation/../Day_21.md "Day 21")

[***Discussion***](../../../../../issues)