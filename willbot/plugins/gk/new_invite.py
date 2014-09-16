from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class NewInvitePlugin(WillPlugin):

    @route("/new-invite/")
    def new_invite_listener(self):
        from plugins.zoho_crm import ZohoCRMPlugin as ZohoClient
        print self.request.headers.__dict__
        new_invite_html = rendered_template("new_invite.html", self.request.query)
        self.say(new_invite_html, html=True)
        
        full_name = self.request.query.full_name
        phone = self.request.query.phone
        email = self.request.query.email
        business_name = self.request.query.business_name
        notes = self.request.query.notes

        response = ZohoClient.create_lead(full_name, phone, email, business_name, notes)

        if response:
            self.say('I just added %s to Zoho CRM Leads.' % full_name)
        else:
            self.say("Heads up, I couldn't add %s to Zoho CRM Leads." % full_name)

        return ""
