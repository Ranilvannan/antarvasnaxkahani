class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    MONGO_URI = "mongodb://localhost:27017/story_book"
    MONGO_DATABASE = "story_book"

    IMPORT_PATH = "/var/story_book"
    CUSTOM_IMAGES_PATH = "/var/story_book/images"

    BLOG_CODE = "Hindi"
    MONGO_GALLERY_TABLE = "gallery"
    MONGO_BLOG_TABLE = "hindi_blog"
    TEMPLATE_FOLDER_PATH = "template"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True