def train():
    import pickle
    import sklearn
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    import numpy as np
    from sklearn.metrics import confusion_matrix
    import seaborn
    import matplotlib.pyplot as plt
    from sklearn.metrics import classification_report


    data_dict = pickle.load(open('./onehand.pickle', 'rb'))
    data_dict2 = pickle.load(open('./twohand.pickle', 'rb'))
    data_one = np.asarray(data_dict['data'])
    data_two = np.asarray(data_dict2['data'])
    labels1 = np.asarray(data_dict['labels'])
    labels2 = np.asarray(data_dict2['labels'])


    x_train, x_test, y_train, y_test, = train_test_split(data_one, labels1, test_size=0.2, shuffle=True, stratify=labels1)
    x_train2, x_test2, y_train2, y_test2, = train_test_split(data_two, labels2, test_size=0.2, shuffle=True, stratify=labels2)

    model1 = RandomForestClassifier()
    model2 = RandomForestClassifier()

    model1.fit(x_train, y_train)
    model2.fit(x_train2, y_train2)

    y_predict = model1.predict(x_test)
    y_predict2 = model2.predict(x_test2)

    conf_mat1 = confusion_matrix(y_test, y_predict)
    print(conf_mat1)

    conf_mat2 = confusion_matrix(y_test2, y_predict2)
    print(conf_mat2)


    seaborn.heatmap(conf_mat1)
    plt.show()
    seaborn.heatmap(conf_mat2)
    plt.show()

    # print("Classification report of One Handed ISL Predictions")
    # print(classification_report(y_test, y_predict))

    # print("Classification report of Two Handed ISL Predictions")
    # print(classification_report(y_test2, y_predict2))


    score1 = accuracy_score(y_predict, y_test)
    score2= accuracy_score(y_predict2, y_test2)

    print('{}% of samples were classified correctly for model1 !'.format(score1 * 100))
    print('{}% of samples were classified correctly for model2 !'.format(score2 * 100))

    f = open('model1.p', 'wb')
    pickle.dump({'model1': model1}, f)
    f.close()
    f = open('model2.p', 'wb')
    pickle.dump({'model2': model2}, f)
    f.close()
