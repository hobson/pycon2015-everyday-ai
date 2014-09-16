% title: Everyday AI
% subtitle: PyCon 2015, Montreal
% subtitle: <i><small>April 7, 2015</small></i>
% author: <a href="https://hobson.github.io/pycon2015-everyday-ai">hobson.github.io/pycon2015-everyday-ai</a>
% thankyou_details: A big shout out to Steven Skoczen and his awesome bot framework
% contact: <a href="http://github.com/skoczen/will">will</a>
% favicon: <img src="https://www.python.org/favicon.ico"/>

---
title: Audience Survey
build_lists: true

* Who has built a webapp before?
* Who has used regular expressions?
* Who has used fuzzy text matching?
* Who has built a chat bot before? 

---
title: Where Else Does Will Live?

* GreenKahuna used to employ will to develop software for the contracting industry
* I use a customized version GoodBot at SharpLabs to collaborate with other devlopers on our BigData project.


---
title: Some packages you should get to know

In addition to `will` we'll be using the following packages to make sense of the gibberish flowing in typical chatroom

* `NTLK` for text parsing and Part of Speech tagging
* `pug` with `fuzzywuzzy` and `regex` for fuzzy string matching
*  `pug` with dateutils for parsing of natural language datetimes like "next Monday"

---
title: Architecture of your bot

* select some open-source plugins appropriate for you application
* start a new plugin that accomplishes something simple but useful
* add fuzziness to your bot logic to imrpove robustness and unpredictability
* add statefulness (a persistent database) to give `willbot` some long term memory

---
title: Existing plugins can handle the following dialog

* recurring reminders for future network or server maintenance tasks

    "@ChatBot: Remind me to check on server xyz every Monday morning."

---
title: If you'd like a search-engine embedded in your chat room

* help finding python libraries and pypi packages: 

    "@ChatBot: Is there a pypi package or github repository that implements a physics engine?"

---
title: Wrap up and credits to open source projects

* A big thanks to the vibrant [will](github.com/skoczen/will) community
