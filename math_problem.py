import random

# Generate a problem for a 1st grader
def generate_problem():
    operation = random.choice(["+", "-"])
    num1 = random.randint(1, 10)
    if operation == "-":
        num2 = random.randint(1, 20)
    else:
        num2 = random.randint(1, 10)
    return operation, num1, num2
    
# Ask the problem and get the user input
def ask_problem():
    op, n1, n2 = generate_problem()
    
    # Avoid negative number answers
    if op == '-':
        n1, n2 = order_numbers(n1, n2)
    
    answer = eval(f"{n1} {op} {n2}")
    user_answer = int(input(f"{n1} {op} {n2} = "))
    return user_answer == answer

# Order largest to smallest to avoid negative answers
def order_numbers(n1, n2):
    if n1 >= n2:
        return n1, n2
    else:
        return n2, n1

# Check the answer and print the commentary
def print_result(is_correct, questions_remain)-> bool:
    if is_correct:
        if questions_remain == 0:
            print(f"Correct! You can play!")
            return True
        elif questions_remain == 1:
            plural = ''
        else:
            plural = 's'

        print(f"Correct! Answer {questions_remain} more question{plural}!")   
    else:
        print("Try again!")
    return False

def main():
    count = 0
    num_probs = 3  #Require 3 problems to be answered
    while True:
        is_correct = False

        # If the answer is correct, then decrement
        is_correct = ask_problem()
        if is_correct:
            count += 1
            questions_remain = num_probs - count

        stop_loop = print_result(is_correct, questions_remain)
        if stop_loop:
            break


if __name__ == "__main__":
    main()