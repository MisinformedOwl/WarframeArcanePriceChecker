import configparser
import os
from pathlib import Path

def run():
    cfg_path = Path(__file__).parent / "config.ini"

    config = configparser.ConfigParser()
    config.read(cfg_path)

    val = config.getint("TEST", "runs")+1
    print(val)
    config.set('TEST', 'runs', str(val))

    with open(cfg_path, "w") as configfile:
        config.write(configfile)