from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route("/")
def show_home():
    """Ubermelon jobs homepage"""

    return render_template("index.html")

@app.route("/application-form")
def get_application():
    """Ubermelon application form page"""

    jobs = ['Software Engineer', 'QA Engineer', 'Product Manager']

    return render_template("application-form.html", jobs=jobs)

@app.route("/application-success", methods=["POST"])
def give_response():
    """Application Success page"""

    first_name = request.form.get("first_name")

    last_name = request.form.get("last_name")

    salary = float(request.form.get("req_salary"))

    if salary.is_integer():
        salary = int(salary)

    job_title = request.form.get("job_title")

    return render_template("application-response.html", first_name=first_name,
     last_name=last_name, salary=salary, job_title=job_title)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
