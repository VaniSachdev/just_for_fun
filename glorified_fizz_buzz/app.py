from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def fizz_buzz_basic():
    number = 100
    list_of_num = list(range(1, number + 1))
    buzz_fizz = []
    for n in list_of_num:
        if n%15 == 0:
            buzz_fizz.append((n, "bf"))
        elif n%5 == 0:
            buzz_fizz.append((n, "b"))
        elif n%3 == 0:
            buzz_fizz.append((n, "f"))
        else:
            buzz_fizz.append((n, "n"))

    return render_template("main.html", list = buzz_fizz, number = number) 




@app.route('/<int:number>')
def fizz_buzz(number):
    list_of_num = list(range(1, number + 1))
    buzz_fizz = []
    for n in list_of_num:
        if n%15 == 0:
            buzz_fizz.append((n, "bf"))
        elif n%5 == 0:
            buzz_fizz.append((n, "b"))
        elif n%3 == 0:
            buzz_fizz.append((n, "f"))
        else:
            buzz_fizz.append((n, "n"))

    return render_template("main.html", list = buzz_fizz, number = number) 


  