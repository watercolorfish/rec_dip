from lxml import etree
import pickle

def parce_to(filename, path, export):
	tree = etree.parse(filename)
	parts = tree.xpath('/score-partwise/part')
	invers_syll_dict = {0: 'single', 1: 'begin', 2: 'middle', 3: 'end'}
	i=0
	for part in parts:
		partschild = part.getchildren()
		for measurechild in partschild:
			if measurechild.tag == "measure":
				measurechilds = measurechild.getchildren()
				for notechild in measurechild:
					if notechild.tag == "note":
						notechilds = notechild.getchildren()
						if notechild.find("pitch"):
							lyric = etree.SubElement(notechild, 'lyric')
							text = etree.SubElement(lyric, 'text')
							text.text = export[i][1]
							syllabic = etree.SubElement(lyric, 'syllabic')
							if export[i][0].isdigit():
								syllabic.text = invers_syll_dict[int(export[i][0])]
							else:
								syllabic.text = invers_syll_dict[0]
							i = i + 1
	tree.write(path + "/" + filename.split("/")[-1])
	with open('path_data.pickle', 'rb') as f:
	    data = pickle.load(f)
	data["lyricsPath"]=None
	with open('path_data.pickle', 'wb') as f:
		pickle.dump(data, f)