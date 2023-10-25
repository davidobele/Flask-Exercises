from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/check', methods=['GET'])
def check_number():
    try:
        number = int(request.args.get('number'))
        if number % 2 == 0:
            result = f"{number} is an even number."
        else:
            result = f"{number} is an odd number."
    except ValueError:
        result = "The input is not a valid integer."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
