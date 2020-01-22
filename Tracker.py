import datetime, json
class Tracker:
    def __init__(self):
        self.moodFile = json.loads(open('moodData.json').read())
        
    def add(self):
        event = input('what happened:   ' )
        date = str(datetime.datetime.now())
        value = int(input('give it a score: '))
        self.moodFile.update(
            {
                date:{
                    event: value
                }
            }
        )
        
    def save(self):
        with open('moodData.json', 'w') as saveFile:
            saveFile.write(
                json.dumps(
                    self.moodFile,
                    indent = 2,
                    sort_keys = True
                )
            )
            
if __name__ == '__main__':
    myTracker = Tracker()
    myTracker.add()
    myTracker.save()
