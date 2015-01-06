Running Mikan CMS is really easy. It just needs python and some dependencies.

To get Mikan running just download a release (or clone the repository).
Place the folder `mikan` and `content` in a containing folder (all other files are optional).
This folder will be known from now on as the application root.
The application root should look like this:

    application_root/
        content/
            errors/
                404.md
            snippets/
            pages/
        mikan/
            __init__.py
            static/
            views/
        requirements.txt
        server.sh

The file `requirements.txt` contains all the dependencies needed to run Mikan.
Virtualenv works fine with this and it's the recommended way to run.
Use `pip -r requirements.txt` to install them all.

## Running Mikan CMS (required)

* **Developers**: Just run `server.sh` and go to `http://localhost:8080/`. This method is **not** production ready.
* **Sysadmins**: Mikan is a WSGI-compilant application and the callable is `mikan:app`. Run it with you preferred WSGI server.

## Customizing Mikan CMS (optional)

This part requires a designer with some basic HTML (and possibly CSS) skills.

* Modify `layout.tpl` and `error.tpl` in the `mikan/views/` folder, so the look and feel looks more appealing to your page.
* Place CSS sheet referenced in your templates and any other needed file (images, javascript) in `mikan/static/` folder.
* Ensure a `404.md` file exists in `content/errors/` folder.
* Put any snippet referenced on the templates in `content/snippets/` folder.

## Editing content (as needed)

This part should be done by a publisher, and requires only markdown knowledge.
All the files editable for a publisher are written in markdown and are contained in `content/` folder.

The main responsabilities for a publisher is to mantain snippets, error pages and creating some more content.

Snippets are created by a designer, and found in `content/snippets/` folder.
There are as many snippets as the designer decided to include. Just update as needed.

Error pages are in `content/errors/` folder. Ath this moment, the only error caught is the 404 error.

The remaining content are pages and are found in `content/pages/` folder, so put your `.md` files in a path relative to here.

Some examples:

* Page `http://www.example.com/about/me` will render markdown file `content/pages/about/me.md`
* Page `http://www.example.com/category/` will render file `content/pages/category/index.md`
