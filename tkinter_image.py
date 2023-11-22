from tkinter import *
from PIL import ImageTk, Image, ImageOps
import os 

root = Tk()
#Lista os arquivos da pasta imagens
arquivos = os.listdir("imagens")

#Variavel para armazenar as imagens
imagens =[]
#Variavel de controle do indice da imagen atual
imagen_atual = 0


#percorre a lista de arquivos
for arquivo in arquivos:
    #Abre a imagen
    img= Image.open("imagens/"+ arquivo)
    #Redimensiona a imagen
    img= ImageOps.contain(img, (600,600))
    
    #adiciona a imagen na lista
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
    img_label.grid(column=2, row=0, columnspan=3)



Prev = Button(root, text="Prev", command=prev_image)
Prev.grid(column=1, row=1,columnspan=3)

Sair = Button(root, text="Sair", command=root.quit)
Sair.grid(column=2, row=1,columnspan=3)

Next = Button(root, text="Next", command=next_image)
Next.grid(column=3, row=1,columnspan=3)

root.mainloop() 