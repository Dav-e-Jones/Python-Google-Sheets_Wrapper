import string
from datetime import date


class Recommendation(object):
    def __init__(self, title, url="", requesters="Anonymous", picked=False, played=False):
        self.title = title
        self.url = url
        self.requesters = requesters
        self.picked = picked
        self.played = played

    def __str__(self):
        return "[ " + self.title + " | " + self.url + " | " + string.replace(self.requesters, "\n", "") + " | " + str(
            self.picked) + " | " + str(self.played) + " ]"

    @staticmethod
    def from_entry(entry):
        title = entry[0]
        url = entry[1]
        requesters = entry[2]
        picked = True if entry[3] == u"TRUE" else False
        played = True if entry[3] == u"TRUE" else False
        return Recommendation(title, url, requesters, picked, played)

    def add_requester(self, name):
        req_tuples = self.interpret_requesters()
        for req_tuple in req_tuples:
            if req_tuple[0].lower().strip() == name.lower().strip():
                return False
        day = date.today()
        day_string = day.strftime(u"%d/%m/%y")
        entry_string = name.strip() + u" " + u"(" + day_string + u"),\n"
        self.requesters += entry_string

    def _format_requesters(self):
        requesters_formatted = string.replace(self.requesters, "\n", "")
        return requesters_formatted.split(",")

    def interpret_requesters(self):
        ret_tuple = []
        requester_list = self._format_requesters()
        for requester in requester_list:
            if not requester:
                continue
            requester_entry = requester.split(" ")
            current_requester = requester_entry[0], requester_entry[1]
            ret_tuple.append(current_requester)
        return ret_tuple

    def spreadsheet_format(self):
        return [self.title, self.url, self.requesters, self.picked, self.played]
