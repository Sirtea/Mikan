from bottle import Bottle, view, abort
from misaka import html
import os

app = Bottle()
CURRENT_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'views'))
PAGES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../content/pages'))
ERRORS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../content/errors'))
SNIPPET_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../content/snippets'))


def load_snippet(snippet):
    path = SNIPPET_DIR + '/' + snippet + '.md'
    try:
        return html(open(path).read().decode('utf-8'))
    except:
        return None


@app.error(404)
@view('error', template_lookup=[TEMPLATE_DIR])
def error404(error):
    path = ERRORS_DIR + '/404.md'
    return {
        'snippet': load_snippet,
        'content': html(open(path).read().decode('utf-8')),
    }


@app.get('/')
@app.get('<channel:path>/')
@app.get('/<page>')
@app.get('<channel:path>/<page>')
@view('layout', template_lookup=[TEMPLATE_DIR])
def show_page(channel='', page='index'):
    path = PAGES_DIR + channel + '/' + page + '.md'
    try:
        return {
            'snippet': load_snippet,
            'content': html(open(path).read().decode('utf-8')),
        }
    except:
        abort(404)
