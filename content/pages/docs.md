### Adding content

Mikan does not use a database engine to render pages.
It just maps paths to markdown files in disk.

Mikan renders mardown pages in `content/pages/` folder, as follows:

* All paths ending with `/` will be rendered from `<path>/index.md`
* All paths not ending with `/` will be rendered from `<path>.md`

Error pages are rendered from `content/errors/` folder, for example from `404.md` file.

Snippets are rendered from `content/snippets/` folder, for example from `header.md` file.

### Modifying layout

Mikan uses a template to render content on it.
It can be located at `mikan/views/layout.tpl`.
Error pages use the template in `mikan/views/error.tpl`.

Rendered content is passed to the templates in a variable called `content`,
and should be placed in the templates as an unescaped variable `{{!content}}`

Snippets of code subject to frequent changes by content publishers
can also be include as snippets. For example, just place a `header.md`
in snippets folder and include in templates as an unescaped variable,
as `{{!snippet('header')}}`.

For more info just look at the template documentation.
The template engine is the one shipped with [bottle](http://bottlepy.org/).

### Static content

Although static content should be served by a more capable web server,
mikan offers the possibility to do this. Please evaluate the risks involved.

All static content will be served from `mikan/static/` folder, and the url
should begin with `/static/`. So, for example, a `style.css` file could be
in `mikan/static/style.css` and should be included at the url `/static/style.css`
