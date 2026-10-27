#!/usr/bin/env python3
"""Llena la plantilla oficial del Anexo 3 (Task 3 - Inglés A2 UNAD) con las
respuestas verificadas, incluyendo referencias en formato APA 7."""
import copy
from docx import Document
from docx.shared import Pt, Inches

SRC = "/home/rootkit/agente/plantillas/apa7/Annex 3 - Task 3_Adventure into Daily Life_Activity Submission.docx"
OUT = "/home/rootkit/Documentos/UNAD/900002_Inglés_A2/Task_3/Anexo 3 - Task 3_ENTREGA_LLENADO.docx"
FOTO_COLLAGE = "/home/rootkit/agente/plantillas/apa7/canva.jpeg"
FOTO_IA = "/home/rootkit/agente/plantillas/apa7/ia .png"

doc = Document(SRC)


def insert_after(par, text, bold=False, italic=False, size=None):
    """Inserta un nuevo párrafo justo después de `par` y lo devuelve."""
    new_p = copy.deepcopy(par._p)
    for child in list(new_p):
        new_p.remove(child)
    par._p.addnext(new_p)
    from docx.text.paragraph import Paragraph
    np = Paragraph(new_p, par._parent)
    run = np.add_run(text)
    run.bold = bold
    run.italic = italic
    if size:
        run.font.size = Pt(size)
    return np


def append_text(par, text, bold=True):
    """Agrega texto al final de un párrafo existente."""
    run = par.add_run(text)
    run.bold = bold
    return par


P = doc.paragraphs

# ---------------- PORTADA ----------------
for p in P:
    t = p.text.strip()
    if t.startswith("Student") and t.endswith(":"):
        append_text(p, " Yeiny Alejandra Suárez Rodríguez")
    elif t == "Group:" or t.startswith("Group") and len(t) < 10:
        append_text(p, " 900002_1957")
    elif t.startswith("Tutor") and len(t) < 16:
        append_text(p, " Jorge Hugo Hernández Villamil")
    elif t == "Date:":
        append_text(p, " October 14th, 2026")

# ---------------- STEP 1 ----------------
for i, p in enumerate(P):
    if p.text.strip() == "Evidence:":
        if "1" in P[i - 2].text:
            insert_after(p, "No attended. The Power-Up Workshops scheduled for "
                            "this course ended on October 13th, 2026, and I was "
                            "not able to attend any of the synchronous sessions. "
                            "I did not present false evidence, following the "
                            "academic integrity rules of the university.",
                         italic=True)
        break

# ---------------- STEP 2 ----------------
qna_step2 = [
    ("1. What place is the person in?",
     "The person is in the city library."),
    ("2. What is the person doing exactly right now?",
     "She is looking for information on the web. And the librarian is "
     "organizing some files."),
    ("3. How often does the person do the main activity?",
     "She studies there for her UNAD courses. She always reads in silence. "
     "And she frequently borrows history books."),
    ("4. How do you get to that place?",
     "Go past the church. The library is across from the main square."),
    ("5. Why are libraries important in many cultures?",
     "Because they are quiet places with thousands of books and a computer "
     "room. People can study there and find information freely."),
]

anchor = None
for p in doc.paragraphs:
    if p.text.strip().startswith("Text") and "title" in p.text and "____" in p.text:
        append_text(p, " The City Library")
        anchor = p
    if p.text.strip() == "Questions and answers of the selected text.":
        cur = p
        for q, a in qna_step2:
            cur = insert_after(cur, q, bold=True)
            cur = insert_after(cur, "    " + a)

# Table 1
tabla = doc.tables[0]
fila = tabla.rows[2]
valores = [
    "The City Library",
    'always — “I always read in silence.”\nfrequently — “I frequently borrow '
    'history books.”',
    'there is — “there is a computer room”\nthere are — “there are thousands '
    'of books”',
    '“I study here for my UNAD courses.”',
    '“go past the church”\n“the library is across from the main square”',
]
for celda, valor in zip(fila.cells, valores):
    celda.text = valor
    for par in celda.paragraphs:
        for run in par.runs:
            run.font.size = Pt(9)

# ---------------- STEP 3 ----------------
qna_step3 = [
    ("1. What is Peter doing right now?",
     "Right now, Peter is ordering a pizza because he is tired."),
    ("2. Which places does he walk past after turning right?",
     "After turning right at the drugstore, he walks past the public library "
     "and the supermarket."),
    ("3. Where exactly is the pizzeria located?",
     "The pizzeria is next to the park, across from the movie theater."),
]
for p in doc.paragraphs:
    if p.text.strip().startswith("Video") and "name" in p.text and len(p.text) < 30:
        append_text(p, " Video 1 — “The New Apartment” "
                       "(https://youtu.be/msaD2OG7MP4)")
    if p.text.strip() == "Activity solved:":
        cur = p
        for q, a in qna_step3:
            cur = insert_after(cur, q, bold=True)
            cur = insert_after(cur, "    " + a)

