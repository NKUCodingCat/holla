from gevent.pywsgi import WSGIServer
from gevent import monkey
from HTTP_Resp import HTTPError, Response
import traceback
monkey.patch_all()


        
class holla_base_app(object):

    def __init__(self, env):
        self.Response = Response  # Just an alias of Response Class
        pass

    def get_resp(self):
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
        return obj.content
        
    def application(self, env, start_response):
        the_app = self.app(env)
        
        # ===== Default Settings ======

        try:
            html_code = the_app.get_resp()
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