import web
urls=(
    '/','test'
)
class test:
    def GET(self):
        return "efgdsaf"

if __name__ == "__main__":
    print(1)
<<<<<<< HEAD
    app=webpy.web.application(urls,globals())
=======
    app=web.application(urls,globals())
>>>>>>> 33cbe645da8e67b4fc1c00259e37aef20fb3aba6
    app.run()