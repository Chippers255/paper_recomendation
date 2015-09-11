import math

def word_freq(word, doc):
    return float(doc.count(word))
# end def word_freq

def word_count(doc):
    return float(len(doc))
# end def word_count

def tf(word, doc):
    return float(word_freq(word, doc) / word_count(doc))
# end def tf

def n_containing(word, doc_list):
    count = 0
    for doc in doc_list:
        count += 1 if word_freq(word, doc) > 0 else 0

    return float(count + 1)
# end def n_containing

def idf(word, doc_list):
    return float(math.log(len(doc_list)) / n_containing(word, doc_list))
# end def idf

def tf_idf(word, doc, doc_list):
    return float((tf(word, doc) * idf(word, doc_list)))
# end def tf_idf

