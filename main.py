#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
