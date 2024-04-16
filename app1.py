from flask import Flask,render_template,redirect,request,jsonify
import json

obj = Flask(__name__)

@obj.route('/')


def Home():
    return "Hello World"

@obj.route('/cal',methods =['GET'])
def cal():
    operation =request.json["operation"]
    number1 = request.json["number1"]
    number2 = request.json["number2"]
    
    if operation =="add":
        result =int(number1)+int(number2)
    elif operation =="multiply":
        result = int(number1)*int(number2)
    elif operation =="divsion":
        result = int(number1)/int(number2)
    elif operation =="subract":
        result=int(number1)-int(number2)
    else:
        result = "please give right input"
    #return jsonify(result)    
    return "the operation is {} and the result is {}".format(operation,result)




if __name__ =='__main__':
    obj.run(debug=True)
