from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from will import settings

class CodeFlowPlugin(WillPlugin):

    @respond_to("CR (?:for )?(?P<pr_id>\d*)$")
    def cr(self, message, pr_id):
        """cr ___: Post a link to GK CR #___""" 
        self.say("@all (crrequest) https://github.com/greenkahuna/scrapbin/pull/%s" % pr_id, message=message)

    @respond_to("CR (?:for )?(?P<pr_id>\d*) g2g$")
    def cr_g2g(self, message, pr_id):
        """cr ___ g2g: CR for ___ is good to go"""
        self.say("Thanks! (crpass) for %s" % pr_id, message=message)
        self.say("@all (frrequest) https://github.com/greenkahuna/scrapbin/pull/%s" % pr_id, message=message)

    @respond_to("FR (?:for )?(?P<pr_id>\d*)$")
    def fr(self, message, pr_id):
        """fr ___: Post a link to GK FR #___""" 
        self.say("@all (frrequest) https://github.com/greenkahuna/scrapbin/pull/%s" % pr_id, message=message)

    @respond_to("FR (?:for )?(?P<pr_id>\d*) g2g$")
    def fr_g2g(self, message, pr_id):
        """fr ___ g2g: FR for ___ is good to go"""
        self.say("Thanks! @all (frpass) for %s" % pr_id, message=message)
