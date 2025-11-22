from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = 23537462
        self.API_HASH = "c9599a5aa61ee8ca4f5e778d20c61f24"

        self.BOT_TOKEN = ("8462016049:AAENqxWLz47Voq014jqH4irYCJ43997Hnd8")
        self.MONGO_URL = ("mongodb+srv://musicxrobot:8Up92WwJbgUS39FV@cluster0.ys1jirt.mongodb.net/")

        self.LOGGER_ID = (-1002456565415)
        self.OWNER_ID = 7654385403

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = "BQFnJzYAB4GU36CiFyCAZSMA6XV6Kt6UXNwFlK3mDROMWjehifYw-BpiKT-iK4benswKx_WysIeUDzvAclj6n9ytVeuQj1N318I2rlVy7YNqSTQfLvnuMeXqC--0cXcuBLkDgq-9E4uEcddedzS2CwU9LL7zL-NeV_kRGtaHeHsSZNbY8zD8EQ51sMsLKoqFdnGvgXyEVQ3Hra8ZXYIkZT4Cy0cSBkUIFbX0gp87SPMHD2UEZzgFJuPqbs33_7gxIcfmtCHRpOzR-7oJDNYHlDANqPa0xxWaNxXYI7oEMjC3xY-GDJjT8J9exPgGP5B8T4_wYWfbQNA5ZaGBg-cnJMld2HM5MwAAAAHY2x8OAA"
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AnimeNexusNetwork/160")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EternalsHelplineBot")

        self.AUTO_END: bool = getenv("AUTO_END",  False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", True)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://batbin.me/bractea").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://files.catbox.moe/da1v00.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/da1v00.jpg")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/da1v00.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
