import view
import models


def run():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                models.view_all()
            case 2:
                models.create_note()
            case 3:
                models.edit_note()
            case 4:
                models.delete_note()
            case 5:
                models.delete_all()
            case 6:
                break
