#!/usr/bin/env python3

from datetime import datetime
from dateutil import tz

def rastafarai_print():
    local_tz = datetime.now(tz.gettz('Europe/Paris')).strftime('%Y-%m-%d %H:%M:%S')
    jamaica_tz = datetime.now(tz.gettz('America/Jamaica')).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Bombo claat! Check it ya, the time inna Paris a run: {local_tz}")
    print(f"Out a Babylon, inna Jamaica, the clock strike: {jamaica_tz}")
    print("Jah guide, every time is the right time under the sun!")

if __name__ == "__main__":
    rastafarai_print()
