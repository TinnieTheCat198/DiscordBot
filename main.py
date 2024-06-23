import discord
import keys
from discord.ext import commands, tasks
import extract_doc
import database

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)
# Keep track of subscribed users
database.create_subscribed_users_storage()

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")
    extract_doc.class_ids = extract_doc.retrieve_class_ids()
    check_for_updates.start()
    await client.tree.sync()

@tasks.loop(minutes=1)
async def check_for_updates():
    tmp_class_ids = extract_doc.retrieve_class_ids()
    if tmp_class_ids <= extract_doc.class_ids:
        print("No new class")
    else:
        print("NEW CLASSES ARE COMING")
        extract_doc.printSet(tmp_class_ids - extract_doc.class_ids)
        subscribed_users = database.getSubscribedUserIDS()
        for user_id in subscribed_users:
            user = await client.fetch_user(user_id[0])
            await user.send("NOTIFICATION: There are new classes at: " + extract_doc.GS_TRI_THUC_URL)
    extract_doc.class_ids = tmp_class_ids

@client.tree.command(name="hello", description="Say hello to the bot")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello, I am a DiscordBot!")

@client.tree.command(name="subscribe", description="Subscribe to new class notifications")
async def slash_command(interaction:discord.Interaction):
    user_id = interaction.user.id
    if database.check_subscription(user_id) == False:
        database.add_subscribed_user(user_id)
        await interaction.response.send_message("You have successfully subscribed to the new class notification. You will be notified when there are updates.")
    else:
        await interaction.response.send_message("You are already subscribed to the new class notification.")

@client.tree.command(name="unsubscribe", description="Stop receiving new class notifications")
async def slash_command(interaction:discord.Interaction):
    user_id = interaction.user.id
    if database.check_subscription(user_id) == False:
        await interaction.response.send_message("You have not subscribed yet!")
    else:
        database.remove_subscribed_user(user_id)
        await interaction.response.send_message("Unsubscribed successfully.")

client.run(keys.BOT_KEY)
