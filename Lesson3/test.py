import re
# Найти все цифры в тексте
pattern = '[0-9]+k'
string = 'If 300 spartans were so brave, so 500 spartans' \
' could destroy more than 10k warriors of Darius, but 15k and even 20k'
print(re.findall(pattern, string))
# Найти все диапазоны
pattern2 = '[0-9]+ *- *[0-9]+'
string2 = 'The temperature can be in range 10- 15C next week ' \
'though it was lesser last week(4 - 9C). It was even ' \
'-5 some time ago'
print(re.findall(pattern2, string2))

log = [
'64 bytes from localhost.localdomain (127.0.0.1): '
'icmp_req=1 ttl=64 time=0.033 ms',
'64 bytes from localhost.localdomain (127.0.0.1): '
'icmp_req=2 ttl=64 time=0.034 ms',
'64 bytes from localhost.localdomain (127.0.0.1): '
'icmp_req=3 ttl=64 time=0.031 ms',
'64 bytes from localhost.localdomain (127.0.0.1): '
'icmp_req=4 ttl=64 time=0.031 ms']
pattern = re.compile('(icmp_req=[\d]+).*(time=[\d\.]+ ms)')
result = []
for line in log:
    result.append(pattern.search(line).groups())
print(result)
# Извлечём из html-кода только теги
html = '<p style="margin-left:10px;">text' \
'<b class="super-bold">bold text</b>.</p>'
pattern = '<[^>]+>'
print(re.findall(pattern, html))
