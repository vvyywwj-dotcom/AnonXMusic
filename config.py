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
        self.COOKIES_URL = []  # External link disable kiya

        # Direct Cookies (Netscape Format)
        self.COOKIE_TEXT = """# Netscape HTTP Cookie File
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.
.youtube.com	TRUE	/	TRUE	1814700675	PREF	f4=4000000&f6=40000000&tz=Asia.Calcutta&f7=100
.youtube.com	TRUE	/	TRUE	1791204823	__Secure-BUCKET	COMH
.youtube.com	TRUE	/	FALSE	1814539843	HSID	AsrRZ84a5a-9k1ssk
.youtube.com	TRUE	/	TRUE	1814539843	SSID	AFFQWeGTwMB2xQYUi
.youtube.com	TRUE	/	FALSE	1814539843	APISID	EOhKOxC1HYP4tCRq/AECxjOeedoEsDE0K1
.youtube.com	TRUE	/	TRUE	1814539843	SAPISID	pUqldSK5c_vPDfZK/Aj3AGeWRG_7qtehIM
.youtube.com	TRUE	/	TRUE	1814539843	__Secure-1PAPISID	pUqldSK5c_vPDfZK/Aj3AGeWRG_7qtehIM
.youtube.com	TRUE	/	TRUE	1814539843	__Secure-3PAPISID	pUqldSK5c_vPDfZK/Aj3AGeWRG_7qtehIM
.youtube.com	TRUE	/	TRUE	1810295239	LOGIN_INFO	AFmmF2swRgIhAOVh4gHOVL34Csg4vByTGrFLHQ7XWn1R1_2_XUyu7ytjAiEA1P1tXSBogu_Hz82hUs6YHdbx_M26D4H5-JVKU143frs:QUQ3MjNmeWFDQUp0OFZYa2daQmN2SmtrM3U4bXVaSC03Zjh3NjRsUFR1SXRWSHA1bVpQZnFmdVZUNzFhMEhZMFZXYXBCZVBOYlB6ZFFjR1dUeXpKeExUeEZvU2E1bk9FNkNBMGFNaGx3WVZZb2FtektyVzNhWmRIRlRhYml6X2ZEaS1wWUFoMWVTNnR6RnoxQ3hUak1qZ0ZaN0VFZW1GUkN3
.youtube.com	TRUE	/	FALSE	1814539843	SID	g.a000-ggvKWTVnvpMNcDPFjMDuZazvpEKaGd_QLx27YQ71rphsTugYY5rkK-aBnYXd0D0B8m_7QACgYKASkSARESFQHGX2MilOdfTs3I-Cl_RcyAj_Fp3xoVAUF8yKrXsEg0t_aVqWAqcfTRg3KJ0076
.youtube.com	TRUE	/	TRUE	1814539843	__Secure-1PSID	g.a000-ggvKWTVnvpMNcDPFjMDuZazvpEKaGd_QLx27YQ71rphsTugnthjVWHgA5N-omvhb4sqCQACgYKAeMSARESFQHGX2MiRyNR2NZUO-dbRP7pjuF8dxoVAUF8yKqPybb2Wgy1emIIeZnka8BV0076
.youtube.com	TRUE	/	TRUE	1814539843	__Secure-3PSID	g.a000-ggvKWTVnvpMNcDPFjMDuZazvpEKaGd_QLx27YQ71rphsTugY5U2nYYrV7Vw8eJ-f3Lq7AACgYKAdwSARESFQHGX2MiLK7pEbHI8kgoWA5grl9lyBoVAUF8yKpWT0iy4SNQIEfOLtkvOnRI0076
.youtube.com	TRUE	/	TRUE	1811676678	__Secure-1PSIDTS	sidts-CjUBhkeRd_aLcxGIgkPKIIs2jd-_guEvFVwZlof11QPpv-rhWesvkYciJhykRaeE58Yoar0QyRAA
.youtube.com	TRUE	/	TRUE	1811676678	__Secure-3PSIDTS	sidts-CjUBhkeRd_aLcxGIgkPKIIs2jd-_guEvFVwZlof11QPpv-rhWesvkYciJhykRaeE58Yoar0QyRAA
.youtube.com	TRUE	/	FALSE	1811676679	SIDCC	AKEyXzXHjNE6qbB1oecHQ3Yexv0McLprOMQhaHmoRVQwhn3rBQ4WhYPLyShbyrKIr5-9sAmxPQ
.youtube.com	TRUE	/	TRUE	1811676679	__Secure-1PSIDCC	AKEyXzXn0nn8md_ZwkT_hzZCRRfNiZ7zLDfEXdU3sX4tKFFTRen8LXMICYpoZ5Mg9TremcQgjA
.youtube.com	TRUE	/	TRUE	1811676679	__Secure-3PSIDCC	AKEyXzVkB3yyR5Jc3cjq65zUljH6cekTc4AhFgBzUnrlZ5d3My0devYgGXSsJeSyZDQp6G--nDc
.youtube.com	TRUE	/	TRUE	1795692679	VISITOR_INFO1_LIVE	t2rPJJoAtoM
.youtube.com	TRUE	/	TRUE	1795692679	VISITOR_PRIVACY_METADATA	CgJJThIEGgAgSw%3D%3D
.youtube.com	TRUE	/	TRUE	1795692671	__Secure-YNID	18.YT=S7vQM6z-VVR6EjkgHn0raebwi-AS2qas3mHsTLl7lluV4_kZPdL46LbX3vwplCjXyr6X9nbA9ZH2VgQd_7eZUsCMvmJjCgl3XtXrCzP5LYVQEgNw_GOWMf6xS54hJvygrQ3hhIu72KSTKkXAipHS5OEX0zXVqztbqfXqoGXc8DMamW6dRiAnwGjgRTXa1gitV6uDlwG3cl4cxLe4ZupKtpJht5qnl2AFw_wHewmQXSeCVv_wBxNhPfcUjfRouCsQbopApC58bczG3Uw6MhOYaGnlgA2tGifPUn_L1vanMQZxl2W-JRkqLdzYER_OF1kB2C7JbYRSquLEIiwSavS0Wg
.youtube.com	TRUE	/	TRUE	0	YSC	EccwQ8MMmGM
.youtube.com	TRUE	/	TRUE	1795692671	__Secure-ROLLOUT_TOKEN	CISKz-i5tNwUENmaq6v3uJMDGObAveL04JQD
"""
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
