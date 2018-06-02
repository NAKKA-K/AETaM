from aetam import app
from aetam import views

app.add_url_rule('/', view_func=views.IndexView.as_view('index'))
app.add_url_rule('/login', view_func=views.LoginView.as_view('login'))
app.add_url_rule('/logout', view_func=views.LogoutView.as_view('logout'))
app.add_url_rule('/signup', view_func=views.SignUpView.as_view('signup'))
