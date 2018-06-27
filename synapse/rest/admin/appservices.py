# -*- coding: utf-8 -*-
# Copyright 2018 Travis Ralston
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

from twisted.internet import defer

from synapse.http.servlet import RestServlet, parse_json_object_from_request
from synapse.api.urls import ADMIN_PREFIX

import logging
import re


logger = logging.getLogger(__name__)


def appservice_to_obj(appservice):
    return {
        "id": appservice.id,
        "as_token": appservice.token,
        "hs_token": appservice.hs_token,
        "url": appservice.url,
        # "enabled": appservice.enabled,
        "legacy": appservice.legacy,
        "sender_localpart": appservice.sender,
        # TODO: Namespaces
    }


class AppservicesListServlet(RestServlet):
    """Lists available application services
    """
    PATTERNS = [re.compile("^" + ADMIN_PREFIX + "/appservices$")]

    def __init__(self, hs):
        super(AppservicesListServlet, self).__init__()
        self.auth = hs.get_auth()
        self.clock = hs.get_clock()
        self.appservices_handler = hs.get_application_service_handler()

    @defer.inlineCallbacks
    def on_GET(self, request):
        requester = yield self.auth.get_user_by_req(request, allow_guest=False)
        # requester_user_id = requester.user.to_string()

        all_services = yield self.appservices_handler.get_services()
        result = {}
        for v in all_services:
            result[v.id] = appservice_to_obj(v)

        defer.returnValue((200, result))


def register_servlets(hs, http_server):
    AppservicesListServlet(hs).register(http_server)
