from gaesessions import SessionMiddleware
import os

def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app, cookie_key='4A21A24CBEC005D868A1DDD4CC40D831045CF193B8DACDF1B1C99ECFBE0CD4C8')
    return app