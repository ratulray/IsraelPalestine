# -*- coding: utf-8 -*-
import pickle
from time import time
from FindSupport import find_tags_by_country


israelTags = ["israelunderattack", "supportisrael",
              "israelunderfire", "freeisrael", "israeldefends",
              "prayforisrael"]
palestineTags = ["palestineunderattack", "supportpalestine",
                 "freepalestine", "gazaunderattack", "gazaunderfire",
                 "palestineunderfire", "prayforgaza"]
palestine = {}
israel = {}
find_tags_by_country(israelTags, israel)

# find_tags_by_country(palestineTags, palestine)

#pickle.dump(palestine, open('palestine-' + str(("%.0f" % time()) + '.pkl'), 'w'))
pickle.dump(israel, open('israel-' + str(("%.0f" % time()) + '.pkl'), 'w'))