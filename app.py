from flask import Flask,render_template

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('my.html') 

# @app.route('/whereami')
# def whereami():
#     return "cape coast"

# @app.route('/foo/<name>')
# def foo (name):
#     return render_template('foo.html', to = name)

# @app.route('/login')

# @app.route('/tryout')
# def tryout():
#     return render_template('tryout2.html')   

if __name__ == '__main__':
    app.run(debug=True)