import sys
import glob
import lucene
from QAmodel.Text_Extractor import QA
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
        path = "QAmodel//"+   path
        for f in glob.glob(path + "//*.*"):
            r = open(f, "r", encoding="utf-8")
            content = r.read()
            doc = Document()
            print(doc)
            noidung = TextField("noidung", content, Field.Store.YES)
            doc.add(noidung)
            self.indexer.addDocument(doc)

        self.indexer.close()
        
    def openIndex(self):
        reader = DirectoryReader.open(self.directory)
        self.searcher = IndexSearcher(reader)
        self.queryparser = QueryParser("noidung", self.analyzer)
    
    def search(self, strQry, label):
        query = self.queryparser.parse(strQry)
        hits = self.searcher.search(query, self.MAX)
        # print(len(hits.scoreDocs), "Result of " + strQry)

		# for hit in hits.scoreDocs: 
		# 	print(hit.score, hit.doc, hit.toString())
		# 	doc = self.searcher.doc(hit.doc)
		# 	print(doc.get("noidung"))
		# 	print("============================================")
        #doc = self.searcher.doc(hits.scoreDocs[0].doc)
        #print(doc.get("noidung"))
        # print('Top 1 result from doc: ' + str(hits.scoreDocs[0].doc) + ' with score: ' + str(hits.scoreDocs[0].score))
        doc_1 = self.searcher.doc(hits.scoreDocs[0].doc)
        return QA.Question_Extraction(label,doc_1.get("noidung"))



lucene.initVM()
engine = IR("index")
engine.index("Data")
engine.openIndex()


    


