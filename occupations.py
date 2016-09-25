from flask import Flask, render_template
import jobpicker

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

main = jobpicker.convertToList('occupations.csv')
randJob = jobpicker.randChooser(main)

@app.route("/occupations")
def tmplt():
    return render_template('occupations.html', foo="Occupations", collection= main[1:], job = randJob, header = main[0])
    
if __name__ == "__main__":
    app.debug = True 
    app.run()
