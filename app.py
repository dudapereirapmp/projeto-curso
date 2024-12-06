from flask import Flask, render_template, request

app = Flask(__name__)
gastos = []

@app.route("/", methods=["GET", "POST"])
def index():
    global gastos
    if request.method == "POST":
        gasto = request.form.get("gasto")
        if gasto:
            gastos.append(float(gasto))
    total = sum(gastos)
    return render_template("index.html", gastos=gastos, total=total)

if __name__ == "__main__":
    app.run(debug=True)