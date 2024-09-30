from flask import Flask, url_for, render_template, request
import random, string

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

# Creates a short, somewhat easy to remember password using the user's favorite animal and favorite word
def shortPass(animal, word):
    # Empty variable to add on to to create the final password
    result = "";
    
    # Array to contain the different parts of the password, gets shuffled before being turned into a string and stored in result
    resultArray = []
    
    # Special characters that can be used in the password, (cannot be separated by spaces)
    specialCharacters = "!?#";
    
    # Splits the special characters string into an array
    specialArray = list(specialCharacters)
    
    # Choosing a random special character to add to the password and adding it to a variable
    random.shuffle(specialArray)
    specialCharacter = specialArray[0]
    
    # Generating a random number to use in the password
    randomNum = int(random.random() * 100)
    
    # Getting rid of spaces in the user's answers
    animal.replace(" ", "")
    word.replace(" ", "")
    
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
    
    # Returning the final result
    return result


# Creates a longer, harder to remember, but more secure password using the user's favorite animal, word, color, 
def longPass(animal, word, media, color):
    # Empty variable to add on to to create the final password
    result = "";
    
    # Array to contain the different parts of the password, gets shuffled before being turned into a string and stored in result
    resultArray = []
    
    # Special characters that can be used in the password, (cannot be separated by spaces)
    specialCharacters = "!?#";
    
    # Splits the special characters string into an array
    specialArray = list(specialCharacters);
    
    # Choosing a random special character to add to the password and adding it to a variable
    random.shuffle(specialArray)
    specialCharacter = specialArray[0]
    
    # Generating a random number to use in the password
    randomNum = int(random.random() * 100)
    
    # Getting rid of spaces in the user's answers
    animal.replace(" ", "")
    word.replace(" ", "")
    media.replace(" ", "")
    color.replace(" ", "")
    
    # Adding all the different parts of the password to the resultArray
    resultArray.append(specialCharacter)
    resultArray.append(str(randomNum))
    resultArray.append(animal)
    resultArray.append(word)
    resultArray.append(media)
    resultArray.append(color)
    
    # Shuffling the result array
    random.shuffle(resultArray)
    
    # Storing the resultArray as one string in result, instead of as an array, before returning the final password
    for value in resultArray:
        result += value
    
    # Returning the final result
    return result


# A very secure but very random, hard to remember password
def randomPass():
    # New variable to add onto to create the final password that gets returned
    result = ""
    
    # Array to contain the different parts of the password, gets shuffled before being turned into a string and stored in result
    resultArray = []
    
    # Special characters that can be used in the password, (cannot be separated by spaces)
    specialCharacters = "!?#";
    
    # Splits the special characters string into an array
    specialArray = list(specialCharacters)
    
    # Choosing a random special character to add to the password and adding it to a variable
    random.shuffle(specialArray)
    specialCharacter = specialArray[0]
    
    # Generating a random number for the length of the password
    randomNum = int(random.random() * 5 + 10)
    
    # Generating a random number to use in the password
    randomNum2 = int(random.random() * 100)
    
    # Creating an array of all printable ASCII characters
    allCharsArray = list(string.printable)
    
    # Creating an array of all printable ASCII characters, excluding characters like tabs and new line characters
    charsArray = []
    for i in range(94):
        charsArray.append(allCharsArray[i])
    
    # Adding randomNum random characters from the charsArray array to the result string
    for i in range(randomNum):
        rand = int(random.random() * 93)
        resultArray.append(charsArray[rand])
    
    # Adding a special character and random num to the password to insure that it works on most/all sites
    resultArray.append(specialCharacter)
    resultArray.append(str(randomNum))
    
    # Shuffling the result array
    random.shuffle(resultArray)
    
    # Storing the resultArray as one string in result, instead of as an array, before returning the final password
    for value in resultArray:
        result += value
    
    # Returning the final result
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
    
@app.route("/long-submit", methods=['GET', 'POST'])
def render_long_submit():
    animal = request.args['animal']
    word = request.args['word']
    media = request.args['media']
    color = request.args['colorName']
    return render_template('long-submit.html', password=longPass(animal, word, media, color))

@app.route("/random-submit", methods=['GET', 'POST'])
def render_random_submit():
    return render_template('random-submit.html', password=randomPass())


if __name__=="__main__":
    app.run(debug=False)



