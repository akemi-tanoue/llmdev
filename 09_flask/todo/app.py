from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ファイルからTODOリストを読み込む関数
def load_todos():
    try:
        with open("todos.txt", "r") as file:
            todos = [line.strip() for line in file]
    except FileNotFoundError:
        todos = []
    return todos

# TODOリストをファイルに保存する関数
def save_todos(todos):
    with open("todos.txt", "w") as file:
        file.write("\n".join(todos))

@app.route("/", methods=["GET", "POST"])
def index():
    todos = load_todos()
    if request.method == "POST":
        new_todo = request.form.get("todo")
        if new_todo:
            todos.append(new_todo)
            save_todos(todos)
        return redirect(url_for("index"))
    return render_template("index.html", todos=todos)

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todos = load_todos()               #todos.txt を読み込む
    if todo_id in range(len(todos)):   #todo_id がリストの範囲内なら削除する
        del todos[todo_id]             #リストからその位置の要素を削除する
        save_todos(todos)              #削除結果をファイルに上書き保存する
    return redirect(url_for("index"))  #一覧へ戻る

if __name__ == "__main__":
    app.run(debug=True)