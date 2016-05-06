from gevent.pywsgi import WSGIServer
from gevent import monkey
from HTTP_Resp import HTTPError, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
import traceback
monkey.patch_all()

        
def add_Route(url, func, url_map, methods = None): #Act as an Function
    if methods:
        url_map.add(Rule(url, endpoint = func, methods = methods))
    else:
        url_map.add(Rule(url, endpoint = func))



        
class holla_base_app(object):


    """
        This Class provide a Response Obj as an alias of HTTP_Resp.Response
        Usage: Let get_resp obj return a Response obj, and you don't need to do anything else 
    """
    
    def __init__(self):
        self.Response = Response  # Just an alias of Response Class
        self.url_map = Map([])
        pass
        
    def route(self, url, methods = None):
        def decorator(callback):
            add_Route(url, callback, self.url_map, methods)
            return callback
        return decorator

    def get_resp(self, env):
        self.env = env
        adapter = self.url_map.bind_to_environ(self.env)
        try:
            endpoint, values = adapter.match()
            return Response(endpoint(**values))
        except NotFound, e:
            return Response(status = 404)
        except HTTPException, e:
            return Response(status = 500)
        return Response(
            "Holla Got your Requests",
            200
        )
    
    


class holla_server(WSGIServer):
    def __init__(self, app, port = 8000, host = "127.0.0.1", debug = False):
        self.port, self.host, self.app = port, host, app
        WSGIServer.__init__(self, listener = (self.host, self.port), application=self.application)
        
    

    def Resp(self, func, obj):
        func(obj.status, obj.header)
        return str(obj.content)
        
    def application(self, env, start_response):
        # ===== Default Settings ======

        try:
            html_code = self.app.get_resp(env)
            if not isinstance(html_code, Response):
                raise HTTPError(500)
        except HTTPError, e:
            html_code = e
            traceback.print_exc()
        except :
            traceback.print_exc()
            html_code = HTTPError(500)
        return self.Resp(start_response, html_code)
        
    def __call__(self, environ, start_response):
        return self.application(environ, start_response)
        
    def run_server(self, reload = False):
        print "Holla has been running on the %s in port %s"%(self.host, self.port)
        if reload:
            from werkzeug.serving import run_simple
            run_simple(self.host, self.port, self, use_debugger=True, use_reloader=True)
        else:
            self.serve_forever()
    

        
if __name__ == "__main__":
    holla_server(holla_base_app, debug = True).run_server(reload = True)