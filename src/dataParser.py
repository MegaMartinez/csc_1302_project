import os
import json
import datetime
import urllib.request as req
import pandas as pd # type: ignore

class enabledPlots:
    main: list[dict] = []
    bonus: list[dict] = []

class settings:
    database: str = None
    operations: str = None
    enabledPlots = enabledPlots()

def dataParser(args: settings, doFetch: bool) -> pd.DataFrame:
    jsonSettings: dict = json.load(open(os.path.join(os.path.dirname(__file__), '../res/settings.json'), 'r'))
    if(args.database == None):
        args.database = jsonSettings['database']
    if(args.operations == None):
        args.operations = jsonSettings['operations']
    if(args.enabledPlots != None):
        args.enabledPlots = enabledPlots()
        args.enabledPlots.main = jsonSettings['enabledPlots']['main']
        args.enabledPlots.bonus = jsonSettings['enabledPlots']['bonus']

    if(not os.path.exists(os.path.join(os.path.dirname(__file__), '../res/localData.json'))):
        updateData = {"lastUpdated": None}
    else:
        updateData = json.load(open(os.path.join(os.path.dirname(__file__), '../res/localData.json'), 'r'))

    if(not os.path.exists(os.path.join(os.path.dirname(__file__), '../res/data.csv')) 
        or updateData["lastUpdated"] == None
        or doFetch
    ):
        data = req.urlopen(jsonSettings['database'])
        open(os.path.join(os.path.dirname(__file__), '../res/data.csv'), 'wb').write(data.read())
        updateData["lastUpdated"] = datetime.datetime.now().isoformat()
        json.dump(updateData, open(os.path.join(os.path.dirname(__file__), '../res/localData.json'), 'w'), indent=4)

    df = pd.read_csv(open(os.path.join(os.path.dirname(__file__), '../res/data.csv'), 'r'))
    return df
