import math
import random

def add(a, b):
    print("Sum:",a + b)

def subtract(a, b):
    print("Difference:",a - b)

def multiply(a, b):
    print("Product:",a * b)

def divide(a, b):
    print("Quotient:",a // b)
    print("Remainder:", a % b)

def power(a,b):
    print("Power:", a ** b)

def square_root(a):
    print("Square Root:", math.sqrt(a))

def square(a):
    print("Square:", a ** 2)

def cube(a):
    print("Cube:", a ** 3)

def cube_root(a):
    print("Cube Root:", a ** (1/3))

def nth_root(a, n):
    print(f"{n}th Root:", a ** (1/n))

def log(a, base):
    print(f"Logarithm base {base}:", math.log(a, base))

def perfect_square(a):
    if (math.sqrt(a) % 1) == 0:
        print(f"{a} is a perfect square.")
    else:
        print(f"{a} is not a perfect square.")

def perfect_cube(a):
    if (a ** (1/3) % 1) == 0:
        print(f"{a} is a perfect cube.")
    else:
        print(f"{a} is not a perfect cube.")    

def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact *= i
    print("Factorial:", fact)

def floor_div(a, b):
    print("Floor Division:", a // b)

def modulus(a, b):
    print("Modulus:", a % b)

def absolute(a):
    print("Absolute Value:", abs(a))

def add_inv(a):
    print("Additive Inverse:", 0-a)

def mult_inv(a):
    print("Multiplicative Inverse:", 1/a)

def min_max(count):
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        if i == 0:
            min_num = num
            max_num = num
        else:
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num
    print(f"Minimum: {min_num}, Maximum: {max_num}")

def avg(count):
    total = 0
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        total += num
    avg = total / count
    print(f"Average: {avg}")

def gcd(count):
    nums = []
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        nums.append(num)

    print("GCD:", math.gcd(*nums))

def lcm(count):
    nums = []
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        nums.append(num)

    print("LCM:", math.lcm(*nums))

def prime_check(num):
    is_p = True
    if num > 1:
        for i in range(2, (num**0.5+1)):
            if num % i == 0:
                is_p = False
                break
    else:
        is_p = False

    if is_p:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

def prime_list(count):
    primes = []
    for i in range(2, count +1):
        is_p = True
        if i > 1:
            for j in range(2, (i**0.5)+1):
                if i % j == 0:
                    is_p = False
                    break
        else:
            is_p = False

        if is_p:
            primes.append(i)

    print(f"Prime numbers between 1 and {count}: {primes}")

def fibonacci(count):
    fib = [0,1]
    curr = 0
    nx = 1
    for i in range(2, count):
        curr += nx
        fib.append(curr)
        nx = fib[i-1]

    print(f"Fibonacci series up to {count} terms: {fib[:count]}")

def div_check(a, b):
    if a % b == 0:
        print(f"{a} is divisible by {b}.")
    else:
        print(f"{a} is not divisible by {b}.")

def sin(a):
    print(f"Sine of {a} degrees:", math.sin(math.radians(a)))

def cos(a):
    print(f"Cosine of {a} degrees:", math.cos(math.radians(a)))

def tan(a):
    print(f"Tangent of {a} degrees:", math.tan(math.radians(a)))

def cosec(a):
    print(f"Cosecant of {a} degrees:", 1/math.sin(math.radians(a)))

def sec(a):
    print(f"Secant of {a} degrees:", 1/math.cos(math.radians(a)))

def cot(a):
    print(f"Cotangent of {a} degrees:", 1/math.tan(math.radians(a)))

def solve_lin(a, b):
    root = (0-b)/a
    print(f"The root of {b}x + {a} = 0 is {root}")

def solve_quad(a, b, c):
    root1 = (-b + math.sqrt((b**2) - 4*a*c))/(2*a)
    root2 = (-b - math.sqrt((b**2) - 4*a*c))/(2*a)

    print(f"The roots of the equation {a}x² + {b}x + {c} = 0 are {root1} and {root2}")

def form_quad(a, b):
    print(f"A quadratic equation using the roots {a} and {b} is x² - {a+b}x + {a*b}")

def floor(a):
    print(math.floor(a))

def chck_armstrong(a):
    ls = list(str(a))
    sum = 0
    for i in ls:
        sum += int(i) ** len(ls)
    
    if a == sum:
        print(f"{a} is an armstrong number.")
    else:
        print(f"{a} is not an armstrong number")

def rand_game(fr, to, ges):
    num = random.randint(fr, to)
    print(num)
    for i in range(ges):
        n = int(input(f"Enter guess number {i+1}: "))
        if n == num:
            print("You won!!")
            break
        if (i+1) == ges and n != num:
            print("You lost, Good luck next time")
        print(f"You have {ges-i+1} guesses left.")

def pi():
    print(f"Pi value is {math.pi}")

def p_sq(s):
    print(f"Perimeter of the square with side {s} units is {4*s} units")

def a_sq(s):
    print(f"Area of square with side {s} units is {s*s} sq. units.")

def p_rect(l, b):
    print(f"Perimeter of rectangle with length {l} units and breadth {b} units is {2*(l+b)} units.")

def a_rect(l, b):
    print(f"Area of rectangle with length {l} units and breadth {b} units is {l*b} sq. units.")

def diag(n):
    print(f"Number of diagonals of polygon with {n} sides is {(n*(n-3))/2}")

def p_poly(s, n):
    print(f"A polygon with {n} sides and each side being {s} units will have a perimeter of {n*s} units")

def palin(s):
    ls_old = list(str(s))
    ls_new = ls_old[::-1]
    if ls_old == ls_new:
        print("It is a palindrome.")

def sa_cube(s):
    sa = 6*(s*s)
    print(f"The total surface area of a cube with side {s} units is {sa} sq. units.")

def v_cube(s):
    vc = s**3
    print(f"The volume of a cube with side {s} units is {vc} cu. units.")

def sa_cuboid(l, b, h):
    sa = 2*((l*b)+(b*h)+(h*l))
    print(f"The surface area of a cuboid with length {l} units, breadth {b} units and height {h} units is {sa} sq. units.")

def v_cuboid(l, b, h):
    vc = l * b * h
    print(f"The volume of a cuboid with length {l} units, breadth {b} units and height {h} units is {vc} cu. units.")

def sa_cone(r, h):
    l = math.sqrt(h*h + r*r)
    sa = math.pi * r * (l+r)
    print(f"The surface area of a cone with radius {r} units and height {h} units is {sa} sq. units.")

def v_cone(r, h):
    vc = (math.pi * r *r * h)/3
    print(f"The volume of a cone with radius {r} units and height {h} units is {vc} cu. units.")

def sa_cyl(r, h):
    sa = 2 * math.pi * r * (h + r)
    print(f"The surface area of a cylinder with radius {r} units and height {h} units is {sa} sq. units.")

def v_cyl(r, h):
    vc = math.pi * r * r * h
    print(f"The volume of a cylinder with radius {r} units and height {h} is {vc} cu. units.")

def sa_sph(r):
    sa  = 4 * math.pi * r * r
    print(f"The surface area of a sphere with radius {r} units is {sa} sq. units.")

def v_sph(r):
    vs = (4 * math.pi * (r ** 3)) / 3
    print(f"The volume of a sphere with radius {r} units is {vs} cu. units")

def sa_hms(r):
    sa = 3 * math.pi * r * r
    print(f"The surface area of a hemisphere with radius {r} units is {sa} sq. units.")

def v_hms(r):
    vs = 2*(math.pi * (r ** 3))/3
    print(f"The volume of a hemisphere with radius {r} units is {vs} cu. units.")

def show_help():
    print("""
1. Addition  
2. Subtraction  
3. Multiplication  
4. Division  
5. Power  
6. Square Root  
7. Square  
8. Cube  
9. Cube Root  
10. Nth Root  
11. Logarithm  
12. Perfect Square Check  
13. Perfect Cube Check  
14. Factorial  
15. Floor Division  
16. Modulus  
17. Absolute Value  
18. Additive Inverse  
19. Multiplicative Inverse  
20. Minimum & Maximum  
21. Average  
22. GCD  
23. LCM  
24. Prime Check  
25. Prime List  
26. Fibonacci Sequence  
27. Divisibility Check  
28. Sine  
29. Cosine  
30. Tangent  
31. Cosecant  
32. Secant  
33. Cotangent  
34. Solve Linear Equation  
35. Solve Quadratic Equation  
36. Form Quadratic Equation from Roots  
37. Floor  
38. Armstrong Number Check  
39. Random Guessing Game  
40. Pi  
41. Square Perimeter  
42. Square Area  
43. Rectangle Perimeter  
44. Rectangle Area  
45. Number of Polygon Diagonals  
46. Polygon Perimeter  
47. Cube Surface Area  
48. Cube Volume  
49. Cuboid Surface Area  
50. Cuboid Volume  
51. Cone Surface Area  
52. Cone Volume  
53. Cylinder Surface Area  
54. Cylinder Volume  
55. Sphere Surface Area  
56. Sphere Volume  
57. Hemisphere Surface Area  
58. Hemisphere Volume  
59. Palindrome Check

Type 'stop' to stop code

""")
