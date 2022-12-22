from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display_checkerboard():
    y_list = []
    for i in range(8):
        x_list = []
        for j in range(8):
            if j%2==0 and i%2==0 or j%2==1 and i%2==1:
                x_list.append('<div class="square black"></div>')
            else:
                x_list.append("<div class='square red'></div>")
        y_list.append(x_list)
    return render_template('checkerboard2.html', y_list=y_list)

@app.route('/<int:x>/')
def display_checkerboard2(x):
    return render_template('checkerboard.html', x=x, y=8, color1="red", color2="black")

@app.route('/<int:x>/<int:y>/')
def display_checkerboard3(x,y):
    return render_template('checkerboard.html',x=x,y=y, color1="red", color2="black")

@app.route('/<int:x>/<int:y>/<string:color1>/')
def display_checkerboard4(x,y,color1):
    return render_template('checkerboard.html',x=x,y=y, color1=color1, color2="black")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>/')
def display_checkerboar5(x,y,color1,color2):
    for i in range(y):
        print(i)
    return render_template('checkerboard.html',x=x,y=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True,port=5001)