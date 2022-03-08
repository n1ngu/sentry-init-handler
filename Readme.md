# Sentry Init Handler
Abuse the logging configuration to inject a `sentry_sdk.init` call in CLI scripts.

See the main issue with the discussion around this: https://github.com/getsentry/sentry-python/issues/1133

## Usage

> Do NOT use this handler as a replacement for
Sentry SDK logging handler classes
https://docs.sentry.io/platforms/python/guides/logging/#handler-classes

If the cumbersome script you are running would still load a
logging file config, place this magic null handler in the
logging tree so it will call `sentry_sdk.init` with its args
and kwargs when it instantiated.

```
[loggers]
keys = root

[handlers]
keys = stdout, initsentry

[logger_root]
level = INFO
handlers = stdout, initsentry

[handler_stdout]
class = StreamHandler
formatter = default
args = (sys.stdout,)

[handler_initsentry]
class=sentry_init_handler.SentryInitHandler
args = (...,)
kwargs = {
 'max_breadcrumbs': 50,
 'debug': True,
 'default_integrations': True,
 'with_locals': True}
```

See the example.logconf for a complete example.

## Proof-Of-Concept

A dumb script to test the handler is provided in bin/sentry-cli-init-poc.
Use it from your terminal with the example logging configuration and wait
for it to report an exception to your sentry endpoint.
```
$ export SENTRY_DSN=https://examplePublicKey@o0.ingest.sentry.io/0
$ python bin/sentry-cli-init-poc --logconf=example.logconf
```
