
from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        # if message.content == 'じゃあの':
            # await message.channel.send('ばいびー')
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/test':
        await message.channel.send(random.choice(('てすてす','あー、あー、マイクテスト','あーあー','本日は晴天なり','超テスト','ファイナルテスト','シンプルイズテスト','過剰なテスト','試験','品質テスト','まごころテスト','テスト','えっ？','てきとーなテスト','ハーデスト','てすてすてすてすてすてすてすてす','TEST','伝説のテスト',':wink')))
    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
