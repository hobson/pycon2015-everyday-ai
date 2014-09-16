from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from will import settings

class GoldStarPlugin(WillPlugin):

    @respond_to("award (?P<num_stars>\d)+ gold stars? to (?P<user_name>.*)")
    def gold_stars(self, message, num_stars=1, user_name=None):
        """award ___ gold stars to ___: Give someone gold stars."""
        stars = self.load("gold_stars", {})
        if user_name in stars:
            stars[user_name] += num_stars
        else:
            stars[user_name] = num_stars

        self.save("gold_stars", stars)

        self.say("Awarded %s stars to %s." % (num_stars, user_name), message=message)
        if hasattr(settings,"GOLD_STAR_URL"):
            self.say(settings.GOLD_STAR_URL, message=message)
