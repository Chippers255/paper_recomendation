import os
import tfidf
import extract

from nltk.corpus import stopwords

def doc_fix(doc):
    new_doc = doc

    new_doc = new_doc.replace('.', ' ')
    new_doc = new_doc.replace(',', ' ')
    new_doc = new_doc.replace('/', ' ')
    new_doc = new_doc.replace('(', ' ')
    new_doc = new_doc.replace(')', ' ')
    new_doc = new_doc.replace(';', ' ')
    new_doc = new_doc.replace(':', ' ')

    new_doc = new_doc.lower()

    stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you','your', 'yours',
            'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
            'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
            'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
            'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
            'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
            'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
            'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
            'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
            'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'dx',
            'publisher', '&', 'http', 'pdf', 'org', 'com', 'e', 'j', 'c', 'r', 'et', 'al', 'm']

    new_doc = new_doc.split()

    for s in stop:
        new_doc = [x for x in new_doc if x != s]

    return new_doc
# end def doc_fix

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

pdf_list = []
for (dir_path, dir_names, file_names) in os.walk(SCRIPT_PATH):
    for file in file_names:
        if '.pdf' in file:
            pdf_list.append(os.path.join(dir_path, file))

doc_list = []
for pdf_path in pdf_list:
    print pdf_path
    doc_list.append(doc_fix(extract.convert_pdf_to_txt(pdf_path)))


score_list = []
for word in doc_list[0]:
    sc = [word, tfidf.tf_idf(word, doc_list[0], doc_list)]
    if sc not in score_list:
        score_list.append(sc)


sort_list = sorted(score_list, key=lambda l: l[1], reverse=True)
for s in sort_list:
    print s