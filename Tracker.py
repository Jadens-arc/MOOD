import datetime, json
class Tracker:
    def __init__(self):
        self.moodFile = json.loads(open('moodData.json').read())
    def add(self):
        key = input('what happened:   ' )
        key = str(datetime.datetime.now()) + ' ' + key
        value = int(input('give it a score: '))
        self.moodFile.update({key: value})
    def save(self):
        with open('moodData.json') as saveFile:
            saveFile.write(str(json.dumps(self.moodFile)))

myTracker = Tracker()
myTracker.add()
myTracker.save()