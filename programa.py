import criar
from tkinter import *
from tkinter import ttk,messagebox,filedialog
import os
import sys
import face_recognition
import threading
import webcam
from datetime import datetime

criar.cria()

minhapasta = os.path.dirname(__file__)

abr = 0
varnome = ''
varnivel = 0

# tela de cadastro

def telacadastraproduto():
    imagem = ''

    appcadastrousuario = Toplevel()
    appcadastrousuario.title('Cadastrar pessoas')
    appcadastrousuario.geometry('900x400')
    appcadastrousuario.resizable(width=0, height=0)

    Label(appcadastrousuario, text='Preencha', fg='#000', font=('arial', 15)).grid(row=0,column=0,pady=10,padx=0,sticky=E)
    Label(appcadastrousuario, text='os dados', fg='#000', font=('arial', 15)).grid(row=0,column=1,pady=10,padx=0,sticky=W)

    Label(appcadastrousuario, text='Nome do usuario:', fg='#000', font=('arial', 15)).grid(row=1,pady=10,padx=10)
    cadprodutonome10 = Entry(appcadastrousuario,width=40,font=('arial', 13))
    cadprodutonome10.grid(row=1,column=1,pady=10,padx=10,ipady=3,sticky=W)
    cadprodutonome10.focus()

    vnivel= IntVar()
    vnivel.set(0)
    Label(appcadastrousuario, text='Nivel de acesso:', fg='#000', font=('arial', 15)).grid(row=2,pady=10,padx=10)
    vb_1 = Radiobutton(appcadastrousuario,text="1",value=1,variable=vnivel)
    vb_1.grid(row=2,column=1)
    vb_2 = Radiobutton(appcadastrousuario,text="2",value=2,variable=vnivel)
    vb_2.grid(row=3,column=1)
    vb_3 = Radiobutton(appcadastrousuario,text="3",value=3,variable=vnivel)
    vb_3.grid(row=4,column=1,pady=10)
    
    nomeimg = Label(appcadastrousuario, text='Selecione a imagem:', fg='#000', font=('arial', 15))
    nomeimg.grid(row=5,column=1,pady=10,padx=10)
    
    def abrir():
        global imagem
        img = filedialog.askopenfile()
        try:
            img_para_verificar =face_recognition.load_image_file(img.name)
            img_para_verificar_encoding = face_recognition.face_encodings(img_para_verificar)[0]
            appcadastrousuario.focus()
            nomeimg.configure(text=img.name)
            imagem = img.name
        except:
            appcadastrousuario.focus()
            nomeimg.configure(text="Rosto não reconhecido")
            imagem = ''

    def tirarfoto():
        global imagem
        global abr
        try:
            os.remove(minhapasta+"\\img.jpg")
        except:
            pass
        messagebox.showinfo(title="INFO",message="Aperte ESC para fechar a webcam\nAperte S para iniciar a verificação")
        webcam.cam()
    
        appcadastrousuario.focus()

        try:
            img_para_verificar =face_recognition.load_image_file(minhapasta+"\\img.jpg")
            img_para_verificar_encoding = face_recognition.face_encodings(img_para_verificar)[0]
            imagem = minhapasta+"\\img.jpg"
            nomeimg.configure(text=minhapasta+"\\img.jpg")
            appcadastrousuario.focus()
            abr = 0
        except:
            nomeimg.configure(text="Rosto não reconhecido")
            appcadastrousuario.focus()
            imagem = ''
            abr = 0

    def cadastrarpessoa():
        global imagem
        nome = cadprodutonome10.get()
        nivel = vnivel.get()
        try:
            if nome != '' and nivel != '' and imagem != '':
                me = criar.cadastrapessoa(nome,nivel,imagem,'Usuario novo')
                if me != None:
                    messagebox.showerror(title="ERROR",message=me)
                    appcadastrousuario.focus()
                else:
                    cadprodutonome10.delete(0,END)
                    vnivel.set(0)
                    imagem = ''
                    nomeimg.configure(text='Selecione a imagem:')
                    appcadastrousuario.focus()
                    pesquisarpessoas()
            else:
                messagebox.showerror(title="ERROR",message='Preencha os dados')
                appcadastrousuario.focus()
                cadprodutonome10.focus()
        except:
            messagebox.showerror(title="ERROR",message='Preencha os dados')
            appcadastrousuario.focus()
            cadprodutonome10.focus()
            
    def sairr():
        appcadastrousuario.destroy()

    btncarregarimagem= Button(appcadastrousuario, text='Procurar',
                        width=10, command=abrir)
    btncarregarimagem.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
    btncarregarimagem.grid(row=5,pady=10,padx=10)

    btntirarfoto= Button(appcadastrousuario, text='Tirar foto',
                        width=10, command=tirarfoto)
    btntirarfoto.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
    btntirarfoto.grid(row=6,pady=10,padx=10)

    btncadproduto = Button(appcadastrousuario, text='Cadastrar', command=cadastrarpessoa,width=10)
    btncadproduto.configure(bd=1, 
                    activebackground="#467", cursor='hand2')
    btncadproduto.grid(row= 7,column=1,sticky=E,pady=20)

    btnsairproduto = Button(appcadastrousuario, text='Sair', command=sairr,width=5)
    btnsairproduto.configure(bd=1, 
                    activebackground="#467", cursor='hand2')
    btnsairproduto.grid(row= 7,column=1,sticky=N,pady=20)

    def enter(event):
        try:
            cadastrarpessoa()  
        except:
            pass

    appcadastrousuario.bind(sequence="<Return>", func=enter)

