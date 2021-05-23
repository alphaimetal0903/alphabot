import discord, datetime, os, asyncio, time, bs4, youtube_dl, selenium, discord.utils
from selenium import webdriver
from bs4 import *
from discord.utils import *

app = discord.Client(intents=discord.Intents.all())
event = app.event
admin = [410763741786013697, 671868944440623164]
activity = discord.Activity
activitytype = discord.ActivityType
color = discord.Colour

@event
async def on_ready():
    print(f"{app.user} ({app.user.id}) 로 접속 성공.")
    print(os.getcwd())

@event
async def on_message(message):
    content = message.content
    command = content.startswith
    author = message.author
    channel = message.channel
    guild = message.guild
    now = datetime.datetime.now().strftime('%Y년 %m월 %d일 %p %I시 %M분 %S.%f초')
    ver = "210522a"
    emfoot = f"By Alpha_#0903, Version {ver} ({now})"
    cmds = ["&clear", "&clean", "&접속", "&setstatus", "&setactivity", "&setpresence", "&도움", "&도움말", "&정보", "&모바일정보", "&서버정보", "&길드정보", "&채널정보", "&log", "&logs"]

    try:
        guild.id
    except AttributeError:
        return 0

    if command("&clear") or command("&clean"):
        if author.id in admin:
            if app.guilds[0].get_member(app.user.id).guild_permissions.manage_messages:
                if int(content[7:]) > 0:
                    await message.delete()
                    await channel.purge(limit=int(content[7:]))
                    embed = discord.Embed(title=f"명령 처리 성공", description=f"<#{channel.id}> 에서 {content[7:]} 개의 메세지를 성공적으로 제거하였습니다.", color=color.green())
                    embed.set_footer(text=emfoot)
                    await channel.send(f"{author.mention}", embed=embed)
                    return 0
                else:
                    embed = discord.Embed(title="명령 처리 실패", description=f"<#{channel.id}> 에서 {content[7:]} 개의 메세지를 제거하는데 실패하였습니다.", color=color.red())
                    embed.add_field(name="원인", value="1개 미만의 채팅은 제거할 수 없습니다.")
                    embed.set_footer(text=emfoot)
                    await channel.send(f"{author.mention}", embed=embed)
                    return 0
            else:
                embed = discord.Embed(title="명령 처리 실패", description=f"<#{channel.id}> 에서 메세지를 제거하는데 실패하였습니다.", color=color.red())
                embed.add_field(name="원인", value="메세지 관리 권한이 없어 제거할 수 없습니다.")
                embed.set_footer(text=emfoot)
                await channel.send(f"{author.mention}", embed=embed)
                return 0
        else:
            embed = discord.Embed(title="명령 처리 실패", description=f"<#{channel.id}> 에서 메세지를 제거하는데 실패하였습니다.", color=color.red())
            embed.add_field(name="원인", value=f"{author.mention} 님은 이 명령어를 사용할 수 있는 권한이 없습니다.")
            embed.set_footer(text=emfoot)
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&log") or command("&logs"):
        if author.id in admin:
            embed = discord.Embed(title="Heroku Log", description="[Open](https://dashboard.heroku.com/apps/alphabotpyc/logs)", color=color.purple())
            embed.set_footer(text=emfoot)
            await author.send(f"{author.mention}", embed=embed)
            return 0
        else:
            embed = discord.Embed(title="명령 처리 실패", description=f"<#{channel.id}> 에서 메세지를 제거하는데 실패하였습니다.", color=color.red())
            embed.add_field(name="원인", value=f"{author.mention} 님은 이 명령어를 사용할 수 있는 권한이 없습니다.")
            embed.set_footer(text=emfoot)
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&도움") or command("&도움말"):
        embed = discord.Embed(title="Alphabot", color=color.gold())
        embed.add_field(name="Supports", value="Alphabot에 대한 지원을 받을 수 있는 곳입니다.\n[Discord](http://disgd.gbgs.kro.kr)\n[KakaoTalk](https://open.kakao.com/me/alpha_0903)\n[GitHub](https://github.com/alphaimetal0903/Alphabot)", inline=True)
        embed.add_field(name="Utilities", value="&정보 <멤버> | 지정한 멤버에 대한 정보를 출력합니다.\n  설정하지 않았을 경우 자신의 정보를 출력합니다.\n&서버정보 | 현재 서버에 대한 정보를 출력합니다.", inline=True)
        embed.set_footer(text=emfoot)
        await channel.send(f"{author.mention}", embed=embed)
        return 0

    if command("&help"):
        if author.id in admin:
            embed = discord.Embed(title="Alphabot", color=color.purple())
            embed.add_field(name="Supports", value="Alphabot에 대한 지원을 받을 수 있는 곳입니다.\n[Discord](http://disgd.gbgs.kro.kr)\n[KakaoTalk](https://open.kakao.com/me/alpha_0903)\n[GitHub](https://github.com/alphaimetal0903/Alphabot)", inline=True)
            embed.add_field(name="Utilities", value="&정보 <멤버> | 지정한 멤버에 대한 정보를 출력합니다.\n  설정하지 않았을 경우 자신의 정보를 출력합니다.\n&서버정보 | 현재 서버에 대한 정보를 출력합니다.", inline=True)
            embed.add_field(name="Admin Tools", value="&setactivity <activity> <details> | activity = play(ing) or gam(e|ing), listen(ing), watch(ing), none\n&setstatus <status> | status = online, idle, dnd or do_not_distrub, offline or invisible or vanish\n&help\n&log(s)", inline=True)
            embed.set_footer(text=emfoot)
            await author.send(f"{author.mention}", embed=embed)
            return 0
        else:
            embed = discord.Embed(title="명령 처리 실패", description=f"도움말을 출력하는데 실패했습니다.", color=color.red())
            embed.add_field(name="원인", value="`&help`는 올바르지 않은 도움말 요청문입니다.")
            embed.add_field(name="해결 방법", value="`&도움` 또는 `&도움말` 을 사용하세요.")
            embed.set_footer(text=emfoot)
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&setstatus"):
        preactivity = app.guilds[0].get_member(app.user.id).activity
        if author.id in admin:
            status = content[11:]

            if status == "online":
                await app.change_presence(status=discord.Status.online, activity=preactivity)
                embed = discord.Embed(title="명령 처리 성공", description="Status를 성공적으로 `Online` 으로 변경하였습니다.", color=color.green())
                embed.set_footer(text=emfoot)
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if status == "idle" or status == "idling":
                await app.change_presence(status=discord.Status.idle, activity=preactivity)
                embed = discord.Embed(title="명령 처리 성공", description="Status를 성공적으로 `Idle` 로 변경하였습니다.", color=color.green())
                embed.set_footer(text=emfoot)
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if status == "dnd" or status == "do-not-distrub" or status == "do_not_distrub":
                await app.change_presence(status=discord.Status.dnd, activity=preactivity)
                embed = discord.Embed(title="명령 처리 성공", description="Status를 성공적으로 `Do Not Distrub` 로 변경하였습니다.", color=color.green())
                embed.set_footer(text=emfoot)
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if status == "offline" or status == "invisible" or status == "vanish":
                await app.change_presence(status=discord.Status.online, activity=preactivity)
                embed = discord.Embed(title="명령 처리 성공", description="Status를 성공적으로 `Offline(Invisible)` 으로 변경하였습니다.", color=color.green())
                embed.set_footer(text=emfoot)
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            else:
                embed = discord.Embed(title="명령 처리 실패", description=f"Status를 `{status}` (으)로 변경하는 도중 문제가 발생하였습니다.", color=color.red())
                embed.set_footer(text=emfoot)
                embed.add_field(name="원인", value=f"`{status}`는 존재하지 않는 StatusType 입니다.")
                await channel.send(f"{author.mention}", embed=embed)
                return 0

        else:
            embed = discord.Embed(title="명령 처리 실패", description="Status를 변경하는 도중 문제가 발생하였습니다.", color=color.red())
            embed.set_footer(text=emfoot)
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
                embed.set_footer(text=emfoot)
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if type == "listening" or type == "listen":
                await app.change_presence(activity=activity(type=activitytype.listening, name=argument[1]), status=prestatus)
                embed = discord.Embed(title="명령 처리 성공", description=f"Activity를 성공적으로 `Listening {argument[1]}` (으)로 변경하였습니다.", color=color.green())
                embed.set_footer(text=emfoot)
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if type == "watching" or type == "watch":
                await app.change_presence(activity=activity(type=activitytype.watching, name=argument[1]), status=prestatus)
                embed = discord.Embed(title="명령 처리 성공", description=f"Activity를 성공적으로 `Watching {argument[1]}` (으)로 변경하였습니다.", color=color.green())
                embed.set_footer(text=emfoot)
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            if type in null:
                await app.change_presence(activity=None, status=prestatus)
                embed = discord.Embed(title="명령 처리 성공", description=f"Activity를 성공적으로 `Nothing(None)` (으)로 변경하였습니다.", color=color.green())
                embed.set_footer(text=emfoot)
                await channel.send(f"{author.mention}", embed=embed)
                return 0

            else:
                embed = discord.Embed(title="명령 처리 실패", description="Activity를 변경하는 도중 문제가 발생하였습니다.", color=color.red())
                embed.set_footer(text=emfoot)
                embed.add_field(name="원인", value=f"`{type}` 은(는) 존재하지 않는 ActivityType 입니다.")
                await channel.send(f"{author.mention}", embed=embed)
                return 0

        else:
            embed = discord.Embed(title="명령 처리 실패", description="Status를 변경하는 도중 문제가 발생하였습니다.", color=color.red())
            embed.set_footer(text=emfoot)
            embed.add_field(name="원인", value=f"{author.mention} 님은 이 명령어를 사용할 수 있는 권한이 없습니다.")
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&정보"):
        if "!" in content[6:25]:
            member = guild.get_member(int(content[7:25]))
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
            embed.add_field(name="서버 가입 일자", value=f"{joineddate} \n접속한지 {joined} 일 지남", inline=True)
            embed.add_field(name="현재 상태", value=str(member.status), inline=True)
            embed.add_field(name="현재 하는 중", value=member.activity, inline=True)
            embed.set_footer(text=emfoot)
            await channel.send(f"{author.mention}", embed=embed)
            return 0
        if ">" in content[6:25]:
            member = guild.get_member(int(content[6:24]))
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
            embed.add_field(name="서버 가입 일자", value=f"{joineddate} \n접속한지 {joined} 일 지남", inline=True)
            embed.add_field(name="현재 상태", value=str(member.status), inline=True)
            embed.add_field(name="현재 하는 중", value=member.activity.name, inline=True)
            embed.set_footer(text=emfoot)
            await channel.send(f"{author.mention}", embed=embed)
            return 0
        else:
            member = author
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
            embed.add_field(name="서버 가입 일자", value=f"{joineddate} \n접속한지 {joined} 일 지남", inline=True)
            embed.add_field(name="현재 상태", value=str(member.status), inline=True)
            embed.add_field(name="현재 하는 중", value=str(member.activity), inline=True)
            embed.set_footer(text=emfoot)
            await channel.send(f"{author.mention}", embed=embed)
            return 0

    if command("&서버정보") or command("&길드정보"):
        today = datetime.date.today()
        created = datetime.date(int(guild.created_at.strftime('%Y')), int(guild.created_at.strftime('%m')), int(guild.created_at.strftime('%d')))
        created = today - created
        created = str(created).split(" ", 1)
        created = created[0]
        createddate = guild.created_at.strftime('%Y년 %m월 %d일\n%p %I시 %M분 %S.%f초')
        embed = discord.Embed(title=f"{guild} 의 정보")
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_image(url=guild.banner_url)
        embed.set_footer(text=emfoot)
        embed.add_field(name="OWNER", value=f"{guild.owner.mention}")
        embed.add_field(name="생성 날짜", value=f"{createddate} \n생성한지 {created} 일 지남")
        embed.add_field(name="멤버 수", value=f"총 {guild.member_count}/{guild.max_members} 명")
        embed.add_field(name="Nitro Server Boost", value=f"{guild.premium_subscription_count}개의 부스트 발견됨.\n{guild.premium_tier} 티어")
        embed.add_field(name="서버 위치", value=f"{guild.region}")
        embed.add_field(name="보안 레벨", value=f"{guild.verification_level}")
        await channel.send(f"{author.mention}", embed=embed)
        return 0

    # if command("&connect"):
    #     try:
    #         await author.voice.channel.connect()
    #     except AttributeError:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value=f"{author.mention} 님이 접속하신 음성 채널을 찾을 수 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="먼저 음성 채널에 접속한 후 다시 시도하세요.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #     except discord.errors.ClientException:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value=f"이미 <#{author.voice.channel.id}> 에 연결되어 있습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&disconnect` 를 사용하여 음성 채널에서 연결을 해제할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #     else:
    #         embed = discord.Embed(title="명령 처리 성공", description=f"<#{author.voice.channel.id}> 에 성공적으로 연결했습니다.", color=color.green())
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    # if command("&disconnect"):
    #     for vc in app.voice_clients:
    #         if vc.guild == guild:
    #             voice = vc
    #     try:
    #         await voice.disconnect()
    #     except:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="접속된 음성 채널을 찾을 수 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #     else:
    #         embed = discord.Embed(title="명령 처리 성공", description=f"성공적으로 연결을 해제했습니다.", color=color.green())
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    # if command("&재생"):
    #     for vc in app.voice_clients:
    #         if vc.guild == guild:
    #             vc = vc
    #
    #     try:
    #         vc.is_connected()
    #     except UnboundLocalError:
    #         await author.voice.channel.connect()
    #
    #     for vc in app.voice_clients:
    #         if vc.guild == guild:
    #             vc = vc
    #
    #     global entireText
    #     YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    #     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    #
    #     dir = os.getcwd()
    #     edgedriver_dir = f"{dir}/driver/msedgedriver.exe"
    #     options = webdriver.EdgeOptions()
    #     options.add_argument("headless")
    #     driver = webdriver.Edge(edgedriver_dir, options=options)
    #     driver.get(f"https://www.youtube.com/results?search_query={content[4:]}")
    #     source = driver.page_source
    #     bs = bs4.BeautifulSoup(source, 'lxml')
    #     entire = bs.find_all('a', {'id': 'video-title'})
    #     entireNum = entire[0]
    #     entireText = entireNum.text.strip()
    #     musicurl = entireNum.get('href')
    #     url = 'https://www.youtube.com'+musicurl
    #     driver.quit()
    #
    #     with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    #         info = ydl.extract_info(url, download=False)
    #     URL = info['formats'][0]['url']
    #
    #     try:
    #         vc.play(discord.FFmpegPCMAudio(executable="C:/Program Files/FFmpeg/bin/ffmpeg.exe", source=URL, options=FFMPEG_OPTIONS))
    #     except UnboundLocalError:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="접속된 음성 채널을 찾을 수 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #     else:
    #         embed = discord.Embed(title="명령 처리 성공", description=f"재생을 시작합니다.", color=color.green())
    #         embed.add_field(name=f"{entireText}", value="By <channel>")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    # if command("&정지"):
    #     for vc in app.voice_clients:
    #         if vc.guild == guild:
    #             voice = vc
    #
    #     try:
    #         voice.is_playing()
    #     except UnboundLocalError:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="접속된 음성 채널을 찾을 수 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    #     if voice.is_playing():
    #         try:
    #             voice.stop()
    #         except:
    #             embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #             embed.add_field(name="원인", value="접속된 음성 채널을 찾을 수 없습니다.", inline=False)
    #             embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #             embed.set_footer(text=emfoot)
    #             await channel.send(f"{author.mention}", embed=embed)
    #             return 0
    #         else:
    #             embed = discord.Embed(title="명령 처리 성공", description=f"재생을 정지했습니다.", color=color.green())
    #             embed.set_footer(text=emfoot)
    #             await channel.send(f"{author.mention}", embed=embed)
    #             return 0
    #     else:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="재생 중인 영상을 찾을 수 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&재생` 을 사용하여 영상을 재생할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    # if command("&멈춰!"):
    #     for vc in app.voice_clients:
    #         if vc.guild == guild:
    #             voice = vc
    #
    #     try:
    #         voice.is_playing()
    #     except UnboundLocalError:
    #         embed = discord.Embed(title="**멈춰!** 실패", description="귀 폭력을 멈추는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="어디서 `멈춰!` 를 사용하는지 알수가 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    #     if voice.is_playing():
    #         try:
    #             voice.stop()
    #         except:
    #             embed = discord.Embed(title="**멈춰!** 실패", description="귀 폭력을 멈추는 도중 문제가 발생하였습니다.", color=color.red())
    #             embed.add_field(name="원인", value="어디서 `멈춰!` 를 사용하는지 알수가 없습니다.", inline=False)
    #             embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #             embed.set_footer(text=emfoot)
    #             await channel.send(f"{author.mention}", embed=embed)
    #             return 0
    #         else:
    #             embed = discord.Embed(title="**멈춰!** 성공", description=f"귀 폭력을 성공적으로 멈추고, 재생중이었던 음악을 `교무실`로 보냈습니다.", color=color.green())
    #             embed.set_footer(text=emfoot)
    #             await channel.send(f"{author.mention}", embed=embed)
    #             return 0
    #     else:
    #         embed = discord.Embed(title="**멈춰!** 실패", description="귀 폭력을 멈추는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="진행중인 귀 폭력이 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&재생` 을 영상을 재생할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    # if command("&일시정지"):
    #     for vc in app.voice_clients:
    #         if vc.guild == guild:
    #             voice = vc
    #
    #     try:
    #         voice.is_playing()
    #     except UnboundLocalError:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="접속된 음성 채널을 찾을 수 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    #     if voice.is_playing():
    #         try:
    #             voice.pause()
    #         except:
    #             embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #             embed.add_field(name="원인", value="접속된 음성 채널을 찾을 수 없습니다.", inline=False)
    #             embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #             embed.set_footer(text=emfoot)
    #             await channel.send(f"{author.mention}", embed=embed)
    #             return 0
    #         else:
    #             embed = discord.Embed(title="명령 처리 성공", description=f"재생을 일시 정지했습니다.", color=color.green())
    #             embed.set_footer(text=emfoot)
    #             await channel.send(f"{author.mention}", embed=embed)
    #             return 0
    #     else:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="재생 중인 영상을 찾을 수 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&재생` 을 사용하여 영상을 재생할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    # if command("&다시재생"):
    #     for vc in app.voice_clients:
    #         if vc.guild == guild:
    #             voice = vc
    #
    #     try:
    #         voice.is_paused()
    #     except UnboundLocalError:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="접속된 음성 채널을 찾을 수 없습니다.", inline=False)
    #         embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0
    #
    #     if voice.is_paused():
    #         try:
    #             voice.resume()
    #         except:
    #             embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #             embed.add_field(name="원인", value="접속된 음성 채널을 찾을 수 없습니다.", inline=False)
    #             embed.add_field(name="해결 방법", value="`&connect` 를 사용하여 음성 채널에 연결할 수 있습니다.")
    #             embed.set_footer(text=emfoot)
    #             await channel.send(f"{author.mention}", embed=embed)
    #             return 0
    #         else:
    #             embed = discord.Embed(title="명령 처리 성공", description=f"다시 재생합니다.", color=color.green())
    #             embed.set_footer(text=emfoot)
    #             await channel.send(f"{author.mention}", embed=embed)
    #             return 0
    #     else:
    #         embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
    #         embed.add_field(name="원인", value="일시 정지 된 영상을 찾을 수 없습니다.", inline=False)
    #         embed.set_footer(text=emfoot)
    #         await channel.send(f"{author.mention}", embed=embed)
    #         return 0

    else:
        if command("&"):
            embed = discord.Embed(title="명령 처리 실패", description="명령어를 처리하는 도중 문제가 발생하였습니다.", color=color.red())
            embed.add_field(name="원인", value=f"{content} 은(는) 존재하지 않는 명령어입니다.", inline=False)
            embed.add_field(name="해결 방법", value="&도움 또는 &도움말을 입력해 명령어를 확인해보세요.")
            embed.set_footer(text=emfoot)
            await channel.send(f"{author.mention}", embed=embed)
            return 0

token = os.environ['TOKEN']
app.run(token)