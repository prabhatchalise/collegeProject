import os
import re
from nltk.parse.stanford import StanfordDependencyParser
from nltk.corpus import stopwords

# for connecting with StanfordNLP
path = 'E:\stanford-corenlp-full-2018-02-27'  # Set this to where you have downloaded the JAR file to
path_to_jar = path + '\stanford-corenlp-3.9.1.jar'
path_to_models_jar = path + '\stanford-corenlp-3.9.1-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
os.environ['JAVAHOME'] = 'C:\Program Files\Java\jdk-9.0.4'  # Set this to where the JDK is

regexpSubj = re.compile(r'subj')
regexpObj = re.compile(r'obj')
regexNouns = re.compile("^N.*|^PR.*")

stopWords = set(stopwords.words('english'))


def get_compounds(triples, word):
    compound = []
    for t in triples:
        if t[0][0] == word:
            if regexNouns.search(t[2][1]):
                compound.append(t[2][0])
    return compound


# removes unnecessary []
def proper_list(topic):
    s = topic
    proper_list = []

    for i in s:
        if isinstance(i, list):
            for j in i:
                proper_list.append(j)

        else:
            proper_list.append(i)

    return proper_list


# removes stop word and make proper list
def wordfilter(words):
    wordsFiltered = []
    words = words
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    return wordsFiltered


# return subject, root and object from sentence
def topic(sentence):
    result = dependency_parser.raw_parse(sentence)
    dep = next(result)
    root = [dep.root["word"]]
    root.append(get_compounds(dep.triples(), root))
    subj = []
    obj = []

    for t in dep.triples():
        if regexpSubj.search(t[1]):
            subj.append(t[2][0])
            subj.append(get_compounds(dep.triples(), t[2][0]))
        if regexpObj.search(t[1]):
            obj.append(t[2][0])
            obj.append(get_compounds(dep.triples(), t[2][0]))

    subj = wordfilter(proper_list(subj))
    root = wordfilter(proper_list(root))
    obj = wordfilter(proper_list(obj))

    return subj, root, obj
