# **Проект "ClientsPlanner"**

### _Данный проект реализует интерфейсное приложение для учета клиентов спорткомплекса_
Представьте, что Вы являетесь тренером по фитнесу, и у вас есть собственная студия.
У Вас есть клиенты, которые оплачивают какое-то количество занятий и ходят на них.
Так как всех запомнить нельзя, Вы должны вести учет ваших клиентов: их ФИО, контакты, сколько занятий у них имеется и тд.
Также Вам было бы полезно иметь расписание ваших занятий, чтобы планировать свое время и дела.
Не лишним будет Вам, как бизнесмену, вести месячные отчеты, чтобы понимать, на какие занятия ходит больше людей, какой заработок за месяц у Вас есть и много другое.

В целом, для всего этого есть отдельные приложения, но гораздо удобнее когда все есть в одном месте и с функциями, которые будут вам полезны.

### _Возможности приложения_
В данном приложении Вам доступно 3 основных Tab-а: Таб с планировщиком, Таб с базой данных клиентов, Таб с месячными отчетами.

Также Вы можете настраивать приложение в соответствующем окне "Настройки" и ознакомиться с функционалом приложения в окне "О программе".

###### _Tab 1_
На "Планировщике" Вы можете просматривать и добавлять занятия и клиентов, посетивших их, в специальные таблицы.
Выбрав день на календаре, вы можете просматривать и редактировать списки занятий и клиентов. Вы также можете запустить таймер для занятия, нажав на кнопку "Начать занятие".

###### _Tab 2_
На "Базе данных клиентов" Вам доступна таблицами со всеми клиентами и информацией о них.
Вы можете добавлять и редактировать записи о клиентах, а также просматривать более подробную информацию о них, нажав на кнопку с их ФИ.
Таблицу можно сортировать по колонкам и фильтровать по ФИО (фильтрация чувствительна к регистру). Чтобы произвести оплату за клиента, нажмите на соответствующую кнопку.

Также поясню некоторую логику таблицы. У каждого клиента есть некоторое количество занятий, а также длительность абонемента, 
по истечении которого, вы можете списать ему оставшиеся занятия (программа не будет делать этого для вас).
Если клиент предупредил, что не может какое-то время посещать, чтобы его дни абонемента не сгорали, вы можете сделать его неактивным, поставив соответствующий checkbox.
Для такого "неактивного состояния" есть ограничение в настройках. Если клиент неактивен больше указанного срока, то программа уведомит вас об этом. Далее вы сами решаете что с этим делать.
При приближении некоторых значений к пороговым, программа будет подсвечивать эти ячейки, чтобы вы обратили на них внимание.
Такая логика была выбрана при общении с реальным тренером и согласована с ним (в защиту целесообразности такого решения).

###### _Tab 3_
На "Отчетах" Вы можете ознакомиться со всей отчетностью за указанный год. В таблице будет приведено количество клиентов, посетивших занятия за месяц, 
а также какую сумму вы заработали (основываясь на платежах за этот месяц). Для более подробной информации о месяце нажмите на кнопку с лупой, тогда откроется окно с подробным описанием всех посещений и оплат в указанный месяц.
"Пустые" месяцы (у которых 0 посещений и 0 оплат) можно скрывать (в настройках). Внизу отображается итоговая сумма за год.

### _Заключение_
В данном файле описывается общие возможности приложения, чтобы узнать конкретно "как сделать что-то?", зайдите во вкладку "О программе".
Также к проекту приложено видео-демонстрация работы приложения.

###### Примечание
Данные в таблице клиентов были составлены случайным набором имен, фамилий и отчеств, а также случайными цифрами для номера телефона.
Любые совпадения случайны, и я точно не знаю до кого вы дозвонитесь, если наберете на эти номера :).
