from aetam import app
from aetam import views

app.add_url_rule('/', view_func=views.IndexView.as_view('index_view'))
app.add_url_rule('/test', view_func=views.TestView.as_view('test_view'))
