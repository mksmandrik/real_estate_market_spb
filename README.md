# real_estate_market_spb
В данном репозитории я отражу индивидуальные проекты для ШАД Яндекс.Практикум.

Номер | Название проекта и ссылка | О чем проект
--- | --- | ---
№1 | [Исследование надежности кредитных заемщиков](http://localhost:8888/notebooks/%D0%9A%D1%80%D0%B5%D0%B4%D0%B8%D1%82%D1%8B%D0%91%D0%B0%D0%BD%D0%BA%D0%91%D0%B5%D0%B7%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D0%B8%D0%B5%D0%B2.ipynb) | Заказчик — кредитный отдел банка. Нужно разобраться, влияет ли семейное положение и количество детей клиента на факт погашения кредита в срок. Входные данные от банка — статистика о платёжеспособности клиентов. Результаты исследования будут учтены при построении модели кредитного скоринга — специальной системы, которая оценивает способность потенциального заёмщика вернуть кредит банку. Оцениваем, влияет ли семейное положение и количество детей на факт погашения кредита в срок. 
№2 | [Исследование рынка недвижимости](http://localhost:8888/notebooks/%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%20%D0%BF%D0%BE%20%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D0%B0%D0%BC%20(%D0%B1%D0%B5%D0%B7%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D0%B8%D0%B5%D0%B2).ipynb) | У нас есть архив объявлений о продаже квартир в Санкт-Петербурге и Ленинградской области за 5 лет. Определим детерминанты ценообразования стоимости недвижимости и их рыночную цену. Определение рыночной стоимости объектов недвижимости (на базе данных ресурса Яндекс.Недвижимость). Задача — установить параметры, которые в той или иной степени оказывают влиение на финальную стоимость. Это позволит построить автоматизированную систему: она отследит аномалии и мошенническую деятельность.
№3 | [Определение перспективного тарифа для телеком-компании](https://nbviewer.jupyter.org/github/mksmandrik/real_estate_market_spb/blob/main/%D0%9C%D0%95%D0%93%D0%90%D0%9B%D0%90%D0%98%CC%86%D0%9D%D0%A4%D0%98%D0%9D%D0%90%D0%9B.ipynb) | Делаем предварительный анализ тарифов на небольшой выборке клиентов. В распоряжении есть данные о 500 пользователей. Нужно проанализировать поведение клиентов и сделать вывод - какой тариф лучше
№4 | [Сборный проект 1. Анализ игровой индустрии](http://localhost:8888/notebooks/MMandrikGamesProject.ipynb) | Выявляем определяющие успешность игры закономерности. Это позволит сделать ставку на потенциально популярный продукт и спланировать рекламные кампании
№5 | [Аналитика для авиакомпании](https://github.com/mksmandrik/real_estate_market_spb/blob/main/S7airlines.ipynb) | Изучаем базу данных и анализируем спрос пассажиров на рейсы в города, где проходят крупнейшие фестивали + Web-mining (get -  запросы)
№6 | [Применение SQL-light, ORM, API в работе в Python (запросы и редактирование баз данных)](https://github.com/mksmandrik/real_estate_market_spb/blob/main/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%20SQL-light%2C%20ORM%2C%20API.ipynb) | Редактирование баз данных (пополнение и удаление) тремя способами: Пандас, ORM, SQLlight, SQLAlchemy
№7 | [Примеры работы с SQL-light, SQLPOstgrees в Python](https://github.com/mksmandrik/real_estate_market_spb/blob/main/%20%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B%20SQL%20%D0%B2%20Python.ipynb) |
№8 | [Оптимизировать маркетинговые затрат для продукта Яндекс.Афиша](http://localhost:8888/notebooks/%D0%9F%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%BE%D0%B2%D1%8B%D0%B5_%D0%9C%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8.ipynb#) | Проект для стажировки в отделе аналитики Яндекс.Афиши. Первое задание: помочь маркетологам оптимизировать маркетинговые затраты. У нас в распоряжении есть данные от Яндекс.Афиши с июня 2017 по конец мая 2018 года: лог сервера с данными о посещениях сайта Яндекс.Афиши, выгрузка всех заказов за этот период, статистика рекламных расходов. В проекте я отвечаю на вопросы: как люди пользуются продуктом, когда они начинают покупать, сколько денег приносит каждый клиент когда клиент окупается. Предлагаются когортный анализ Retention, LTV, ROMI, сравнительный анализ конверсий различных источников трафика и маркетинговых затрат. В финале: я даю рекомендацию по оптимизации расходов на трафики и по развитию юзибилити продукта. Библиотеки: pandas, matplotlib.pyplot, seaborn, math, numpy, scipy
№9 | [Приоритезация гипотез, проверка качества системы сплитования и статистический анализ результатов А/В тестов + bootstrap ](https://nbviewer.jupyter.org/github/mksmandrik/real_estate_market_spb/blob/main/%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82_%D0%90%D0%92_%D1%82%D0%B5%D1%81%D1%82_%D0%9C%D0%B0%D0%BD%D0%B4%D1%80%D0%B8%D0%BA_%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC.ipynb) | Задача: Есть список гипотез для увеличения выручки. Приоритезация гипотез, запуск A/B-теста и анализ рехультатов. Библиотеки: pandas, matplotlib.pyplot, seaborn, math, numpy, scipy, bootstrap
№10 | [Анализ рынка общественного питания в Москве: парсинг внешних данных и нестандартная визуализация](http://localhost:8889/notebooks/%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D1%8B%D0%BD%D0%BA%D0%B0%20%D0%BE%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%B2%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5.ipynb) | Задача: Решено открыть небольшое кафе в Москве. Оно оригинальное — гостей должны обслуживать роботы. Проект многообещающий, но дорогой. Инвесторов интересует текущее положение дел на рынке — сможет ли кафе снискать популярность на долгое время, когда все зеваки насмотрятся на роботов-официантов? Исследуем рынок. У нас есть открытые данные о заведениях общественного питания в Москве. Библиотеки: pandas, matplotlib.pyplot, seaborn, plotly, math, numpy, scipy. Парсинг данных: requests, BeautifulSoup, json. Google Sheets: BytesIO, df2gspread, ServiceAccountCredentials
№11 | [Копия блокнота "А/А/В тест для приложения сервиса доставке еды.ipynb](https://colab.research.google.com/drive/1g_Wp3Lq4vzyCYa28-EyPCk6zReM8k7Lj?usp=sharing) | Проект для стартапа, который продаёт продукты питания. Нужно разобраться, как ведут себя пользователи мобильного приложения. Изучаем воронку продаж. Узнаем, как пользователи доходят до покупки. Сколько пользователей доходит до покупки, а сколько — «застревает» на предыдущих шагах? На каких именно? После этого исследуем результаты A/A/B-эксперимента. Дизайнеры захотели поменять шрифты во всём приложении, а менеджеры испугались, что пользователям будет непривычно. Договорились принять решение по результатам A/A/B-теста. Пользователей разбили на 3 группы: 2 контрольные со старыми шрифтами и одну экспериментальную — с новыми. Выясним, какой шрифт лучше.
№12 | [ML Прогнозирование оттока посетителей из фитнес-центров](https://colab.research.google.com/drive/1SNoH8hzFK0sOZK8GFrnRjTmc8io8YcV0?usp=sharing) | Построение модели прогнозирования факта оттока посетителей сети фитнесс-центров. Сегментация посетителей. Logistic Regression, Random Forest, Hierarchial cluster analysis, K-means.
№13 | [Построение модели поиска аномали в аналитических логах в VK](https://colab.research.google.com/drive/1SNoH8hzFK0sOZK8GFrnRjTmc8io8YcV0?usp=sharing) | 1. Воспроизведите график числа рекламных событий по дням, 2. Поиск причины резкого увеличения количества рекламных событий и объясните, что произошло, 3. Детектирование аномальных изменений. 


В данном репозитории я отражу выборочные индивидуальные проекты для Karpov.courses (Data Analysis).

Номер | Название проекта и ссылка | О чем проект
--- | --- | ---
№1 | Минипроект по [Airflow (DAG)](https://github.com/mksmandrik/real_estate_market_spb/blob/main/DAG%20Mandrik%20Mini-Project-AirFlow.py), [VK API](https://github.com/mksmandrik/real_estate_market_spb/blob/main/send_df_vk.py), [CTR Расчеты метрик](https://github.com/mksmandrik/real_estate_market_spb/blob/main/collect_df%20(1).py) | Написание исполняемых ДАГ-ов через AirFlow c подключением к VK API с настройкой отправки сообщений в ЛС ВК по расписанию. Цель: автоматизация рассчета динамики показателей метрик: количество показов, количество кликов, CTR, сумма потраченных денег для 121 тысячи объявлений за 2 дня
