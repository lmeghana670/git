from flask import Flask

app= Flask(__name__)
@app.route('/home')
def home():
    return "i hate you"

if __name__=='__main__':
    app.run(debug=True)