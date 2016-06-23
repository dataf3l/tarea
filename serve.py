import cherrypy
from tarea import get_all_cities_html


class HelloWorld(object):
    def index(self):
        return get_all_cities_html()
    index.exposed = True

cherrypy.quickstart(HelloWorld())
