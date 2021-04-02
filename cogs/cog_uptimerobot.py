import console
import datetime
import discord
from discord.ext import commands
import os
import requests
import getFriendlyNames


uptimeRobotRootEndpoint = "https://api.uptimerobot.com/v2"


class UptimeRobot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='getMonitors', aliases=['gm'])
    async def getMonitors(self, ctx):
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

        print(friendly_names)
        print(statuses)

        fields = [
            {
                "name": "**Monitor Title**",
                "value": self.stringifyValues(friendly_names),
            },
            {
                "name": "**Status**",
                "value": self.stringifyValues(statuses),
            }
        ]

        for field in fields:
            if field['value']:
                embed.add_field(name=field['name'],
                                value=field['value'],
                                inline=True)

        await ctx.send(embed=embed)


    '''
    Retrieves information for GET commands in the UptimeRobot API
    '''
    async def fetch(self, APIFunction):
        url = "{}/{}".format(uptimeRobotRootEndpoint, APIFunction)
        payload = "api_key={}&format=json".format(os.environ.get('uptimeRobotToken'))
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
        
        console.log(arr, 'no_decorator')
        return arr

    def stringifyValues(self, inputData):
        print(inputData)
        output = ""
        counter = 0
        for item in inputData:
            counter += 1
            output = output + item + '\n'
        return output


            

    @commands.command(name='createMonitor', aliases=['cm'])
    async def createMonitor(self, ctx):
        await self.commandNotImplemented('createMonitor')

    @commands.command(name='getAlertContacts', aliases=['gac'])
    async def getAlertContacts(self, ctx):
        await self.commandNotImplemented(ctx, 'getAlertContacts')

    async def commandNotImplemented(self, ctx, commandName):
        await ctx.send(f'`Command: {commandName} response not yet implemented.`')

        
        



"""
url = "{}/newMonitor".format(apiRootURL)
  payloadAttributes = [APIKey, friendlyName, monitorURL]
  encodedAttributes = []

  console.info("Encoding Payload Attributes")
  for attribute in payloadAttributes:
    encodedAttributes.append(query.encode(attribute))
  
  payload = "api_key={}&format=json&type=1&url={}&friendly_name={}".format(encodedAttributes[0], encodedAttributes[2], encodedAttributes[1])
  headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
  }

  console.info("Sending Payload")
  response = requests.request("POST", url, data=payload, headers=headers)
  
  json_data = json.loads(response.text)
  print(response.text)
  output.generate(json_data)

"""


def setup(bot):
	bot.add_cog(UptimeRobot(bot))
