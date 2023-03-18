import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "e9c63cacf52d59607b769f13140af417"))
API_HASH = getenv("API_HASH", "20154655")

BOT_TOKEN = getenv("BOT_TOKEN", "5742586097:AAHziLjqXrNuQEhOFm1eZdmzpeEVpK7mUpo")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://AlexRobot:AlexRobotOp555@cluster0.emsuz0p.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001643520230"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "LAILA-MUSIC PLAYER")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5847378475").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AnonymousX1025/AnonXMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/THE_ALONE_LAV")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/lav_fed_and_log")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQB2OciDTNpX3fVV3cdC_V3ZOgDcv3F6s33_PO8REsrjQWLNYLF3Y11_ctBPrJs3A9V6cGqa0uM2t8v8ZLb9XPBj8xx3XcEI21ihd4H37aRYSIyBBer-csJE77n4zk0getbcPBVGS9q9UTMPfxBYLO1eyD5w27Pp3_6tdEQUYm2YM7urgsSgo-tSZLie3lT6Q5lMh6oKje095FjLKDx2TL2zZ51e7e3FpFbQoXHzW1dd7s0KHOtu0qMA8xTH4rdEwTTWb80UaTq32e8yAAM9_eUcNLnDfyg8DzMIgKu660hgG61DjG-r5OyWs4CHMdAKtZrrhNihyIfrpFUifGAuaP0iAAAAAU7lD5oA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/7db356b1e3ad7a9058099.jpg"
