from flask import Flask, render_template, request
from logger import send_notification
from config import IMAGE_URL

app = Flask(__name__)

visitors = 0


@app.route("/")
def home():
    return render_template(
        "index.html",
        image_url=IMAGE_URL
    )


@app.route("/visit", methods=["POST"])
def visit():
    global visitors

    consent = request.form.get("consent")
    country = request.form.get("country", "").strip()

    if consent != "yes":
        return "Consent required.", 400

    visitors += 1

    send_notification(
        f"New consenting visitor!\n"
        f"Country provided: {country or 'Not provided'}\n"
        f"Total visits: {visitors}"
    )

    return "Thank you for visiting!"


if __name__ == "__main__":
    app.run(debug=True)
