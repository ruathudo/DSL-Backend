class Config(object):
    """
    Common configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = '/tmp/'
    STORAGE_BUCKET = 'cdn.datasciencelog.com'
    STORAGE_URL = 'http://cdn.datasciencelog.com/'
    ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    IMAGE_SIZES = [1200, 800, 400, 100]

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    SQLALCHEMY_ECHO = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

error_codes = {
    400: 'BAD_REQUEST',
    409: 'DUPLICATED',
    404: 'NOT_FOUND',
    401: 'UNAUTHORIZED',
    403: 'FORBIDDEN',
    422: 'INVALID_INPUT',
    499: 'TOKEN_REQUIRED',
    498: 'INVALID_TOKEN',
    500: 'UNEXPECTED_ERROR'
}
