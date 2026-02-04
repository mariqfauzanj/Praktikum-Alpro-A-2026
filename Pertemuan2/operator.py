# operator

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

# operator aritmatika

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# operator assignment

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# operator perbandingan

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# operator logika

x = 5
print(x > 0 and x < 10) # operator and


x = 5
print(x < 5 or x > 10) # operator or


x = 5
print(not(x > 3 and x < 10)) # operator not

# operator identitas

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) # is, mengecek ketika dua variable memiliki nilai yang sama di memori
print(x is y) # ==, mengecek ketika dua variable menunjuk ke object yang sama

# operator keanggotaan

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# operator bitwise

print(6 & 3)

print(6 | 3)

print(6 ^ 3)

# operator presedens

print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

print(5 + 4 - 7 + 3)