from flask import Flask, url_for, render_template, request
import random

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

def shortPass(animal, word):
    # Empty variable to add on to to create the final password
    result = "";
    
    # Array to contain the different parts of the password, gets shuffled before being turned into a string and stored in result
    resultArray = []
    
    # Special characters that can be used in the password, must be separated by spaces
    specialCharacters = "! ? #";
    
    # Splits the special characters string into an array
    specialArray = specialCharacters.split();
    
    # Choosing a random special character to add to the password and adding it to a variable
    random.shuffle(specialArray)
    specialCharacter = specialArray[0]
    
    # Generating a random number to use in the password
    randomNum = int(random.random() * 100)
    
    # Adding all the different parts of the password to the resultArray
    resultArray.append(specialCharacter)
    resultArray.append(animal)
    resultArray.append(word)
    resultArray.append(str(randomNum))
    
    # Shuffling the result array
    random.shuffle(resultArray)
    
    # Storing the resultArray as one string in result, instead of as an array, before returning the final password
    for value in resultArray:
        result += value
    
    return result

@app.route("/")
def render_home():
    return render_template('home.html')
    
@app.route("/short")
def render_short():
    return render_template('short.html')
    
@app.route("/long")
def render_long():
    return render_template('long.html')
    
@app.route("/random")
def render_random():
    return render_template('random.html')

@app.route("/short-submit", methods=['GET', 'POST'])
def render_short_submit():
    animal = request.args['animal']
    word = request.args['word']
    return render_template('short-submit.html', password=shortPass(animal, word))


if __name__=="__main__":
    app.run(debug=True)



