import numpy as np
import pandas as pd
from QAmodel.Question_classifier import QC


def system(qa):
    QA = qa
    qestion = QC.vect.transform([QA])
    result = QC.clfrNB.predict_proba(qestion)
    result = result * 100
    result = pd.DataFrame(result)
    result_1 = QC.clfrNB.predict(qestion)
    print(result)
    print('Label: ' + result_1[0] + '   Score: ' + str(result[max(result)]))
    from QAmodel.Text_retrieval import engine

    return engine.search(QA, result_1[0]), result_1[0]

