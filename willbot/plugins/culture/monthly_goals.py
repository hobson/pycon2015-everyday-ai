from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from will import settings

class MonthlyGoalsPlugin(WillPlugin):

    @respond_to("Set (?:the )?monthly goals to (?P<goals>.*)", multiline=True)
    def set_goals(self, message, goals=""):
        """set the monthly goals to ___: Set our monthly goals."""
        print "goals: %s" % goals
        self.save("monthly_goals", goals)
        self.say("Got it.", message=message)

    @periodic(hour='9', minute='0', day_of_week="mon")
    def say_goals_on_monday(self):
        self.say_goals()

    @respond_to("^(?:What are the )?(?:monthly )?goals")
    def respond_to_goals_question(self, message):
        """what are the monthly goals?: Posts the monthly goals."""
        self.say_goals(message=message)


    def say_goals(self, message=None):
        goals = self.load("monthly_goals", False)
        if goals:
            self.say("@all our monthly goals:\n %s" % goals, message=message)
        else:
            self.say("No montly goals set.", message=message)
