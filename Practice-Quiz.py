import random as rd
def questions():
    bank = [
    [
        """
    What will be printed from the following code\n
    s = "python rocks"\n
    print(s[3])\n

    """, """
    A. t\n
    B. h\n
    C. c\n
    D. Error, you cannot use the [ ] operator with a string.
    """, 'B'
    ],  
    [
    """
    What is printed by the following statements?\n

    s = "python rocks"\n
    print(s[2] + s[-5])
        ""","""
        A. tr\n
        B. ps\n
        C. nn\n
        D. Error, you cannot use the [ ] operator with the + operator.\n
        """,'A'   
    ],
    [
        """
    What is a variable's scope?
        ""","""
    A. Its value\n
    B. The range of statements in the code where a variable can be accessed.\n
    C. Its name\n    
        """, 'B'
    ],
    [
        """
        What is a local variable?
        ""","""
        A. A temporary variable that is only used inside a function\n
        B. The same as a parameter\n
        C. Another name for any variable\n
        """, 'A'
    ],[
        """
        Can you use the same name for a local variable as a global variable?
        """,
        """        
        A. Yes, and there is no reason not to.\n
        B. Yes, but it is considered bad form.\n
        C. No, it will cause an error.\n
        """,'B'
    ],[
        """
        What is wrong with the following function definition:\n\n

        def addEm(x, y, z):\n
            return x + y + z\n
            print('the answer is', x + y + z)""",
            """
            A. You should never use a print statement in a function definition.\n
            B. You should not have any statements in a function after the return statement. Once the function gets to the return statement it will immediately stop executing the function.\n
            C. You must calculate the value of x+y+z before you return it.\n
            D. A function cannot return a number.""",'B'
    ],[
        """
        What will the following function return?\n\n

        def addEm(x, y, z):\n
        print(x + y + z)
        """,
        """
        A. None\n
        B. The value of x + y + z\n
        C. The string 'x + y + z'\n
        """,'B'
    ],[
        """
        What will the following code print if x = 3, y = 5, and z = 2?\n
        \n
        if x < y and x < z:\n
            print("a")\n
        elif y < x and y < z:\n
            print("b")\n
        else:\n
            print("c")\n
        ""","""
        A. a\n
        B. b\n
        C. c\n
        """, 'C'
    ],[
        """
        What is a Boolean function?
        ""","""
        A. A function that returns True or False\n
        B. A function that takes True or False as an argument\n
        C. The same as a Boolean expression\n
        """,'A'
    ],[
        """
        Is the following statement legal in a Python function (assuming x, y and z are defined to be numbers)?\n
        return x + y < z
        ""","""
        A. Yes\n
        B. No\n
        """,'A'
        
    ],[
        """
        What is printed by the following statements?
        \n
        \n
        s = "python rocks"\n
        print(s[3:8])
        """, """
        A. python\n
        B. rocks\n
        C. hon r\n
        D. Error, you cannot have two numbers inside the [ ].
        """,'C'
    ],[
        """
        What is printed by the following statements?
        \n
        s = "python rocks"\n
        print(s[7:11] * 3)
        ""","""
        A. rockrockrock\n
        B. rock rock ro\n
        C. rocksrocksrocks\n
        D. Error, you cannot use repetition with slicing.
        """,'A'
    ],[
        """
        Evaluate the following comparison:
        \n
        "Dog" < "Doghouse"\n
        ""","""
        A. True\n
        B. False
        """,'A'
    ],[
        """
        Evaluate the following comparison:
        \n
        "dog" < "Dog"
        ""","""
        A. True\n
        B. False\n
        """, 'B'
    ],[
        """
        Evaluate the following comparison:
        \n
        "dog" < "Dog"
        ""","""
        A. True\n
        B. False\n
        C. They are the same word
        """,'B'
    ],[
        """
        Evaluate the following comparison:
        \n
        "dog" < "Doghouse"
        ""","""
        A. True\n
        B. False
        """,'B'
    ],[
        """
        How many times is the word HELLO printed by the following statements?
        \n
        s = "python rocks"\n
        for ch in s:\n
        print("HELLO")
        ""","""
        A. 10\n
        B. 11\n
        C. 12\n
        D. Error, the for statement needs to use the range function.
        """,'C'
        
    ],[
        """
        How many times is the word HELLO printed by the following statements?
        \n
        s = "python rocks"\n
        for ch in s[3:8]:\n
        print("HELLO")
        ""","""
        A. 4\n
        B. 5\n
        C. 6\n
        D. Error, the for statement cannot use slice.
        """,'B'
    ],[
        """
        What is printed by the following statements?
        \n
        s = "python rocks"\n
        print(s[1] * s.index("n"))
        ""","""
        A. yyyyy\n
        B. 55555\n
        C. n\n
        D. Error, you cannot combine all those things together.
        """,'A'
    ],[
        """
        What is printed by the following statements?
        \n
        v = 2.34567\n
        print("{:.1f} {:.2f} {:.7f}".format(v, v, v))
        ""","""
        A. 2.34567 2.34567 2.34567\n
        B. 2.3 2.34 2.34567\n
        C. 2.3 2.35 2.3456700
        """,'C'
    ]
        ]
    return bank

def compare_Answer(response, right_Answer):
    return response.capitalize() == right_Answer

def calculate_Score(points, total):
    return points, total, (points/total)*100

def main():
    question = questions()
    rd.shuffle(question)
    score = 0
    for i in question:
        print(i[0],'\n', i[1])
        answer = input('Pick the multiple choice letter: ')
        if compare_Answer(answer, i[2]):
            score +=1
            print(f"That's right! It was {i[2]}")
        else:
            print(f'You picked {answer.capitalize()}, the correct answer was {i[2]}')
    grade = calculate_Score(score, len(question))
    print("_________________________________________")
    print(f"You got {grade[0]} out of {grade[1]}. That's {grade[2]:.2f}%")
    
main()

# rd.shuffle(bank)

# score = 0
# for item in bank: 
#     print(item[0], "\n", item[1])
#     answer = input('Pick the multiple choice letter: ')
#     if answer.capitalize() == item[2]:
#         score += 1
#         print(f"That's right! It was {item[2]}")
#     else:
#         print(f'You picked {answer}, the correct answer was {item[2]}')
# print("--------------------------------------\n")
# print(f"You got {score} out of {len(bank)}")