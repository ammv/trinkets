#from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from data import Values
import os

if __name__ == '__main__':
    names = Values.names()
    imgs = os.listdir('test')
    spaces = ' ' * len(max(imgs, key=len))
    test = []
    for img in imgs:
        if '50r' in img:
            test.append(0)
        elif '100r' in img:
            test.append(1)
        elif '500r' in img:
            test.append(2)
        elif '1000r' in img:
            test.append(3)
        elif '5000r' in img:
            test.append(4)
            
    for x in range(1, 11):
        i = 0
        answers = []
        sv = svm.SVC()
        sv.fit(Values.data()[0], Values.target()[1])
        #neigh = KNeighborsClassifier(n_neighbors=x)
        #neigh.fit(Values.data()[0], Values.target()[1])
        print('Соседи: ',x)
        for img in imgs:
            s = len(img)
            if s != spaces:
                s = ' ' * (len(spaces) + (len(spaces)-s))
            pred = sv.predict(Values.get_data(img))
            answers.append(pred[0])
            print(f'№{i} {img}{s}{names[str(pred[0])]}')
            i += 1

        true_answers = '{1}/{0}'.format(
            len(imgs),len([a for i, a in enumerate(test) if a == answers[i]]))

        print(true_answers)
    
