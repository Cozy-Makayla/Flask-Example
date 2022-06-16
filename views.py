from flask import(
    render_template,
    Blueprint,
    request
)

message_list = []

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/contacts', methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        task = request.form.get("Message")
        message_list.append(task)
        print(message_list)
        return render_template("contacts.html", message_list=message_list)
    return render_template('contacts.html')

@views.route('/about')
def about():
    return render_template('about.html')

