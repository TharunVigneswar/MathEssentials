import libs as l
import time
import keyboard

tx1 = """-------------------- Welcome To Math Essentials --------------------
You can solve fundamental and some advanced mathematic problems here"""

for char in tx1:
    print(char, end="", flush=True)
    time.sleep(0.025)


print("")



while True:
    prompt = "Enter which function you want to use: "
    print()
    for char in prompt:
        print(char, end="", flush=True)
        time.sleep(0.025)

    func = input().lower()
    print()
    if func == "1" or func == "add":
        print("Addition")
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        l.add(a, b)
    elif func == "2" or func == "subtract":
        print("Subtraction")
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        l.subtract(a, b)
    elif func == "3" or func == "product":
        print("Multiplication")
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        l.multiply(a, b)
    elif func == "4" or func == "divide":
        print("Division")
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        l.divide(a, b)
    elif func == "5" or func == "power":
        print("Exponent")
        a = int(input("Enter base number: "))
        b = int(input("Enter power: "))
        l.power(a, b)        
    elif func == "6" or func == "sqrt":
        print("Square Root")
        a = int(input("Enter Number: "))
        l.square_root(a)
    elif func == "7" or func == "square":
        print("Square")
        a = int(input("Enter Number: "))
        l.square(a)
    elif func == "8" or func == "cube":
        print("Cube")
        a = int(input("Enter Number: "))
        l.cube(a)
    elif func == "9" or func == "cube root":
        print("Cube Root")
        a = int(input("Enter Number: "))
        l.cube_root(a)
    elif func == "10" or func == "nth root":
        print("Nth Root")
        a = int(input("Enter base number: "))
        b = int(input("Enter root: "))
        l.nth_root(a, b)
    elif func == "11" or func == "log":
        print("Logarithm")
        a = int(input("Enter number to find log: "))
        b = int(input("Enter base number: "))
        l.log(a, b)
    elif func == "12" or func == "square check":
        print("Perfect Square Check")
        a = int(input("Enter Number: "))
        l.perfect_square(a)
    elif func == "13" or func == "cube check":
        print("Perfect Cube Check")
        a = int(input("Enter Number: "))
        l.perfect_cube(a)
    elif func == "14" or func == "factorial":
        print("Factorial")
        a = int(input("Enter number: "))
        l.factorial(a)
    elif func == "15" or func == "floor division":
        print("Floor Division")
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        l.floor_div(a, b)
    elif func == "16" or func == "mod":
        print("Modulus")
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        l.modulus(a, b)
    elif func == "17" or func == "abs" or func == "absolute":
        print("Absolute")
        a = int(input("Enter number: "))
        l.absolute(a)
    elif func == "18" or func == "additive inverse":
        print("Additive Inverse")
        a = int(input("Enter number: "))
        l.add_inv(a)
    elif func == "19" or func == "multiplicative inverse":
        print("Multiplicative Inverse")
        a = int(input("Enter number: "))
        l.mult_inv(a)
    elif func == "20" or func == "min max":
        print("Min Max")
        a = int(input("Enter total number of numbers you want to compare: "))
        l.min_max(a)
    elif func == "21" or func == "avg":
        print("Average")
        a = int(input("Enter total number of numbers you want to find average of: "))
        l.avg(a)
    elif func == "22" or func == "gcd":
        print("Greatest Common Divisor")
        a = int(input("Enter the total number of numbers you want to find GCD of: "))
        l.gcd(a)
    elif func == "23" or func == "lcm":
        print("Least Common Multiple")
        a = int(input("Enter the total number of numbers you want to find LCM of: "))
        l.lcm(a)
    elif func == "24" or func == "check prime":
        print("Check if given number is prime")
        a = int(input("Enter number: "))
        l.prime_check(a)
    elif func == "25" or func == "list primes":
        print("List Prime numbers")
        a = int(input("Till what number to print prime numbers: "))
        l.prime_list(a)
    elif func == "26" or func == "fibonacci":
        print("Fibonacci Sequence")
        a = int(input("Enter number: "))
        l.fibonacci(a)
    elif func == "27" or func == "div check":
        print("Divisibility Check")
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        l.div_check(a, b)
    elif func == "28" or func == "sin":
        print("Sine value of an angle")
        a = int(input("Enter degree value: "))
        l.sin(a)
    elif func == "29" or func == "cos":
        print("Cosine value of an angle")
        a = int(input("Enter degree value: "))
        l.cos(a)
    elif func == "30" or func == "tan":
        print("Tangent value of an angle")
        a = int(input("Enter degree value: "))
        l.tan(a)
    elif func == "31" or func == "cosec":
        print("Cosecant value of an angle")
        a = int(input("Enter degree value: "))
        l.cosec(a)
    elif func == "32" or func == "sec":
        print("Secant value of an angle")
        a = int(input("Enter degree value: "))
        l.sec(a)
    elif func == "33" or func == "cot":
        print("Cotangent value of an angle")
        a = int(input("Enter degree value: "))
        l.cot(a)
    elif func == "34" or func == "solve linear equation":
        print("Solve a linear equation")
        a = int(input("Enter coefficient of x: "))
        b = int(input("Enter constant value: "))
        l.solve_lin(a, b)
    elif func == "35" or func == "solve quadratic equation":
        print("Solve a quadratic equation")
        a = int(input("Enter coefficient of x²: "))
        b = int(input("Enter coefficient of x: "))
        c = int(input("Enter constant value: "))
        l.solve_quad(a, b, c)
    elif func == "36" or func == "form quadratic equation":
        print("Form Quadratic Equation from Roots")
        a = int(input("Enter first root: "))
        b = int(input("Enter second root: "))
        l.form_quad(a, b)
    elif func == "37" or func == "floor":
        print("Floor Value")
        a = int(input("Enter number to find floor of: "))
        l.floor(a)
    elif func == "38" or func == "check armstrong":
        print("Check if given number is an armstrong number")
        a = int(input("Enter number: "))
        l.chck_armstrong(a)
    elif func == "39" or func == "number guesser":
        print("Number Guesser Game")
        fr = int(input("Enter start number: "))
        to = int(input("Enter end number: "))
        ges = int(input("Enter number of guesses: "))
        l.rand_game(fr, to, ges)
    elif func == "40" or func == "pi":
        l.pi()
    elif func == "41" or func == "square perimeter":
        print("Perimeter of Square")
        s = int(input("Enter square side length: "))
        l.p_sq(s)
    elif func == "42" or func == "square area":
        print("Area of Square")
        s = int(input("Enter square side length: "))
        l.a_sq(s)
    elif func == "43" or func == "rectangle perimeter":
        print("Perimeter of Rectangle")
        l = int(input("Enter rectangle length: "))
        b = int(input("Enter rectangle breadth: "))
        l.p_rect(l, b)
    elif func == "44" or func == "rectangle area":
        print("Area of Rectangle")
        l = int(input("Enter rectangle length: "))
        b = int(input("Enter rectangle breadth: "))
        l.a_rect(l, b)
    elif func == "45" or func == "diagonal count":
        print("Find number of diagonals of a polygon")
        n = int(input("Enter number of sides of polygon: "))
        l.diag(n)
    elif func == "46" or func == "perimeter of polygon":
        print("Find perimeter of polygon")
        n = int(input("Enter number of sides: "))
        s = int(input("Enter length of each side: "))
        l.p_poly(s, n)
    elif func == "47" or func == "surface area of cube":
        print("Find surface area of cube")
        s = int(input("Enter length of each side of cube: "))
        l.sa_cube(s)
    elif func == "48" or func == "volume of cube":
        print("Find volume of cube")
        s = int(input("Enter length of each side of cube: "))
        l.v_cube(s)
    elif func == "49" or func == "surface area of cuboid":
        print("Find surface area of cuboid")
        l = int(input("Enter length of cuboid: "))
        b = int(input("Enter breadth of cuboid: "))
        h = int(input("Enter height of cuboid: "))
        l.sa_cuboid(l, b, h)
    elif func == "50" or func == "volume of cuboid":
        print("Find volume of cuboid")
        l = int(input("Enter length of cuboid: "))
        b = int(input("Enter breadth of cuboid: "))
        h = int(input("Enter height of cuboid: "))
        l.v_cuboid(l, b, h)
    elif func == "51" or func == "surface area of cone":
        print("Find surface area of cone")
        r = int(input("Enter radius of cone: "))
        h = int(input("Enter height of cone: "))
        l.sa_cone(r, h)
    elif func == "52" or func == "volume of cone":
        print("Find volume of cone")
        r = int(input("Enter radius of cone: "))
        h = int(input("Enter height of cone: "))
        l.v_cone(r, h)
    elif func == "53" or func == "surface area of cylinder":
        print("Find surface area of cylinder")
        r = int(input("Enter radius of cylinder: "))
        h = int(input("Enter height of cylinder: "))
        l.sa_cyl(r, h)
    elif func == "54" or func == "volume of cylinder":
        print("Find volume of cylinder")
        r = int(input("Enter radius of cylinder: "))
        h = int(input("Enter height of cylinder: "))
        l.v_cyl(r, h)
    elif func == "55" or func == "surface area of sphere":
        print("Find surface area of sphere")
        r = int(input("Enter radius of sphere: "))
        l.sa_sph(r)
    elif func == "56" or func == "volume of sphere":
        print("Find volume of sphere")
        r = int(input("Enter radius of sphere: "))
        l.v_sph(r)
    elif func == "57" or func == "surface area of hemisphere":
        print("Find surface area of hemisphere")
        r = int(input("Enter radius of hemisphere: "))
        l.sa_hms(r)
    elif func == "58" or func == "volume of hemisphere":
        print("Find volume of hemisphere")
        r = int(input("Enter radius of hemisphere: "))
        l.v_hms(r)
    elif func == "59" or func == "check palindrome":
        print("Check if given number/string is palindrome")
        p = input("Enter number/string to check for palindrome: ")
        l.palin(p)
    elif func == "help":
        l.show_help()
    elif func == "stop":
        end = "Thank You for using Math Essentials!! Hoping to see you come back soon!!"
        
        for char in end:
            if keyboard.is_pressed("esc"):
                print("\nShutdown cancelled!")
                break
    
            print(char, end="", flush=True)
            time.sleep(0.025)
    
        else:
            print("\n")
    
            cancelled = False
            quit = "Press Esc to stop quitting." 
            for i in quit:
                print(i, end="", flush=True)
                time.sleep(0.02)

            print("\n")

            for i in range(3, 0, -1):
                print(f"Closing application in {i}")
    
                for _ in range(10):
                    if keyboard.is_pressed("esc"):
                        cancelled = True
                        break
                    time.sleep(0.12)
    
                if cancelled:
                    break
    
            if cancelled:
                tx = "Shutdown cancelled! Returning to Math Essentials..."
                for i in tx:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
            else:
                print("\nGoodbye!")
                exit()
    else:
        print("Invalid Choice. Retry")
        print("")
        continue
    print("")
