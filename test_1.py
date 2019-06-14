import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.concurrent import Future
from tornado.httpclient import AsyncHTTPClient, HTTPClient

#1


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("What's up, man!")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
# #5
# import motor
# db = motor.MotorClient().test
#
#
# @gen.coroutine
# def loop_example(collection):
#     cursor = db.collection.find()
#     while (yield cursor.fetch_next):
#         doc = cursor.next_object()

# async def call_blocking(blocking_func=None, args=None):
#     await tornado.IOLoop.current().run_in_executor(None, blocking_func, args)

# #4
# def c():
#     print("What's up, man!")
#
#
# async def a():
#     b = await c()
#
#     return b

# #3
# def async_fetch_manual(url):
#     http_client = AsyncHTTPClient()
#     my_future = Future()
#     fetch_future = http_client.fetch(url)
#
#     def on_fetch(f):
#         my_future.set_result(f.result().body)
#
#     fetch_future.add_done_callback(on_fetch)
#     return my_future

# #2
# def synchronous_fetch(url):
#     http_client = HTTPClient()
#     response = http_client.fetch(url)
#     return response.body
