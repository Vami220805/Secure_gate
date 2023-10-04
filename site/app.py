from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In a real application, you would store user data in a database.
# For simplicity, we'll use hardcoded values here.
valid_email = "example@example.com"
valid_password = "password123"  # You should hash this password in production

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == valid_email and password == valid_password:
            # Successful login
            # You can set session variables, redirect the user, etc.
            return redirect(url_for("dashboard"))
        else:
            # Invalid credentials
            return "Invalid email or password. Please try again."

    return render_template("index.html")

@app.route("/site/dashboard.html")
def dashboard():
    # This is a simple example; you can render a dashboard template here.
    return "Welcome to the dashboard!"

if __name__ == "__main__":
    app.run(debug=True)
