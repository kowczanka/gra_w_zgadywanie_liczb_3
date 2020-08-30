from flask import Flask, render_template, request

""" zgadywanka z komputerem we flasku """

app = Flask(__name__)

@app.route("/gra", methods = ["GET", "POST"])
def gra():
    if request.method == "GET":
        min_num = int(request.form.get("min_num"))  #te dwa wersy sa chyba nieprawidłowe, ale nie wiem jak je poprawić
        max_num = int(request.form.get("max_num"))
        return render_template('zgadywanie_3.html', min_num=min_num, max_num=max_num)
    else:
        min_num = int(request.form.get("min_num"))
        max_num = int(request.form.get("max_num"))
        user_answer = request.form.get("user_answer")
        computer_guess = int(request.form.get("computer_guess", 500))

        if user_answer == "too small":
            min_num = computer_guess
        elif user_answer == "too big":
            max_num = computer_guess
        elif user_answer == "win":
            return render_template("zgadywanie_3_post.html")

        computer_guess = (max_num - min_num) // 2 + min_num
        return render_template("zgadywanie_3.html", computer_guess=computer_guess, min_num=min_num, max_num=max_num)


if __name__ == "__main__":
    app.run()

