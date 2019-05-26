#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.externals import joblib


def identify_intention(chuoi):
    result = {}
    test_data = []
    test_data.append({"body": chuoi})
    df_test = pd.DataFrame(test_data)

    clf = joblib.load('D:/TK 13.3/Doantotnghiep/Code/demo/save/data.pkl', )
    predicted = clf.predict_proba(df_test["body"])
    for x in predicted:
        for y in range(0, len(x)):
            if x[y] > 0.56:
                bool = True
                break
            else:
                bool = False
    if bool:
        result['status'] = 'Có'
        predicted = clf.predict(df_test["body"])
        result['name'] = predicted[0]
    elif bool is False:
        result['status'] = 'Khong'

    return result
