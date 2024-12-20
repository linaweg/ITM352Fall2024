import urllib.request

url = https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data

ssl._create_default_http_context = ssl._create_unvertified_context
webpage =url.request.urlopen(url)

for line in web:
  print(line.decode()"utf-8") 
  if "<title>" in html:line:
  print(html_line)