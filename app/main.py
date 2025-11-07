from flask import Flask, jsonify, request, render_template, redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from app.routes import bp
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(bp)
Scss(app)

class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
class MyTask(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    #content = db.Column(db.String(100), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    #complete = db.Column(db.Integer, default=0)
    complete: Mapped[bool] = mapped_column(default=0)
    #created = db.Column(db.DateTime, default=datetime.utcnow)
    created: Mapped[datetime] = mapped_column(default=datetime.now)

    def __repr__(self) -> str:
        return f"Task {self.id}"
        

@app.route("/", methods=["POST","GET"])
def index():
    # Add a task
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"
    # See all current tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR:{e}"

@app.route("/update/<int:id>", methods=["GET","POST"])
def edit(id:int):
    edit_task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        edit_task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR:{e}"
    else:
        return render_template('edit.html', task=edit_task)

@app.route("/health")
def health():
    return jsonify({"Status":"ok"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True,host="0.0.0.0", port=1234) 