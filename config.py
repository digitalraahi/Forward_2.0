import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","hemant")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQGMcpgAbaN39PQVmksmwDtmwFYNtRmk4waFNtRA4illWqR3lZlOg4JJvXIttSPYAQBVHJwYhdSErtSFYEspsGUw1jGVqng-g_CxGE4IDHKugySCF7znBGmjTmptEwfi2ebWEpyJtRbXJMo1bi3tXLisNGwqXoIiYY_j1EVnd4LPWmyUCCKas1ncs3zo1VgU22CLRMpquFbVc43amuCTsUgBZPOpV7FGWnxRJQ2xKzz5xBBP7EbSCvY4Uh8lyWe0eGZuHLDrVSzGsx9F_VTxZTsNFQ1NmOwlreYB8_-zdJIgNIDQ-ssAMozJvH0b4990akI1g5HmdujDRFkE_D1F-MKXi0zBcQAAAAE1FccZAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "fdboxbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
