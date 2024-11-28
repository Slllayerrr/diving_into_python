# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import json
import csv
import pickle
import os

__all__ = ['save_results_to_join', 'save_results_to_csv', 'save_results_to_pickle', 'traverse_directory', 'format_save']

def save_results_to_join(list):
    with open('traverse_dir.json', 'w', encoding='utf-8') as f:
        json.dump(list, f, indent=4, ensure_ascii=False)


def save_results_to_csv(list):
    fieldnames = ['имя', 'объект', 'размер в байтах', 'родительская директория']
    with open('traverse_dir.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=fieldnames, dialect='excel')
        csv_write.writeheader()
        csv_write.writerows(list)


def save_results_to_pickle(list):
    with open('traverse_dir.pickle', 'wb') as f_wb:
        pickle.dump(list, f_wb)


def traverse_directory(directory):
    list_directory = []
    for i in os.listdir(directory):
        dict_dir = {}
        dict_dir['имя'] = i
        if os.path.isdir(directory + '\\' + i):
            dict_dir['объект'] = 'dir'
            traverse_directory(directory + '\\' + i)
            sumb = 0
            for b in os.listdir(directory + '\\' + i):
                sumb += int(os.path.getsize(directory + '\\' + i + '\\' + b))
            dict_dir['размер в байтах'] = sumb
        else:
            if os.path.abspath(directory + '\\' + i) == os.path.abspath(directory):
                dict_dir['объект'] = 'file'
                dict_dir['размер в байтах'] = os.path.getsize(directory + '\\' + i)
            else:
                dict_dir['объект'] = 'file'
                dict_dir['размер в байтах'] = os.path.getsize(directory + '\\' + i)
                dict_dir['родительская директория'] = os.path.dirname(directory + '\\' + i)
        list_directory.append(dict_dir)
    return list_directory


def format_save():
    res = traverse_directory(r'C:\Users\User\Desktop\obxod_file')
    format_s = input('Введите цифру в каком формате сохранить(json - 1, csv - 2, pickle - 3): ')
    if format_s == '1':
        save_results_to_join(res)
    elif format_s == '2':
        save_results_to_csv(res)
    elif format_s == '3':
        save_results_to_pickle(res)
    else:
        print("Введено некорректное значение")

if __name__ == '__main__':
    format_save()
