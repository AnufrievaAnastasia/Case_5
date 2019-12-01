"""Case-study #4 Парсинг web-страниц
Разработчики:
Ануфриева
Журавлева

"""
import urllib.request

output_file = open('output.txt', 'w')
output_file.close()

with open('input.txt') as out_file:
    line = out_file.readline()
    while line != '':
        url = line
        f = urllib.request.urlopen(url)
        s = f.read()
        text = str(s)
        part_name = text.find("player-name")
        name = text[text.find('>', part_name) + 1:text.find('&', part_name)]
        part_total = text.find("TOTAL")
        total = text[text.find('<td>', part_total)+ 4:text.find('</tr>', part_total)]
        total = total.replace('t', '')
        total = total.replace('n', '')
        total = total.replace('\\', '')
        total = total.replace('</d><d>', ' ')
        total = total.replace('</d>', '')
        total = total.split()
        comp = total[0]
        att = total[1]
        yds = total[3]
        td = total[5]
        int = total[6]
        player = name + ' ' + comp + ' ' + att + ' ' + yds + ' ' + td + ' ' + int



        print(player)
        line = out_file.readline()

