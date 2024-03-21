from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dummy portfolio data
portfolio_data = [
    {
        'title': 'Personal Details',
        'category': 'Personal Details',
        'description': 'The name is Angne, Gargi Angne. I am a student who lives in Mumbai and am currently in my 3rd year of IT engineering.',
    },
    {
        'title': 'Education',
        'category': 'Education',
        'description': 'I completed my high school education from Holy Cross Convent High School. I went to PES JR. colllege for HSC. I am currently a student of VESIT, Chembur.',
    },
    {
        'title': 'Skills',
        'category': 'Skills',
        'description': 'I have a whole lot of skills which cannot be written and expressed in a few lines. So, go to contact and contact me. Don\'t be shy!',
    }
]

# Portfolio Website route
@app.route('/portfolio')
def portfolio():
    category_filter = request.args.get('category')  # Get category filter from request URL
    if category_filter:
        filtered_portfolio_data = [project for project in portfolio_data if project['category'] == category_filter]
    else:
        filtered_portfolio_data = portfolio_data

    return render_template('portfolio.html' , portfolio_data=filtered_portfolio_data)


# Landing page route
@app.route('/')
def index():
    return render_template('index.html')

# Contact Us Form route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Dummy implementation: Print the received data
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        # Redirect to a thank you page after submitting the form
        return redirect('/thankyou')
    return render_template('contact.html')

# # Portfolio Website route
# @app.route('/portfolio')
# def portfolio():
#     return render_template('portfolio.html', portfolio_data=portfolio_data)

# Thank You page route
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
