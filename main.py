from flask import Flask , request
from caesar import rotate_string

app = Flask (__name__)
app.config ['DEBUG'] = True

form = ''' 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form name="my_form" action="/" method="POST" >
            <label>Rotate by: 
                <input name="rot" type="text" value ="0">
            </label>
            <textarea name ="text" ></textarea>
            <input name="submit" type="submit" value="Submit Query">

        </form>
    </body>
</html>

'''

@app.route("/")

def index():
    return form

@app.route("/" , methods=['POST'])
def encrypt():
    rotation=request.form["rot"]
    text_to_encrypt=request.form["text"]
    answer = rotate_string(text_to_encrypt,rotation)
    respond = ("<h1>" + answer + "</h1>")
    return respond






app.run()
