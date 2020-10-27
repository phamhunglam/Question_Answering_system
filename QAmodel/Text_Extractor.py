import re

class QA:
    def Question_Extraction(qa, doc):
        if (qa == 'NAM_SINH'):
            if (re.search(r'[0-9]{4}', doc)):
                result = re.findall(r'[0-9]{4}', doc)
                # print('Answer: ' + str(result[0]))
                # print('Top answers: ')
                # for x in result:
                #     print(x)
                return result[0]
            else:
                print('Answer: None')
        elif (qa == 'NAM_MAT'):
            if (re.search("mất", doc)):
                rs_1 = re.findall(r'mất+[^.!?]*[0-9][^\s\.\,]*', doc)
                rs_2 = re.findall(r'[0-9]{4}', rs_1[0])
                # print('Answer: ' + str(rs_2[0]))
                # print('Top answers: ')
                # for x in rs_2:
                #     print(x)
                return rs_2[0]
            elif (re.search(r'[0-9]{4}', doc)):
                result = re.findall(r'[0-9]{4}', doc)
                # print('Answer: ' + str(result[1]))
                # print('Top answers: ')
                # for x in result:
                #     print(x)
                return result[1]
            else:
                print('Answer: None')

        elif (qa == 'QUE_QUAN'):
            if re.search(r'tỉnh+[^.!?]*[A-ZĐ][^\s\.\,\)\(]*', doc):
                result_1 = re.search(r'tỉnh+[^.!?]*[A-ZĐ][^\s\.\,\)\(]*', doc)
                result_2 = re.search(r'[A-ZĐ]+[^\s\.\,]*\s+([A-ZĐ]+[^\s\,\.\(\)]*\s*)*', result_1.group())
                # print('Answer: ' + result_2.group())
                return result_2.group()
            elif re.search(r'thành phố+[^.!?]*[A-ZĐ][^\s\.\,\)\(]*', doc):
                result_1 = re.search(r'thành phố+[^.!?]*[A-ZĐ][^\s\.\,\)\(]*', doc)
                result_2 = re.search(r'[A-ZĐ]+[^\s\.\,]*\s+([A-ZĐ]+[^\s\,\.\(\)]*\s*)*', result_1.group())
                # print('Answer: ' + result_2.group())
                return result_2.group()
            else:
                print('Answer: ' + 'None')
        elif (qa == 'NAM_DO'):
            if re.search(r"[A-ZĐỨ]+[^\s\.\,]*\s+([A-ZĐỨ]+[^\s\,\.\(\)]*\s*)* +thứ +[0-9][^\s\.\,\)\(]*", doc):
                result = re.search(r"[A-ZĐỨ]+[^\s\.\,]*\s+([A-ZĐỨ]+[^\s\,\.\(\)]*\s*)* +thứ +[0-9][^\s\.\,\)\(]*", doc)
                # print('Answer: ' + result.group())
                return result.group()
            elif re.search(r"[A-ZĐỨ]+[^\s\.\,]*\s+([A-ZĐỨ]+[^\s\,\.\(\)]*\s*)* +năm thứ +[0-9][^\s\.\,\)\(]*", doc):
                result = re.search(r"[A-ZĐỨ]+[^\s\.\,]*\s+([A-ZĐỨ]+[^\s\,\.\(\)]*\s*)* +năm thứ +[0-9][^\s\.\,\)\(]*",
                                   doc)
                # print('Answer: ' + result.group())
                return result.group()
            else:
                print('Answer: ' + 'None')
