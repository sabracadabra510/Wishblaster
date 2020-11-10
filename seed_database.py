import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb User')
os.system('createdb User')