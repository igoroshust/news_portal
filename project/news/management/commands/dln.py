from django.core.management.base import BaseCommand, CommandError
from news.models import Article, Category

class Command(BaseCommand):
    help = 'Удаление новостей из категории'
    requires_migrations_checks = True # напоминание о миграциях

    def handle(self, *args, **kwargs):
        self.stdout.readable()
        self.stdout.write('Выберите категорию, из которой хотите удалить статьи: ')
        lst = Category.objects.all()
        s = 1
        for i in lst:
            self.stdout.write(f'>>> Нажмите {s} для категории "{i.name}"')
            s += 1
            # self.stdout.write(Category.objects.get().name)
        answer = int(input(': '))
        if answer == 1:
            self.stdout.write(f'Вы точно хотите удалить все статьи? Введите yes/no')
            choice = input(': ')
            if choice == 'yes':
                Article.objects.filter(category_id=1).delete()
                self.stdout.write(f'Статьи успешно удалены!')
            elif choice == 'no':
                self.stdout.write(f'В удалении отказано!')
            else:
                self.stdout.write('Только корректные значения!')