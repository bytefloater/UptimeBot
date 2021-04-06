# UptimeRobot (Discord Bot)
This bot is a fork of the Discord.py bot template making use of the commands extension and [cogs](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html). It will integrate with the UptimeRobot API to allow the end-user to manage their Uptime and Monitor status through Discord.


## Pre-configuration
To use this bot, if you don't already have a Discord Bot you will be required to create an application on the [Discord Developer Portal](https://discordapp.com/developers/).

Enter your new application and under the bots section, select "Add Bot". When prompted for confirmation, select "Yes, do it!"

![Left panel](/webserver/static/images/Bots-1.png)

Once the bot account is created, you will need to copy its token.
![](/webserver/static/images/Bots-2.png)


## Setup
Create a file named `.env`

Your .env file should look something like this:
```
discordBotToken=<botToken>
discordAuthorID=<yourDiscordID>
discordWebHookURL=<discordWebHookURL>

requestSecret=<yourAuthSecret>
uptimeRobotToken=<uptimeRobotAPIToken>
```
When you hit start everything should startup fine.



## Uptime
Projects made on the Repl.it Free Plan will only stay running 1 hour after the last request was made so additional steps are needed to keep the bot online permenantly. To achieve constant uptime you will need to step up a ping to the Flask Web Server approximately every 5 minutes.

Go to [UptimeRobot](https://uptimerobot.com/) and create an accout, if you dont have one.  After verifying your account, click "Add New Monitor".

+ For Monitor Type select "HTTP(s)"
+ In Friendly Name put the name of your bot
+ For your url, put the url of the website made for your repl.
+ Select any alert contacts you want, then click "Create Monitor" 
![Uptime robot example](https://i.imgur.com/Qd9LXEy.png)

## Documentation

+ For all embed parametes, see the [Discord Webhook Documentation](https://discordapp.com/developers/docs/resources/webhook#execute-webhook)
+ For the API Documentation, visit the [UptimeRobot RESET API Docs](https://uptimerobot.com/api).
