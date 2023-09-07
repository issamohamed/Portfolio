from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('advanced_portfolio.html')

@app.route('/about')
def About():
    return render_template('advanced_about.html')

@app.route('/projects')
def Projects():
    return render_template('projects.html')

@app.route('/education')
def Education():
    return render_template('education.html')

if __name__ == '__main__':
    # Specifying a unique port number to avoid possible port conflicts
    app.run(host="0.0.0.0", port=3333)
    app.run(debug=True)
