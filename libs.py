import math
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich import box

console = Console()


def show_function(title, description=""):
    console.print()

    content = f"[bold bright_cyan]{title.upper()}[/bold bright_cyan]"

    if description:
        content += f"\n[white]{description}[/white]"

    console.print(
        Panel(
            content,
            border_style="bright_magenta",
            box=box.DOUBLE,
            padding=(1, 3),
            expand=False
        )
    )
    console.print()



def func_head(title, category="MATH ENGINE"):
    console.print()
    console.print(
        Rule(
            f"[bold bright_cyan]{category}[/bold bright_cyan]",
            style="bright_magenta"
        )
    )
    console.print(f"[bold white]  {title}[/bold white]")
    console.print(Rule(style="bright_cyan"))
    console.print()


def func_inp(prompt):
    return console.input(
        f"[bold bright_cyan]{prompt}[/bold bright_cyan] "
        "[bright_magenta]› [/bright_magenta]"
    )


def func_res(value):
    console.print()
    console.print("[dim]  RESULT[/dim]")
    console.print(f"  [bold bright_green]{value}[/bold bright_green]")
    console.print()


def add(a, b):
    func_res(a + b)

def subtract(a, b):
    func_res(a - b)

def multiply(a, b):
    func_res(a * b)

def divide(a, b):
    func_res(a // b)

def power(a,b):
    func_res(a ** b)

def square_root(a):
    func_res(math.sqrt(a))

def square(a):
    func_res(a ** 2)

def cube(a):
    func_res(a ** 3)

def cube_root(a):
    func_res(a ** (1/3))

def nth_root(a, n):
    func_res(a ** (1/n))

def log(a, base):
    func_res(math.log(a, base))

def perfect_square(a):
    if (math.sqrt(a) % 1) == 0:
        func_res(f"{a} is a perfect square.")
    else:
        func_res(f"{a} is not a perfect square.")

def perfect_cube(a):
    if (a ** (1/3) % 1) == 0:
        func_res(f"{a} is a perfect cube.")
    else:
        func_res(f"{a} is not a perfect cube.")    

def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact *= i
    func_res(fact)

def floor_div(a, b):
    func_res(a // b)

def modulus(a, b):
    func_res(a % b)

def absolute(a):
    func_res(abs(a))

def add_inv(a):
    func_res(0-a)

def mult_inv(a):
    func_res(1/a)

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
    func_res(f"Minimum: {min_num}, Maximum: {max_num}")

def avg(count):
    total = 0
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        total += num
    avg = total / count
    func_res(avg)

def gcd(count):
    nums = []
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        nums.append(num)

    func_res(math.gcd(*nums))

def lcm(count):
    nums = []
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        nums.append(num)

    func_res(math.lcm(*nums))

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
        func_res(f"{num} is a prime number.")
    else:
        func_res(f"{num} is not a prime number.")

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

    func_res(primes)

def fibonacci(count):
    fib = [0,1]
    curr = 0
    nx = 1
    for i in range(2, count):
        curr += nx
        fib.append(curr)
        nx = fib[i-1]

    func_res(fib[:count])

def div_check(a, b):
    if a % b == 0:
        func_res(f"{a} is divisible by {b}.")
    else:
        func_res(f"{a} is not divisible by {b}.")

def sin(a):
    func_res(math.sin(math.radians(a)))

def cos(a):
    func_res(math.cos(math.radians(a)))

def tan(a):
    func_res(math.tan(math.radians(a)))

def cosec(a):
    func_res(1/math.sin(math.radians(a)))

def sec(a):
    func_res(1/math.cos(math.radians(a)))

def cot(a):
    func_res(1/math.tan(math.radians(a)))

def solve_lin(a, b):
    root = (0-b)/a
    func_res(root)

def solve_quad(a, b, c):
    root1 = (-b + math.sqrt((b**2) - 4*a*c))/(2*a)
    root2 = (-b - math.sqrt((b**2) - 4*a*c))/(2*a)

    func_res(f"{root1} and {root2}")

def form_quad(a, b):
    func_res(f"x² - {a+b}x + {a*b}")

def floor(a):
    func_res(math.floor(a))

def chck_armstrong(a):
    ls = list(str(a))
    sum = 0
    for i in ls:
        sum += int(i) ** len(ls)
    
    if a == sum:
        func_res(f"{a} is an armstrong number.")
    else:
        func_res(f"{a} is not an armstrong number")

def rand_game(fr, to, ges):
    num = random.randint(fr, to)
    for i in range(ges):
        n = int(input(f"Enter guess number {i+1}: "))
        if n == num:
            func_res("You won!!")
            break
        if (i+1) == ges and n != num:
            func_res("You lost, Good luck next time")
        func_res(f"You have {ges-i+1} guesses left.")

def pi():
    func_res(math.pi)

def p_sq(s):
    func_res(4*s)

def a_sq(s):
    func_res(s*s)

def p_rect(l, b):
    func_res(2*(l+b))

def a_rect(l, b):
    func_res(l*b)

def diag(n):
    func_res((n*(n-3))/2)

def p_poly(s, n):
    func_res(n*s)

def palin(s):
    ls_old = list(str(s))
    ls_new = ls_old[::-1]
    if ls_old == ls_new:
        func_res("It is a palindrome.")
    else:
        func_res("It is not a palindrome.")

def sa_cube(s):
    sa = 6*(s*s)
    func_res(sa)

def v_cube(s):
    vc = s**3
    func_res(vc)

def sa_cuboid(l, b, h):
    sa = 2*((l*b)+(b*h)+(h*l))
    func_res(sa)

def v_cuboid(l, b, h):
    vc = l * b * h
    func_res(vc)
    
def sa_cone(r, h):
    l = math.sqrt(h*h + r*r)
    sa = math.pi * r * (l+r)
    func_res(sa)

def v_cone(r, h):
    vc = (math.pi * r *r * h)/3
    func_res(vc)
    
def sa_cyl(r, h):
    sa = 2 * math.pi * r * (h + r)
    func_res(sa)
    
def v_cyl(r, h):
    vc = math.pi * r * r * h
    func_res(vc)
    
def sa_sph(r):
    sa  = 4 * math.pi * r * r
    func_res(sa)

def v_sph(r):
    vs = (4 * math.pi * (r ** 3)) / 3
    func_res(vs)

def sa_hms(r):
    sa = 3 * math.pi * r * r
    func_res(sa)
    
def v_hms(r):
    vs = 2*(math.pi * (r ** 3))/3
    func_res(vs)

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
