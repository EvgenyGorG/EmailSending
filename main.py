import smtplib
import os

email_from = "9djon9@mail.ru"
email_to = "jekagorohovdiablo@mail.ru"
login = os.getenv('MAIL_RU_LOGIN')
password = os.getenv('MAIL_RU_PASSWORD')

letter = f'''\
From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";\n\n
'''

message = '''\
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
'''

friend_name = 'Иван'
website_name = 'https://dvmn.org/referrals/zLsUAtGw6wsPLGyqi79GQQ260wfNrti2NFrDR5Jz/'
my_name = 'Евгений'

message = message.replace('%website%', website_name)
message = message.replace('%friend_name%', friend_name)
message = message.replace('%my_name%', my_name)

final_letter = letter + message

final_letter = final_letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, final_letter)
server.quit()