# def basicas 

def log():
    global varnome
    global varnivel

    app.geometry('1200x650')
    login.place(x=-1200, y=0, width=500, height=350)
    logado.place(x=0, y=0, width=1200, height=650)
    labelpessoalogada.configure(text='Nome: '+varnome)
    labelnivelpessoalogada.configure(text='Nivel: '+str(varnivel))
    if varnivel == 1:
        btncadastrar.config(state=DISABLED)
        btndeleta.config(state=DISABLED)
        btndeletatudo.config(state=DISABLED)
        btnabrirpla.config(state=DISABLED)
        btntxt.config(state=DISABLED)
    elif varnivel == 2:
        btncadastrar.config(state=NORMAL)
        btndeleta.config(state=DISABLED)
        btndeletatudo.config(state=DISABLED)
        btnabrirpla.config(state=NORMAL)
        btntxt.config(state=DISABLED)
    else:
        btncadastrar.config(state=NORMAL)
        btndeleta.config(state=NORMAL)
        btndeletatudo.config(state=NORMAL)
        btnabrirpla.config(state=NORMAL)
        btntxt.config(state=NORMAL)
    data = datetime.now().strftime('%d/%m/%Y')
    criar.alterapessoaultima(varnome,str(data))
    mostrarpessoas()
    
def volta():
    finaliza = messagebox.askyesno(title="AVISO",message="Deseja finalizar a sessao?")
    if finaliza == True:
        app.geometry('500x350')
        login.place(x=0, y=0, width=500, height=350)
        logado.place(x=-1200, y=0, width=1200, height=650)


def abrplanilha():
    global abr
    if abr == 0:
        threading.Thread(target=abrplanilha2).start()
        abr = 1

def abrplanilha2():
    global abr
    try:
        os.startfile(minhapasta+"\\dados.xlsx")
        abr = 0
    except:
        abr = 0

def abrtxt():
    global abr
    if abr == 0:
        threading.Thread(target=abrtxt2).start()
        abr = 1

def abrtxt2():
    global abr
    try:
        os.startfile(minhapasta+"\\Informacoes_Secretas.txt")
        abr = 0
    except:
        abr = 0


def enter(event):
    pesquisarpessoas()

def qui():
    sys.exit(0)

# tela   
app = Tk()
app.title('Programa brabo')
app.geometry('500x350')
app.resizable(width=0,height=0)
app.iconbitmap(minhapasta+'\\ico.ico')

