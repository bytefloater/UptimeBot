import console
import datetime
import discord
from discord.ext import commands
import os
import requests
import getFriendlyNames
import json

uptimeRobotRootEndpoint = "https://api.uptimerobot.com/v2"


class UptimeRobot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    '''
    Retrieves monitor info and returns embed to discord
    '''
    @commands.command(name='getMonitors', aliases=['gm'])
    async def getMonitors(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed()
        embed.title = 'Monitor Information'
        embed.timestamp = datetime.datetime.now()

        monitors = await self.fetch('getMonitors')
        monitors = monitors.json()['monitors']
        console.log('Response Received')

        friendly_names = self.concatResponses(monitors, 'friendly_name')
        statuses = self.concatResponses(monitors, 'status')
        for status in range(len(statuses)):
            statuses[status] = getFriendlyNames.monitorStatus(statuses[status])

        #console.log(friendly_names, 'no_decorator')
        #console.log(statuses, 'no_decorator')

        fields = [{
            "name": "**Monitor Title**",
            "value": self.stringifyValues(friendly_names),
        }, {
            "name": "**Status**",
            "value": self.stringifyValues(statuses),
        }]

        for field in fields:
            if field['value']:
                embed.add_field(name=field['name'],
                                value=field['value'],
                                inline=True)

        await ctx.send(embed=embed)


    '''
    Retrieves account info and returns embed to discord
    '''
    @commands.command(name='getAccountInfo', aliases=['gai', 'gad'])
    async def getAccountInfo(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed()
        embed.title = 'Account Information'
        embed.timestamp = datetime.datetime.now()

        accountInfo = await self.fetch('getAccountDetails')
        accountInfo = accountInfo.json()['account']
        console.log('Response Received')
        print(json.dumps(accountInfo, indent=4))

        fields = [
            {
                "name": "**Email Address**",
                "value": accountInfo['email'].split('@')[0][0] + "\*\*\*\*\*\*\*@" + accountInfo['email'].split('@')[1],
                "inline": False
            },
            {
                "name": "**Up Monitors**",
                "value": str(accountInfo['up_monitors']),
                "inline": True
            },
            {
                "name": "**Down Monitors**",
                "value": str(accountInfo['down_monitors']),
                "inline": True
            },
            {
                "name": "**Paused Monitors**",
                "value": str(accountInfo['paused_monitors']),
                "inline": True
            },
            {
                "name": "**Monitor Interval**",
                "value": str(accountInfo['monitor_interval']),
                "inline": True
            },
            {
                "name": "**SMS Credits**",
                "value": str(accountInfo['sms_credits']),
                "inline": True
            },
        ]
        for field in fields:
            if field['value']:
                embed.add_field(name=field['name'],
                                value=field['value'],
                                inline=field['inline'])

        await ctx.send(embed=embed, delete_after=20)


    '''
    Retrieves Public Status Pages (PSPs) and returns embed to discord
    '''
    @commands.command(name='getStatusPages', aliases=['getPSPs'])
    async def getStatusPages(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed()
        embed.title = 'Status Pages'
        embed.timestamp = datetime.datetime.now()

        statusPages = await self.fetch('getPSPs')
        statusPages = statusPages.json()['psps']
        console.log('Response Received')
        print(json.dumps(statusPages, indent=4))


        friendly_names = self.concatResponses(statusPages, 'friendly_name')
        statuses = self.concatResponses(statusPages, 'status')
        for status in range(len(statuses)):
            statuses[status] = getFriendlyNames.pspStatus(statuses[status])

        fields = [
            {
                "name": "**Friendly Name**",
                "value": self.stringifyValues(friendly_names),
                "inline": True
            },
            {
                "name": "**Status**",
                "value": self.stringifyValues(statuses),
                "inline": True
            }
        ]

        for field in fields:
            if field['value']:
                embed.add_field(name=field['name'],
                                value=field['value'],
                                inline=field['inline'])

        await ctx.send(embed=embed)
















    '''
    Retrieves information for GET commands in the UptimeRobot API
    '''
    async def fetch(self, APIFunction):
        url = "{}/{}".format(uptimeRobotRootEndpoint, APIFunction)
        payload = "api_key={}&format=json".format(
            os.environ.get('uptimeRobotToken'))
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        console.log(f'Fetching Information: {url}')
        return response

    def concatResponses(self, inputData, field):
        arr = []
        for i in range(len(inputData)):
            arr.append(str(inputData[i][field]))

        console.log(f'Extracting values for: {field}')
        console.log(arr, 'no_decorator')
        return arr

    def stringifyValues(self, inputData):
        output = ""
        for item in inputData:
            output = output + item + '\n'  # Discord will ignore the final return.
        return output

    def redactEmail(self, inputData):
        return

    @commands.command(name='authTest')
    async def authTest(self, ctx):
        await ctx.message.delete()
        authorID = ctx.message.author.id

        if str(authorID) == os.environ.get('discordAuthorID'):
            await ctx.send('Authorised')
            #return True
        else:
            await ctx.send('You are not authorised')
            #return False

    @commands.command(name='createMonitor', aliases=['cm'])
    async def createMonitor(self, ctx):
        await self.commandNotImplemented(ctx, 'createMonitor')

    @commands.command(name='getAlertContacts', aliases=['gac'])
    async def getAlertContacts(self, ctx):
        await self.commandNotImplemented(ctx, 'getAlertContacts')

    async def commandNotImplemented(self, ctx, commandName):
        await ctx.message.delete()
        await ctx.send(f'`Command: {commandName} response not yet implemented.`')



def setup(bot):
    bot.add_cog(UptimeRobot(bot))
