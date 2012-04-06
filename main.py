import urllib2
import urlparse
import re
import os
import random
import json
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from images import handler


class HelpHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
        <pre>
                       .--.
                      (    )
             ,   ,         |
             |\_/|_________|
             |+ +          o
             |_^_|-||_____||
               U   ||     ||
                  (_|    (_|

        <a href="/img/random">/img/random</a>             Returns a random image
        <a href="/img/random.gif">/img/random.gif</a>         Returns a random image
        <a href="/img/wakewhenicare.gif">/img/(.*)</a>               Returns an image, given its file name

        <a href="/html/list">/hmtl/list</a>              Returns an HTML page containing the list of all image names
        <a href="/html/viewall">/html/viewall</a>           Returns an HTML page containing all images (this may freeze your browser)
        <a href="/html/search">/html/search</a>            Returns an HTML page containing a search engine for images

        <a href="/json/random?cb=callback">/json/random</a>            Returns a jsonp response for a random image (pass ?cb= for a jsonp response)
        <a href="/json/search/cat?cb=callback">/json/search?q=</a>         Returns a jsonp response for a list of images matching the search query string (pass ?cb= for a jsonp response)
        <a href="/json/list?cb=callback">/json/list</a>              Returns a jsonp response for the complete list of images (pass ?cb= for a jsonp response)
        </pre>
        """)


def main():
    application = webapp.WSGIApplication([

        ('/html/list', handler.GetListOfImagesAsHtmlHandler),
        ('/html/viewall', handler.DisplayAllImagesAsHtmlHandler),
        ('/html/search', handler.SearchThroughImagesAsHtmlHandler),

        ('/img/random\.gif', handler.GetRandomImageHandler),
        ('/img/random', handler.GetRandomImageHandler),
        ('/img/(.*)', handler.GetImageHandler),

        ('/json/random', handler.GetRandomImageAsJsonHandler),
        ('/json/search/(.*)', handler.GetImageSearchListAsJsonHandler),
        ('/json/list', handler.GetListOfImagesAsJsonHandler),

        ('/__/steal/bukit', handler.StealBukitImages),
        ('/__/steal/giftv', handler.StealGifTvImages),

        ('.*', HelpHandler)

    ], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