# estilo da tabela
ns = ttk.Style()
ns.configure('Treeview', background='gray', foreground='black',
             rowheight=25, fieldbackground='white', borderwidth=1, relief='solid')
ns.map('Treeview', background=[('selected', '#0a0')],
       foreground=[('selected', 'black')])

# frame login

login = Frame(app, bg='#48d')
login.place(x=0, y=0, width=500, height=350)

Label(login,text='Selecione como deseja logar', bg='#48d', fg='#000', font=(
    'arial', 18)).place(x=85, y=30, width=350, height=40)

labelVerificando = Label(login,text='Verificando banco de dados', bg='#48d', fg='#000', font=(
    'arial', 18))

# def frame login

def carregaimage():
    global abr
    if abr == 0:
        threading.Thread(target=carregaimage2).start()
        abr = 1

def carregaimage2():
    global varnome
    global varnivel
    global abr
    try:
        os.remove(minhapasta+"\\img.jpg")
    except:
        pass
    
    try:
        img = filedialog.askopenfile()
        img_para_verificar =face_recognition.load_image_file(img.name)
        
        labelVerificando.place(x=85, y=300, width=350, height=40)

        labelVerificando.configure(text="Verificando banco de dados")

        linhas = criar.mostrar("SELECT img,nome,nivel FROM pessoas")
        for imagens in linhas:
            imgs = imagens[0]
            with open(minhapasta+"\\img.jpg","wb") as f:
                f.write(imgs)
            imagens_banco = face_recognition.load_image_file("img.jpg")
        
            img_para_verificar_encoding = face_recognition.face_encodings(img_para_verificar)[0]
            imagens_banco_encoding = face_recognition.face_encodings(imagens_banco)[0]
            
            results = face_recognition.compare_faces([img_para_verificar_encoding], imagens_banco_encoding)
            imagens_banco = ''
            os.remove(minhapasta+"\\img.jpg")

            if results[0] == True:
                re = True
            else:
                re = False

            if re == True:
                varnome = imagens[1]
                varnivel = imagens[2]
                labelVerificando.place(x=-1200, y=300, width=350, height=40)
                log()
                abr = 0
                return

        labelVerificando.configure(text="Usuario não encontrado")
        abr = 0
    except:
        labelVerificando.configure(text="Usuario não encontrado")
        abr = 0

def carregacam():
    global abr
    if abr == 0:
        threading.Thread(target=carregacam2).start()
        abr = 1

def carregacam2():
    global varnome
    global varnivel
    global abr
    try:
        os.remove(minhapasta+"\\img.jpg")
    except:
        pass
    
    messagebox.showinfo(title="INFO",message="Aperte ESC para fechar a webcam\nAperte S para iniciar a verificação")
    webcam.cam()

    app.focus()

    try:
        img_para_verificar =face_recognition.load_image_file(minhapasta+"\\img.jpg")
        
        labelVerificando.place(x=85, y=300, width=350, height=40)

        labelVerificando.configure(text="Verificando banco de dados")

        linhas = criar.mostrar("SELECT img,nome,nivel FROM pessoas")
        for imagens in linhas:
            imgs = imagens[0]
            with open(minhapasta+"\\img.jpg","wb") as f:
                f.write(imgs)
            imagens_banco = face_recognition.load_image_file("img.jpg")
        
            img_para_verificar_encoding = face_recognition.face_encodings(img_para_verificar)[0]
            imagens_banco_encoding = face_recognition.face_encodings(imagens_banco)[0]
            
            results = face_recognition.compare_faces([img_para_verificar_encoding], imagens_banco_encoding)
            imagens_banco = ''
            os.remove(minhapasta+"\\img.jpg")

            if results[0] == True:
                re = True
            else:
                re = False

            if re == True:
                varnome = imagens[1]
                varnivel = imagens[2]
                labelVerificando.place(x=-1200, y=300, width=350, height=40)
                log()
                abr = 0
                return

        labelVerificando.configure(text="Usuario não encontrado")
        abr = 0
    except:
        labelVerificando.configure(text="Usuario não encontrado")
        abr = 0

