from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

user_data_list = []  # Список для хранения данных всех пользователей

@main.route('/', methods=['GET', 'POST'])
def anketa():
    if request.method == 'POST':
        user_data = {
            'name': request.form.get('name'),
            'city': request.form.get('city'),
            'hobby': request.form.get('hobby'),
            'age': request.form.get('age')
        }
        user_data_list.append(user_data)  # Добавляем новую анкету в список
    return render_template('anketa.html', user_data_list=user_data_list)
