"""
    To launch the application, you simply need to point Python at it:
    >>> $ python application.py

    Now, if you navigate to the port you defined in the configuration ('8080'), you will see the text you put in your view
    function: hellow_world
    >>> $ open http://127.0.0.1:8081

"""

# imports the make_server function, which can create a simple web server when it is passed an application.
from wsgiref.simple_server import make_server

# The second and third line import the Configurator and Response functions from Pyramid.
# These functions are used to configure details and set parameters for the application and
# application and respond to requests, respectively.
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    """
    This function represents a "view" for our application. Remember, most web frameworks implement an MVC (model,
    view, controller) paradigm. A function that fulfills the requirements of a view is responsible for rendering the
    text that will be passed back to the requesting entity.

    In this case, the function, when called, uses the Response function we imported earlier. This passes back a value that
    should be given to the client. In our simple app, this is a very trivial view implementation
    """
    return Response('Hello %(name)s!' % request.matchdict)


def default(request):
    """
    """
    return Response('Default Response!')

# The first line here creates a variable called config out of the object created by the Configurator function that we imported at the top of the program.
# The next line calls the add_view method of this object. This method is used to define a view that can be used by the application. As you can see, we pass in the hello_world function we defined earlier. This is where that function is actually incorporated as a view.
# The following lines actually creates the WSGI application by calling the make_wsgi_app method of the config object. This uses the objects attributes, such as the view we added, to create an application.
# This application is then passed to the make_server function we imported in order to create an object that can launch a web server to serve our application. The last line launches this server.
if __name__ == '__main__':
    config = Configurator()
    config.add_view(default)
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8081, app)
    server.serve_forever()