# botoes frame login

btncarregarimg= Button(login, text='Carregar imagem',
                        width=10, command=carregaimage)
btncarregarimg.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
btncarregarimg.place(x=170, y=100, width=180, height=50)

btnwebcam= Button(login, text='Utilizar webcam',
                        width=10, command=carregacam)
btnwebcam.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
btnwebcam.place(x=170, y=200, width=180, height=50)

# frame logado

logado = Frame(app, bg='#48d')

Label(logado,text='Usuario logado', bg='#48d', fg='#000', font=(
    'arial', 18)).place(x=70, y=30, width=390, height=40)

labelpessoalogada= Label(logado, text='Nome:', bg='white', fg='#000', font=(
    'arial', 18),anchor=W)
labelpessoalogada.place(x=10, y=80, width=550, height=35)

labelnivelpessoalogada= Label(logado, text='Nivel:', bg='white', fg='#000', font=(
    'arial', 18),anchor=W)
labelnivelpessoalogada.place(x=10, y=115, width=550, height=35)

Label(logado,text='Apenas usuarios de nivel 3 podem\ncadastrar e deletar.', bg='#48d', fg='#000', font=(
    'arial', 18)).place(x=30, y=200, width=500, height=75)

Label(logado,text='Pessoas com nível menor ou igual ao seu', bg='#48d', fg='#000', font=(
    'arial', 18)).place(x=650, y=10, width=500, height=40)

pesquisapessoa = Entry(logado, width=25, font=('arial', 13))
pesquisapessoa.place(x=700, y=60, width=320, height=35)

tablepessoas = ttk.Treeview(logado, columns=(
    'nome','nivel','ultima'), show='headings')
tablepessoas.column('nome', minwidth=300,
                    width=300, anchor=CENTER, stretch=NO)
tablepessoas.column('nivel', minwidth=120,
                    width=120, anchor=CENTER, stretch=NO)
tablepessoas.column('ultima', minwidth=140,
                    width=140, anchor=CENTER, stretch=NO)

tablepessoas.heading('nome', text='Nome', anchor=CENTER)
tablepessoas.heading('nivel', text='Nível de acesso', anchor=CENTER)
tablepessoas.heading('ultima', text='Ultimo login', anchor=CENTER)

tablepessoas.tag_configure('oddrow', background="lightblue", font=('arial', 12))
tablepessoas.tag_configure('evenrow', background="#fff", font=('arial', 12))

tablepessoas.place(x=600, y=100, width=575, height=486)

scrollbartablepessoas = Scrollbar(tablepessoas)
scrollbartablepessoas.pack(side=RIGHT, fill=Y)
tablepessoas.config(yscrollcommand=scrollbartablepessoas.set)
scrollbartablepessoas.config(command=tablepessoas.yview)

# def frame logado

def mostrarpessoas():
    global varnome
    global varnivel

    tablepessoas.column('nome', minwidth=300,
                        width=300, anchor=CENTER, stretch=NO)
    tablepessoas.column('nivel', minwidth=120,
                        width=120, anchor=CENTER, stretch=NO)
    tablepessoas.column('ultima', minwidth=140,
                        width=140, anchor=CENTER, stretch=NO)
    cor = 0
    tablepessoas.delete(*tablepessoas.get_children())
    vquery = "SELECT nome,nivel,ultima FROM pessoas"
    linhas = criar.mostrar(vquery)
    for i in linhas:
        if cor == 0:
            if i[0] == varnome:
                pass
            else:
                if i[1] > varnivel:
                    pass
                else:
                    tablepessoas.insert("", "end", values=i, tags=('oddrow',))
                    cor = 1
        else:
            if i[0] == varnome:
                pass
            else:
                if i[1] > varnivel:
                    pass
                else:
                    tablepessoas.insert("", "end", values=i, tags=('evenrow',))
                    cor = 0

    pesquisapessoa.delete(0,END)          

