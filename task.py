def task_1(numbers, N): # Numbers is a list of integer values, times is how many times to operatate (int)
    int(input("please enter a number"))
    for _ in range(N):
        if N % 2 != 0:
            + 2
        else:
            - 2



    return numbers
print(task_1())

def task_2(N): # N is any integer value
    msg = ""
    N
    if N == 1:
        msg += "Brilliant"
    if N == 2:
        msg += "Exciting"
    if N == 3:
        msg += "Fantastic"
    if N == 4:
        msg += "Virtious"
    if N == 5:
        msg += "Heart-warming"
    if N == 6:
        msg += "Tear-jerking"
    if N == 7:
        msg += "Beautiful"
    if N == 8:
        msg += "Echilarating"
    if N == 9:
        msg += "Emotional"
    if N == 10:
        msg += "Inspiring"
    
    msg = f" number is {N}."





    return msg
def task_3(calc): # Calc is a string
    num1 = int(input("please enter a number "))
    num2 = int(input("please enter another number "))
    method = input("please enter a mathmatical method ")

    if method == '-':
        num1 - num2
    if method == '+':
        num1 + num2
    if method == '*':
        num1 * num2
    if method == '/':
        if num2 !=0:
            result = num1 / num2
        else:
            result = -1




    return result # Result should be a number answer

print(task_3("6 - 3"))