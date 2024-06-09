import discord
from discord.ext import commands, tasks
import extract_doc

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)
# Keep track of subscribed users
subscribed_users = set()

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")
    extract_doc.get_init_txt()
    check_for_updates.start()
    await client.tree.sync()

@tasks.loop(minutes=1)
async def check_for_updates():
    extract_doc.get_new_txt()
    if extract_doc.compare_files("init_class.txt", "new_class.txt") == False:
        print("NEW CLASSES ARE COMING")
        for user_id in subscribed_users:
            user = await client.fetch_user(user_id)
            await user.send("NOTIFICATION: There are new classes at: " + extract_doc.GS_TRI_THUC_URL)
    else:
        print("No new class")
    extract_doc.replace_file("init_class.txt", "new_class.txt")

@client.tree.command(name="hello", description="Say hello to the bot")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello, I am a DiscordBot!")

@client.tree.command(name="subscribe", description="Subscribe to new class notifications")
async def slash_command(interaction:discord.Interaction):
    user_id = interaction.user.id
    if user_id not in subscribed_users:
        subscribed_users.add(user_id)
        await interaction.response.send_message("You have successfully subscribed to the new class notification. You will be notified when there are updates.")
    else:
        await interaction.response.send_message("You are already subscribed to the new class notification.")

client.run('MTI0NjY2NTc0ODI2NTQzOTMyNA.G9JQ6t.ihOjht1Ym-pXsRCYGJ7sSqFYCH2XZexRywVlFc')
