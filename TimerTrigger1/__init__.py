import datetime
import logging
from . import main as m

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    m.main()