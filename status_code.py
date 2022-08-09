import logparser
import sys

usage = "Syntax: python3 status_code.py <status code>"

access_log = open("access.log","r")

status_code = {}

for line in access_log:
    
  logDict = logparser.parser(line)

  ip = logDict['host']
    
  try:
    
    if len(sys.argv) == 2:
          
      argument = sys.argv[1]
    
      if logDict['status'] == argument and ip not in status_code:
    
        status_code[ip] = 1

      elif logDict['status'] == argument and ip in status_code:
    
        status_code[ip] = status_code[ip] + 1
        
    else:
    
      print(usage)
        
      break
      
  
  except:
    
    print(usage)
    break
    
    
def status(x):
    
  return x[-1]

    
    
sort = sorted(status_code.items(),key=status,reverse=True)[:15]

for item in sort:

  ip,status = item

  print("{:14} - {}".format(ip,status))

    
access_log.close()
