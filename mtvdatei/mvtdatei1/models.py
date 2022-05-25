from django.db import models

class Zitat:
    f = open("zitate.txt", "r")
    zitate = f.read()
