import contextlib
import socket
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer, test


def serve():
    handler_class = partial(SimpleHTTPRequestHandler, directory="public")

    class DualStackServer(ThreadingHTTPServer):
        def server_bind(self):
            with contextlib.suppress(Exception):
                self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
            return super().server_bind()

    test(
        HandlerClass=handler_class,
        ServerClass=DualStackServer,
        port="5600",
        bind="localhost",
    )
