from __future__ import print_function

import json

from lib.structures.Recommendation import Recommendation
from lib.api import Sheets


if __name__ == '__main__':
    with open('config.json') as config_file:
        config_data = json.load(config_file)
        Sheets.REC_SPREADSHEET_ID = config_data['spreadsheet_id']
        Sheets.REC_RANGE_NAME = config_data['all_range']

    Sheets.init_service()
    values = Sheets.read_sheet()
    for row in values:
        print(row)
        rec = Recommendation.from_entry(row)
        print(rec)
        print(rec.interpret_requesters())
        rec.add_requester("test_name123")
        print(rec)
