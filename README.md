Mikan
=====

## A simplistic approach to content publishing

Mikan CMS is a content publishing platform with no database.
It just maps markdown files to pages.

As a feature, Mikan also generates a `/sitemap.xml` from content folder, and serves static files.

The main idea behind is that a content publisher does not need to know html nor css nor javascript.

* A designer should take care of html templates, css style sheets and javascript (if needed), in an infrequent basis.
* A publisher should know only markdown and should modify those files in a regular timing, in order to have an up-to-date web page.

If you want to see it in action, just clone the repository (or download) a tarball release and run `server.sh`.
Please notice that mikan has some python requirements as shown in `requirements.txt`.
Virtualenv is a good friend to avoid system level modifications.
