import config

w_choose_developer = [
    'Вам rare или well-done?',
    'Нужен старший или младший разработчик?',
    'Здесь есть опытные и не очень. Вам кого?',
    'Есть и стар, и млад — на любой вкус!',
    'Выбери калибр разработчика.',
    'Choose your fighter:'
]

w_choose_developer_buttons = [
    ['👶🏼', '👨🏼‍🦳'],
    ['👼', '👹'],
    ['🍼', '🍺'],
    ['👁', '👀'],
    ['🐴', '🦄'],
    ['🐬', '🐳'],
]

w_final_list_header = [
    'Встречайте финалистов:',
    'В финальный раунд отбора прошли:',
    'Как же я люблю разработчиков, вот они слева направо:',
    'Кандидаты на ревью:',
]

w_final_list_footer = [
    'Осчастливим случайного!',
    'Пусть победителя определит жребий!',
    'Кидаем кубик...',
    'Восславьтесь, хаос и рандом!',
]

w_the_chosen_one = [
    '@{}, я выбираю тебя!',
    '@{}, это не я, это всё кубик, честно!',
    '@{}, ты победил или проиграл?',
    '@{}, добро пожаловать в PR.',
    '@{}, тебе предстоит code-review.',
]

w_close_keyboard = [
    'Галя, отмена!',
    'Хватит с меня разработчиков',
    'Больше не надо',
    'Закрыть набор',
]

w_delete_message = [
    'Здесь была красивая картинка с котиком, но вы уже всё пропустили.',
    'Невиновные наказаны, непричастные награждены.',
    'На этом мои полномочия всё.',
    'Тут что-то было.',
]

w_temporary_keyboard = [
    '🗿',
    '🤔',
    '⏳',
    '...',
]

w_introduction_text = \
    f'''Всем привет в этом чатике 💅💅💅

Я ваша сваха: помогаю PR и ревьюверам найти друг друга.
Просто упомяните меня, @{config.BOT_USERNAME}, в своём описании к PR, и я предложу интерфейс \
для случайного выбора среди младших или старших разработчиков в чате.
Кнопки интерфейса общие для любого участника чата.

После выбора ранга разработчика я сформирую случайный список финалистов до 6 человек. \
Победителя определит кубик 🎲

Даже если меня не позвали в описании к PR (а я искренне верю, что вы просто забыли), \
меня можно позвать, ответив на сообщение про PR. В таком случае жребий укажет на сообщение, \
в ответ на которое меня вызвали.

Чтобы узнать прочие технические детали, есть команда /help_tech.
'''

w_help_tech = \
    '''ДИСКЛЕЙМЕР:
НЕ ДОБАВЛЯЙТЕ ЭТОГО БОТА В ДРУГИЕ ЧАТЫ!
Он не будет в них работать. Сейчас он спроектирован для работы в одном конкретном чате.
Кроме того, он использует API моего аккаунта Telegram @morrisnein для доступа к списку участников группы.
Используемый аккаунт должен присутствовать в чате для работы бота.
    
Репозиторий бота:
https://github.com/MorrisNein/code_review_bot

Отредактировать распределение разработчиков по младшими или старшим \
пока что можно только через меня, @morrisnein.
'''