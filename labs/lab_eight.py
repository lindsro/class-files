from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

try:
    from lxml import etree
    print('running with lxml.etree')
except ImportError:
    print('you\'re not running with lxml active')

import re
from pathlib import Path

MODS_collection = Path('2018_lcwa_MODS_5.xml')
MODS_file = Path('2018_lcwa_MODS_5.xml')

mods_collec = etree.parse(MODS_collection)