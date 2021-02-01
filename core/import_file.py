import pandas as pd
from .models import Student, PhonesStudent

def excel_read(filename: str):
    table_students = pd.read_excel(f'core/media/{filename}')
    table_students = table_students.rename(columns={'Matrícula': 'Matricula', 'Código Curso': 'codeCurso', 'Descrição do Curso': 'descCurso', 'Email Acadêmico': 'emailAcad', 'Situação no Curso': 'statusCurso'})
    
    return table_students

def save_data(data):
    list_names = []
    list_matriculation = []
    list_campus = []
    list_codeCourse = []
    list_descCourse = []
    list_emailAcad = []
    list_statusCourse = []
    list_phones = []
    list_classSchool = []
    list_shift = []
    list_gender = []

    for x in range(len(data)):
        list_names.append(data['Nome'].loc[[x]][x])
        list_matriculation.append(data['Matricula'].loc[[x]][x])
        list_campus.append(data['Campus'].loc[x])
        list_codeCourse.append(data['codeCurso'].loc[x])
        list_descCourse.append(data['descCurso'].loc[x])
        list_emailAcad.append(data['emailAcad'].loc[x])
        list_statusCourse.append(data['statusCurso'].loc[x])
        list_phones.append(data['Telefone'].loc[x])
        list_classSchool.append(data['Turma'].loc[x])
        list_shift.append(data['Turno'].loc[x])
        list_gender.append(data['Sexo'].loc[x])

    students_aux = []
    phones_student_aux = []

    for i in range(len(data)):
        name = list_names[i]
        matriculation = list_matriculation[i]
        campus = list_campus[i]
        codeCourse = list_codeCourse[i]
        descCourse = list_descCourse[i]
        emailAcad = list_emailAcad[i]
        statusCourse = list_statusCourse[i]
        class_school = list_classSchool[i]
        shift = list_shift[i]
        gender = list_gender[i]

        obj = Student(
            name=name, 
            matriculation=matriculation, 
            campus=campus, 
            code_course=codeCourse, 
            desc_course=descCourse, 
            email_acad=emailAcad, 
            gender=gender, 
            status_course=statusCourse, 
            class_school=class_school, 
            shift=shift
        )

        students_aux.append(obj)
    print(students_aux)

    Student.objects.bulk_create(students_aux)

    for i in range(len(data)):
        list_phones_student = list_phones[i].split(', ')
        obj_student = Student.objects.get(matriculation=list_matriculation[i])

        for ph in list_phones_student:
            phones = PhonesStudent(
                student=obj_student,
                phone=ph
            )

            phones_student_aux.append(phones)
    
    PhonesStudent.objects.bulk_create(phones_student_aux)
    