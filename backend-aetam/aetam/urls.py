from aetam import app
from aetam import views

app.add_url_rule('/', view_func=views.IndexView.as_view('index'))
app.add_url_rule('/login', view_func=views.LoginView.as_view('login'))
