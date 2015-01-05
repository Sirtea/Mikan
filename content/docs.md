# Mikan

## A simplistic approach to content publishing

Mikan does not use a database engine to render pages.
It just maps paths to markdown files in disk.

Mikan renders mardown pages in `content` folder, as follows:

* All paths ending with `/` will be rendered from `<path>/index.md`
* All paths not ending with `/` will be rendered from `<path>.md`
