import discord
from discord.ext import commands
from discord.utils import get
import os

import requests
from discord import Webhook, RequestsWebhookAdapter

import time as t
import random as ran
import json

from reqconcept1 import getreddit
from owoify.owoify import owoify
from emojifier import Emojifier
from keepalive import dorevive



print('hello world')

#print(getreddit('https://www.reddit.com/r/NoStupidQuestions/comments/qt2ntb/grandma_died_but_grandpa_doesnt_know_should_we/'))

import asyncio

clientuse=discord.Client()
client = commands.Bot(command_prefix='s')
shushbotid=888118494695153694

def emojify(textinput):
    with open('emoji.json','r',encoding="utf8") as f:
        mapping=json.load(f)
    emojiobj = Emojifier.of_custom_mappings(mapping)
    return emojiobj.generate_emojipasta(text=textinput)


global sendable, hook, Webhook,hook_trusted,hook_horny,hook_moan



global allowedtrusted
allowedtrusted=['trusted-chat','moan-moan','horny-jail','better-discord-please-fuck-off','shushbot']


hook_moan = ("https://discord.com/api/webhooks/906911537342611526/_nq-8T7xsfF9sGGAuq0NV4-Upmh9FarQBoyJovZ1_Wt6V3ejDjmxRunMydS0SnSOiXfi")
hook_trusted=('https://discord.com/api/webhooks/909065480747241494/9pyuZFRxfinn4v01FhXyuBJsp4HXyzQfjE8ChIaYV0WKRJ7plwzhRhChyFjSCBT49jm6')
hook_horny=('https://discord.com/api/webhooks/909065726743167036/kB5hvoQkv-mwj4sWv8bwel0nwbIeVxV5n5S6jawkKdPPRqfAgXBYm2GqOEW_4KbqPepV')



def send(i):

    global reddit

    reddit=False

    #print(name)

    with open(i, mode='rb') as f:
        image=discord.File(f)


    used_hook=(hook_horny)

    if str(name)==('trusted-chat'):
        used_hook=hook_trusted
    if str(name)==('moan-moan'):
        used_hook=hook_moan

    print(name)


    webhook = Webhook.from_url(used_hook, adapter=RequestsWebhookAdapter())

    webhook.send(file=image)
    #print((round(((i) / (len(sendable))) * 100)), '%')
    t.sleep(0.4)





@client.event
async def on_ready():
    print('bot up')





#print(characters)




@client.command()
async def get_channel(ctx, given_name=None):
    for channel in ctx.guild.channels:
        if channel.name == given_name:
            wanted_channel_id = channel.id

    await ctx.send(wanted_channel_id)


