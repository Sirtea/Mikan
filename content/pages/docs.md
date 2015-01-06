# Mikan

## A simplistic approach to content publishing

### Adding content

Mikan does not use a database engine to render pages.
It just maps paths to markdown files in disk.

Mikan renders mardown pages in `content/` folder, as follows:

* All paths ending with `/` will be rendered from `<path>/index.md`
* All paths not ending with `/` will be rendered from `<path>.md`

### Modifying layout

Mikan uses a template to render content on it.
It can be located at `mikan/views/layout.tpl`.
Error pages use the template in `mikan/views/error.tpl`.

Rendered content is passed to the templates in a variable called `content`,
and should be placed in the templates as an unescaped variable `{{!content}}`

For more info just look ath the template documentation.
The template engine is the one shipped with [bottle](http://bottlepy.org/).
