from celery import shared_task
import random
import time

@shared_task(queue="math_queue")
def add(number1, number2):
    result = number1 + number2
    print(f"Sum: {number1} + {number2} = {result}")
    delay = random.randint(1, 5)
    print(f"waiting {delay} seconds...")
    time.sleep(delay)
    return result

@shared_task(queue="math_queue")
def mul(num1, num2):
    result = num1 * num2
    print(f"Mul: {num1} * {num2} = {result}")
    delay = random.randint(1, 5)
    print(f"waiting {delay} seconds...")
    time.sleep(delay)
    return result

@shared_task(queue="math_queue")
def div(num1, num2):
    result = num1 // num2
    print(f"Mul: {num1} / {num2} = {result}")
    delay = random.randint(1, 5)
    print(f"waiting {delay} seconds...")
    time.sleep(delay)
    return result

@shared_task(queue="math_queue")
def sub(num1, num2):
    result = num1 // num2
    print(f"Mul: {num1} / {num2} = {result}")
    delay = random.randint(1, 5)
    print(f"waiting {delay} seconds...")
    time.sleep(delay)
    return result