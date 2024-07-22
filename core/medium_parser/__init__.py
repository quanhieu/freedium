import jinja2
from aiohttp_retry import ExponentialRetry

from medium_parser import exceptions as exceptions
from medium_parser import exceptions as medium_parser_exceptions

retry_options = ExponentialRetry(attempts=3)
jinja_env = jinja2.Environment()
