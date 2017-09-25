from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']=True

form_box = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = "post">
            <label for="rotate by">Rotate by:</label>
            <input type="text" name ="rot" value ="0" />
            <textarea name ="text" value ="0">{0}
            </textarea>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

#add two culy brackets in the text area to "escape". Meaning we want the text area to be ignored since we added 0

@app.route("/")
def index():
    return form_box.format("") 

@app.route("/", methods=['POST'])
#store the values of request parameters: rot & text.
#then encrypt the value of text using rotate_string
#return the encrypted string, wrapped in <h1>


def encrypt():
    req= request.form
    rot = int(req['rot'])
    text = req['text']
    
    text_input = rotate_string(text, rot) 

    return form_box.format(text_input)

app.run()