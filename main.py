import web
urls=(
    "/test",'test'
)
class test:
    def GET(self):
        inp = web.input().json()
        return inp

if __name__ == "__main":
    app=web.application(urls,globals())
    app.run()