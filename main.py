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
import webapp2
from webapp2_extras import sessions

import index

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([('/step/(?P<stepNum>¥d{1})', index.StepHandler),
                                          ('/oauthcallback', index.CallbackHandler),
                                          ('/accepttoken', index.AcceptTokenHandler),
                                          ('/logout', index.LogoutHandler),
                                          ('/logoutandremove', index.LogoutAndRemoveHandler),
                                          ('/', index.MainHandler)],
                                         config=config, debug=True)
