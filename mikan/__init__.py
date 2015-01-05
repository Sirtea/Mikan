from bottle import Bottle, view, abort
from misaka import html
import os

app = Bottle()
CURRENT_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'views'))
CONTENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../content'))


@app.get('/')
@app.get('<channel:path>/')
@app.get('/<page>')
@app.get('<channel:path>/<page>')
@view('layout', template_lookup=[TEMPLATE_DIR])
def show_page(channel='', page='index'):
    path = CONTENT_DIR + channel + '/' + page + '.md'
    try:
        return {
            'content': html(open(path).read().decode('utf-8')),
        }
    except:
        abort(404)
