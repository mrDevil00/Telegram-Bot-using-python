from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes,filters

TOKEN: Final = '6985163788:AAEmAOaS_DDbrZeqTkcFt1DGznRwaciLNko'

BOT_USERNAME: Final = '@Joy_python_bot'

#setup some predefined commands with its output
#start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! Thanks for chatting with me! I am a Python_Bot!""")

#help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! This is help command! How can i help!
If you are facing any problem or having problem related to Bot then you can mail on xyz987@gmail.com.""")

#question command
async def questions_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! This is question command!
    Here you can find the sets of basic questions of python programming and their solutions.
    
    For generating output type like "QA" or "QO".
    
    Q1. Write a program to take integer input from user and check whether it is even or odd and display it.
    Q2. Write a program to find the given number is positive or negative.
    Q3. Write a program to find the sum of two numbers.
    Q4. Write a program to find if the given number is prime or not.
    Q5. Write a program to check if the given number is palindrome or not.
    Q6. Write a program to check if the given number is Armstrong or not.
    Q7. Write a program to check if the given strings are anagram or not.
    Q8. Write a program to find a maximum of two numbers.
    Q9. Write a program to find a minimum of two numbers.
    Q.10. Write a program to find a maximum of three numbers.
    Q.11. Write a program to find a minimum of three numbers.
    Q.12. Write a program to find a factorial of a number.
    Q.13. Write a program to find a fibonacci of a number.
    Q.14. Write a program to find GCD of two numbers.
    Q.15. Write a program to print the following pattern.
                *
                * * 
                * * *
                * * * *
                * * * * *
    Q.16. Write a program to print the following pattern.
                    *
                   * *
                 *  *  *
                *  *  *  *
               *  *  *  *  *
    """)

#custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""This is a custom command!
    Here are some predefined commands that can be answered by Python_Bot. You can access it by writing 'py' or 'python'. 
    1.python (py)
    2.Comment (cmt)
    3.Variables (var)
    4.Keywords (kw)
    5.Operator (op)
    6.Arithematic Operator (aro)
    7.Assignment Operator (aso)
    8.Comparison Operator (co)
    9.Logical Operator (lo)
    10.Identity Operator (io)
    11.Membership Operator (mo)
    12.Bitwise Operator (bo)
    13.Data types (dtyp)
    14.list (li)
    15.Tuple (tu)
    16.Set 
    17.Dictonary (dict)
    18.String (str)
    19.Functions (func)
    20.libraries (lib)
    21.Exception handling (eh)
    22.File handling (fh)""")



# text responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    

    if "hello" in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I am good!'

    if 'i love python' in processed:
        return 'I love too!'
    
    if 'i want to learn' in processed:
        return 'Great! lets start from basics.'
    
    if 'what is your name' in processed:
        return 'I am Joy! A python bot.'
    
    if 'who made you' in processed:
        return 'I am created as a project which includes many people.'
    
    if 'thank you' in processed:
        return 'Welcome! Feel free to ask anything.'
    
    if 'hi' in processed:
        return 'Hey there!'
    
    if 'i want to play games' in processed:
        return 'Sorry! We dont have games right now.'
    
    if 'bye' in processed:
        return 'Bye! Have a good day.'
    
    if 'python' in processed:
        return ' Python is a high-level programming language known for its simplicity and readability. Its versatile, used in web development, data analysis, artificial intelligence, and more.'  
    
    if 'comment' in processed:
        return """for multiple line (''' ''') and '#' for single line comment."""
        
    if 'data types' in processed:
        return "Python has several data types including int for integers, float for floating-point numbers, str for strings, bool for Boolean values, list, tuple, and dict for data structures, among others."
    
    if 'keywords' in processed:
        return """ Here are some keywords that are used in python language.
        False  , await	, else	, import , pass
        None , break , except , in , raise
        True , class , finally , is , return
        and , continue , for , lambda , try
        as , def , from , nonlocal , while
        assert , del , global , not , with
        async , elif , if , or , yield
        for more result you can click on this list https://www.w3schools.com/python/python_ref_keywords.asp"""    
                    
    if 'operator' in processed:
        return """Here are some operators in python language.
        1.Arithmetic Operators
        2.Comparison Operators
        3.Assignment Operators
        4.Logical Operators
        5.Bitwise Operators
        6.Membership Operators
        7.Identity Operators
        if you want for more information then you can visit https://www.w3schools.com/python/python_operators.asp"""        
                    
    if 'arithematic operator' in processed:
        return """Arithmetic operators used between two operands for a particular operation. There are many arithmetic operators. 
        It includes the exponent (**) operator as well as the + (addition), - (subtraction), * (multiplication), / (divide), % (reminder), and // (floor division) operators.
        Example of Assignment Operator:
        a = 32    # Initialize the value of a  
        b = 6      # Initialize the value of b  
        print('Addition of two numbers:',a+b)  # Addition of two numbers: 38
        print('Subtraction of two numbers:',a-b)  # Subtraction of two numbers: 26
        print('Multiplication of two numbers:',a*b)  # Multiplication of two numbers: 192
        print('Division of two numbers:',a/b)  # Division of two numbers: 5.333333333333333
        print('Reminder of two numbers:',a%b)  # Reminder of two numbers: 2 
        print('Exponent of two numbers:',a**b)  # Exponent of two numbers: 1073741824
        print('Floor division of two numbers:',a//b) # Floor division of two numbers: 5
        for more information visit https://www.w3schools.com/python/python_operators.asp"""  
        
    if 'assignment operator' in processed:
        return """Using the assignment operators, the right expression's value is assigned to the left operand. 
        There are some examples of assignment operators like =, +=, -=, *=, %=, **=, //=. In the below table, we explain the works of the operators.
        Example of Assignment Operator:
        a = 32         # Initialize the value of a  
        b = 6          # Initialize the value of b  
        print('a=b:', a==b)  
        print('a+=b:', a+b)  
        print('a-=b:', a-b)  
        print('a*=b:', a*b)  
        print('a%=b:', a%b)  
        print('a**=b:', a**b)  
        print('a//=b:', a//b) 
        for more information https://www.w3schools.com/python/python_operators.asp"""   
                
    if 'comparision operator' in processed:
        return """Comparison operators mainly use for comparison purposes. Comparison operators compare the values of the two operands and return a true or false Boolean value in accordance. 
        The example of comparison operators are ==, !=, <=, >=, >, <. In the below table, we explain the works of the operators.
        Example of Comparision operator:
        a = 32      # Initialize the value of a  
        b = 6       # Initialize the value of b  
        print('Two numbers are equal or not:',a==b)  
        print('Two numbers are not equal or not:',a!=b)  
        print('a is less than or equal to b:',a<=b)  
        print('a is greater than or equal to b:',a>=b)  
        print('a is greater b:',a>b)  
        print('a is less than b:',a<b) 
        for more information https://www.w3schools.com/python/python_operators.asp"""  
                  
    if 'bitwise operator' in processed:
        return """The two operands' values are processed bit by bit by the bitwise operators. 
        The examples of Bitwise operators are bitwise OR (|), bitwise AND (&), bitwise XOR (^), negation (~), Left shift (<<), and Right shift (>>). Consider the case below.
        Example of Logical Operator:
        a = 5          # initialize the value of a  
        b = 6          # initialize the value of b  
        print('a&b:', a&b)  
        print('a|b:', a|b)  
        print('a^b:', a^b)  
        print('~a:', ~a)  
        print('a<<b:', a<<b)  
        print('a>>b:', a>>b)  
        for more information https://www.w3schools.com/python/python_operators.asp"""
                  
    if 'logical operator' in processed:
        return """The assessment of expressions to make decisions typically uses logical operators. The examples of logical operators are and, or, and not. 
        In the case of logical AND, if the first one is 0, it does not depend upon the second one. In the case of logical OR, if the first one is 1, it does not depend on the second one. 
        Python supports the following logical operators. In the below table, we explain the works of the logical operators.
        Example of logical operator:
        a = 5          # initialize the value of a          
        print(Is this statement true?:',a > 3 and a < 5)  
        print('Any one statement is true?:',a > 3 or a < 5)  
        print('Each statement is true then return False and vice-versa:',(not(a > 3 and a < 5)))  
        for more information https://www.w3schools.com/python/python_operators.asp"""
                  
    if 'identity operator' in processed:
        return """Here are identity operator,
        is :-If the references on both sides point to the same object, it is determined to be true.
        is not :- If the references on both sides do not point at the same object, it is determined to be true.
        Example of Identity Operator:
        a = ["Rose", "Lotus"]  
        b = ["Rose", "Lotus"]  
        c = a  
        print(a is c)  
        print(a is not c)  
        print(a is b)  
        print(a is not b)  
        print(a == b)  
        print(a != b)  
        for more infromation https://www.w3schools.com/python/python_operators.asp"""
                  
    if 'membership operator' in processed:
        return """The membership of a value inside a Python data structure can be verified using Python membership operators. 
        The result is true if the value is in the data structure; otherwise, it returns false.
        Operator Description
          in	:-If the first operand cannot be found in the second operand, it is evaluated to be true (list, tuple, or dictionary).
          not in :-If the first operand is not present in the second operand, the evaluation is true (list, tuple, or dictionary).
        Examples of Membership operators in Python. The code is given below -
        x = ["Rose", "Lotus"]  
        print(' Is value Present?', "Rose" in x)  
        print(' Is value not Present?', "Riya" not in x)  
        for more information https://www.w3schools.com/python/python_operators.asp"""
                    
    if 'variables' in processed:
        return """You can declare a variable in Python by assigning a value to a name.
        Like x=5,abc1=10, etc. But never start a variable name with digit.
        We can start a variable name with _ , a1 , a not like 12a. 
        for more information https://www.w3schools.com/python/python_variables.asp"""
        
    if 'functions' in processed:
        return """By using 'def' keyword we can create function.
        There are two types of functions in python 
        1. Built in function
        2. User define function.
        Built in function:- The functions which are coming along with Python software automatically, are called built in functions or predefined functionsExample: id() , type() , input() , eval() , etc..
        User define function:- The functions which are developed by programmer explicitly according to business requirements, are called user defined functions.
        Syntax to create user defined functions:
        def function_name(parameters):
        for more information https://www.w3schools.com/python/python_functions.asp"""
        
    if 'library' in processed:
        return """A Python library is a collection of functions and 
        methods that allow you to perform many actions without writing your own code.
        Some of the python libraries are Pandas, Numpy, turtle, time and many more."""
    
    if 'exception handling' in processed:
        return """Exceptions in Python can be handled using try, except, and optionally 'finally' blocks. For example
        try:
        # code that might raise an exception
        result = 10 / 0
        except ZeroDivisionError:
        print("Cannot divide by zero!")"""
        
    if 'file handling' in processed:
        return """ 
        You can open a file using the open() function, read or write content, and 
        close the file using close(). For instance:
        file = open('example.txt', 'r')  # 'r' for reading, 'w' for writing
        content = file.read()  # read file content
        file.close()  # close the file"""
                  
    if 'py' in processed:
        return """Python is a high-level programming language known for its simplicity and readability. Its versatile, used in web development, data analysis, artificial intelligence, and more.""" 
    
    if 'cmt' in processed:
        return """Comment in python can be used i.e for multiple line (''' ''') and '#' for single line comment."""
        
    if 'dtyp' in processed:
        return """Python has several data types including int for integers, float for floating-point numbers, str for strings, 
        bool for Boolean values, list, tuple, and dict for data structures, among others."""
    
    if 'kw' in processed:
        return """ Here are some keywords that are used in python language.
        False  , await	, else	, import , pass
        None , break , except , in , raise
        True , class , finally , is , return
        and , continue , for , lambda , try
        as , def , from , nonlocal , while
        assert , del , global , not , with
        async , elif , if , or , yield
        for more result you can click on this list https://www.w3schools.com/python/python_ref_keywords.asp"""    
                    
    if 'op' in processed:
        return """Here are some operators in python language.
                    1.Arithmetic Operators
                    2.Comparison Operators
                    3.Assignment Operators
                    4.Logical Operators
                    5.Bitwise Operators
                    6.Membership Operators
                    7.Identity Operators
                    if you want for more information then you can visit https://www.w3schools.com/python/python_operators.asp"""        
                    
    if 'aro' in processed:
        return """Arithmetic operators used between two operands for a particular operation. There are many arithmetic operators. 
        It includes the exponent (**) operator as well as the + (addition), - (subtraction), * (multiplication), / (divide), % (reminder), and // (floor division) operators.
        Example of Assignment Operator:
        a = 32    # Initialize the value of a  
        b = 6      # Initialize the value of b  
        print('Addition of two numbers:',a+b)  # Addition of two numbers: 38
        print('Subtraction of two numbers:',a-b)  # Subtraction of two numbers: 26
        print('Multiplication of two numbers:',a*b)  # Multiplication of two numbers: 192
        print('Division of two numbers:',a/b)  # Division of two numbers: 5.333333333333333
        print('Reminder of two numbers:',a%b)  # Reminder of two numbers: 2 
        print('Exponent of two numbers:',a**b)  # Exponent of two numbers: 1073741824
        print('Floor division of two numbers:',a//b) # Floor division of two numbers: 5
        for more information visit https://www.w3schools.com/python/python_operators.asp""" 
        
    if 'aso' in processed:
        return """Using the assignment operators, the right expression's value is assigned to the left operand. 
        There are some examples of assignment operators like =, +=, -=, *=, %=, **=, //=. In the below table, we explain the works of the operators.
        Example of Assignment Operator:
        a = 32         # Initialize the value of a  
        b = 6          # Initialize the value of b  
        print('a=b:', a==b)  
        print('a+=b:', a+b)  
        print('a-=b:', a-b)  
        print('a*=b:', a*b)  
        print('a%=b:', a%b)  
        print('a**=b:', a**b)  
        print('a//=b:', a//b) 
        for more information https://www.w3schools.com/python/python_operators.asp"""   
                
    if 'co' in processed:
        return """Comparison operators mainly use for comparison purposes. Comparison operators compare the values of the two operands and return a true or false Boolean value in accordance. 
        The example of comparison operators are ==, !=, <=, >=, >, <. In the below table, we explain the works of the operators.
        Example of Comparision operator:
        a = 32      # Initialize the value of a  
        b = 6       # Initialize the value of b  
        print('Two numbers are equal or not:',a==b)  
        print('Two numbers are not equal or not:',a!=b)  
        print('a is less than or equal to b:',a<=b)  
        print('a is greater than or equal to b:',a>=b)  
        print('a is greater b:',a>b)  
        print('a is less than b:',a<b) 
        for more information https://www.w3schools.com/python/python_operators.asp"""  
                  
    if 'bo' in processed:
        return """The two operands' values are processed bit by bit by the bitwise operators. 
                  The examples of Bitwise operators are bitwise OR (|), bitwise AND (&), bitwise XOR (^), negation (~), Left shift (<<), and Right shift (>>). Consider the case below.
                  Example of Logical Operator:
                  a = 5          # initialize the value of a  
                  b = 6          # initialize the value of b  
                  print('a&b:', a&b)  
                  print('a|b:', a|b)  
                  print('a^b:', a^b)  
                  print('~a:', ~a)  
                  print('a<<b:', a<<b)  
                  print('a>>b:', a>>b)  
                  for more information https://www.w3schools.com/python/python_operators.asp"""
                  
    if 'lo' in processed:
        return """The assessment of expressions to make decisions typically uses logical operators. The examples of logical operators are and, or, and not. 
                  In the case of logical AND, if the first one is 0, it does not depend upon the second one. In the case of logical OR, if the first one is 1, it does not depend on the second one. 
                  Python supports the following logical operators. In the below table, we explain the works of the logical operators.
                  Example of logical operator:
                  a = 5          # initialize the value of a          
                  print(Is this statement true?:',a > 3 and a < 5)  
                  print('Any one statement is true?:',a > 3 or a < 5)  
                  print('Each statement is true then return False and vice-versa:',(not(a > 3 and a < 5)))  
                  for more information https://www.w3schools.com/python/python_operators.asp"""
                  
    if 'io' in processed:
        return """Here are identity operator,
                  is :-If the references on both sides point to the same object, it is determined to be true.
                  is not :- If the references on both sides do not point at the same object, it is determined to be true.
                  Example of Identity Operator:
                  a = ["Rose", "Lotus"]  
                  b = ["Rose", "Lotus"]  
                  c = a  
                  print(a is c)  
                  print(a is not c)  
                  print(a is b)  
                  print(a is not b)  
                  print(a == b)  
                  print(a != b)  
                  for more infromation https://www.w3schools.com/python/python_operators.asp"""
                  
    if 'mo' in processed:
        return """The membership of a value inside a Python data structure can be verified using Python membership operators. 
                  The result is true if the value is in the data structure; otherwise, it returns false.
                  Operator Description
                    in	:-If the first operand cannot be found in the second operand, it is evaluated to be true (list, tuple, or dictionary).
                    not in :-If the first operand is not present in the second operand, the evaluation is true (list, tuple, or dictionary).
                  Examples of Membership operators in Python. The code is given below -
                  x = ["Rose", "Lotus"]  
                  print(' Is value Present?', "Rose" in x)  
                  print(' Is value not Present?', "Riya" not in x)  
                  for more information https://www.w3schools.com/python/python_operators.asp"""
                    
    if 'var' in processed:
        return """You can declare a variable in Python by assigning a value to a name.
                  Like x=5,abc1=10, etc. But never start a variable name with digit.
                  We can start a variable name with _ , a1 , a not like 12a. 
                  for more information https://www.w3schools.com/python/python_variables.asp"""
        
    if 'func' in processed:
        return """By using 'def' keyword we can create function.
                  There are two types of functions in python 1. Built in function and 2. User define function.
                  Built in function:- The functions which are coming along with Python software automatically, are called built in functions or predefined functionsExample: id() , type() , input() , eval() , etc..
                  User define function:- The functions which are developed by programmer explicitly according to business requirements, are called user defined functions.
                  Syntax to create user defined functions:
                  Like this- def function_name(parameters):
                  for more information https://www.w3schools.com/python/python_functions.asp"""
        
    if 'lib' in processed:
        return """A Python library is a collection of functions and methods that allow you to perform many actions without writing your own code.
                  Some of the python libraries are Pandas, Numpy, turtle, time and many more."""
    
    if 'eh' in processed:
        return """Exceptions in Python can be handled using try, except, and optionally 'finally' blocks. For example
                  try:
                  # code that might raise an exception
                  result = 10 / 0
                  except ZeroDivisionError:
                  print("Cannot divide by zero!")"""
        
    if 'fh' in processed:
        return """ You can open a file using the open() function, read or write content, and 
                close the file using close(). For instance:
            file = open('example.txt', 'r')  # 'r' for reading, 'w' for writing
              content = file.read()  # read file content
              file.close()  # close the file
              """
        
    if 'q1' in processed:
        return """
        num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))"""
            
    if "q2" in processed:
        return """
        num = float(input("Enter a number: "))
        # Input: 1.2
        if num > 0:
            print("Positive number")
        elif num == 0:
            print("Zero")
        else:
            print("Negative number")

        #output: Positive number"""
    
    if 'q3' in processed:
        return """
        num1 = int(input("Enter Number1: "))
        # Input1 : 21
        num2 = int(input("Enter Number2: "))
        #  Input2 : 11
        print("sum of given numbers is:", num1 + num2)
        #  Output2 : 32 """
        
    if 'q4' in processed:
        return """"
    num = int(input("enter a number: "))
    # input: 23
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
    # 23 is a prime number"""
    
    if 'q5' in processed:
        return """
    num = int(input("Enter a number: "))
    # Input: 12321
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
        print('Palindrome')
    else:
        print("Not Palindrome")
    # Output: Palindrome"""
    
    if 'q6' in processed:
        return """
    num = int(input("Enter a number: "))
    # Input: 407
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")
    # Output: 407 is an Armstrong number"""
    
    if 'q7' in processed:
        return """
        def check(s1, s2):
    
        if(sorted(s1)== sorted(s2)):
            print("The strings are anagrams.")
        else:
            print("The strings aren't anagrams.")        
        
    s1 = input("Enter string1: ")
    # input1: "listen"
    s2 = input("Enter string2: ")
    # input2: "silent"
    check(s1, s2)
    # Output: the strings are anagrams."""
    
    if 'q8' in processed:
        return """
        def maximum(a, b):
    
            if a >= b:
                return a
            else:
                return b
    
        a = int(input("Enter a number: "))
        # input1: 2
        b = int(input("Enter a number: "))
        # input2: 4
        print(maximum(a, b))
        # output: 4"""
    
    if 'q9' in processed:
        return """
    def minimum(a, b):
    
        if a <= b:
            return a
        else:
            return b
    
    a = int(input("Enter a number: "))
    # input1: 2
    b = int(input("Enter a number: "))
    # input2: 4
    print(minimum(a, b))
    # output: 2"""
    
    if 'q.10' in processed:
        return """
    def maximum(a, b, c):

        if (a >= b) and (a >= c):
            largest = a

        elif (b >= a) and (b >= c):
            largest = b
        else:
            largest = c
        
        return largest


    a = int(input("Enter a number: "))
    # Input1: 10
    b = int(input("Enter a number: "))
    # Input2: 14
    c = int(input("Enter a number: "))
    # Input3: 12
    print(maximum(a, b, c))
    # Output: 14"""
    
    if "q.11" in processed:
        return """"
        a = int(input('Enter first number  : '))
        # 12
        b = int(input('Enter second number : '))
        # 14
        c = int(input('Enter third number  : '))
        # 11
        smallest = 0
        if a < b and a < c :
            smallest = a
        if b < a and b < c :
            smallest = b
        if c < a and c < b :
            smallest = c
        print(smallest, "is the smallest of three numbers.")
        # 11 is the smallest of three numbers."""
        
    if 'q.12' in processed:
        return """
        num = int(input("Enter a number: "))
        # 7
        factorial = 1
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,num + 1):
                factorial = factorial*i
                print("The factorial of",num,"is",factorial)
        # 5040"""
   
    if 'q.13' in processed:
        return """
        nterms = int(input("How many terms? "))
# 7
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8"""
    if 'q.14' in processed:
        return """
        def gcd(a, b):
    
    if (a == 0):
        return b
    if (b == 0):
        return a

    if (a == b):
        return a

    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

a = 98
b = 56
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')"""
    
    if 'q.15' in processed:
        return """
        def myfunc(n):
        for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")

    n = 5
    myfunc(n)"""
    
    if 'q.16' in processed:
        return """
        def myfunc(n):
        k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
    n = 5
    myfunc(n)"""
    
    return "I don't understand what you wrote...please use custom or question command and ask questions according to it. Thanks!!.."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:',  response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print("starting bot...")
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('questions', questions_command))
    

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #errors
    app.add_error_handler(error)


    #polls the bot
    print("polling...")
    app.run_polling(poll_interval=3)