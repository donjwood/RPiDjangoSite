import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

def get_env_vars(request):
    return {
        'ENVIRONMENT': env.str('ENVIRONMENT'),
        'RASPBERRY_PI_NAME': env.str('RASPBERRY_PI_NAME'),
        'IS_RASPBERRY_PI': env.bool('IS_RASPBERRY_PI'),
        'ENABLE_SENSE_HAT_APP': env.bool('ENABLE_SENSE_HAT_APP'),
    }