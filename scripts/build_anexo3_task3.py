#!/usr/bin/env python3
# Genera el Anexo 3 de Task 3 (Inglés A2 - UNAD) ya rellenado con las respuestas.
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

st = doc.styles['Normal']
st.font.name = 'Calibri'
st.font.size = Pt(11)

def h(text, level=1):
    p = doc.add_heading(text, level=level)
    return p

def para(text, bold=False, italic=False, size=None):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    if size:
        r.font.size = Pt(size)
    return p

def bullet(text):
    doc.add_paragraph(text, style='List Bullet')

def ph(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.color.rgb = RGBColor(0xC0, 0x00, 0x00)
    return p

# ---------------- PORTADA ----------------
para('Universidad Nacional Abierta y a Distancia', bold=True, size=14)
para('Vicerrectoría Académica e Investigación — Instituto Virtual de Lenguas (INVIL)', size=10)
para('Curso: Inglés A2 — Código 900002', bold=True)
doc.add_paragraph()
para('TASK 3: ADVENTURE INTO DAILY LIFE', bold=True, size=16)
para('Inglés A2', italic=True, size=12)
doc.add_paragraph()
para('Student’s Name: Yeiny Alejandra Suárez Rodríguez')
para('Group: 900002_1957')
para('Tutor’s Name: Jorge Hugo Hernández Villamil')
para('Date: October 14th, 2026')
doc.add_paragraph()
ph('[ADJUNTA AQUÍ LAS CAPTURAS DE PANTALLA PEDIDAS EN CADA PASO]')
doc.add_page_break()

# ---------------- STEP 1 ----------------
h('Step 1: Participation in the Power-Up Workshops', 1)
para('Evidence of your participation in the workshops.', italic=True)
para('Power-Up Workshop 1')
para('Date: ______________   Topic: ______________   Tutor’s name: ______________')
ph('[PEGAR AQUÍ LA CAPTURA DE LA ASISTENCIA — 18 pts en juego]')
para('Power-Up Workshop 2')
para('Date: ______________   Topic: ______________   Tutor’s name: ______________')
ph('[PEGAR AQUÍ LA CAPTURA DE LA ASISTENCIA]')
para('Nota: si no asististe a ningún taller, deja este espacio en blanco. No se '
     'permite presentar evidencias falsas (Acuerdo 029 de 2013, Art. 99).', italic=True)

# ---------------- STEP 2 ----------------
doc.add_page_break()
h('Step 2: Reading and Vocabulary', 1)
para('Text’s title: The City Library', bold=True)
para('Questions and answers of the selected text:', italic=True)

qa = [
    ("1. What place is the person in?",
     "The person is in the city library."),
    ("2. What is the person doing exactly right now?",
     "Right now, she is searching for information on the web, and the librarian "
     "is organizing some files."),
    ("3. How often does the person do the main activity?",
     "She studies there for her UNAD courses. She always reads in silence and "
     "she frequently borrows history books."),
    ("4. How do you get to that place?",
     "To get to the library, go past the church. The library is across from the "
     "main square."),
    ("5. Why are libraries considered important in many cultures?",
     "Because they are quiet places with thousands of books and a computer room, "
     "where people can study and find information freely."),
]
for q, a in qa:
    para(q, bold=True)
    para('    ' + a)

para('Table 1: Identifying Grammatical Structures in the Text', bold=True)
para('Text’s title: The City Library', bold=True)

tabla = [
    ("Frequency adverbs",
     "always — “I always read in silence.”\nfrequently — “I frequently borrow "
     "history books.”"),
    ("there is / there are",
     "there is — “there is a computer room”\nthere are — “there are thousands "
     "of books”"),
    ("Sentences in simple present",
     "“I study here for my UNAD courses.”\n“I always read in silence.”"),
    ("Directions",
     "“go past the church”\n“the library is across from the main square”"),
]
t = doc.add_table(rows=1, cols=2)
t.style = 'Table Grid'
hdr = t.rows[0].cells
hdr[0].paragraphs[0].add_run('Text’s title: The City Library').bold = True
hdr[1].paragraphs[0].add_run('Grammatical structures found').bold = True
for k, v in tabla:
    row = t.add_row().cells
    row[0].text = k
    row[1].text = v

# ---------------- STEP 3 ----------------
doc.add_page_break()
h('Step 3: Listening immersion', 1)
para('Video’s name: Video 1 — “The New Apartment”', bold=True)
para('https://youtu.be/msaD2OG7MP4', italic=True)
para('Activity solved:', italic=True)
for q, a in [
    ("1. What is Peter doing right now?",
     "Right now, Peter is ordering a pizza because he is tired."),
    ("2. Which places does he walk past after turning right?",
     "After turning right at the drugstore, he walks past the public library and "
     "the supermarket."),
    ("3. Where exactly is the pizzeria located?",
     "The pizzeria is next to the park, across from the movie theater."),
]:
    para(q, bold=True)
    para('    ' + a)

# ---------------- STEP 4 ----------------
doc.add_page_break()
h('Step 4: Mondly time', 1)
para('Mondly category completed: Daily Life', bold=True)
ph('[PEGAR AQUÍ LA CAPTURA DONDE SE VEAN EL ICONO DE CATEGORÍA TERMINADA '
   'Y TU NOMBRE DE PERFIL — 8 pts]')

# ---------------- STEP 5 ----------------
doc.add_page_break()
h('Step 5: Writing — My Weekly Life: Photo Collage', 1)
para('Part A', bold=True)
ph('[PEGAR AQUÍ TU PHOTO COLLAGE — créalo en Canva con estas 10 oraciones]')
oraciones = [
    "1. I usually wake up at five o’clock on weekdays.",
    "2. I always make my bed after taking a shower.",
    "3. I take out the trash on Wednesdays and on Saturdays.",
    "4. I go to the water plant from Monday to Friday.",
    "5. The plant gives water to all the families of Saboyá.",
    "6. In the evening, I usually mop the floors of my house.",
    "7. I do the dishes after dinner with my family.",
    "8. On Saturdays, I do the laundry and I vacuum my bedroom.",
    "9. On Sundays, I sometimes visit the main park with my family.",
    "10. I never go to bed late because I wake up early the next day.",
]
for o in oraciones:
    bullet(o)

para('Screenshot of the AI correction', bold=True)
ph('[PEGAR AQUÍ LA CAPTURA DE LA CORRECCIÓN QUE TE HIZO LA IA]')

para('Part B', bold=True)
para('Photo Collage author: ____________________________')
para('Comment using the Three-Step Rule', bold=True)
para('(Similarity) I also wake up early and I always have breakfast with my '
     'family. (Question) What time do you usually finish your work? '
     '(Compliment) Your collage is very organized and I love the colors and the '
     'icons you used. Great job!')
para('Note for the tutor:', bold=True)
para('I checked the Task 3 forum several times before the deadline, but no '
     'classmate from my group had published a photo collage to comment on. '
     'Because of that, I could not complete the three-step rule comment with a '
     'real classmate work. I am available to do it as soon as a classmate '
     'shares the collage.', italic=True)

# ---------------- STEP 6 ----------------
doc.add_page_break()
h('Step 6: My Life and My Surroundings — Video Presentation', 1)
ph('[PEGA AQUÍ EL LINK PÚBLICO DEL VIDEO — mínimo 2 minutos, sin contraseña]')

para('Video Link: ________________________________________________', bold=True)
para('Script of my video', bold=True)

script = [
    ("Introduction",
     "Hello. My name is Yeiny Alejandra Suárez Rodríguez. I am a student at "
     "UNAD, and I live in Saboyá, a small town in Boyacá, Colombia. Today I "
     "want to talk about my house, my family, my routine and my town."),
    ("1. My house and my family now",
     "In my house, there is a small kitchen and there is a comfortable living "
     "room. There are two bedrooms and one bathroom. The living room is my "
     "favorite place because it is warm and quiet. Right now, three members of "
     "my family are busy: my mother is cooking dinner in the kitchen, my "
     "brother is watching TV in the living room, and my little sister is doing "
     "her homework in her bedroom."),
    ("2. My occupation and routine",
     "I am a student at UNAD and I work at a water plant in my town. The plant "
     "gives water to all the families of Saboyá, and I really like my job. On a "
     "typical weekday, I usually wake up at five in the morning and I always "
     "have breakfast with my family. I start work at seven o’clock and I "
     "rarely arrive late. In the evening, I usually study for my UNAD courses, "
     "and I sometimes listen to music while I study. I never go to bed late "
     "because I wake up early the next day."),
    ("3. An important place and directions",
     "An important place in my town is the church of San Vicente Ferrer, in the "
     "main park. It is old, quiet and beautiful, and many people visit it, "
     "especially on Sundays. To get there from the bus terminal, go straight on "
     "the main street for two blocks, turn left at the school, and the church "
     "is across from the park, next to the bakery. You can’t miss it."),
    ("Closing",
     "Thank you very much for watching my video. Have a nice day!"),
]
for title, text in script:
    para(title, bold=True)
    para('    ' + text)

doc.add_paragraph()
para('References', bold=True)
para('Richmond Learning Platform+. (2026). The Big Picture A2 — Student’s Book. '
     'Richmond Publishing.', italic=True)
para('Mondly. (2026). Mondly language learning app [Mobile application]. '
     'ATi Studios.', italic=True)

out = "/home/rootkit/Documentos/UNAD/900002_Inglés_A2/Task_3/Anexo_3_Task3_ENTREGA_Yeiny_Suarez.docx"
doc.save(out)
print("OK ->", out)
