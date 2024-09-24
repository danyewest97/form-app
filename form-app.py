from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

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

@app.route("/short.py")
def render_random():
    return render_template('random.html')


if __name__=="__main__":
    app.run(debug=False)
