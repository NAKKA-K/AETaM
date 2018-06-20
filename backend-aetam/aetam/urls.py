from aetam import app
from aetam import views

app.add_url_rule('/login', view_func=views.LoginView.as_view('login'))
app.add_url_rule('/logout', view_func=views.LogoutView.as_view('logout'))
app.add_url_rule('/api/signup', view_func=views.SignUpView.as_view('signup'))
app.add_url_rule('/api/statuses', view_func=views.StatusApiView.as_view('get_status'))
app.add_url_rule('/api/word', view_func=views.WordApiView.as_view('post_word'))
app.add_url_rule('/api/image', view_func=views.ImageApiView.as_view('post_image'))
