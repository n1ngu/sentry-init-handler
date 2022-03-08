import sentry_sdk
import logging


class SentryInitHandler(logging.NullHandler):
    def __init__(self, *args, **kwargs):
        super(SentryInitHandler, self).__init__()
        sentry_sdk.init(*args, **kwargs)
