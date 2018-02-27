# coding:utf-8
import codecs

class DataOutput(object):

	def __init__(self):
		self.datas = []

	def store_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = codecs.open('baike.html','w',encoding='GBK')
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>"%data['url'])
			fout.write("<td>%s</td>"%data['title'])
			fout.write("<td>%s</td>"%data['summary'])
			fout.write("</tr>")
			self.datas.remove(data)
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		fout.close()

'''
此方法并不是很好的方式，更好的做法应该是将数据分批存储到文件，而不是将所有数据存储到内存。
一次性写入文件容易是系统出现异常，造成数据丢失。
由于我们只需要100条数据，速度很快，所以这种方法可行。
'''