@client.command()
async def hush(ctx,member:discord.Member=None):


    print(str(ctx.message.channel))
    if str(ctx.message.channel) in allowedtrusted:

        if member is not None:
            channel=member.dm_channel
            if channel is None:
                channel = await member.create_dm()

            for i in range(1):

                await channel.send("I would literally never stop trying to impregnate Klee.Every day I would wake her up by coming in her and every night I would cum in her right before going to sleep, which I would do with my dick stuck inside her rotton pussy. I would take some viagra before bed just to maintain my erection so that she'll be messy in the morning when I thrust into her like an animal and slather her in kisses. Part of our wedding vows would have as many children as physically possible. I wouldn't even care if she's already pregnant, I'll fuck her while she's pregnant and she'll get double pregnant. I'll fill her with so much cum every day that she'll look pregnant even when she isn't (which she will never be after we're married) I would do everything in my power to make Klee as fertile as possible. I'd give her fertility drugs, I'd give her uterus massages, breast massages, I wouldn't let her go 12 hours  without at least one spastic orgasm. I'll even bake her home made lactation inducing biscuits to help her get to a point of hyperlactation syndrome so that she'll be seeping out multiple quarts of sweet cream per day. Which I will save and drink just so that I can tell her how delicious it is. I'll make her so fertile that triplets will be the minimum number she's carrying at any given time. Her natural belly shape will be a fucking sphere. I would respond to her every beck and call and I would cum inside her again each time she asks for something. She would be so pregnant all the time that she should literally not be able to stand up anymore even after menopause. Her spine would be permanently bent out of shape to accommodate a pregnant belly. Even after she can't get pregnant anymore I would just keep putting more eggs into her. I would clone her purely so that I can put fresh eggs from the clone inside her after she runs out of them. If she doesn't have any eggs I will synthesize them from her DNA. She would have so much progresterone running through her veins at any given time t")
                await channel.send('''hat even the thought of not being pregnant would seem alien to her. Imagine marrying Klee and she tells you she wants a kod and that she'll be fine and she'll keep her nightly duties up while pregnant. When she finally gets two lines on her pregnancy test she'll jump and full body hug you crying about how happy she is after trying so hard. Everything is going great for a few months, Klee is glowing and her knight activities are working out and her belly is quite small on her toned body. Now imagine in a few months Klee has to stop her knight activities because her feet hurt and her legs aren't used to holding up her new weight. Her belly extends almost a full foot infron of her and she's gained nearly 15 kilos. Imagine the look on Klee's face when her doctor tells her that she would take a break on her knight activities for a while because she is carrying triplets and the excessive movement is doing more harm than good. Imagine Klee reluctantly smiling at you and promising to stop doing her favonious reps for the sake of preparing to take care of three kids at once. Imagine as the weeks go by and her womb fills up more and as her appetite and weight increase with it. Imagine finding your 7 month old pregnant wife Klee raiding the fridge in the dark at 4:00 AM with a guilty look in her face when you find her, like a puppy and thay gnawed holes into your pillow. Imagine towering above Klee while she sits on the floor nerveously wiping ice cream drips off of her massive belly and mumbling how the kids made her do it. Imagine helping Klee up and princess carrying her back to bed and having her ask if she can lie on top of you because you're warm. Imagine rubbing Klee's nipples and having her complain about how you might get milk everywhere and how she needs to save it for the kids. Imagine teasing Klee about her breasts are too small to feed three kids and how she'll need to start saving up early, leading to her not milking herself for weeks and accidentally turning her''')
                await channel.send('''tiny supple breasts into overfilled perky veiny milktanks that spurt succulent cream at the slightest touch. Imagine Klee being proud of her breast growth despite it being painful and unhealthy and imagine the look on her face when the doctor says she would just start milking herself and how her husband (you) would be probably willing to help. Imagine spending hours with Klee's now plump squishy body resting on your lap while you suck the milk out of her tits. Imagine the extra weight from her pregnancy making it difficult to walk for her and turning her partially immobile during the last month.Imagine Klee try harding motherly charms like learning to cook and decorating the baby room and lactating. Imagine your comments having made her self concious about her milk production so she starts try harding supplements and massages to increase her yield to nearly a quart of milk per day.''')



        else:
            await ctx.send('@ doesnt work dickead')

    else:
        print(str(ctx.message.author)+' tried to use trusted command')