# ---------------- STEP 4 ----------------
for p in doc.paragraphs:
    if p.text.strip() == "Share the Mondly category completed.":
        insert_after(p, "Category completed: Daily Life.", bold=True)

# ---------------- STEP 5 ----------------
ORACIONES = [
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
COMENTARIO = ("(Similarity) I also wake up early and I always have breakfast "
              "with my family. (Question) What time do you usually finish "
              "your work? (Compliment) Your collage is very organized and I "
              "love the colors and the icons you used. Great job!")
NOTA_TUTOR = ("Note for the tutor: I checked the Task 3 forum several times "
              "before the deadline, but no classmate from my group had "
              "published a photo collage to comment on. Because of that, I "
              "could not complete the three-step rule comment with a real "
              "classmate work. I am available to do it as soon as a classmate "
              "shares the collage.")

for p in doc.paragraphs:
    t = p.text.strip()
    if t == "Share your Photo Collage here":
        cur = p
        for o in ORACIONES:
            cur = insert_after(cur, o)
        cur = insert_after(cur, "My weekly routine collage (created with "
                                "Canva):")
        run = cur.add_run()
        run.add_picture(FOTO_COLLAGE, width=Inches(6.0))
    elif t == "Screenshot of the AI correction":
        cur = insert_after(p, "AI review of my own sentences (draft with "
                              "mistakes → corrected version):")
        run = cur.add_run()
        run.add_picture(FOTO_IA, width=Inches(6.0))
    elif t.startswith("Photo Collage author"):
        append_text(p, " ______________________________")
    elif t == "Comment using the Three-Step Rule":
        cur = insert_after(p, COMENTARIO)
        insert_after(cur, NOTA_TUTOR, italic=True)

# ---------------- STEP 6 ----------------
SCRIPT = [
    ("1. MY HOUSE AND MY FAMILY NOW",
     "In my house, there is a small kitchen and there is a comfortable living "
     "room. There are two bedrooms and one bathroom. The living room is my "
     "favorite place because it is warm and quiet. Right now, three members of "
     "my family are busy: my mother is cooking dinner in the kitchen, my "
     "brother is watching TV in the living room, and my little sister is "
     "doing her homework in her bedroom."),
    ("2. MY OCCUPATION AND ROUTINE",
     "I am a student at UNAD and I work at a water plant in my town. The plant "
     "gives water to all the families of Saboyá, and I really like my job. On "
     "a typical weekday, I usually wake up at five in the morning and I always "
     "have breakfast with my family. I start work at seven o’clock and I "
     "rarely arrive late. In the evening, I usually study for my UNAD "
     "courses, and I sometimes listen to music while I study. I never go to "
     "bed late because I wake up early the next day."),
    ("3. AN IMPORTANT PLACE AND DIRECTIONS",
     "An important place in my town is the church of San Vicente Ferrer, in "
     "the main park. It is old, quiet and beautiful, and many people visit "
     "it, especially on Sundays. To get there from the bus terminal, go "
     "straight on the main street for two blocks, turn left at the school, "
     "and the church is across from the park, next to the bakery. You can’t "
     "miss it."),
]
NOTA_VIDEO = ("Note for the tutor: I could not record the video before the "
              "closing date of the activity because of my work schedule at "
              "the water plant. I am attaching the full script I prepared for "
              "the recording, following the four required points: my house "
              "with there is / there are, three family members using the "
              "present continuous, my occupation with a daily routine and "
              "frequency adverbs, and the directions to an important place in "
              "my town. I am available to record and share the video as soon "
              "as I have the time.")

for p in doc.paragraphs:
    if p.text.strip().startswith("Video") and "Link" in p.text:
        append_text(p, " Not available before the closing date")
        cur = insert_after(p, NOTA_VIDEO, italic=True)
        cur = insert_after(cur, "Script prepared for the video:", bold=True)
        for titulo, texto in SCRIPT:
            cur = insert_after(cur, titulo, bold=True)
            cur = insert_after(cur, "    " + texto)

# ---------------- REFERENCIAS APA 7 ----------------
last = doc.paragraphs[-1]
cur = insert_after(last, "References", bold=True)
cur = insert_after(cur, "ATi Studios. (2026). Mondly: Learn languages "
                        "[Mobile application]. https://www.mondly.com")
cur = insert_after(cur, "Richmond Learning Platform. (2026). The Big Picture "
                        "A2: Student’s book [Online learning platform]. "
                        "Richmond Publishing.")
cur = insert_after(cur, "Universidad Nacional Abierta y a Distancia, "
                        "Instituto Virtual de Lenguas. (2026). Learning guide "
                        "- Task 3: Adventure into daily life [Activity "
                        "guide]. https://campus138.unad.edu.co")

import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print("OK ->", OUT)
