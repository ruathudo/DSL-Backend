class Config(object):
    """
    Common configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
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
    409: 'DUPLICATED',
    404: 'NOT_FOUND',
    401: 'UNAUTHORIZED',
}
