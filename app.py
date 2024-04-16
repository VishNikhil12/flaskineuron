from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1> HELLO WORLD </h1>"



@app.route('/welcome')
def welcome():
    return "Welocme to Flask"


@app.route('/success/<int>:score')
def success(score):
    return "You Have Passed the score is "+ str(score) +"Congrasulations!!"

@app.route('/fail/<int>:score')
def fail(score):
    return "Sorry you have the score is " +str(score)+ "failed.."

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/calculate' , methods = ['GET' ,'POST'])
def calculate():
    if request.method == 'GET':
        
            return render_template('calculate.html')
    else:
        
        pyhsics = float(request.form['physics'])
        maths = float(request.form['maths'])
        science = float(request.form['science'])
   
        average_marks = ( pyhsics + maths + science)/3
        
    return render_template('results.html',results=average_marks)



if __name__ == '__main__':
    app.run(debug=True)
 
 
 
 
 
 
 
 
    