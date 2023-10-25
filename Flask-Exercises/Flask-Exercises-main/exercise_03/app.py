from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dictionary to store registered users
registered_users = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        organization = request.form.get('organization')
        
        if name and organization:
            registered_users[name] = organization
            flash('Registration successful', 'success')
            return redirect(url_for('registrations'))
        else:
            flash('Please fill in all fields', 'danger')
    
    return render_template('home.html')

@app.route('/registrations')
def registrations():
    return render_template('registrations.html', registered_users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)
