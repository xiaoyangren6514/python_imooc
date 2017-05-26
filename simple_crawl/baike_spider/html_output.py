# encoding=utf8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        with open('output.html', 'w') as fout:
            fout.write('<html>')
            fout.write('<body>')
            fout.write('<table>')

            for data in self.datas:
                print(data)
                # fout.write('<tr>')
                # fout.write('<td>%s</td>' % data['url'])
                # fout.write('<td>%s</td>' % data['title'])
                # fout.write('<td>%s</td>' % data['summary'])
                # fout.write('</tr>')

            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')
