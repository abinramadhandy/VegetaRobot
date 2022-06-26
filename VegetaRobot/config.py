# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json #by ctzfamioy
import os


def get_user_list(config, key):
    with open('{}/LuffyRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 10206770  # integer value, dont use ""
    API_HASH = "b06187ed06bf10b7c386bc3f7b25a4ee"
    TOKEN = "5405005909:AAFp_wbI_UFp14yubqeexfKr9K-QpyUAJso"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1338177846  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "itsabin"
    SUPPORT_CHAT = 'familynoe'  #Your own group for support, do not add the @
    UPDATES_CHANNEL = 'dailyabinnn' #Your own channel for Updates of bot, Do not add @
    JOIN_LOGGER = -1001532254724  #Prints any new group the bot is added to, prints just the name and ID.
    REM_BG_API_KEY = "dxsh728mZMDmj4ijSZCNPZig"
    STRING_SESSION = "BQAagHa0TbBC1KKl_tOdKSsouNEbV22QFbc--r8dKnW9drA1HWv42yuFec61zMyOJlNnxGnRLHk094IAbEbFZWSiSH7SkqtyWG-7_YInmR4PWicjXA5m1qRusF_EenzhM_h0etZOvai_b8AFGxumDj_3Bk-StpkNFpTBNQpY3X1oXn2XvSi_npm2VWfvQyn3wWB914NtsUPMZzBZeln2ss2lv5rYLFTk-vSe0fLEz4EGBXX84PvDdmB8oqcy3JRXWvazJb6r6YvufE84knEX1tkjrwsvRhamtoQpNCSXQwzVd8Z27H-NuTzvuEVX3XNzPb9X24P1_4q1aNeT1phy83oLT8L5NgA"
    TEMP_DOWNLOAD_DIRECTORY = ""
    EVENT_LOGS = -1001543354286  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    SQLALCHEMY_DATABASE_URI = ''"
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key -
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_ID = "5405005909"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    ARQ_API_URL = "http://thearq.tech/"
    ARQ_API_KEY = "HMHMJX-FWNZXS-UZFXHP-FSDJXU-ARQ"
    CASH_API_KEY = 'awoo'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    OPENWEATHERMAP_ID = 'awoo'
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
