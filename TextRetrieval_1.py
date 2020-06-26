import sys
import glob
import lucene
import re

from java.nio.file import Path, Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, StoredField, StringField, TextField

from org.apache.lucene.index import IndexOptions, IndexWriter, IndexWriterConfig, DirectoryReader

from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import IndexReader

from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory


class IR:
    directory = None
    analyzer = None
    indexer = None
    searcher = None
    queryparser = None
    MAX = 1000
    def __init__(self, path):
        self.directory = SimpleFSDirectory(Paths.get(path))
        self.analyzer = StandardAnalyzer()
        cf = IndexWriterConfig(self.analyzer)		
        cf.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
        self.indexer = IndexWriter(self.directory, cf)
        
    def index(self, path):
        print("Indexing " + path)
        for f in glob.glob(path + "\*.*"):
            r = open(f, "r", encoding="utf-8")
            content = r.read()
            
            doc = Document()
            noidung = TextField("noidung", content, Field.Store.YES)
            doc.add(noidung)
            self.indexer.addDocument(doc)

        self.indexer.close()
        
    def openIndex(self):
        reader = DirectoryReader.open(self.directory)
        self.searcher = IndexSearcher(reader)
        self.queryparser = QueryParser("noidung", self.analyzer)
    
    def search(self, strQry):
        query = self.queryparser.parse(strQry)
        hits = self.searcher.search(query, self.MAX)
        print(len(hits.scoreDocs), "Result of " + strQry)

#		for hit in hits.scoreDocs:
#			print(hit.score, hit.doc, hit.toString())
#			doc = self.searcher.doc(hit.doc)
#			print(doc.get("noidung"))
#			print("============================================")
        print('Top 1 result from doc: ' + str(hits.scoreDocs[0].doc))
        doc_1 = self.searcher.doc(hits.scoreDocs[0].doc)
        QA.Question_Extraction(strQry,doc_1.get("noidung"))

        
class QA:
    def Question_Extraction(qa, doc):
        if(re.search("sinh năm", qa)):
            result = re.findall(r'[0-9]{4}', doc)
            print(result[0])
        elif(re.search("mất năm", qa)):
            if(re.search("mất",doc)):
                rs_1 = re.findall(r'mất+[^.!?]*[0-9][^\s\.\,]*',doc)
                rs_2 = re.findall(r'[0-9]{4}',rs_1[0])
                print(rs_2[0])
            else:
                result = re.findall(r'[0-9]{4}', doc)
                print(result[1])
        elif(re.search("ở đâu",qa)):
            result_1 = re.search(r'tỉnh+[^.!?]*[A-Z][^\s\.\,\)\(]*',doc)
            result_2 = re.search(r'[A-ZĐ]+[^\s\.\,]*\s+([A-ZĐ]+[^\s\,\.\(\)]*\s*)*',result_1.group())
            print(result_2.group())
        elif(re.search('đổ năm',qa)):
            result_1 = re.search(r'[\.]+[^.!?]*thứ +[0-9][^\s\.\,\)\(]*',doc)
            result_2 = re.search(r"[A-ZĐỨ]+[^\s\.\,]*\s+([A-ZĐỨ]+[^\s\,\.\(\)]*\s*)* +thứ +[0-9][^\s\.\,\)\(]*",result_1.group())
            print(result_2.group())
            






lucene.initVM()
engine = IR("index")
engine.index("Data")
engine.openIndex()
question = input('Question: ')
engine.search(question)

    


