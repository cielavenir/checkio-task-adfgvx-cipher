from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.code import CheckiORefereeCode
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiORefereeCode(
        tests=TESTS,
    ).on_ready)