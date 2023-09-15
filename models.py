from datetime import datetime
import glob
import json
import os
import tkinter as tk
import uuid
import menu

my_notes = []


class Note:
    def __init__(self):
        self.note_id = str(uuid.uuid1())[0:3]
        self.note_date = datetime.now().strftime('%d.%m.%y / %H:%M')
        self.note_title = input("Please enter a note name\n")
        self.note_body = input("Please place your text here\n")

    def save_all(self):
        notice = {'Id': self.note_id, 'Date': self.note_date, 'Title': self.note_title, 'Body': self.note_body}
        my_notes.append(notice)


def view_all():
    with open('all_notes.json') as file:
        all_notes = sorted(json.load(file), key=lambda date: date['Date'])
        if len(all_notes) == 0:
            print("You don't have any notes")

        else:

            print(f"Your notes contains: {all_notes}")


def create_note():
    note = Note()
    note.save_all()
    with open('all_notes.json', 'w') as file:
        json.dump(my_notes, file)
    print(menu.note_added)


def edit_note():
    view_all()
    with open('all_notes.json') as file:
        all_notes = json.load(file)
    edit_title = input(menu.note_title)
    for note in all_notes:
        if note['Title'] == edit_title:
            note['Title'] = input(menu.new_title)
            note['Body'] = input(menu.edit_text)
            note['Date'] = datetime.now().strftime('%d.%m.%y / %H:%M')
            with open('all_notes.json', 'w') as file:
                json.dump(all_notes, file)
            return print(menu.save_text)
    return print(menu.wrong_title)


def delete_note():
    view_all()
    with open('all_notes.json') as file:
        all_notes = json.load(file)
    delete_title = input(menu.note_title)
    for note in all_notes:
        if note['Title'] == delete_title:
            all_notes.remove(note)
            with open('all_notes.json', 'w') as file:
                json.dump(all_notes, file)
            return print(menu.note_delete)
    return print(menu.wrong_title)


def delete_all():
    with open('all_notes.json', 'w') as file:
        json.dump(my_notes, file)
    print(menu.all_clear)
