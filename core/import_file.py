import pandas as pd
from .models import Student, PhonesStudent
from django.core.files.storage import default_storage

def excel_read(filename: str):
    table_students = pd.read_excel(f'core/media/{filename}')
    table_students = table_students.rename(columns={'Matrícula': 'Matricula', 'Código Curso': 'codeCurso', 'Descrição do Curso': 'descCurso', 'Email Acadêmico': 'emailAcad', 'Situação no Curso': 'statusCurso'})

    table_students.dropna(inplace=True)

    if default_storage.exists(filename):
        default_storage.delete(filename)

    return table_students

def save_data(data):
    students_aux = []
    phones_student_aux = []

    for x in range(len(data)):

        obj = Student(
            name=data['Nome'].loc[[x]][x], 
            matriculation=data['Matricula'].loc[[x]][x], 
            campus=data['Campus'].loc[x], 
            code_course=data['codeCurso'].loc[x], 
            desc_course=data['descCurso'].loc[x], 
            email_acad=data['emailAcad'].loc[x], 
            gender=data['Sexo'].loc[x], 
            status_course=data['statusCurso'].loc[x], 
            class_school=data['Turma'].loc[x], 
            shift=data['Turno'].loc[x]
        )

        if not Student.objects.filter(matriculation=obj.matriculation).exists() and not checkListStudents(students_aux, obj):
            students_aux.append(obj)

    Student.objects.bulk_create(students_aux)

    for x in range(len(data)):
        if Student.objects.filter(matriculation=data['Matricula'].loc[[x]][x]).exists():

            if not verification_object_null(data, 'Telefone', x):
                list_phones_student = data['Telefone'].loc[x].split(', ')
                obj_student = Student.objects.get(matriculation=data['Matricula'].loc[[x]][x])

                for ph in list_phones_student:
                    phones = PhonesStudent(
                        student=obj_student,
                        phone=ph
                    )

                    if not PhonesStudent.objects.filter(phone=ph, student=obj_student.pk).exists():
                        phones_student_aux.append(phones)

    PhonesStudent.objects.bulk_create(phones_student_aux)

    
def verification_object_null(data, column, enum):
    aux_data = data.isnull()
    return aux_data[column][enum]


def checkListStudents(students: list, student: Student):
    for obj in students:
        if obj.matriculation == student.matriculation:
            return True
    
    return False

