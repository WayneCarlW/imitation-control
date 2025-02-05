import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "wNqWcEDrtfjFvalI5Z6VeXGuSUkOiPg1")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/imitation-control-app")

class DevelopmentConfig(Config):
    DEBUG = True

# class ProductionConfig(Config):
    # DEBUG = False
    # MONGO_URI = os.getenv("MONGO_URI_PROD", "")

config = {
        "development": DevelopmentConfig,
        #"production": ProductionConfig
}
