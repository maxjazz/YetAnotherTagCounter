# YetAnotherTagCounter
Home project for Python Introduction Course

Программа для подсчета количества html тегов на странице

Получения списка тегов

yatc.py --get 'http://yandex.ru'
или
yatc.py -g 'http://yandex.ru'

Вывод:

+----------+-----------+
| Tags     |   Numbers |
|----------+-----------|
| aqwf     |         1 |
| body     |         1 |
| dqs      |         1 |
| form     |         1 |
| head     |         1 |
| html     |         1 |
| title    |         1 |
| br       |         2 |
| button   |         2 |
| path     |         2 |
| svg      |         2 |
| input    |         3 |
| style    |         3 |
| noscript |         4 |
| ol       |         4 |
| img      |         6 |
| i        |         7 |
| ul       |        10 |
| link     |        15 |
| meta     |        16 |
| h1       |        18 |
| script   |        18 |
| li       |        54 |
| a        |       144 |
| span     |       260 |
| div      |       379 |
+----------+-----------+

Прочитать сохраненные данные в БД
yatc.py --view "http://yandex.ru"

