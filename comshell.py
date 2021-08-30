#CHEATSHEET КОМАНД

# django-admin startproject NewsPortal
# python3 manage.py startapp news

# python3 manage.py makemigrations
# python3 manage.py migrate

#команда для запуска этого файла из оболочки джанги, т.к. запуск файла из терминала ругается матом - нет времени разбираться.
# exec(open('comshell.py').read())

#ГЕНЕРАТЦИЯ ДАННЫХ
#сервис для генерации текстов: https://gsgen.ru/tools/fish-text/
#Скрипт для быстрой генерации тестовых данных.
#параметр from_the_scratch определяет будут ли генерироваться данные с нуля.
#если генерация уже один раз была - from_the_scratch = 1 выдаст ошибки, т.к. такие авторы и усеры уже есть
#в таком случае надо выставлять в from_the_scratch = 0

from news.models import *

import random

#исходные данные для генерации количества объектов
ptype = ['NS', 'AL']
aindex = [1, 2]
usersQTY = 11
authQTY = 3
postQTY = 16
commQTY = 26
catQTY = 5
from_the_scratch = 1

category_name = ['Электоринка','Индустрия 4.0','Робототехника','Нанотехнологии']
post_name = ['Практический опыт', 'Задача организации', 'Богатый опыт', 'Значимость проблем']
user_name = []
text_data = {
    1: "Практический опыт показывает, что новая модель организационной деятельности обеспечивает широкому "
       "кругу специалистов участие в формировании дальнейших направлений развитая системы массового участия! "
       "Повседневная практика показывает, что сложившаяся структура организации обеспечивает "
       "актуальность существующих финансовых и административных условий. "
       "Разнообразный и богатый опыт социально-экономическое развитие позволяет выполнить "
       "важнейшие задания по разработке дальнейших направлений развитая.",
    2: "Задача организации, в особенности же дальнейшее развитие различных форм деятельности "
       "требует определения и уточнения дальнейших направлений развитая системы массового участия? "
       "Задача организации, в особенности же постоянное информационно-техническое обеспечение нашей "
       "деятельности представляет собой интересный эксперимент проверки соответствующих условий активизации. "
       "Значимость этих проблем настолько очевидна, что постоянный количественный рост и сфера нашей.",
    3: "Разнообразный и богатый опыт постоянное информационно-техническое обеспечение нашей деятельности "
       "влечет за собой процесс внедрения и модернизации всесторонне сбалансированных нововведений. "
       "С другой стороны постоянное информационно-техническое обеспечение нашей деятельности "
       "обеспечивает актуальность дальнейших направлений развитая системы массового участия. "
       "Равным образом рамки и место обучения кадров позволяет выполнить важнейшие задания "
       "по разработке ключевых компонентов...",
    4: "Значимость этих проблем настолько очевидна, что социально-экономическое развитие "
       "позволяет выполнить важнейшие задания по разработке направлений прогрессивного развития! "
       "Дорогие друзья, повышение уровня гражданского сознания требует определения и уточнения "
       "ключевых компонентов планируемого обновления! Дорогие друзья, консультация с профессионалами "
       "из IT создаёт предпосылки качественно новых шагов для модели развития. Дорогие друзья, сложившаяся структура..."
}

comment_text = {
    1: "Разнообразный и богатый опыт курс на социально-ориентированный национальный проект "
       "требует от нас анализа системы масштабного изменения ряда параметров.",
    2: "Равным образом курс на социально-ориентированный национальный проект "
       "обеспечивает актуальность ключевых компонентов планируемого обновления? ",
    3: "Задача организации, в особенности же дальнейшее развитие различных форм "
       "деятельности играет важную роль в формировании модели развития.",
    4: " С другой стороны, консультация с профессионалами из IT позволяет "
       "оценить значение дальнейших направлений развитая системы массового участия."
}

list_name = ['Сергей','Андрей','Иван','Никита','Михаил']
list_last_name = ['Иванов','Белов','Смирнов','Перов','Сидоров']

# Создать двух пользователей (с помощью метода User.objects.create_user)
if from_the_scratch:
    for n in range(1, usersQTY):
        globals()[f'user{n}'] = User.objects.create_user(username = f"UserName{n}", password = f"UN{n}pass",
                                                         last_name=f"{list_last_name[random.choice(range(1, 6))]}",
                                                         first_name = f"{list_name[random.choice(range(1, 6))]}",)

    # Создать два объекта модели Author, связанные с пользователями.
    for n in range(1, authQTY):
        globals()[f'author{n}'] = Author.objects.create(authorUser = globals()[f'user{n}'])

    # Добавить 4 категории в модель Category
    for n in range(1, catQTY):
        globals()[f'cat{n}'] = Category.objects.create(name = f'Категория {n}: {category_name[random.choice(range(1, 5))]}')

# Добавить 2 статьи и 1 новость
for n in range(1, postQTY):
    d=random.choice(range(1, 5))
    globals()[f'post{n}'] = Post.objects.create(postType = f'{random.choice(ptype)}',
                                                postName = f'Публикация номер {n}: {post_name[d]}',
                                                postBody = f'{text_data.get(d)}',
                                                postAuthor = Author.objects.get(id = random.choice(aindex)),
                                                )
# Присвоить им категории
for n in range(1, postQTY):
    Post.objects.get(id = n).postCategory.add(Category.objects.get(id = random.choice(range(1, catQTY))))

# (как минимум в одной статье/новости должно быть не меньше 2 категорий)
for n in [3, 5, 7]:
    Post.objects.get(id = n).postCategory.add(Category.objects.get(id = random.choice(range(1, catQTY))))

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
for n in range(1, commQTY):
    globals()[f'comment{n}'] = Comment.objects.create(post = globals()[f'post{random.choice(range(1, postQTY))}'],
                                                      user = globals()[f'user{random.choice(range(1, usersQTY))}'],
                                                      commentBody = f'{comment_text.get(random.choice(range(1, 5)))}')

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
for n in range(1, 100):
    Comment.like(Comment.objects.get(id = random.choice(range(1, commQTY))))
    Post.like(Post.objects.get(id = random.choice(range(1, postQTY))))


# Обновить рейтинги пользователей.
for n in range(1, 3):
    Author.objects.get(id = n).update_rating()


#ВЫДОД ДАННЫХ

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.order_by('-autorRating')[:1]

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
pid = 0 #сохраним сюда айди поста, чтобы потом использовать для выведения коментов
p = Post.objects.order_by('-postRating')[:1].values()
for i in p:
    print(f"Дата поста: {i['postDate']}")
    print(f"Автор поста: {Author.objects.get(id=i['postAuthor_id']).authorUser.username}")
    print(f"Рейтинг поста: {i['postRating']}")
    print(f"Заголовок поста: {i['postName']}")
    print(f"Предпросмотр поста: {Post.objects.get(id=i['id']).preview()}")
    pid = i['id']

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
c = Comment.objects.filter(post=pid) #используем сохранённый айди поста
for i in c.values():
    print(f"Comment date: {i['commentDate']}")
    usr = i["user_id"]
    print(f"Comment user: {User.objects.get(id=usr).username}")
    print(f"Comment rating: {i['commentRating']}")
    print(f"Comment: {i['commentBody']}")
    print("----------------")

#вывод категории поста
# cat=Post.objects.get(id=1).postCategory.values("name")
# for i in cat.values():
#     print(i['name'])

#готовая команда для создания отдельных тестовых постов
#Post.objects.create(postType = 'AR', postName = 'Пост для проверки типа', postBody = f'Проверяем, как работает тип поста по умолчанию.', postAuthor = Author.objects.get(id = 1))


