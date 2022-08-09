# access.log-Analysis-via-python
Analyze the access log of apache web server to find various data.


## Scripts and Usage

### dates_hits.py

- Prints Dates on which Most Number of hits took place sorted according to number of hits
- sample O/P

```bash
21/Feb/2021 - 41218
28/Dec/2020 - 7478
25/Dec/2020 - 5644
18/Jan/2021 - 4988
11/Jan/2021 - 4283
08/Jan/2021 - 4056
21/Dec/2020 - 3982
23/Dec/2020 - 3856
20/Dec/2020 - 3698
22/Dec/2020 - 3645
24/Dec/2020 - 3607
07/Jan/2021 - 3098
29/Dec/2020 - 2919
27/Jan/2021 - 2898
09/Jan/2021 - 2805
```

### hits_location.py
- IPs from which most number of hits took place and the Country belongs the IP.
- Sample O/P


```bash
193.106.31.130 -  93873 - Ukraine   
197.52.128.37  -  39660 - Egypt     
173.255.176.5  -   5220 - United States
178.44.47.170  -   2824 - Russia    
51.210.183.78  -   2684 - France    
45.15.143.155  -   1927 - United States
45.144.0.179   -    946 - Germany   
176.222.58.254 -    934 - Germany   
45.132.207.154 -    890 - Germany   
45.153.227.55  -    888 - Germany   
45.138.4.22    -    880 - Germany   
45.153.227.31  -    876 - Germany   
45.138.4.35    -    872 - Germany   
45.132.51.62   -    868 - Germany   
176.222.58.90  -    860 - Germany   
```

### hits_per_ip.py
- IPs with most number Hits Sorted according to Number of hits.
- Sample O/P


```bash
193.106.31.130  - 93873
197.52.128.37   - 39660
173.255.176.5   - 5220
178.44.47.170   - 2824
51.210.183.78   - 2684
45.15.143.155   - 1927
45.144.0.179    - 946
176.222.58.254  - 934
45.132.207.154  - 890
45.153.227.55   - 888
45.138.4.22     - 880
45.153.227.31   - 876
45.138.4.35     - 872
45.132.51.62    - 868
176.222.58.90   - 860
```
### status_code.py
- Prints the number of status code from IPs in descending order
- The status code to search can be provided as argument, Like:
```
Syntax: python3 status_code.py <status code>
``` 
- Sample O/P


```bash
# python3 status_code.py 404

173.255.176.5  - 2026
212.9.160.24   - 99
13.77.204.88   - 78
193.106.30.100 - 75
89.159.228.206 - 72
104.131.51.209 - 63
51.210.243.185 - 58
140.122.127.190 - 45
62.35.7.187    - 41
213.171.211.253 - 37
52.66.242.202  - 36
167.71.100.247 - 32
91.171.55.234  - 28
104.140.103.41 - 27
194.96.112.31  - 25

# python3 status_code.py 403
173.255.176.5  - 32
212.9.160.24   - 27
5.176.255.173.unassigned.as54203.net - 2
145.219.89.34.bc.googleusercontent.com - 2
37.131.204.41  - 2

# python3 status_code.py 200
193.106.31.130 - 58985
51.210.183.78  - 2684
173.255.176.5  - 2154
45.15.143.155  - 1285
45.144.0.179   - 906
176.222.58.254 - 882
45.132.207.154 - 845
45.153.227.55  - 837
45.153.227.31  - 834
45.138.4.22    - 830
45.132.51.62   - 828
45.138.145.131 - 820
45.138.4.35    - 818
176.222.58.90  - 812
45.132.207.221 - 805

# python3 status_code.py
Syntax: python3 status_code.py <status code>

```
### logparser.py
- Converts each line of access log into meaningful dictionary from which we can iterate the data.

```python
import logparser
access_log = open("access.log","r")

for line in access_log:
    
  print(logparser.parser(line))

  break
access_log.close()
```
- sample O/P
```bash
{'host': '13.66.139.0', 'identity': '-', 'user': '-', 'time': '19/Dec/2020:13:57:26 +0100', 'request': 'GET /index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53 HTTP/1.1', 'status': '200', 'size': '32653', 'referer': '-', 'agent': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'}
```

### geomodule.py

- The custom module which contains function to fetch geolocation of an IP using API call.
- The api_key and ip should be passed as argument to the function.
- The api key can be obtained from [This is an external link to ipgeolocation.io]
(https://ipgeolocation.io/)
- sample I/O
```json
'{"ip":"1.1.1.1","continent_code":"NA","continent_name":"North America","country_code2":"US","country_code3":"USA","country_name":"United States","country_capital":"Washington, D.C.","state_prov":"California","district":"Los Angeles","city":"Los Angeles","zipcode":"90012","latitude":"34.05361","longitude":"-118.24550","is_eu":false,"calling_code":"+1","country_tld":".us","languages":"en-US,es-US,haw,fr","country_flag":"https://ipgeolocation.io/static/flags/us_64.png","geoname_id":"5332870","isp":"APNIC Research and Development","connection_type":"","organization":"Cloudflare, Inc.","currency":{"code":"USD","name":"US Dollar","symbol":"$"},"time_zone":{"name":"America/Los_Angeles","offset":-8,"current_time":"2022-08-04 07:43:25.185-0700","current_time_unix":1659624205.185,"is_dst":true,"dst_savings":1}}'
```
