import discord, datetime, os

app = discord.Client(intents=discord.Intents.all())
event = app.event
admin = [410763741786013697, 671868944440623164]
activity = discord.Activity
activitytype = discord.ActivityType
color = discord.Colour

@event
async def on_ready():
    print(f"{app.user} ({app.user.id}) 로 접속 성공.")
    await app.change_presence(activity=discord.Activity(type=activitytype.playing, name="Temporarily undergoing"), status=dnd)

token = os.environ['TOKEN']
app.run(token)
