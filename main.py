import webpy.web
urls=(
    "/test",'test'
)
class test:
    def GET(self):
        inp = webpy.web.input().json()
        return inp

if __name__ == "__main":
    app=webpy.web.application(urls,globals())
    app.run()