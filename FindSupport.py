from TwitterSearch import TwitterSearch
from TwitterSearch import TwitterSearchOrder
from TwitterSearch import TwitterSearchException
import re
# from pygeocoder import Geocoder
# from pygeocoder import GeocoderError
from countryinfo import countries

country_desc = {}
for c in countries:
    country_desc[c['name']] = [c['capital'], c['code'], c['continent']]


def __increment(support, country):
    if country is None:
        return
    if support.has_key(country):
        support[country] += 1
    else:
        support[country] = 1


def count_for_tag(support, hashtag):
    print "Searching for %s " % hashtag
    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.setKeywords([hashtag])  # let's define all words we would like to have a look for
        #tso.setLanguage('en')
        tso.setCount(100)  # please dear Mr Twitter, only give us 7 results per page
        tso.setIncludeEntities(False)  # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key="TNX9jTHJgTEyB1IcUECPJ4uSY",
            consumer_secret="5B1R0geyT1Iv2mBc601gaDwuBBjVkabab72UXbzVTDEJ7Z6XAb",
            access_token="143109809-5IAGEaGuuiBRjVVJT9WHUQnAQlOkVcemzhnOpMkx",
            access_token_secret="Yh5WeJo9Z01j42jbTk6tL47zl1Rdox1LJ1d2lJgAAPm0r",
            verify=False
        )

        for tweet in ts.searchTweetsIterable(tso):
            #print tweet['coordinates']
            if tweet['place'] != None and tweet['place'].has_key('country'):
                country = tweet['place']['country']
                __increment(support, country)
                continue
            location = tweet['user']['location']
            if len(location) == 0:
                continue
            # try:
            # results = Geocoder.geocode(location)
            #                country = results[0].country
            #                increment(support, country)
            #                continue
            #            except GeocoderError as e:
            #                #print "Could not parse ", location
            #                pass
            country = None
            for cn, cd in country_desc.iteritems():
                if (cn.lower() in location.lower()):
                    country = cn
                    break
                for desc_part in cd:
                    desc_word = re.compile(r'\b%s\b' % desc_part)
                    if desc_word.search(location):
                        country = cn
                        break
                if country is not None:
                    break
            if country is None:
                pass
                #print( '%s' % location)
            else:
                #print ("Found %s in \"%s\"" % (country, location))
                __increment(support, country)
            if ts.getStatistics()['tweets'] > 1000:
                break

    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
        print(e)


def find_tags_by_country(tags, countryCount):
    """

    :type tags: list
    """
    for tag in tags:
        count_for_tag(countryCount, tag)
