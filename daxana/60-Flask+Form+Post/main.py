from flask import Flask, render_template, send_file, request
import smtplib
import requests

# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
OWN_EMAIL = 'YOUR OWN EMAIL ADDRESS'
OWN_PASSWORD = 'YOUR OWN EMAIL PASSWORD'

app = Flask(__name__)

# @app.route('/')
# def get_all_posts():
#     return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/', methods=["GET", "POST"])
# @app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # data = request.form
        data = request.form
        print(123, request.files)
        # send_email(data["name"], data["email"], data["phone"], data["message"])
        # send_file(data["file"], mimetype='image/jpg', as_attachment=True)
        return render_template("contact.html", msg_sent=True, form_name=data["name"], form_email=data["email"],
                               form_phone=data["phone"], form_message=data["message"], form_file=request.form.get('file'))
    return render_template("contact.html", msg_sent=False)


# def send_email(name, email, phone, message):
#     print(name, email, phone, message)
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
        # connection.login(OWN_EMAIL, OWN_PASSWORD)
        # connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)



if __name__ == "__main__":
    app.run(debug=True)
