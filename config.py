from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        # ==================== HARDCODED VALUES ====================
        self.API_ID = 34848798
        self.API_HASH = "210df233d07183ee955143092259dabb"
        self.BOT_TOKEN = "8713743302:AAEcHql2nKGgEnoGsqHUFtRxtS0sIGtKK5w"
        
        self.MONGO_URL = "mongodb+srv://shauryaragini:shibu123@cluster0.vlosfji.mongodb.net/?retryWrites=true&w=majority&appName=AnonXMusic"
        
        self.LOGGER_ID = -1003877525072
        self.OWNER_ID = 6271039736
        
        # Session
        self.SESSION1 = "BQITwB4AdCUU0-BNSb2aUa8gHvvtlWsFiX5THJRDvFCh1M0-_0383seECU7ge58xOusZMB06TLBOXMLEhdHD_YNHSu4N4qd-bXIx5eWJTTBAbiQGxCRWZAL-t2N3ETih5JeV_PfRrb5e9aqSyByJNqusfnYbC_6-Ao7gi89_XPVUElb-Y2T26HVBLjzsVOKCL7_ZJ969LZXb5HDEDoDC7qRrojpS5TH7KIW9d9dytoPPv1Q7CDYBadWULMqsMCZmfFjiplxXgXI72o-e7ZMd70xLQM1TZTld17kUiPP-XkF8vTuK7id6Yt89bYSimxvnw_AXQTBjsWTY7L2LNI98PHFkWLIs9QAAAAGqkXGbAA"
        self.SESSION2 = None
        self.SESSION3 = None

        # Other Settings (You can change later if needed)
        self.DURATION_LIMIT = 60 * 60
        self.QUEUE_LIMIT = 20
        self.PLAYLIST_LIMIT = 20
        
        self.SUPPORT_CHANNEL = "https://t.me/s0ffm"
        self.SUPPORT_CHAT = "https://t.me/mewzicx"
        
        self.AUTO_LEAVE = False
        self.AUTO_END = False
        self.THUMB_GEN = True
        self.VIDEO_PLAY = True
        self.LANG_CODE = "en"
        
                # ==================== COOKIES (Hardcoded) ====================
        self.COOKIES_URL = ["https://hastebin.com/share/rexitupora.graphql"]  # External link disable kiya

        #
        self.DEFAULT_THUMB = "https://te.legra.ph/file/3e40a408286d4eda24191.jpg"
        self.PING_IMG = "https://files.catbox.moe/haagg2.png"
        self.START_IMG = "https://files.catbox.moe/zvziwk.jpg"

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
        print("✅ All required configurations loaded successfully!")
