from google.appengine.ext import ndb
import webapp2
import time

HTML = """
        <!DOCTYPE html>
            <html>
                <head lang="en">
                    <meta charset="UTF-8">
                    <title></title>
                </head>
                <body>
                    <form method="post" action="/">
                        <div id="chat_area">
                            <input type="text" name="message"/>
                            <input type="submit" value="send"/>
                        </div>
                    </form>
                    <div id="messages">
                        {0}
                    </div>


                </body>
            </html>
        """
def compose_response():
    lines = Messages.query().fetch()
    result = ""
    for line in lines:
        result += line.text + "</br>"
    return HTML.format(result)


class Messages(ndb.Model):
    text = ndb.StringProperty()



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(compose_response())

    def post(self):
        message = self.request.get("message")
        database = Messages()
        database.text = message
        database.put()
        time.sleep(2)
        self.response.write(compose_response())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
