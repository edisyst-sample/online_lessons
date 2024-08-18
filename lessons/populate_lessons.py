import os
import django
import random
import sys


# Aggiungi il percorso del progetto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_lessons.settings')
django.setup()

from lessons.models import Teacher, Lesson

def create_teachers_and_lessons():
    # Elimina tutti i dati esistenti per evitare duplicazioni
    Lesson.objects.all().delete()
    Teacher.objects.all().delete()

    # Nomi fittizi per gli insegnanti
    teacher_names = ["Alessandro Rossi", "Maria Bianchi", "Luca Verdi"]

    for name in teacher_names:
        teacher = Teacher.objects.create(name=name)
        for i in range(1, 6):
            Lesson.objects.create(
                title=f"Lezione {i} di {teacher.name}",
                description=f"Descrizione della lezione {i} di {teacher.name}",
                max_students=random.randint(10, 30),  # Numero massimo di studenti casuale
                teacher=teacher
            )

    print("Insegnanti e lezioni creati con successo.")

if __name__ == "__main__":
    create_teachers_and_lessons()
