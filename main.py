import numpy as np
import pandas as pd
from Text_retrieval import engine
from Question_classifier import QC

loop = True
while loop:
    option = input('Nhập cách chọn: 1.Điền từng câu hỏi| 2.Điền nhiều câu hỏi bằng file csv: ')
    option = int(option)
    if option == 1:
        while loop:
            QA = input('Enter Question: ')
            qestion = QC.vect.transform([QA])
            result = QC.clfrNB.predict_proba(qestion)
            result = result * 100
            result = pd.DataFrame(result)
            result_1 = QC.clfrNB.predict(qestion)
            print(result)
            print('Label: ' + result_1[0] + '   Score: ' + str(result[max(result)]))
            engine.search(QA, result_1[0])
    elif option == 2:
        csv_file = input('Nhập tên file csv (questions only): ')
        df_q = pd.read_csv(csv_file)
        df_aq = np.array(df_q)
        count = 1
        for q in df_aq:
            print('câu: ' + str(count))
            question = QC.vect.transform(q)
            result_1 = QC.clfrNB.predict(question)
            engine.search(q[0], result_1[0])
            count = count + 1
        # q = str(df.)

        # for k,q in df_q.items():
        #     q = str(q)
        #     print(type(q))

        #
        #     # result = clfrNB.predict_proba(question)
        #     # result = result * 100
        #     # result = pd.DataFrame(result)
        #     result_1 = clfrNB.predict(question)
        #     # print(result)
        #     # print('Label: ' + result_1[0] + '   Score: ' +str(result[max(result)]))
        #     engine.search(q, result_1[0])
    else:
        raise ValueError('Cách chọn là số 1 hoặc 2!')

