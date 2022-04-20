from turtle import title
from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_Secret_key'

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route("/")
@app.route("/index")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="Про flask", menu=menu)

@app.route("/profile/<username>")
def profile(username, path):
    return f"Ползователь: {username}, {path}"

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template('contact.html', title = "Обратная связь", menu = menu)

#тестирование
# with app.test_request_context():
#     print(url_for('about'))
#     print(url_for('profile', username="sfsff"))


if __name__ == "__main__":
    app.run(debug=True)