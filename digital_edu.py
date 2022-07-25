import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score



df = pd.read_csv('train.csv')

# df.info()

# education_form переделать в цифры
# education_status переделать в цифры
# langs удoлить
# life_main False заменить на цифру
# occupation_type переделать в цифры
# occupation_name удалить
# career_start False заменить или удалить
# career_end False заменить или удалить

def clean_form(self):
    if self == 'Full-time':
        return 1
    if self == 'Distance Learning':
        return 2
    if self == 'Part-time':
        return 3

def clean_type(self):
    if self == 'Alumnus (Specialist)':
        return 1
    if self == 'Student (Specialist)':
        return 2
    if self == "Student (Bachelor's)":
        return 3
    if self == "Student (Bachelor's)":
        return 4
    if self == "Alumnus (Master's)":
        return 5
    if self == 'PhD':
        return 6
    if self == "Student (Master's)":
        return 7
    if self == 'Undergraduate applicant':
        return 8
    if self == 'Candidate of Sciences':
        return 9


def clean_false(self):
    if self == 'False':
        return -1
    else:
        return self
def clean_occup_type(self):
    if self == 'university':
        return 0
    if self == 'work':
        return 1

def tofloat(self):
    return float(self)

def langs_clean(self):
    if self == 'False':
        return 0
    else:
        if not ';' in self:
            return 1
        else:
            return (self.count(';')+1)
        


df['education_form'] = df['education_form'].apply(clean_form)
df['education_status'] = df['education_status'].apply(clean_type)
# df = df.drop('langs', axis=1)
df['life_main'] = df['life_main'].apply(clean_false)
df['occupation_type'] = df['occupation_type'].apply(clean_occup_type)
df = df.drop('occupation_name', axis=1)
df['career_start'] = df['career_start'].apply(clean_false)
df['career_end'] = df['career_end'].apply(clean_false)
df = df.fillna({'bdate': '01.01.1901'})
df = df.fillna({'education_form': 0})
df = df.fillna({'education_status': 0})
df = df.drop('city', axis=1)

df['life_main'] = df['life_main'].apply(tofloat)
df['people_main'] = df['people_main'].apply(clean_false)
df['people_main'] = df['people_main'].apply(tofloat)
df['career_start'] = df['career_start'].apply(tofloat)
df['career_end'] = df['career_end'].apply(tofloat)

df = df.drop('bdate', axis=1)
df = df.drop('last_seen', axis=1)


df['langs'] = df['langs'].apply(langs_clean)
df = df.dropna()

# print(df['langs'].value_counts())

# df.info()

x = df.drop('result', axis = 1)
y = df['result']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = KNeighborsClassifier(n_neighbors = 999)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

percent = accuracy_score(y_test, y_pred) * 100

print(percent)







