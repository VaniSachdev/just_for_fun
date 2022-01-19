from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def basic():
    key_word = "[INSERT YOUR OWN WORD]"
    anagram = ["PUT", "A", "WORD", "IN", "THE", "URL!"]
   
    return render_template("main.html", key_word = key_word, anagram = anagram) 


@app.route('/<key_word>')
def anagrams(key_word):
    lines = []
    with open('words.txt') as f:
        lines = f.readlines()
    
    key_word = key_word.upper()

    anagram = []

    for word in lines:
        if sorted(key_word) == sorted(word.strip()):
            anagram.append(word.strip())
   
    return render_template("main.html", key_word = key_word, anagram = anagram) 







  