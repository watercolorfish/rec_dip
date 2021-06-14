from lxml import etree
import pickle
import os

steps_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
octavs_dict = [0, 1, 2, 3, 4, 5, 6, 7, 8]
types_dict = {'breve': 0, 'whole': 1, 'half': 2, 'quarter': 3, 'eighth': 4, '16th': 5, '32nd': 6, '64th': 7}
syllabic_dict = {'single': 0, 'begin': 1, 'middle': 2, 'end': 3}

def generate_list_of_xml():
    with open('path_data.pickle', 'rb') as f:
        data = pickle.load(f)
    return os.listdir(data.get("trainPath"))

def parce_from(file):
    tree = etree.parse(file)
    melody = list()

    parts = tree.xpath('/score-partwise/part')
    for part in parts:
        partschild = part.getchildren()
        for measurechild in partschild:
            if measurechild.tag == "measure":
                measurechilds = measurechild.getchildren()
                for notechild in measurechild:
                    if notechild.tag == "note":
                        notechilds = notechild.getchildren()
                        step = None
                        octave = None
                        type = None
                        text = None
                        syllabic = None
                        for note_components in notechilds:
                            if note_components.tag == "pitch":
                                pitchchilds = note_components.getchildren()
                                for pitch in pitchchilds:
                                    if pitch.tag == "step":
                                        step = steps_dict[pitch.text]
                                    if pitch.tag == "octave":
                                        octave = int(pitch.text)
                            if note_components.tag == "type":
                                type = types_dict[note_components.text]
                        if step != None:
                            melody.append(str(step)+', '+str(octave)+', '+str(type))
    return melody

def check_for_new_files():
    for file in generate_list_of_xml():
        if file.count("[trained]")==0:
            return True
    return False

def generate_sample():
    melody = list()
    ans = str()
    for file in generate_list_of_xml():
        if file.count("[trained]")>0:
            continue
        with open('path_data.pickle', 'rb') as f:
            path = pickle.load(f)
        f = str(path.get("trainPath")) + "/"+ str(file)
        tree = etree.parse(f)
        parts = tree.xpath('/score-partwise/part')
        for part in parts:
            partschild = part.getchildren()
            for measurechild in partschild:
                if measurechild.tag == "measure":
                    measurechilds = measurechild.getchildren()
                    for notechild in measurechild:
                        if notechild.tag == "note":
                            notechilds = notechild.getchildren()
                            step = None
                            octave = None
                            type = None
                            text = None
                            syllabic = None
                            for note_components in notechilds:
                                if note_components.tag == "pitch":
                                    pitchchilds = note_components.getchildren()
                                    for pitch in pitchchilds:
                                        if pitch.tag == "step":
                                            step = steps_dict[pitch.text]
                                        if pitch.tag == "octave":
                                            octave = int(pitch.text)
                                if note_components.tag == "type":
                                    type = types_dict[note_components.text]
                                if note_components.tag == "lyric":
                                    lyricchilds = note_components.getchildren()
                                    for lyric in lyricchilds:
                                        if lyric.tag == "text":
                                            text = lyric.text
                                        if lyric.tag == "syllabic":
                                            syllabic = syllabic_dict[lyric.text]
                            melody.append([[step, octave, type],[syllabic,text]])
        #os.rename(path.get("trainPath")+"/"+file, path.get("trainPath") + "/" + file[:-4]+"[trained].xml")
    for note in melody:
        if note[1][0]:
            ans+=str(note[0])+"\t"+str(note[1])+"\n"
    return([i.split('\t') for i in (ans[:-1].strip().split('\n'))])