@client.command()
async def end(ctx,message):

    if str(ctx.message.channel) in allowedtrusted:


        name=name1

        link=str(ctx.message.content)

        reddit = True
        print('reddit link')



        # print(link)



        #link = ''.join(link)

        link.replace('send ','')

        print(link)

        #link=('https://'+link)

        whole = getreddit((link))

        print(whole)

        sendable = []
        maxl = 2000

        for i in range((len(whole) // maxl) + 1):
            index = i * maxl
            # print(index)
            current = []
            for i in range(maxl):
                try:
                    current.append(whole[i + index])
                except:
                    break
            x = ''.join(current)
            sendable.append(x)

        for i in range(len(sendable)):
            pass

        print(len(sendable), 'messages')


        def sendall():
            for i in range(len(sendable)):

                if name == ('trusted-chat'):
                    used_hook = hook_trusted
                elif name == ('moan-moan'):
                    used_hook = hook_moan
                else:
                    used_hook = hook_horny

                webhook = Webhook.from_url(used_hook, adapter=RequestsWebhookAdapter())
                webhook.send(sendable[i])
                print((round(((i) / (len(sendable))) * 100)), '%')
                t.sleep(0.4)


        sendall()







#print(a)

triggerwords=['send','shush']


async def get_emoji(guild: discord.Guild, arg):
    return get(ctx.guild.emojis, name=arg)

@client.event
async def on_message(message,member:discord.Member=None):
    global lastmessage
    global name
    if message.author.id==724236148599291986:
      message.delete()

    messageuse = (message.content)

    if message.author.id==542767106123628554:
        razasent=await message.channel.history(limit=2).flatten()
        await razasent[0].add_reaction('🥶')

    if message.author.id != (shushbotid):
        msg = await message.channel.history(limit=2).flatten()
        if ('owo') in messageuse:
            await message.channel.send(owoify(msg[1].content))

    if ('raza') in message.content and message.author.id != (shushbotid):
        for emoji in message.guild.emojis:
            if emoji.name==('razacold'):
                coldmessage= (str(emoji)+str(emoji)+str(emoji))
                await message.channel.send(coldmessage)

        coldmessage= await message.channel.history(limit=2).flatten()
        await coldmessage[0].add_reaction('🥶')
        await coldmessage[0].add_reaction('🥶')
        await coldmessage[0].add_reaction('🥶')
    try:
        name=str(message.channel.name)
    except:
        print('name error')

    if str(message.channel) in allowedtrusted:





        tick=False

        for i in range(len(triggerwords)):
            if triggerwords[i] in message.content:
                tick=True
        reddit=False

        if ('https://www.reddit.com/') in message.content:
            reddit=True
            tick=False

        #print(message.author)

        if message.author.id==313551541120532490:
            print('dickead said something')

            #await message.channel.send('78.147.238.108')
            await message.channel.send('dickead stfu this is why you dont have trusted')

        messageuse=(message.content)

        # if message.author.id!=(shushbotid):
        #     msg = await message.channel.history(limit=2).flatten()
        #     if ('owo') in messageuse:
        #         await message.channel.send(owoify(msg[1].content))
        #     elif ('emoji') in messageuse:
        #         await message.channel.send(emojify(msg[1].content))











        if tick==True:


            #                                                             REDUNDANT
            # if ('shush') in message.content:
            #     #print('shush detected',member)
            #
            #     if member is not None:
            #         channel = member.dm_channel
            #
            #         if channel is None:
            #             channel = await member.create_dm()
            #         #print(member.nick,'name')
            #         for i in range(1):
            #             await channel.send(
            #                 "I would literally never stop trying to impregnate Klee.Every day I would wake her up by coming in her and every night I would cum in her right before going to sleep, which I would do with my dick stuck inside her rotton pussy. I would take some viagra before bed just to maintain my erection so that she'll be messy in the morning when I thrust into her like an animal and slather her in kisses. Part of our wedding vows would have as many children as physically possible. I wouldn't even care if she's already pregnant, I'll fuck her while she's pregnant and she'll get double pregnant. I'll fill her with so much cum every day that she'll look pregnant even when she isn't (which she will never be after we're married) I would do everything in my power to make Klee as fertile as possible. I'd give her fertility drugs, I'd give her uterus massages, breast massages, I wouldn't let her go 12 hours  without at least one spastic orgasm. I'll even bake her home made lactation inducing biscuits to help her get to a point of hyperlactation syndrome so that she'll be seeping out multiple quarts of sweet cream per day. Which I will save and drink just so that I can tell her how delicious it is. I'll make her so fertile that triplets will be the minimum number she's carrying at any given time. Her natural belly shape will be a fucking sphere. I would respond to her every beck and call and I would cum inside her again each time she asks for something. She would be so pregnant all the time that she should literally not be able to stand up anymore even after menopause. Her spine would be permanently bent out of shape to accommodate a pregnant belly. Even after she can't get pregnant anymore I would just keep putting more eggs into her. I would clone her purely so that I can put fresh eggs from the clone inside her after she runs out of them. If she doesn't have any eggs I will synthesize them from her DNA. She would have so much progresterone running through her veins at any given time t")
            #             await channel.send(
            #                 '''hat even the thought of not being pregnant would seem alien to her. Imagine marrying Klee and she tells you she wants a kod and that she'll be fine and she'll keep her nightly duties up while pregnant. When she finally gets two lines on her pregnancy test she'll jump and full body hug you crying about how happy she is after trying so hard. Everything is going great for a few months, Klee is glowing and her knight activities are working out and her belly is quite small on her toned body. Now imagine in a few months Klee has to stop her knight activities because her feet hurt and her legs aren't used to holding up her new weight. Her belly extends almost a full foot infron of her and she's gained nearly 15 kilos. Imagine the look on Klee's face when her doctor tells her that she would take a break on her knight activities for a while because she is carrying triplets and the excessive movement is doing more harm than good. Imagine Klee reluctantly smiling at you and promising to stop doing her favonious reps for the sake of preparing to take care of three kids at once. Imagine as the weeks go by and her womb fills up more and as her appetite and weight increase with it. Imagine finding your 7 month old pregnant wife Klee raiding the fridge in the dark at 4:00 AM with a guilty look in her face when you find her, like a puppy and thay gnawed holes into your pillow. Imagine towering above Klee while she sits on the floor nerveously wiping ice cream drips off of her massive belly and mumbling how the kids made her do it. Imagine helping Klee up and princess carrying her back to bed and having her ask if she can lie on top of you because you're warm. Imagine rubbing Klee's nipples and having her complain about how you might get milk everywhere and how she needs to save it for the kids. Imagine teasing Klee about her breasts are too small to feed three kids and how she'll need to start saving up early, leading to her not milking herself for weeks and accidentally turning her''')
            #             await channel.send(
            #                 '''tiny supple breasts into overfilled perky veiny milktanks that spurt succulent cream at the slightest touch. Imagine Klee being proud of her breast growth despite it being painful and unhealthy and imagine the look on her face when the doctor says she would just start milking herself and how her husband (you) would be probably willing to help. Imagine spending hours with Klee's now plump squishy body resting on your lap while you suck the milk out of her tits. Imagine the extra weight from her pregnancy making it difficult to walk for her and turning her partially immobile during the last month.Imagine Klee try harding motherly charms like learning to cook and decorating the baby room and lactating. Imagine your comments having made her self concious about her milk production so she starts try harding supplements and massages to increase her yield to nearly a quart of milk per day.''')
            #             #print(channel.name,'name')
            #
            #     else:
            #         pass
            #         #await ctx.send('@ doesnt work dickead')






                # else:
                #     await message.channel.send('@ doesnt work dickead')

            link=message.content

            alldad=['dad','Dad','father','Father']
            dad=False



            name=message.channel.name

            for i in range(len(alldad)):
                if alldad[i] in link:
                    await message.channel.send('no')
                    dad=True

                    continue

            ak=['send ak','send Ak']
            ak1=['send Akshayian','send akshayian']

            if dad==False:



                #print(message.channel.name)


                global currentchannel
                currentchannel=message.channel


                if link==('send Andrei') or link==('send andrei'):
                    send('andrei.png')

                elif link in ak:
                    send('ak.png')
                elif link in ak1:
                    send('ak1.png')
                elif ('dylan') in link:
                    send('dylan.png')
                elif ('feet') in link:
                    send('feet.png')
                elif ('zafir') in link:
                    send('zafir.png')
                elif ('andreidrip') in link:
                    send('andreidrip.png')
                elif ('paki') in link:
                    send('paki.png')
                elif ('artur') in link:
                    send('pedo.jpeg')
                elif ('addy') in link:

                    if name==('trusted-chat'):
                        used_hook=hook_trusted
                    elif name==('moan-moan'):
                        used_hook=hook_moan
                    else:
                        used_hook=hook_horny
                    webhook = Webhook.from_url(used_hook, adapter=RequestsWebhookAdapter())
                    for i in range(3):
                        webhook.send('81.100.155.10 \n ha28sn carlyon avenue 103')
                        send('house.png')
                # elif ('meme') in link:
                #     continue
                #     print('meme')
                #     which=(str(ran.randint(1,135)))
                #     name=('meme ('+which+').jpg')
                #     name2=('meme ('+which+').png')
                #     try:
                #
                #         send(name)
                #     except:
                #         send(name2)
                # elif ('dickeaddancing') in link:
                #     send('andreidancing.gif')





                elif ('send klee') in link:
                    from urllib.request import Request, urlopen
                    from urllib.request import Request, urlopen
                    with open('klee.txt', 'r') as f:
                        whole = f.readlines()
                    whole = ''.join(whole)

                    if name == ('trusted-chat'):
                        used_hook = hook_trusted
                    elif name == ('moan-moan'):
                        used_hook = hook_moan
                    else:
                        used_hook = hook_horny

                    sendable = []
                    maxl = 1000
                    for i in range((len(whole) // maxl) + 1):
                        index = i * maxl
                        # print(index)
                        current = []
                        for i in range(maxl):
                            try:
                                current.append(whole[i + index])
                            except:
                                break
                        x = ''.join(current)
                        sendable.append(x)
                    for i in range(len(sendable)):
                        pass
                    print(len(sendable), 'messages')
                    print(sendable[i])

                    def sendall():
                        for i in range(len(sendable)):
                            print('works')

                            if name == ('trusted-chat'):
                                used_hook = hook_trusted
                            elif name == ('moan-moan'):
                                used_hook = hook_moan
                            else:
                                used_hook = hook_horny

                            webhook = Webhook.from_url(used_hook, adapter=RequestsWebhookAdapter())

                            webhook.send(sendable[i])

                            print((round(((i) / (len(sendable))) * 100)), '%')
                            t.sleep(0.4)

                    sendall()
                    print('done')
                elif ('quran9816') in link:
                    from urllib.request import Request, urlopen
                    from urllib.request import Request, urlopen
                    with open('quran.txt', 'r') as f:
                        whole = f.readlines()
                    whole = ''.join(whole)
                    hook = hook
                    sendable = []
                    maxl = 1000
                    for i in range((len(whole) // maxl) + 1):
                        index = i * maxl
                        # print(index)
                        current = []
                        for i in range(maxl):
                            try:
                                current.append(whole[i + index])
                            except:
                                break
                        x = ''.join(current)
                        sendable.append(x)
                    for i in range(len(sendable)):
                        pass
                    print(len(sendable), 'messages')
                    print(sendable[i])

                    def sendall():
                        for i in range(len(sendable)):

                            name = (message.channel.name)

                            if name == ('trusted-chat'):
                                used_hook = hook_trusted
                            elif name == ('moan-moan'):
                                used_hook = hook_moan
                            else:
                                used_hook = hook_horny
                            webhook = Webhook.from_url(used_hook, adapter=RequestsWebhookAdapter())
                            webhook.send(sendable[i])
                            print((round(((i) / (len(sendable))) * 100)), '%')
                            t.sleep(0.4)

                    sendall()
                    print('done')







                #elif ('https://www.reddit.com/') not in link:
                #    await message.channel.send('not a reddit link dickead')














            else:
                await message.channel.send('he left')
        else:
            pass

        try:
            name=message.channel.name
        except:
            print('name error')
        global name1
        name1=name
        await client.process_commands(message)

    else:
        print(str(message.author)+' tried to use trusted command')







@client.command(aliases=['ush'])
async def test(ctx):
    #global f
    f=open('quran.txt')
    a=('')
    for i in f:
        a+=i


    lines = 0
    words = 0
    characters = 0
    for line in f:
        wordslist = line.split()
        lines = lines + 1
        words = words + len(wordslist)
        characters = characters + len(line)

    f.close()
    f=open('quran.txt')
    if str(ctx.message.channel) in allowedtrusted:

        shift=0
        for i in range(characters-1//2000):
            one=('')
            for i in range(2000):
                one+=a[i+shift]
            shift+=2000


            await ctx.send(one)
    else:
        print(str(ctx.message.author)+' tried to use trusted command')

@client.command()
async def dm(ctx,member:discord.Member=None):

    if str(ctx.message.channel) in allowedtrusted:


        try:

            if member is not None:
                channel=member.dm_channel
                if channel is None:
                    channel = await member.create_dm()
        except:



            await ctx.send('ID no work')

        print(channel,'channel')



        for i in range(1):

            message=ctx.message.content

            message=list(message)

            for i in range(23):
                message.pop(0)


            await channel.send(''.join(message))






dorevive()
token = ('ODg4MTE4NDk0Njk1MTUzNjk0.YUOCzQ.0TkIKQ53dkGVw2UP0q_MeOHAfdQ')


client.run(token)



x=input('')

