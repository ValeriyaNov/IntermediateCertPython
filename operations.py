#import controller
import import_data


def new_contact():
    first_name = input_firstname()
    last_name = input_lastname()
    patronymic = input_patronymic()
    date_of_birth = input('Дата рождения: ')
    phone_number = input('Номер телефона: ')
    mail = input('Эл. почта: ')
    contact_details = ('[' + first_name + ' ' + last_name + ' ' + patronymic +
                       '; ' + date_of_birth + '; ' + phone_number + '; ' + mail + ']')
    #myfile = open(filename, 'a')
    import_data.import_csv(contact_details)
    import_data.import_json(contact_details)
    # myfile.write(contact_details)
    print('Данные успешно сохранены')


def input_firstname():
    first = input('Имя: ')
    fi_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + fi_name


def input_lastname():
    first = input('Фамилия: ')
    la_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + la_name


def input_patronymic():
    first = input('Отчество: ')
    pa_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + pa_name
