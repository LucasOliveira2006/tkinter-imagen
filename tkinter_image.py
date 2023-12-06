from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image, ImageOps
import os 
#seleciona uma pasta
def open_file():
    folder_path= filedialog.askdirectory()
    if folder_path:
        #mostra uma caixa de mensagem com uma informação
        messagebox.showinfo(
            title='Abrindo diretório...',
            message=f'O arquivo selecionado foi: {folder_path}'
)
    #mostra uma caixa de mensagem caso ocorra algum erro
    else:
        messagebox.showerror(
            title='Erro ao abrir diretório',
            message='Nenhum diretório foi selecionado'
        )


root = Tk()
root.title("Imagens engraçadas e aleatorias :)")
#Cria uma barra de menu
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(   
    label="Open",
    command=open_file
)
filemenu.add_command(label='Save')
filemenu.add_command(label='Exit')

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

#Lista os arquivos da pasta imagens
arquivos = os.listdir("imagens")

#Variavel para armazenar as imagens
imagens =[]
#Variavel de controle do indice da imagen atual
imagen_atual = 0


#percorre a lista de arquivos
for arquivo in arquivos:
    try:
        #Abre a imagen
        img= Image.open("imagens/"+ arquivo)
    except Exception as e:
        print(e)
        continue
    else:
        #Redimensiona a imagen
        img= ImageOps.contain(img, (400,400))
        #adiciona a imagen na list
        imagens.append(ImageTk.PhotoImage(img))

#Exibe os arquivos em um Label
#arquivos_label = Label(root, text=arquivos)
#arquivos_label.pack()
#img = Image.open('imagens/Egg.png')
#img_Tk = ImageTk.PhotoImage(img)

img_label = Label(root, image=imagens[imagen_atual])
img_label.grid(column=2, row=0,columnspan=3)

def prev_image():
    global imagen_atual
    global img_label
    global imagens
#Verifica se é a primeira imagen se sim volta para a ultima imagen
    if imagen_atual == 0:
        imagen_atual = len(imagens) -1
    else:
        imagen_atual -= 1
#Apaga a imagen atual
    img_label.grid_forget()

    img_label = Label(root, image=imagens[imagen_atual])
    img_label.grid(column=2, row=0, columnspan=3)

def next_image():
    global imagen_atual
    global img_label
    global imagens
#Verifica se é a primeira imagen se sim volta para a ultima imagen
    if  imagen_atual == len(imagens) -1:
        imagen_atual == 0
    else:
        imagen_atual += 1
#Apaga a imagen atual
    img_label.grid_forget()

    img_label = Label(root, image=imagens[imagen_atual])
    img_label.grid(column=2, row=0, columnspan=5)



Prev = Button(root, text="Prev", command=prev_image, bg ="#cb4a34", fg="#f6f0e9")
Prev.grid(column=1, row=1, columnspan=3,)

Sair = Button(root, text="Sair", command=root.quit, bg ="#1c1f21", fg="#f6f0e9")
Sair.grid(column=2, row=1, columnspan=3)

Next = Button(root, text="Next", command=next_image, bg ="#cb4a34", fg="#f6f0e9")
Next.grid(column=3, row=1, columnspan=3,)

root.bind('<Right>', lambda event:next_image())
root.bind('<Left>', lambda event:prev_image())
root.bind('<Escape>', lambda event:root.quit())

root.mainloop() 