from flask import Flask, render_template, request

app = Flask(__name__)

menu = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        base_price = float(request.form["price"])
        tax = float(request.form["tax"])
        discount = float(request.form["discount"])

        final_price = base_price + (base_price * tax / 100) - (base_price * discount / 100)

        item = {
            "name": name,
            "base_price": base_price,
            "tax": tax,
            "discount": discount,
            "final_price": round(final_price, 2)
        }

        menu.append(item)

    return render_template("index.html", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)