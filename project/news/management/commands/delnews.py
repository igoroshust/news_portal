from django.core.management.base import BaseCommand, CommandError
from news.models import Article, Category

class Command(BaseCommand):
    help = 'Удаление новостей из категории'
    requires_migrations_checks = True # напоминание о миграциях

    def handle(self, *args, **kwargs):
        self.stdout.write('>>> Выберите категорию, из которой хотите удалить статьи: ')
        cat = Category.objects.all()
        di = {}
        s = 1

        for i in cat:
            di[f'{s}'] = i.name
            s += 1

        for key, value in di.items():
            self.stdout.write(f'Нажмите "{key}" для категории "{value}"')

        answer = input(': ')
        for key, value in di.items():
            if answer == key:
                self.stdout.write(f'Вы точно хотите удалить все статьи? Введите yes/no')
                choice = input(': ')
                if choice == 'yes':
                    Article.objects.filter(category_id=key).delete()
                    self.stdout.write(f'Статьи успешно удалены!')
                elif choice == 'no':
                    self.stdout.write(f'В удалении отказано!')
                else:
                    self.stdout.write('Только корректные значения!')





