from bottle import Bottle, view, abort, response, static_file
from misaka import html
import os

app = Bottle()
CURRENT_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'views'))
PAGES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../content/pages'))
ERRORS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../content/errors'))
SNIPPET_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../content/snippets'))
STATIC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'static'))


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


@app.get('/sitemap.xml')
@view('sitemap', template_lookup=[TEMPLATE_DIR])
def sitemap():
    urls = []
    for dirpath, dirnames, filenames in os.walk(PAGES_DIR):
        prefix = dirpath != PAGES_DIR and dirpath[len(PAGES_DIR):] or '/'
        for file in filenames:
            if file.endswith('.md'):
                file = file[:-3]
                if file.endswith('index'):
                    file = file[:-5]
                urls.append(os.path.join(prefix, file))
    response.content_type = 'application/xml'
    return {'urls': urls}


@app.get('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=STATIC_DIR)


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
