import logparser

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

for item in sort:
  
  ip,hits = item
    
  print("{:16}- {}".format(ip,hits))
  
access_log.close()
