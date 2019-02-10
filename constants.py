import collections


form_status = (
    ('pending', 'В ожидании'),
    ('in_process', 'В процессе'),
    ('completed', 'Закрыто')
)

form_category = (
    ('road', 'Жолдор/Дороги'),
    ('street_lights', 'Уличное освещение'),
    ('gardening', 'Жашылдандыруу/Озеленение'),
    ('electricity', 'Элект камсыздоо/Электроснабжение'),
    ('water', 'Водоснабжение'),
    ('rubbish', 'Таштанды/Мусор'),
    ('heat', 'Жылуулук/Теплоснабжение'),
    ('other', 'Башка/Другое')
)


status_filter_choice = collections.OrderedDict()
status_filter_choice['pending'] = 'В ожидании'
status_filter_choice['in_progress'] = 'В процессе'
status_filter_choice['completed'] = 'Завершенные'

category_filter_choice = collections.OrderedDict()
category_filter_choice['road'] = 'Жолдор/Дороги'
category_filter_choice['street_lights'] = 'Уличное освещение'
category_filter_choice['gardening'] = 'Жашылдандыруу/Озеленение'
category_filter_choice['electricity'] = 'Элект камсыздоо/Электроснабжение'
category_filter_choice['water'] = 'Водоснабжение'
category_filter_choice['rubbish'] = 'Таштанды/Мусор'
category_filter_choice['heat'] = 'Жылуулук/Теплоснабжение'
category_filter_choice['other'] = 'Башка/Другое'

users_form_filter_choice = collections.OrderedDict()
users_form_filter_choice['users_form'] = 'Мои заявки'

created_date_filter_choice = collections.OrderedDict()
created_date_filter_choice['created_date'] = 'Дата создания'


government_branch_emails = {
    'road': 'road_ministry@gmail.com',
    'street_lights': 'street_lights_ministry@gmail.com',
    'gardening': 'gardening_ministry@gmail.com',
    'electricity': 'electricity_ministry@gmail.com',
    'water': 'water_ministry@gmail.com',
    'rubbish': 'rubbish_ministry@gmail.com',
    'heat': 'heat_ministry@gmail.com',
    'other': 'other_ministry@gmail.com'
}

