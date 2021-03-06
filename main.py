import os
import tfidf
import extract
import jaccard

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
    new_doc = new_doc.replace('-', ' ')
    new_doc = new_doc.replace('=', ' ')
    new_doc = new_doc.replace('0', ' ')
    new_doc = new_doc.replace('1', ' ')
    new_doc = new_doc.replace('2', ' ')
    new_doc = new_doc.replace('3', ' ')
    new_doc = new_doc.replace('4', ' ')
    new_doc = new_doc.replace('5', ' ')
    new_doc = new_doc.replace('6', ' ')
    new_doc = new_doc.replace('7', ' ')
    new_doc = new_doc.replace('8', ' ')
    new_doc = new_doc.replace('9', ' ')
    new_doc = new_doc.replace('"', ' ')
    new_doc = new_doc.replace("'", ' ')

    new_doc = new_doc.lower()

    new_doc = new_doc.replace('jolicoeur', ' ')
    new_doc = new_doc.replace('tnq', ' ')
    new_doc = new_doc.replace('vstm', 'visual short term memory')
    new_doc = new_doc.replace('vwm', 'visual working memory')
    new_doc = new_doc.replace('spcn', 'sustained posterior contralateral negativity')
    new_doc = new_doc.replace('ips', 'intraparietal sulcus')


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
            'publisher', '&', 'http', 'pdf', 'org', 'com', 'e', 'j', 'c', 'r', 'et', 'al', 'm', 'l',
            'books', 'publish', 'reviewer', 'copy', 'p', 'doi']

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


score_list_1 = []
for word in doc_list[0]:
    sc = [word, tfidf.tf_idf(word, doc_list[0], doc_list)]
    if sc not in score_list_1:
        score_list_1.append(sc)

score_list_2 = []
for word in doc_list[1]:
    sc = [word, tfidf.tf_idf(word, doc_list[1], doc_list)]
    if sc not in score_list_2:
        score_list_2.append(sc)

sort_list_1 = sorted(score_list_1, key=lambda l: l[1], reverse=True)
sort_list_2 = sorted(score_list_2, key=lambda l: l[1], reverse=True)

print
print sort_list_1[:50]
print sort_list_2[:50]
print
print jaccard.jaccard_distance(sort_list_1, sort_list_2, top=50)
