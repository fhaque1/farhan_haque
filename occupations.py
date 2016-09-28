from flask import Flask, render_template
from utils import jobpicker as jp

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('homepage.html', foo = 'Homepage', Link = "/occupations")



@app.route("/occupations")
def tmplt():
    main = jp.convertToList('data/occupations.csv')
    return render_template('occupations.html', foo="Occupations", collection= main[1:], job = jp.randChooser(main), header = main[0])
    
if __name__ == "__main__":
    app.debug = True 
    app.run()

