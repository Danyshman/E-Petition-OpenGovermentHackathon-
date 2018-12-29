import collections

form_status = (
    ('pending', 'Pending'),
    ('in_process', 'In_Process'),
    ('completed', 'Completed')
)

status_filter_choice = collections.OrderedDict()
status_filter_choice['pending'] = 'В ожидании'
status_filter_choice['in_progress'] = 'В процессе'
status_filter_choice['completed'] = 'Завершенные'

users_form_filter_choice = collections.OrderedDict()
users_form_filter_choice['users_form'] = 'Мои заявки'

created_date_filter_choice = collections.OrderedDict()
created_date_filter_choice['created_date'] = 'Дата создания'


