import logparser

access_log = open("access.log","r")

dt_counter = {}

for line in access_log:
    
  logDict = logparser.parser(line)

  dat = logDict['time'][:11]
    
  if dat not in dt_counter:
    
    dt_counter[dat] = 1
    
  else:
    
    dt_counter[dat] = dt_counter[dat] + 1
    
def hits(x):

  return x[-1]
    
sort = sorted(dt_counter.items(),key=hits,reverse=True)[:15]


for item in sort:
    
  dt,hits = item

  print("{:12}- {}".format(dt,hits))
    
access_log.close()
