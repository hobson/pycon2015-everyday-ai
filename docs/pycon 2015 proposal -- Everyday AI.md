Description
-----------

We are surrounded by AI that is designed by others. Often technology and automation are exercising influence over us for someone else's benefit, ignoring our own values.  Python and a new breed of customizable apps is changing that.  Take control of your own personal and professional development by building a chat bot to help you. 

Audience
--------

Quantified self, AI, and machine learning enthusiasts. Any python developer excited about automating an aspect of their workflow or personal life.

Objectives
----------

1. Increase awareness of several natural language processing packages `nltk`, `fuzzywuzzy`, `regex`, `pug`, and `will`
2. Spread awarenes of the state of the art in AI for chat bots and personal digital assistants.
3. Inspire developers to apply their expertise to self improvement, productivity enhancement, and social cooperation. 

Detailed Abstract
-----------------

This talk will demonstrate how surprisingly simple rules, in the form of a few lines of python code, can produce complex behavior with the power to influence the way you live your life, your work flow, or steer a whole community of developers within your organization. This influence is designed by you, so it pushes you in a direction that reflects *your* values and will, rather than that of a person or organization that may not have your best interests at heart.

This talk will bring together several open source projects to produce a surprisingly useful AI agent for supporting developers in their everyday life and system administration tasks at work. Attendees will learn how to combine the off-the-shelf modules `nltk` and [`pug`](http://github.com/pug/pug) (and their component packages) with the pluggable open source chat bot [`will`](http://github.com/skockzen/will) to produce a customized, friendly, interesting chat bot that can respond to natural queries and commands such as 

    "@WillBot what is the python command to read keyboard input from the user?"

or

    "@WillBot what did I chat about most last month?"

or

    "@Willbot remind me to take out the trash on Monday mornings." 

The chat bot will also be able to spontaneously offer advice and support.

    "@Pythonista, You've sure been busy today, when are you going to take a break for that 5 minute stretch you promised?"


Outline
-------

1. (5 min) Audience survey for skill level and interest
2. (5 min) Introduction to existing implementations of `will` in dev ops environments
3. (7 min) Introduction to `NLTK` and `pug` and their uses for natural language processing

    a. `NTLK` for text parsing and Part of Speech tagging
    b. `pug` with `fuzzywuzzy` and `regex` for fuzzy string matching
    c.  `pug` with dateutils for parsing of natural language datetimes like "next Monday"

4. (10 min) Architect and build a `will` plugin to add customized functionality appropriate for python software development, and developer team-building

    a. recurring reminders for future network or server maintenance tasks "@ChatBot: Remind me to check on server xyz every Monday morning."
    b. help finding python libraries and pypi packages: "@ChatBot: Is there a pypi package or github repository that implements a physics engine?"

5. (3 min) Wrap up and credits to open source projects, mainly [will](github.com/skoczen/will) 


Additional Notes
----------------

Instructions for building plugins and examples that incorporate the regex package are available at [this fork of the will repository](https://github.com/hobson/will/)

All slides and code presented during the talk will be provided at a [github repo](http://github.com/hobson/pycon2015-everyday-ai)