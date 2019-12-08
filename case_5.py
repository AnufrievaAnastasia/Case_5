"""Case-study #4 Парсинг web-страниц
Разработчики:
Ануфриева 70%
Журавлева 60%

"""
import urllib.request

out_file = open('output.txt', 'w')

# To open a file containing links.

with open('input.txt') as inp_file:
    line = inp_file.readline()
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
        comp = comp.replace(',', '')
        att = total[1]
        att = att.replace(',', '')
        yds = total[3]
        yds = yds.replace(',', '')
        td = total[5]
        td = td.replace(',', '')
        int = total[6]
        int = int.replace(',', '')
        a = (float(comp) / float(att) - 0.3) * 5
        b = (float(yds) / float(att) - 3) * 0.25
        c = (float(td) / float(att)) * 20
        d = 2.375 - (float(int) / float(att) * 25)
        pass_rate = ((a + b + c + d) / 6) * 100

        # To group the parameters for each player.

        player = name + ' ' + comp + ' ' + att + ' ' + yds + ' ' + td + ' ' + int + ' ' + '{0:.2f}'.format(pass_rate) + '\n'

        # Print values to a new file.

        out_file.write(player)
        line = inp_file.readline()




