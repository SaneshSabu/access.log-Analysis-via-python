import logparser

import geomodule

access_log = open("access.log","r")

counter = {}

for line in access_log:
    
  parsed = logparser.parser(line)

  if parsed['host'] not in counter:
        
    counter[parsed['host']] = 1
    
  else:
    
    counter[parsed['host']] = counter[parsed['host']] + 1
    
def hits(x):
    
  return x[-1]

sort = sorted(counter.items(),key=hits,reverse=True)[:15]

api_key = '3476eff26e4f4ffe8417144f10369082'

for item in sort:
  
  ip,hits = item
    
  print("{:14} -{:7} - {:10}".format(ip,hits,geomodule.geolocation(ip,api_key)))
  
access_log.close()
