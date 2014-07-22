# -*- coding: utf-8 -*-
import pickle
from time import time
from FindSupport import findTagsByCountry


israelTags = ["israelunderattack", "supportisrael",
              "israelunderfire", "freeisrael", "israeldefends",
              "prayforisrael"]
palestineTags = ["palestineunderattack", "supportpalestine",
                 "freepalestine", "gazaunderattack", "gazaunderfire",
                 "palestineunderfire", "prayforgaza"]
palestine = {}
israel = {}
findTagsByCountry(israelTags, israel)

#findTagsByCountry(palestineTags, palestine)
    
#pickle.dump(palestine, open('palestine-' + str(("%.0f" % time()) + '.pkl'), 'w'))
pickle.dump(israel, open('israel-' + str(("%.0f" % time()) + '.pkl'), 'w'))