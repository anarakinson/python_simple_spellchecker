# Simple spellchecker RU-EN

В рамках соревнования была поставлена задача за короткий срок (1.5 дня) разработать быстро работающий spellchecker для поисковой системы, способный исправлять орфографические ошибки, ошибки раскладки и ошибки слипшихся слов.

В качестве основы решения были использованы три элемента: свободное ПО Hunspell, свободная библиотека wordninja и простой скрипт подстановки для исправления раскладки.

Hunspell — свободное ПО для проверки орфографии языков со сложной системой словообразования и морфологией. Выбран за свою скорость и качество обработки грамматики.

wordninja - свободное ПО для разделения слипшихся слов по морфологическим признакам. Изначально библиотека предназначена только для английского языка. Была доработана для работы с русским языком.


---

Пример орфографической ошибки: превед - привед -> привет

Пример ошибки раскладки: ghbdtn -> привет

Пример ошибки слипшихся слов: приветкакдела -> привет как дела


---

Скрипт принимает строку и возвращает словарь с вариантами исправления.

```
text = "приветдрузья hello rfr ltkf дывочка"

print(spellcheck(text))

>>> {0: 'привет друзья hello как дела девочка', 
>>>  1: 'привет друзья hello как дела дырочка', 
>>>  2: 'привет друзья hello как дела дымочка', 
>>>  3: 'привет друзья hello как дела'}
```

У спеллчекера отсутствует какое либо внутреннее ранжирование вариантов исправлений. Есть идея добавить простой алгоритм (скорее всего на базе эмбеддингов) для ранжирования каждого слова на каждой позиции. 

Этот функционал планируется доработать когда-нибудь никогда.


---

Словари взяты из репозитория: https://github.com/titoBouzout/Dictionaries/
