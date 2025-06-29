import discord
import dotenv
import os

from server import server_thread

dotenv.load_dotenv()

TOKEN = os.environ.get("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} がログインしました！')
    print(f'サーバー数: {len(client.guilds)}')

@client.event
async def on_message(message):
    print(f'メッセージ受信: {message.content} from {message.author}')
    
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print('$helloコマンド実行中...')
        await message.channel.send('Hello!')

# Koyeb用 サーバー立ち上げ
server_thread()
client.run(TOKEN)