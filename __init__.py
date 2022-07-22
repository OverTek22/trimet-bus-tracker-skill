from mycroft import MycroftSkill, intent_file_handler


class TrimetBusTracker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tracker.bus.trimet.intent')
    def handle_tracker_bus_trimet(self, message):
        self.speak_dialog('tracker.bus.trimet')


def create_skill():
    return TrimetBusTracker()

