
from flask import Flask, request

app = Flask(__name__)

@app.route("/ussd", methods=["POST"])
def ussd():
    text = request.form.get("text", "")

    if text == "":
        response = "CON Welcome!\n1. Check balance\n2. Exit"
    elif text == "1":
        response = "END Your demo balance is KES 1,000."
    elif text == "2":
        response = "END Thank you for using our service."
    else:
        response = "END Invalid option."

    return response, print("USSD response:", repr(response)), {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
