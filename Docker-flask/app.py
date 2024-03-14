from flask import Flask
app = Flask(__name__)
@app.route("/")
def Helloworld():
    return 'Hoohoo'
@app.route("/about")
def Byeworld():
    return 'Heehee'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5100,debug=True)