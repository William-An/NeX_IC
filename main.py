import web
urls=(
    '/','test'
)
class test:
    def GET(self):
        return "efgdsaf"

if __name__ == "__main__":
    print(1)
    app=web.application(urls,globals())
    app.run()