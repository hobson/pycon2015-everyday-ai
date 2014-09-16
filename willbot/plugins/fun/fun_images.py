from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class FunImagesPlugin(WillPlugin):

    @hear("high(-| )(5|five)")
    def hear_highfive(self, message):
        """high 5: Will's got spirit."""
        self.say("https://gk-will.s3.amazonaws.com/highfive.jpg", message=message)

    @hear(" a bug[^A-z]")
    def hear_bug(self, message):
        self.say("https://gk-will.s3.amazonaws.com/bugfeature.gif", message=message)

    @hear("(?i)i .* love (it|this|that)")
    def hear_i_love_it(self, message):
        self.say("https://gk-will.s3.amazonaws.com/omgilovethisstick.jpg", message=message)
