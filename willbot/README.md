
This is our bot, a [https://github.com/skoczen/will](will) bot.


Verifying environment...
ERROR: WILL_USERNAME... missing!
  To obtain a WILL_USERNAME: 
  1. Go to hipchat, and create a new user for will.
  2. Log into will, and go to Account settings>XMPP/Jabber Info.
  3. On that page, the 'Jabber ID' is the value you want to use.
  
  To set your WILL_USERNAME:
  1. On your local machine, add this to your virtual environment's bin/postactivate file:
     export WILL_USERNAME=YOUR_ACTUAL_WILL_USERNAME
  2. If you've deployed will on heroku, run
     heroku config:set WILL_USERNAME=YOUR_ACTUAL_WILL_USERNAME
  
ERROR: WILL_PASSWORD... missing!
  To obtain a WILL_PASSWORD: 
  1. Go to hipchat, and create a new user for will.  Note that password - this is the value you want.  It's used for signing in via XMPP.
  
  To set your WILL_PASSWORD:
  1. On your local machine, add this to your virtual environment's bin/postactivate file:
     export WILL_PASSWORD=YOUR_ACTUAL_WILL_PASSWORD
  2. If you've deployed will on heroku, run
     heroku config:set WILL_PASSWORD=YOUR_ACTUAL_WILL_PASSWORD
  
ERROR: WILL_V2_TOKEN... missing!
  To obtain a WILL_V2_TOKEN: 
  1. Log into hipchat using will's user.
  2. Go to https://your-org.hipchat.com/account/api
  3. Create a token.
  4. Copy the value - this is the WILL_V2_TOKEN.
  
  To set your WILL_V2_TOKEN:
  1. On your local machine, add this to your virtual environment's bin/postactivate file:
     export WILL_V2_TOKEN=YOUR_ACTUAL_WILL_V2_TOKEN
  2. If you've deployed will on heroku, run
     heroku config:set WILL_V2_TOKEN=YOUR_ACTUAL_WILL_V2_TOKEN
