import discord, datetime, os, youtube_dl

app = discord.Client(intents=discord.Intents.all())
event = app.event
admin = [410763741786013697, 671868944440623164]
activity = discord.Activity
activitytype = discord.ActivityType
color = discord.Colour

@event
async def on_ready():
    print(f"{app.user} ({app.user.id}) 로 접속 성공.")

@event
async def on_message(message):
    content = message.content
    command = content.startswith
    author = message.author
    channel = message.channel
    cmds = ["&clear", "&clean", "&접속", "&setstatus", "&setactivity", "&setpresence", "&도움", "&도움말", "&정보", "&모바일정보", "&서버정보", "&채널정보", "&log", "&logs"]

    if command("&clear") or command("&clean"):
        if author.id in admin:
            if app.guilds[0].get_member(app.user.id).guild_permissions.manage_messages:
                if int(content[7:]) > 0:
                    await message.delete()
                    await channel.purge(limit=int(content[7:]))
                    embed = discord.Embed(title=f"명령 처리 성공", description=f"<#{channel.id}> 에서 {content[7:]} 개의 메세지를 성공적으로 제거하였습니다.", color=color.green())
                    await channel.send(f"{author.mention}", embed=embed)
                    return 0
                else:
                    embed = discord.Embed(title="명령 처리 실패", description=f"<#{channel.id}> 에서 {content[7:]} 개의 메세지를 제거하는데 실패하였습니다.", color=color.red())
                    embed.add_field(name="원인", value="1개 미만의 채팅은 제거할 수 없습니다.")
                    await channel.send(f"{author.mention}", embed=embed)
                    return 0
            else:
                embed = discord.Embed(title="명령 처리 실패", description=f"<#{channel.id}> 에서 메세지를 제거하는데 실패하였습니다.", color=color.red())
                embed.add_field(name="원인", value="메세지 관리 권한이 없어 제거할 수 없습니다.")
                await channel.send(f"{author.mention}", embed=embed)
                return 0
        else:
            embed = discord.Embed(title="명령 처리 실패", description=f"<#{channel.id}> 에서 메세지를 제거하는데 실패하였습니다.", color=color.red())
            embed.add_field(name="원인", value=f"{author.mention} 님은 이 명령어를 사용할 수 있는 권한이 없습니다.")
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&log") or command("&logs"):
        if author.id in admin:
            embed = discord.Embed(title="Heroku Log", description="[Open](https://dashboard.heroku.com/apps/alphabot/logs)", color=color.purple())
            await author.send(f"{author.mention}", embed=embed)
            return 0
        else:
            embed = discord.Embed(title="명령 처리 실패", description=f"<#{channel.id}> 에서 메세지를 제거하는데 실패하였습니다.", color=color.red())
            embed.add_field(name="원인", value=f"{author.mention} 님은 이 명령어를 사용할 수 있는 권한이 없습니다.")
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&도움") or command("&도움말"):
        embed = discord.Embed(title="Alphabot", color=color.gold())
        embed.add_field(name="Supports", value="Alphabot에 대한 지원을 받을 수 있는 곳입니다.\n[Discord](http://disgd.gbgs.kro.kr)\n[KakaoTalk](https://open.kakao.com/me/alpha_0903)\n[GitHub](https://github.com/alphaimetal0903/Alphabot)", inline=True)
        embed.add_field(name="Utilities", value="&정보 <멤버> | 지정한 멤버에 대한 정보를 출력합니다.\n  설정하지 않았을 경우 자신의 정보를 엽니다.\n  모바일의 경우 정상적으로 출력되지 않을 경우 &모바일정보 <멤버> 를 사용하세요.", inline=True)
        await channel.send(f"{author.mention}", embed=embed)
        return 0

    if command("&help"):
        if author.id in admin:
            embed = discord.Embed(title="Alphabot", color=color.purple())
            embed.add_field(name="Supports", value="Alphabot에 대한 지원을 받을 수 있는 곳입니다.\n[Discord](http://disgd.gbgs.kro.kr)\n[KakaoTalk](https://open.kakao.com/me/alpha_0903)\n[GitHub](https://github.com/alphaimetal0903/Alphabot)", inline=True)
            embed.add_field(name="Utilities", value="&정보 <멤버> | 지정한 멤버에 대한 정보를 출력합니다.\n  설정하지 않았을 경우 자신의 정보를 엽니다.\n  모바일의 경우 정상적으로 출력되지 않을 경우 &모바일정보 <멤버> 를 사용하세요.", inline=True)
            embed.add_field(name="Admin Tools", value="&setactivity <activity> <details> | activity = play(ing) or gam(e|ing), listen(ing), watch(ing), none\n&setstatus <status> | status = online, idle, dnd or do_not_distrub, offline or invisible or vanish\n&help\n&log(s)", inline=True)
            await author.send(f"{author.mention}", embed=embed)
            return 0
        else:
            embed = discord.Embed(title="명령 처리 실패", description=f"도움말을 출력하는데 실패했습니다.", color=color.red())
            embed.add_field(name="원인", value="`&help`는 올바르지 않은 도움말 요청문입니다.")
            embed.add_field(name="해결 방법", value="`&도움` 또는 `&도움말` 을 사용하세요.")
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&setstatus"):
        preactivity = app.guilds[0].get_member(app.user.id).activity
        if author.id in admin:
            status = content[11:]

            if status == "online":
                await app.change_presence(status=discord.Status.online, activity=preactivity)
                embed = discord.Embed(title="명령 처리 성공", description="Status를 성공적으로 `Online` 으로 변경하였습니다.", color=color.green())
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if status == "idle" or status == "idling":
                await app.change_presence(status=discord.Status.idle, activity=preactivity)
                embed = discord.Embed(title="명령 처리 성공", description="Status를 성공적으로 `Idle` 로 변경하였습니다.", color=color.green())
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if status == "dnd" or status == "do-not-distrub" or status == "do_not_distrub":
                await app.change_presence(status=discord.Status.dnd, activity=preactivity)
                embed = discord.Embed(title="명령 처리 성공", description="Status를 성공적으로 `Do Not Distrub` 로 변경하였습니다.", color=color.green())
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if status == "offline" or status == "invisible" or status == "vanish":
                await app.change_presence(status=discord.Status.online, activity=preactivity)
                embed = discord.Embed(title="명령 처리 성공", description="Status를 성공적으로 `Offline(Invisible)` 으로 변경하였습니다.", color=color.green())
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            else:
                embed = discord.Embed(title="명령 처리 실패", description=f"Status를 `{status}` (으)로 변경하는 도중 문제가 발생하였습니다.", color=color.red())
                embed.add_field(name="원인", value=f"`{status}`는 존재하지 않는 StatusType 입니다.")
                await channel.send(f"{author.mention}", embed=embed)
                return 0

        else:
            embed = discord.Embed(title="명령 처리 실패", description="Status를 변경하는 도중 문제가 발생하였습니다.", color=color.red())
            embed.add_field(name="원인", value=f"{author.mention} 님은 이 명령어를 사용할 수 있는 권한이 없습니다.")
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&setactivity") or command("&setpresence"):
        prestatus = app.guilds[0].get_member(app.user.id).status
        preactivity = app.guilds[0].get_member(app.user.id).activity
        if author.id in admin:
            argument = content[13:].split(" ", 1)
            type = argument[0]
            playing = ["playing", "gaming", "play", "game"]
            null = ["null", "none", "disable", "false", "off"]

            if type in playing:
                await app.change_presence(activity=activity(type=activitytype.playing, name=argument[1]), status=prestatus)
                embed = discord.Embed(title="명령 처리 성공", description=f"Activity를 성공적으로 `Playing {argument[1]}` (으)로 변경하였습니다.", color=color.green())
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if type == "listening":
                await app.change_presence(activity=activity(type=activitytype.listening, name=argument[1]), status=prestatus)
                embed = discord.Embed(title="명령 처리 성공", description=f"Activity를 성공적으로 `Listening {argument[1]}` (으)로 변경하였습니다.", color=color.green())
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if type == "watching":
                await app.change_presence(activity=activity(type=activitytype.watching, name=argument[1]), status=prestatus)
                embed = discord.Embed(title="명령 처리 성공", description=f"Activity를 성공적으로 `Watching {argument[1]}` (으)로 변경하였습니다.", color=color.green())
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if type in null:
                await app.change_presence(activity=None, status=prestatus)
                embed = discord.Embed(title="명령 처리 성공", description=f"Activity를 성공적으로 `Nothing(None)` (으)로 변경하였습니다.", color=color.green())
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            else:
                embed = discord.Embed(title="명령 처리 실패", description="Activity를 변경하는 도중 문제가 발생하였습니다.", color=color.red())
                embed.add_field(name="원인", value=f"`{type}` 은(는) 존재하지 않는 ActivityType 입니다.")
                await channel.send(f"{author.mention}", embed=embed)

        else:
            embed = discord.Embed(title="명령 처리 실패", description="Status를 변경하는 도중 문제가 발생하였습니다.", color=color.red())
            embed.add_field(name="원인", value=f"{author.mention} 님은 이 명령어를 사용할 수 있는 권한이 없습니다.")
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&정보"):
        member = message.guild.get_member(int(content[7:25]))
        today = datetime.date.today()
        created = datetime.date(int(member.created_at.strftime('%Y')), int(member.created_at.strftime('%m')), int(member.created_at.strftime('%d')))
        created = today - created
        created = str(created).split(" ", 1)
        created = created[0]
        createddate = member.created_at.strftime('%Y년 %m월 %d일\n%p %I시 %M분 %S.%f초')
        joined = datetime.date(int(member.joined_at.strftime('%Y')), int(member.joined_at.strftime('%m')), int(member.joined_at.strftime('%d')))
        joined = today - joined
        joined = str(joined).split(" ", 1)
        joined = joined[0]
        joineddate = member.joined_at.strftime('%Y년 %m월 %d일\n%p %I시 %M분 %S.%f초')
        embed = discord.Embed(title=f"{member} 의 정보", color=member.color)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="계정 생성 일자", value=f"{createddate} \n생성한지 {created} 일 지남", inline=True)
        embed.add_field(name="서버 가입 일자", value=f"{joineddate} \n생성한지 {joined} 일 지남", inline=True)
        embed.add_field(name="현재 상태", value=str(member.status), inline=True)
        embed.add_field(name="현재 하는 중", value=str(member.activity), inline=True)
        await channel.send(f"{author.mention}", embed=embed)
        return 0

    if command("&모바일정보"):
        member = message.guild.get_member(int(content[9:27]))
        today = datetime.date.today()
        created = datetime.date(int(member.created_at.strftime('%Y')), int(member.created_at.strftime('%m')), int(member.created_at.strftime('%d')))
        created = today - created
        created = str(created).split(" ", 1)
        created = created[0]
        createddate = member.created_at.strftime('%Y년 %m월 %d일\n%p %I시 %M분 %S.%f초')
        joined = datetime.date(int(member.joined_at.strftime('%Y')), int(member.joined_at.strftime('%m')), int(member.joined_at.strftime('%d')))
        joined = today - joined
        joined = str(joined).split(" ", 1)
        joined = joined[0]
        joineddate = member.joined_at.strftime('%Y년 %m월 %d일\n%p %I시 %M분 %S.%f초')
        embed = discord.Embed(title=f"{member} 의 정보", color=member.color)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="계정 생성 일자", value=f"{createddate} \n생성한지 {created} 일 지남", inline=True)
        embed.add_field(name="서버 가입 일자", value=f"{joineddate} \n생성한지 {joined} 일 지남", inline=True)
        embed.add_field(name="현재 상태", value=str(member.status), inline=True)
        embed.add_field(name="현재 하는 중", value=str(member.activity), inline=True)
        await channel.send(f"{author.mention}", embed=embed)
        return 0

    else:
        if command("&"):
            if command not in cmds:
                embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
                embed.add_field(name="원인", value=f"{content} 은(는) 존재하지 않는 명령어입니다.", inline=False)
                embed.add_field(name="해결 방법", value="&도움 또는 &도움말을 입력해 명령어를 확인해보세요.")
                await channel.send(f"{author.mention}", embed=embed)
                return 0

token = os.environ['TOKEN']
app.run(token)