
willbot
=======

This instantiation of `will` called `willbot` was developed for the PyCon 2015 talk entitled "Everyday AI". The title comes from the fact that you'll probably want to interract with your version of `willbot` nearly every day. It'll watch out for you every day and night, if you wish. This `will` is the brain-child of the AI-assisted mind of Steven Skoczen and his community of developers on the [will project](https://github.com/skoczen/will). Their documentation is so good it could be called poetic, so I won't duplicate it here. And `will` is so easy to deploy and train, you might almost call it self-replicating (I'm sure the `will` team is working on that feature too).

Installation
------------

If you just want to *use* willbot, and you know how to use `pip`:

    pip install https://github.com/hobson/pycon2015-everyday-ai.git#egg=eai-master

But if you really want to have some fun, you'll want to put the source code somewhere more easily hacked up:

    git clone https://github.com/hobson/pycon2015-everyday-ai.git


Quick Start
-----------

If you want to use this willbot (or some frakenstein version of him that you've coded up here) you'll need to configure some environment variables. The key ones are:

`WILL_USERNAME` and `WILL_PASSWORD`

If you'd like willbot to keep you company in a HipChat room, he'll need an account there. Create a new user and find it's XMPP/Jabber ID under Account settings. The `Jabber ID` is the WILL_USERNAME and the password you selected is the WILL_PASSWORD

You'll also need to set the variable

`WILL_V2_TOKEN`

This allows willbot to find your room within your organization (even if it's just your personal account) and see when you're around. You can find the WILL_V2_TOKEN at `https://<your-org>.hipchat.com/account/api`

Ideally, all 3 of these environment variables should be set in your virtualenv postactivate script that is run just before you issue the `python run_will.py` command from the commandline.

