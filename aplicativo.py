from tkinter import *
import YoutubeComments

#def App():
#-----------------------------------------------------------------------------------------------------------------------
#                                                   GUI
#-----------------------------------------------------------------------------------------------------------------------
#menuInicial.state('zoomed') #janela maxmizada ou iconic para janela minimizada

'''menuInicial = Tk()
menuInicial.title('Youtube Comments')
menuInicial.geometry(newGeometry="650x200+300+20")'''
#menuInicial.iconbitmap('icones/comments.ico')

msg = StringVar()

#-----------------------------------------------------------------------------------------------------------------------
#                                                   Widgets
#-----------------------------------------------------------------------------------------------------------------------

#Label --->  bd=1, relief='solid', #width=5, #height=4, anchor=W, #padx=10, justify=LEFT
# .grid --> columnspan=2 --> (ocupar duas colunas) / sticky ="we" --> (colar borda na esquerda e direita)
#text_box_link = Entry(menuInicial, width=60, font= 'Arial 12').grid(row=3, column=1)

frame_tela_comments = Frame(YoutubeComments.menuInicial)
label1 = Label(frame_tela_comments)
label2 = Label(frame_tela_comments)
label3 = Label(frame_tela_comments)

link = Label(frame_tela_comments, text="Link:", font="Arial 12")

label4 = Label(frame_tela_comments)
label5 = Label(frame_tela_comments)
label6 = Label(frame_tela_comments)
label7 = Label(frame_tela_comments)
label8 = Label(frame_tela_comments)
label9 = Label(frame_tela_comments)

text_box_link = Entry(frame_tela_comments, width=60, font= 'Arial 12')
btn = Button(frame_tela_comments, text='OK', width=30, command=YoutubeComments.executar)

label10 = Label(frame_tela_comments)
label11 = Label(frame_tela_comments)
label_result1 = Message(frame_tela_comments, textvariable=msg, width=100)


#-----------------------------------------------------------------------------------------------------------------------
#                                                   Layout
#-----------------------------------------------------------------------------------------------------------------------
#sticky = pontos cardinais

label1.grid(row=1, column=0)
label2.grid(row=2, column=0)
label3.grid(row=3, column=0)

link.grid(row=4, column=0, sticky=W)
text_box_link.grid(row=4, column=1)

label4.grid(row=5, column=0)
label5.grid(row=6, column=0)

text_box_link.focus()
frame_tela_comments.grid()

btn.grid(row=18, column=1)
label_result1.grid(row=19, column=1)

YoutubeComments.menuInicial.mainloop()

