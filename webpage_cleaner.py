"""Our team has just discovered that search engines are negatively scoring
our web-pages that include a link to the domain shittylistings.com. For
simplicity assume that we have 50,000 HTML files in a Unix directory tree
under a folder called "/website" (e.g. /website/home.html,
/website/san-diego/2505-via-clarita.html, etc). We have 24 hours to
get a list of file paths to the editorial staff so they can
edit the pages and remove the links. You need to make a list of the
.html files that contain links to the domain. How would you
solve the problem? Keep in mind our team is on a short deadline.

python has an OS function called walk which is meant to traverse
a directory and all subdirectories for paths. Using this, we can
go through each directory, and scan all .HTML files for the url
that is undesirable, we can then create a list of paths to those
files. (The prompt just says that we need to get a list of them, not
actually erase the instances so that's what I'll go with)."""

import os
import re

bad_url = re.compile("href=\"shittylistings\.com\"")
bad_files = []
for root, directory, files in os.walk('./website'):
    for file in files:
        # only deal with html files
        if file.endswith('.html'):
            with open(root + '/' + file) as html_file:
                for line in html_file:
                    # if the file contains a link to shittylistings
                    # add it to the list
                    if bad_url.search(line):
                        bad_files.append(root + "/" + file)
print(bad_files)

