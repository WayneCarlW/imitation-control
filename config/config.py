import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    MONGO_URI = os.getenv("MONGO_URI", "")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    MONGO_URI = os.getenv("MONGO_URI_PROD", "")

config = {
        "development": DevelopmentConfig,
        "production": ProductionConfig
}
