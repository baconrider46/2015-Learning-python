"""This is destiny quiz"""
import colors as c
from utils import ask
import random
import time
import time as t

intro = c.clear + c.cyan+ '''
Welcome to the the test guardian.
''' + c.reset

def q1():
    answer = ask(c.cyan + "What is the first gun you get in the beginning?")
    if answer == 'khovostav':
        print(c.green + "Well done traveler!")    
        return True
    print(c.red + "failure is not acceptable guardian")
    return False

def q2():
    answer = ask(c.cyan + "What is the first enemy race you incounter at the beginning?")
    if answer.startswith("fallen"):
        print(c.green + "sucess guardian!")
        return True
    print(c.red + "Nice try guardian.")
    return False

def q3():
    answer = ask(c.cyan + "What is one race you can pick at the beginning?" + c.reset)
    if answer.startswith("human") or ("awoken") or ("exo"):
        print(c.green + "Great guardian!")
        return True
    print(c.red + "Next time you will get it guardian.")
    return False

def q4():
    answer = ask(c.cyan + "What is the first ship you aquire?" + c.reset)
    if answer.startswith("arcadia class jumpship"): 
        print(c.green + "Success Guardian")
        return True
    print(c.red + "Failure Gardian")
    return False

def q5():
    answer = ask(c.cyan + "What is the maximum level that you have to then use light?")
    if answer.startswith("20"):
        print(c.green + "Well done Guardian")
        return True
    print(c.red + "Better luck next time Guardian.")
    return False







questions = [q1,q2,q3,q4,q5]



