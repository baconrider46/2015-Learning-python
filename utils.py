"""THis is my utility sink"""

import colors as c

def ask(question,color=c.magenta):
    print(color + question + c.reset)
    answer = input('> '+ c.base3).strip().lower()
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear)
    color = ask("what is your name in color" ,c.random_color())
    name = ask("Whats your name young one")
    








