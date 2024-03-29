

</details>

# Question 47

### **Question**

> ***Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.***

----------------------
<details>  <summary>Show the answer</summary>

### Hints
> ***Use def methodName(self) to define a method.***

---------------------

**Main author's Solution: Python 2**
```python
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()
```
----------------
**My Solution: Python 3**
```python
class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)


circle = Circle(5)
print(circle.area())
```
----------------


</details>

# Question 48

### **Question**

> ***Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.***

----------------------
<details>  <summary>Show the answer</summary>

### Hints 
> ***Use def methodName(self) to define a method.***

----

**Main author's Solution: Python 2**
```python
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print aRectangle.area()

```
----------------
**My Solution: Python 3**
```python
class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width


rect = Rectangle(2,4)
print(rect.area())

```
----------------


</details>

# Question 49

### **Question**

> ***Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.***

----------------------

<details>  <summary>Show the answer</summary>
### Hints 
> ***To override a method in super class, we can define a method with the same name in the super class.***

----------------------

**Main author's Solution: Python 2**
```python
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print aSquare.area()
```
----------------
**My Solution: Python 3**
```python
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())      # prints 25 as given argument

print(Square().area())  # prints zero as default area
```
---------------------


</details>

# Question 50

### **Question**

> ***Please raise a RuntimeError exception.***

----------------------
### Hints
> ***UUse raise() to raise an exception.***

-----------
<details>  <summary>Show the answer</summary>

**Solution:**
```python
raise RuntimeError('something wrong')
```
----------------

</details>

## Conclusion

***Well It seems that the above problems are very much focused on basic concpets and implimantation of object oriented programming.As the concepts are not about to solve any functional problem rather design the structure , so both codes are very much similar in there implimantation part.***

[***go to previous day***](Documentation/../Day_12.md "Day 12")

[***go to next day***](Documentation/../Day_14.md "Day 14")

[***Discussion***](../../../../../issues)