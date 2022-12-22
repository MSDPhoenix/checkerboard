from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display_checkerboard():
    return render_template(
        'checkerboard.html', 
        x=8, 
        y=8, 
        style1="style='background-color:pink'",
        style2="style='background-color:black'"
        )

@app.route('/<int:x>/')
def display_checkerboard2(x):
    return render_template(
        'checkerboard.html', 
        x=x, 
        y=8, 
        style1="style='background-color:lime'",
        style2="style='background-color:black'"
    )

@app.route('/<int:x>/<int:y>/')
def display_checkerboard3(x,y):
    return render_template(
        'checkerboard.html',
        x=x,
        y=y, 
        style1="style='background-color:lime'",
        style2="style='background-color:pink'"
    )

@app.route('/<int:x>/<int:y>/<string:color1>/')
def display_checkerboard4(x,y,color1):
    return render_template(
        'checkerboard.html',
        x=x,
        y=y, 
        style1=f"style='background-color:{color1}'",
        style2="style='background-color:pink'"
    )

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>/')
def display_checkerboar5(x,y,color1,color2):
    return render_template(
        'checkerboard.html',
        x=x,
        y=y, 
        style1=f"style='background-color:{color1}'",
        style2=f"style='background-color:{color2}'",
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)