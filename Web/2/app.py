from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def home():
    cookie = request.cookies.get('best_cookie')
    if cookie == "chocolate_chip":
        return "Congratulations! Here is your flag: G8KEY{C00k13_M@st3r_H@ck}"
    
    resp = make_response(render_template('index.html'))
    resp.set_cookie('best_cookie', 'unknown')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)