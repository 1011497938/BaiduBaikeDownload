# coding:utf-8
import time
import os

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.time = time.strftime('%Y_%m_%d %H_%M_%S',time.localtime(time.time()))

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('./data/' + self.time + '_output.html','w', encoding='utf-8')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()

    def output_text(self, data, isNeed = True):
        if isNeed:
            dirPath = './data/' + self.time
        else:
            dirPath = './data/' + self.time + '/trash'
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        fout = open(dirPath + '/' + data['title'],'w', encoding='utf-8')
        fout.write(data['title'] + '\n')
        fout.write(data['url'] + '\n')
        fout.write(data['summary'] + '\n')
        fout.write(data['content'] + '\n')
        fout.close()