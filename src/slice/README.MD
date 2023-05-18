
## Slice a list or string in Python
## s[:] and s[::]
   -都是copy原string或list
```python
   s = [1, 2, 3, 4, 5]
   s_copy_1 = s[::]
   s_copy_2 = s[:]

   print(s_copy_1)  # [1, 2, 3, 4, 5]
   print(s_copy_2)  # [1, 2, 3, 4, 5]

   print(s_copy_1 is s)  # False (s_copy_1 is a different list object)
   print(s_copy_2 is s)  # False (s_copy_2 is a different list object)
```
      
## s[:-1] and s[::-1]
 s[:-1] Includes all elements of the list s **except** the last element.

 ```python
         s = [1, 2, 3, 4, 5]
         result = s[:-1]
         print(result)  # [1, 2, 3, 4]
 ```
 s[::-1] **Reverses** the order of elements in the list s
 ```python
         s = [1, 2, 3, 4, 5]
         result = s[::-1]
         print(result)  # [5, 4, 3, 2, 1]
  ```
 
 ## s[3:-1] and s[3::-1] and s[3:][::-1]
 s[3:-1]: This slice includes elements from index 3 **up to, but not including**, the last element of the list s
 ```python
   s = [1, 2, 3, 4, 5, 6]
   result = s[3:-1]
   print(result)  # [4, 5]
 ```
 s[3::-1] **Reverses** the order of elements from index 3 to the beginning of the list.
```python
   s = [1, 2, 3, 4, 5, 6]
   result = s[3::-1]
   print(result)  # [4, 3, 2, 1]
```


