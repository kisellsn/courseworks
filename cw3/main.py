import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report, \
    f1_score, roc_auc_score, precision_recall_curve
from sklearn.preprocessing import StandardScaler


test_data = pd.read_csv("files/archive/test.csv")
test_data = test_data.drop('Artist Name', axis=1)
test_data = test_data.drop('Track Name', axis=1)

def get_confusion_matrix(y_test, y_pred):
    # матриця помилок
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.show()
if __name__ == '__main__':
    train_data = pd.read_csv("files/archive/train.csv")
    genres = pd.read_csv("files/archive/submission.csv")


    train_data = train_data.drop('Artist Name', axis=1)
    train_data = train_data.drop('Track Name', axis=1)



    print(train_data.info())
    print(train_data.describe())
    print(train_data.head())
    print(train_data.isnull().sum())
    #----------------------- Замінюємо пропущені значення модою за групою
    train_data['key'] = train_data.groupby('Class')['key'].transform(lambda x: x.fillna(x.mode()[0]))
    train_data['instrumentalness'] = train_data.groupby('Class')['instrumentalness'].transform(lambda x: x.fillna(x.mode()[0]))
    train_data['Popularity'] = train_data.groupby('Class')['Popularity'].transform(lambda x: x.fillna(x.mode()[0]))
    # Перевіряємо, чи більше немає пропущених значень
    print(train_data.isnull().sum())

    '''
    # кореляційна матриця
    plt.figure(figsize=(16, 10))
    sns.heatmap(train_data.corr(), annot=True, annot_kws={"size": 14})
    sns.set_style('white')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()
    '''

    # Об'єднуємо дані за допомогою id
    train_data_g = pd.merge(train_data, genres, on="Class")
    '''
    # Рахуємо кількість даних для кожного жанру
    sns.countplot(data=train_data_g, x='Name')
    plt.xticks(rotation=90)
    plt.xlabel("Жанр")
    plt.ylabel("Кількість даних")
    plt.title("Розподіл даних за жанрами")
    plt.show()
    '''



    labels = train_data['Class']
    features = train_data.drop(['Class'], axis=1)
    '''
    #----------------------- графіки розподілу
    columns = features.columns
    num_rows = (len(columns) - 1) // 3 + 1
    num_cols = 3
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))
    for i, col in enumerate(columns):
        ax_row = i // num_cols
        ax_col = i % num_cols
        # Вибираємо поточний підграфік
        ax = axes[ax_row, ax_col] if num_rows > 1 else axes[ax_col]
        sns.histplot(features[col], ax=ax)
        ax.set_title(col)
    plt.tight_layout()
    plt.show()

    '''
    #----------------------- Стандартизуємо дані
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features)
    features = pd.DataFrame(scaled_data, columns=features.columns)
    '''
    columns = features.columns
    num_rows = (len(columns) - 1) // 3 + 1
    num_cols = 3
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))
    for i, col in enumerate(columns):
        ax_row = i // num_cols
        ax_col = i % num_cols
        # Вибираємо поточний підграфік
        ax = axes[ax_row, ax_col] if num_rows > 1 else axes[ax_col]
        sns.histplot(features[col], ax=ax)
        ax.set_title(col)
    plt.tight_layout()
    plt.show()

    '''


    #----------------------- Розділення даних на тренувальний та тестовий набори
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

    # ----------------------- Naive Bayes -----------------------
    nb = GaussianNB(priors=None)
    nb.fit(X_train, y_train)
    y_predG = nb.predict(X_test)
    print("Accuracy Naive Bayes on train data:", nb.score(X_train, y_train))
    print("Accuracy Naive Bayes on test data:", nb.score(X_test, y_test))
    # get_confusion_matrix(y_test, y_pred)
    unique_classes = set(y_test)

    # Ініціалізуємо словник для збереження точності та повноти для кожного класу
    precision = dict()
    recall = dict()

    # Розраховуємо точність та повноту для кожного класу
    for cls in unique_classes:
        # Створюємо бінарний вектор, де 1 означає клас cls, а 0 - інші класи
        binary_true_labels = [1 if label == cls else 0 for label in y_test]
        binary_predicted_labels = [1 if label == cls else 0 for label in y_predG]

        # Розраховуємо точність та повноту за допомогою функції precision_recall_curve
        precision[cls], recall[cls], _ = precision_recall_curve(binary_true_labels, binary_predicted_labels)

        # Виводимо значення точності та повноти для поточного класу
        print(f'Клас: {cls},Точність: {precision[cls][0]}')

    #----------------------- Gradient Boosting -----------------------
    clf = GradientBoostingClassifier(n_estimators=50)
    clf.fit(X_train, y_train)
    y_predGR = clf.predict(X_test)
    print("Accuracy Gradient Boosting Classifier on train data:", clf.score(X_train, y_train))
    print("Accuracy Gradient Boosting Classifier on test data:", clf.score(X_test, y_test))
    #get_confusion_matrix(y_test, y_pred)
    unique_classes = set(y_test)

    # Ініціалізуємо словник для збереження точності та повноти для кожного класу
    precision = dict()
    recall = dict()

    # Розраховуємо точність та повноту для кожного класу
    for cls in unique_classes:
        # Створюємо бінарний вектор, де 1 означає клас cls, а 0 - інші класи
        binary_true_labels = [1 if label == cls else 0 for label in y_test]
        binary_predicted_labels = [1 if label == cls else 0 for label in y_predGR]

        # Розраховуємо точність та повноту за допомогою функції precision_recall_curve
        precision[cls], recall[cls], _ = precision_recall_curve(binary_true_labels, binary_predicted_labels)

        # Виводимо значення точності та повноти для поточного класу
        print(f'Клас: {cls},Точність: {precision[cls][0]}')
    #----------------------- Random Forest -----------------------
    clf = RandomForestClassifier(max_features=50, random_state=42)
    clf.fit(X_train, y_train)
    # Прогнозуємо класи на тестових даних та обчислюємо точність класифікації
    y_predR = clf.predict(X_test)
    print("Accuracy Random Forest Classifier on train data:", clf.score(X_train, y_train))
    print("Accuracy Random Forest Classifier on test data:", clf.score(X_test, y_test))
    #get_confusion_matrix(y_test, y_pred)
    unique_classes = set(y_test)

    # Ініціалізуємо словник для збереження точності та повноти для кожного класу
    precision = dict()
    recall = dict()

    # Розраховуємо точність та повноту для кожного класу
    for cls in unique_classes:
        # Створюємо бінарний вектор, де 1 означає клас cls, а 0 - інші класи
        binary_true_labels = [1 if label == cls else 0 for label in y_test]
        binary_predicted_labels = [1 if label == cls else 0 for label in y_predR]

        # Розраховуємо точність та повноту за допомогою функції precision_recall_curve
        precision[cls], recall[cls], _ = precision_recall_curve(binary_true_labels, binary_predicted_labels)

        # Виводимо значення точності та повноти для поточного класу
        print(f'Клас: {cls},Точність: {precision[cls][0]}')


    #----------------------- K Neighbors -----------------------
    #Пошук найкращих параметрів для методу KNN 
    knn = KNeighborsClassifier()
    parameters={'n_neighbors':range(2,25)}
    gridsearch=GridSearchCV(knn, parameters,cv=10,verbose=1)
    gridsearch.fit(X_train,y_train)
    print ("Best parametrs for KNN-", gridsearch.best_estimator_)

    knn = KNeighborsClassifier(n_neighbors=24)
    knn.fit(X_train, y_train)
    y_predK = knn.predict(X_test)
    print("Accuracy K Neighbors Classifier on train data:", knn.score(X_train, y_train))
    print("Accuracy K Neighbors Classifier on test data:", knn.score(X_test, y_test))
    #get_confusion_matrix(y_test, y_pred)
    unique_classes = set(y_test)

    # Ініціалізуємо словник для збереження точності та повноти для кожного класу
    precision = dict()
    recall = dict()

    # Розраховуємо точність та повноту для кожного класу
    for cls in unique_classes:
        # Створюємо бінарний вектор, де 1 означає клас cls, а 0 - інші класи
        binary_true_labels = [1 if label == cls else 0 for label in y_test]
        binary_predicted_labels = [1 if label == cls else 0 for label in y_predK]

        # Розраховуємо точність та повноту за допомогою функції precision_recall_curve
        precision[cls], recall[cls], _ = precision_recall_curve(binary_true_labels, binary_predicted_labels)

        # Виводимо значення точності та повноти для поточного класу
        print(f'Клас: {cls},Точність: {precision[cls][0]}')

    #----------------------- Побудова матриць помилок
    cm1 = confusion_matrix(y_test, y_predGR)
    cm2 = confusion_matrix(y_test, y_predR)
    cm3 = confusion_matrix(y_test, y_predK)
    cm4 = confusion_matrix(y_test, y_predG)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    sns.heatmap(cm1, annot=True, cmap='Greens', fmt='g', ax=axes[0, 0])
    axes[0, 0].set_xlabel('Predicted label')
    axes[0, 0].set_ylabel('True label')
    axes[0, 0].set_title('Gradient Boosting Classifier')

    sns.heatmap(cm2, annot=True, cmap='Purples', fmt='g', ax=axes[0, 1])
    axes[0, 1].set_xlabel('Predicted label')
    axes[0, 1].set_ylabel('True label')
    axes[0, 1].set_title('Random Forest Classifier')

    sns.heatmap(cm3, annot=True, cmap='BuPu', fmt='g', ax=axes[1, 0])
    axes[1, 0].set_xlabel('Predicted label')
    axes[1, 0].set_ylabel('True label')
    axes[1, 0].set_title('K Neighbors Classifier')

    sns.heatmap(cm4, annot=True, cmap='YlOrRd', fmt='g', ax=axes[1, 1])
    axes[1, 1].set_xlabel('Predicted label')
    axes[1, 1].set_ylabel('True label')
    axes[1, 1].set_title('Naive Bayes  Classifier')

    plt.tight_layout()
    plt.show()