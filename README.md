## The Beholder
 
#### This API informs you via SMS when the VK user you are looking for is online. The mechanic is similar to services provided by mobile operators via sending SMS like "The number you called is available now".

***How does it work:***
- Enter User ID of the VK user you are looking for
- API checks his status with a set frequency
- When the user is online API sends you SMS "{User ID} is now online!"

***Technology stack:***
- VK API
- Twilio Cloud communications platform 


## Наблюдатель

#### Это API смс-сообщением сообщает юзеру, когда интересующий пользователь ВКонтакте появляется онлайн, то есть является неким аналогом сервиса, который предоставляют телефонные операторы - "Абонент снова в сети".


***Как это работает:***
- Введите id пользователя, статус которого хотите отслеживать
- API c заданной периодичностью проверяет его статус
- Когда пользователя появляется онлайн, API направляет на ваш номер сообщение вида "{id пользователя} сейчас онлайн!"


***Использованные технологии и сервисы:***
- API ВКонтакте
- Сервис отправки смс-сообщений Twilio
