import tornado
from tornado.ioloop import IOLoop

from controller.CompareTwoStringController import CompareTwoStringController


def _map_request_routes():
    # Set up the routes and handlers
    requests = [
        (r'/v1/compare-two-strings', CompareTwoStringController),
        (r'/v2/compare-two-strings', CompareTwoStringController),
    ]

    return requests


if __name__ == "__main__":

    ROUTES = _map_request_routes()

    application = tornado.web.Application(_map_request_routes())
    server = tornado.httpserver.HTTPServer(application)
    server.bind(9090)
    server.start()  # Specify number of subprocesses
    print("Started server on 9090")
    IOLoop.instance().start()