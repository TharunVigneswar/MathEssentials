import libs as l
import time
import keyboard
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

console.clear()

console.print(
    Panel(
        "[bold bright_cyan]MATH ESSENTIALS[/bold bright_cyan]\n\n"
        "[white]Your all-in-one mathematics toolkit[/white]\n"
        "[bright_magenta]59 Functions | Endless Possibilities[/bright_magenta]",
        border_style="bright_magenta",
        box=box.DOUBLE,
        padding=(1, 4),
        expand=False
    ),
    justify="center"
)



while True:
    console.print()
    func = console.input(
        "[bold bright_cyan]➜ Enter function[/bold bright_cyan] "
        "[dim](number or name)[/dim]: "
    ).lower().strip()
    console.print()

    if func == "1" or func == "add":
        l.func_head("Addition", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number 1: "))
        b = int(l.func_inp("Enter number 2: "))
        l.add(a, b)
    elif func == "2" or func == "subtract":
        l.func_head("Subtraction", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number 1: "))
        b = int(l.func_inp("Enter number 2: "))
        l.subtract(a, b)
    elif func == "3" or func == "product":
        print("Multiplication", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number 1: "))
        b = int(l.func_inp("Enter number 2: "))
        l.multiply(a, b)
    elif func == "4" or func == "divide":
        l.func_head("Division", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number 1: "))
        b = int(l.func_inp("Enter number 2: "))
        l.divide(a, b)
    elif func == "5" or func == "power":
        l.func_head("Exponent", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter base number: "))
        b = int(l.func_inp("Enter power: "))
        l.power(a, b)        
    elif func == "6" or func == "sqrt":
        l.func_head("Square Root", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter Number: "))
        l.square_root(a)
    elif func == "7" or func == "square":
        l.func_head("Square", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter Number: "))
        l.square(a)
    elif func == "8" or func == "cube":
        l.func_head("Cube", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter Number: "))
        l.cube(a)
    elif func == "9" or func == "cube root":
        l.func_head("Cube Root", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter Number: "))
        l.cube_root(a)
    elif func == "10" or func == "nth root":
        l.func_head("Nth Root", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter base number: "))
        b = int(l.func_inp("Enter root: "))
        l.nth_root(a, b)
    elif func == "11" or func == "log":
        l.func_head("Logarithm", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number to find log: "))
        b = int(l.func_inp("Enter base number: "))
        l.log(a, b)
    elif func == "12" or func == "square check":
        l.func_head("Perfect Square Check", "NUMBER PROPERTIES & SEQUENCES")
        a = int(l.func_inp("Enter Number: "))
        l.perfect_square(a)
    elif func == "13" or func == "cube check":
        l.func_head("Perfect Cube Check", "NUMBER PROPERTIES & SEQUENCES")
        a = int(l.func_inp("Enter Number: "))
        l.perfect_cube(a)
    elif func == "14" or func == "factorial":
        l.func_head("Factorial", "NUMBER PROPERTIES & SEQUENCES")
        a = int(l.func_inp("Enter number: "))
        l.factorial(a)
    elif func == "15" or func == "floor division":
        l.func_head("Floor Division", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number 1: "))
        b = int(l.func_inp("Enter number 2: "))
        l.floor_div(a, b)
    elif func == "16" or func == "mod":
        l.func_head("Modulus", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number 1: "))
        b = int(l.func_inp("Enter number 2: "))
        l.modulus(a, b)
    elif func == "17" or func == "abs" or func == "absolute":
        l.func_head("Absolute", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number: "))
        l.absolute(a)
    elif func == "18" or func == "additive inverse":
        l.func_head("Additive Inverse", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number: "))
        l.add_inv(a)
    elif func == "19" or func == "multiplicative inverse":
        l.func_head("Multiplicative Inverse", "BASIC ARITHMETIC")
        a = int(l.func_inp("Enter number: "))
        l.mult_inv(a)
    elif func == "20" or func == "min max":
        l.func_head("Min Max", "STATISTICS & NUMBER THEORY")
        a = int(l.func_inp("Enter total number of numbers you want to compare: "))
        l.min_max(a)
    elif func == "21" or func == "avg":
        l.func_head("Average", "STATISTICS & NUMBER THEORY")
        a = int(l.func_inp("Enter total number of numbers you want to find average of: "))
        l.avg(a)
    elif func == "22" or func == "gcd":
        l.func_head("Greatest Common Divisor", "STATISTICS & NUMBER THEORY")
        a = int(l.func_inp("Enter the total number of numbers you want to find GCD of: "))
        l.gcd(a)
    elif func == "23" or func == "lcm":
        l.func_head("Least Common Multiple", "STATISTICS & NUMBER THEORY")
        a = int(l.func_inp("Enter the total number of numbers you want to find LCM of: "))
        l.lcm(a)
    elif func == "24" or func == "check prime":
        l.func_head("Check if given number is prime", "NUMBER PROPERTIES & SEQUENCES")
        a = int(l.func_inp("Enter number: "))
        l.prime_check(a)
    elif func == "25" or func == "list primes":
        l.func_head("List Prime numbers", "NUMBER PROPERTIES & SEQUENCES")
        a = int(l.func_inp("Till what number to print prime numbers: "))
        l.prime_list(a)
    elif func == "26" or func == "fibonacci":
        l.func_head("Fibonacci Sequence", "NUMBER PROPERTIES & SEQUENCES")
        a = int(l.func_inp("Enter number: "))
        l.fibonacci(a)
    elif func == "27" or func == "div check":
        l.func_head("Divisibility Check", "NUMBER PROPERTIES & SEQUENCES")
        a = int(l.func_inp("Enter number 1: "))
        b = int(l.func_inp("Enter number 2: "))
        l.div_check(a, b)
    elif func == "28" or func == "sin":
        l.func_head("Sine value of an angle", "TRIGONOMETRY")
        a = int(l.func_inp("Enter degree value: "))
        l.sin(a)
    elif func == "29" or func == "cos":
        l.func_head("Cosine value of an angle", "TRIGONOMETRY")
        a = int(l.func_inp("Enter degree value: "))
        l.cos(a)
    elif func == "30" or func == "tan":
        l.func_head("Tangent value of an angle", "TRIGONOMETRY")
        a = int(l.func_inp("Enter degree value: "))
        l.tan(a)
    elif func == "31" or func == "cosec":
        l.func_head("Cosecant value of an angle", "TRIGONOMETRY")
        a = int(l.func_inp("Enter degree value: "))
        l.cosec(a)
    elif func == "32" or func == "sec":
        l.func_head("Secant value of an angle", "TRIGONOMETRY")
        a = int(l.func_inp("Enter degree value: "))
        l.sec(a)
    elif func == "33" or func == "cot":
        l.func_head("Cotangent value of an angle", "TRIGONOMETRY")
        a = int(l.func_inp("Enter degree value: "))
        l.cot(a)
    elif func == "34" or func == "solve linear equation":
        l.func_head("Solve a linear equation", "ALGEBRA & EQUATION")
        a = int(l.func_inp("Enter coefficient of x: "))
        b = int(l.func_inp("Enter constant value: "))
        l.solve_lin(a, b)
    elif func == "35" or func == "solve quadratic equation":
        l.func_head("Solve a quadratic equation", "ALGEBRA & EQUATION")
        a = int(l.func_inp("Enter coefficient of x²: "))
        b = int(l.func_inp("Enter coefficient of x: "))
        c = int(l.func_inp("Enter constant value: "))
        l.solve_quad(a, b, c)
    elif func == "36" or func == "form quadratic equation":
        l.func_head("Form Quadratic Equation from Roots", "ALGEBRA & EQUATION")
        a = int(l.func_inp("Enter first root: "))
        b = int(l.func_inp("Enter second root: "))
        l.form_quad(a, b)
    elif func == "37" or func == "floor":
        l.func_head("Floor Value", "BASIC ARITHMETIC"   )
        a = int(l.func_inp("Enter number to find floor of: "))
        l.floor(a)
    elif func == "38" or func == "check armstrong":
        l.func_head("Check if given number is an armstrong number", "NUMBER PROPERTIES & SEQUENCES")
        a = int(l.func_inp("Enter number: "))
        l.chck_armstrong(a)
    elif func == "39" or func == "number guesser":
        l.func_head("Number Guesser Game", "GAME")
        fr = int(l.func_inp("Enter start number: "))
        to = int(l.func_inp("Enter end number: "))
        ges = int(l.func_inp("Enter number of guesses: "))
        l.rand_game(fr, to, ges)
    elif func == "40" or func == "pi":
        l.func_head("Pi", "CONSTANT")
        l.pi()
    elif func == "41" or func == "square perimeter":
        l.func_head("Perimeter of Square", "2D GEOMETRY")
        s = int(l.func_inp("Enter square side length: "))
        l.p_sq(s)
    elif func == "42" or func == "square area":
        l.func_head("Area of Square", "2D GEOMETRY")
        s = int(l.func_inp("Enter square side length: "))
        l.a_sq(s)
    elif func == "43" or func == "rectangle perimeter":
        l.func_head("Perimeter of Rectangle", "2D GEOMETRY")
        le = int(l.func_inp("Enter rectangle length: "))
        b = int(l.func_inp("Enter rectangle breadth: "))
        l.p_rect(le, b)
    elif func == "44" or func == "rectangle area":
        l.func_head("Area of Rectangle", "2D GEOMETRY")
        l = int(l.func_inp("Enter rectangle length: "))
        b = int(l.func_inp("Enter rectangle breadth: "))
        l.a_rect(l, b)
    elif func == "45" or func == "diagonal count":
        l.func_head("Find number of diagonals of a polygon", "2D GEOMETRY")
        n = int(l.func_inp("Enter number of sides of polygon: "))
        l.diag(n)
    elif func == "46" or func == "perimeter of polygon":
        l.func_head("Find perimeter of polygon", "2D GEOMETRY")
        n = int(l.func_inp("Enter number of sides: "))
        s = int(l.func_inp("Enter length of each side: "))
        l.p_poly(s, n)
    elif func == "47" or func == "surface area of cube":
        l.func_head("Find surface area of cube", "3D GEOMETRY")
        s = int(l.func_inp("Enter length of each side of cube: "))
        l.sa_cube(s)
    elif func == "48" or func == "volume of cube":
        l.func_head("Find volume of cube", "3D GEOMETRY")
        s = int(l.func_inp("Enter length of each side of cube: "))
        l.v_cube(s)
    elif func == "49" or func == "surface area of cuboid":
        l.func_head("Find surface area of cuboid", "3D GEOMETRY")
        l = int(l.func_inp("Enter length of cuboid: "))
        b = int(l.func_inp("Enter breadth of cuboid: "))
        h = int(l.func_inp("Enter height of cuboid: "))
        l.sa_cuboid(l, b, h)
    elif func == "50" or func == "volume of cuboid":
        l.func_head("Find volume of cuboid", "3D GEOMETRY")
        l = int(l.func_inp("Enter length of cuboid: "))
        b = int(l.func_inp("Enter breadth of cuboid: "))
        h = int(l.func_inp("Enter height of cuboid: "))
        l.v_cuboid(l, b, h)
    elif func == "51" or func == "surface area of cone":
        l.func_head("Find surface area of cone", "3D GEOMETRY")
        r = int(l.func_inp("Enter radius of cone: "))
        h = int(l.func_inp("Enter height of cone: "))
        l.sa_cone(r, h)
    elif func == "52" or func == "volume of cone":
        l.func_head("Find volume of cone", "3D GEOMETRY")
        r = int(l.func_inp("Enter radius of cone: "))
        h = int(l.func_inp("Enter height of cone: "))
        l.v_cone(r, h)
    elif func == "53" or func == "surface area of cylinder":
        l.func_head("Find surface area of cylinder", "3D GEOMETRY")
        r = int(l.func_inp("Enter radius of cylinder: "))
        h = int(l.func_inp("Enter height of cylinder: "))
        l.sa_cyl(r, h)
    elif func == "54" or func == "volume of cylinder":
        l.func_head("Find volume of cylinder", "3D GEOMETRY")
        r = int(l.func_inp("Enter radius of cylinder: "))
        h = int(l.func_inp("Enter height of cylinder: "))
        l.v_cyl(r, h)
    elif func == "55" or func == "surface area of sphere":
        l.func_head("Find surface area of sphere", "3D GEOMETRY")
        r = int(l.func_inp("Enter radius of sphere: "))
        l.sa_sph(r)
    elif func == "56" or func == "volume of sphere":
        l.func_head("Find volume of sphere", "3D GEOMETRY")
        r = int(l.func_inp("Enter radius of sphere: "))
        l.v_sph(r)
    elif func == "57" or func == "surface area of hemisphere":
        l.func_head("Find surface area of hemisphere", "3D GEOMETRY")
        r = int(l.func_inp("Enter radius of hemisphere: "))
        l.sa_hms(r)
    elif func == "58" or func == "volume of hemisphere":
        l.func_head("Find volume of hemisphere", "3D GEOMETRY")
        r = int(l.func_inp("Enter radius of hemisphere: "))
        l.v_hms(r)
    elif func == "59" or func == "check palindrome":
        l.func_head("Check if given number/string is palindrome", "NUMBER PROPERTIES & SEQUENCES")
        p = l.func_inp("Enter number/string to check for palindrome: ")
        l.palin(p)
    elif func == "help":
        l.show_help()
    elif func == "stop":
        console.print()

        end = "Thank You for using Math Essentials Hoping to see you come back soon!!"

        for char in end:
            if keyboard.is_pressed("esc"):
                console.print()
                console.print(
                    Panel(
                        "[bold bright_yellow]⚠ SHUTDOWN CANCELLED![/bold bright_yellow]\n\n"
                        "[white]Your session is safe. Returning to Math Essentials...[/white]",
                        border_style="bright_yellow",
                        box=box.DOUBLE,
                        padding=(1, 3),
                        expand=False
                    ),
                    justify="center"
                )
                break

            console.print(char, end="", highlight=False, markup=False, soft_wrap=True)
            time.sleep(0.025)

        else:
            console.print("\n")

            console.print(
                Panel(
                    "[bold bright_cyan]Press ESC to cancel shutdown[/bold bright_cyan]",
                    border_style="bright_magenta",
                    box=box.ROUNDED,
                    expand=False
                ),
                justify="center"
            )

            console.print()
            cancelled = False

            for i in range(3, 0, -1):
                console.print(
                    Panel(
                        f"[bold bright_red]CLOSING APPLICATION IN {i}..[/bold bright_red]",
                        border_style="bright_magenta",
                        box=box.DOUBLE,
                        expand=False
                    ),
                    justify="center"
                )

                for _ in range(10):
                    if keyboard.is_pressed("esc"):
                        cancelled = True
                        break
                    time.sleep(0.12)

                if cancelled:
                    break

            if cancelled:
                console.print()
                console.print(
                    Panel(
                        "[bold bright_yellow]⚠ SHURDOWN CANCELLED![/bold bright_yellow]\n\n"
                        "[white]You're back in Math Essentials![/white]\n"
                        "[bright_cyan]Ready for your next calculation.[/bright_cyan]",
                        border_style="bright_yellow",
                        box=box.DOUBLE,
                        padding=(1, 3),
                        expand=False
                    ),
                    justify="center"
                )
                console.print()

            else:
                console.print()
                console.print(
                    Panel(
                        "[bold bright_cyan]THANK YOU FOR USING[bold bright_cyan]\n"
                        "[bold bright_magenta]MATH ESSENTIALS[/bold bright_magenta]\n\n"
                        "[white]Hoping to see you come back soon![/white]\n"
                        "[dim]Until next time...[/dim]",
                        border_style="bright_magenta",
                        box=box.DOUBLE,
                        padding=(1, 4),
                        expand=False
                    ),
                    justify="center"
                )
                console.print()
                exit()
    else:
        print("Invalid Choice. Retry")
        print()
        continue
    print()