def pesquisarpessoas():
    global varnome
    global varnivel

    tablepessoas.column('nome', minwidth=300,
                        width=300, anchor=CENTER, stretch=NO)
    tablepessoas.column('nivel', minwidth=120,
                        width=120, anchor=CENTER, stretch=NO)
    tablepessoas.column('ultima', minwidth=140,
                        width=140, anchor=CENTER, stretch=NO)
    cor = 0
    tablepessoas.delete(*tablepessoas.get_children())
    vquery = "SELECT nome,nivel,ultima FROM pessoas WHERE nome LIKE '%" + \
        pesquisapessoa.get()+"%'"
    linhas = criar.mostrar(vquery)
    for i in linhas:
        if cor == 0:
            if i[0] == varnome:
                pass
            else:
                if i[1] > varnivel:
                    pass
                else:
                    tablepessoas.insert("", "end", values=i, tags=('oddrow',))
                    cor = 1
        else:
            if i[0] == varnome:
                pass
            else:
                if i[1] > varnivel:
                    pass
                else:
                    tablepessoas.insert("", "end", values=i, tags=('evenrow',))
                    cor = 0

def deleta():
    try:
        itens = tablepessoas.selection()[0]
        valores = tablepessoas.item(itens, 'values')

        finaliza = messagebox.askyesno(title="AVISO",message="Deseja finalizar a sessao?")
        if finaliza == True:
            try:
                criar.deletapessoa(valores[0])
                mostrarpessoas()
            except:
                messagebox.showerror(title="ERROR",message='Erro ao deletar')
    except:
        messagebox.showerror(title='ERROR',message='Selecione um item da tabela para deletar')

def deletatudo():
    global varnome
    finaliza = messagebox.askyesno(title="AVISO",message="Deseja deletar todos usuarios?")
    if finaliza == True:
        try:
            criar.deletatodaspessoas(varnome)
            mostrarpessoas()
        except:
            messagebox.showerror(title="ERROR",message='Erro ao deletar')

# botoes frame logado
imagereturn = PhotoImage(file=minhapasta+"\\1.png")

btnpesquisarpessoas= Button(logado, text='Buscar', width=10,command= pesquisarpessoas )
btnpesquisarpessoas.configure(bd=1, activebackground="#467", cursor='hand2')
btnpesquisarpessoas.place(x=1050, y=62, width=50, height=30)

btnmostrarpessoas = Button(logado, text='', width=10, command=mostrarpessoas)
btnmostrarpessoas.configure(bd=1, activebackground="#467",
                      cursor='hand2', image=imagereturn)
btnmostrarpessoas.place(x=1110, y=62, width=32, height=30)

btncadastrar= Button(logado, text='Cadastrar',
                        width=10, command=telacadastraproduto)
btncadastrar.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
btncadastrar.place(x=200, y=280, width=180, height=50)

btndeleta= Button(logado, text='Deletar pessoa',
                        width=10, command=deleta)
btndeleta.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
btndeleta.place(x=700, y=600, width=180, height=40)

btndeletatudo= Button(logado, text='Deletar todos',
                        width=10, command=deletatudo)
btndeletatudo.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
btndeletatudo.place(x=900, y=600, width=180, height=40)

btnfinaliza= Button(logado, text='Finalizar sessao',
                        width=10, command=volta)
btnfinaliza.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
btnfinaliza.place(x=200, y=400, width=180, height=50)

btnabrirpla= Button(logado, text='Abrir Planilha',
                        width=10, command=abrplanilha)
btnabrirpla.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
btnabrirpla.place(x=100, y=500, width=180, height=50)

btntxt= Button(logado, text='Informaçoes Ambientais',
                        width=10, command=abrtxt)
btntxt.configure(bd=1, activebackground="#467", cursor='hand2', font=('arial', 14))
btntxt.place(x=300, y=500, width=250, height=50)

app.wm_protocol('WM_DELETE_WINDOW', qui)
app.bind(sequence="<Return>", func=enter)



app.mainloop()