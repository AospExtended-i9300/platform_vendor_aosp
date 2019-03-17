import json
try:
    # For python3
    import urllib.error
    import urllib.parse
    import urllib.request
except:
    # For python2
    import imp
    import urllib2
    import urlparse
    urllib = imp.new_module('urllib')
    urllib.error = urllib2
    urllib.parse = urlparse
    urllib.request = urllib2

from os.path import dirname, join, realpath

try:
    top = realpath(join(dirname(__file__), ".."))
    devices = "{top}/devices.json".format(top = top)
    data = json.loads(open(devices, "r").read())
    for res in data:
	for version in res['supported_versions']:
		if version['version_code'] == 'pie' or version['version_code'] == 'pie_go':
		        print (res['codename'])
except:
    print ("")
