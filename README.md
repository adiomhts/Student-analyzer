
# Studentы analyzer



This code is made for analyzing database about students and it can do literally nothing.
BUT it gives a number... and thats all.

there will be a picture


## What this programm actually does?
Actually this programm can be very helpful if you want to know who would buy studying courses
This programm analyzes really big dataframe. And studying while does that. 

there will be a picture
## How it works?

The programm is made with nearest neighbors priciple, and what does it means?
For example: you can give the data about a Student (I don't actually know how) and it will make kinda graph (as i understand) (и здесь я понял что устал писать на английском)
график, на котором будет отыскивать ближайших соседей по разным параметрам (однажды поставил включать в исследование 4799 соседей и мне удалось загрузить мой проц так что ноут казалось бы взлетит в космос, к слову больше не есть лучше(успешность была всего около 50 проценту))

| neighbors | sucsess  | 
| :-------- | :------- | 
|4799|~54%|
|3|~70|
|2000|82%|
|1600|~83%|
|999|up to 84.1|


сейчас программа показывает результаты около 80-84 процентов правильных. Это значит что с вероятностью 80-84 процента программа подскажет, является ли этот ученик потенциальным покупателем учебных курсов.





для увеличения точности приходилось прибегать к "костылям" например, в исходных данных предоставлен список языков которые знает ученик.

Однако машинное обучение работает по математической модели, логически можно понять что оно принимает только численные данные. Потому пришлось сделать новые данные 

