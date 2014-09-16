from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class HelloPlugin(WillPlugin):

    @respond_to("^hello")
    def hello(self, message):
        self.reply(message, "hi!")
    