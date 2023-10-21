from PyQt5.QtWidgets import QApplication
#------------------------
#урок 3
from random import choice, shuffle
from time import sleep
#------------------------
app = QApplication([])
from m2 import *
from m3 import *
#------------------
#урок3
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2,
                 wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1
q1 = Question('Какого происхождение слова "serendipity"' , 'Cлово '"serendipity"' происходит от названия Серендип (современный Шри-ланка) и означает неожыданные счпсливые находки.', '"Serendipity" - это слово, которое придумали волшебники.', '', '')
q2 = Question('В чем разница между "affect" и "effect"', ' "Affent" - глагол, используеться для обозначения возднействия или влияния. "Effect" - существительное, обозначает результат или воздействие.', ' "Affect" и "Effect" оба обозначают одно и то же', '', '')
q3 = Question('Какие пять времен английского языка вы знаете?', 'Пять основных времен аглийского языка: Present Simple, Present Continuous,Past Simple,Past Continuous,Future Simple.', '' '', '', "")
q4 = Question('Как правильно сказать "Я был бы рад увидеть тебя" в условной форме?', ' "I wound be glad to see you" - это форма условной конструкции в будущем времени.', 'В условной форме нужно сказать: "I would being glad to see you." ', '', '')
q5 = Question('Какие слова в английском языке начинаються на "x" ', 'Некоторые слова, наинаються с "x": xylophone, xenophobia, xenon, xerography, xenial.', 'В английском языке просто не существует слов которые начинаються на "x" ', '', '')
q6 = Question('Какой артикль (the, a, an) ставиться перед словами, начинающимися на гласные и соглыные ', '', '', '', '')
q7 = Question('', '', '', '', '')
q8 = Question('', '', '', '', '')
q9 = Question('', '', '', '', '')
q10 = Question('', '', '', '', '')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
#
def new_question():
   global cur_q
   cur_q = choice(questions)
   lb_question.setText(cur_q.question)
   lb_right_answer.setText(cur_q.answer)
   shuffle(radio_buttons)

   radio_buttons[0].setText(cur_q.wrong_answer1)
   radio_buttons[1].setText(cur_q.wrong_answer2)
   radio_buttons[2].setText(cur_q.wrong_answer3)
   radio_buttons[3].setText(cur_q.answer)

new_question()
#
#
def check():
   RadioGroup.setExclusive(False)
   for answer in radio_buttons:
       if answer.isChecked():
           if answer.text() == lb_right_answer.text():
               lb_result.setText('Правильно!')
               answer.setChecked(False)
               break
   else:
       lb_result.setText('Неправильно!')

   RadioGroup.setExclusive(True)

#
#
def click_ok():
   if btn_next.text() == 'Відповісти':
       check()
       gb_question.hide()
       gb_answer.show()

       btn_next.setText('Наступне запитання')
   else:
       new_question()
       gb_question.show()
       gb_answer.hide()

       btn_next.setText('Відповісти')
#
#
btn_next.clicked.connect(click_ok)
#
def rest():
   window.hide()
   n = sp_rest.value() * 60
   sleep(n)
   window.show()
#
#
btn_rest.clicked.connect(rest)
#-----------------------------------------

#----------------------------------



def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)
window.show()
app.exec_()