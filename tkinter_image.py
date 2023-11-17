from tkinter import *
from PIL import ImageTk, Image
import os 

root = Tk()
#Lista os arquivos da pasta imagens
arquivos = os.listdir("imagens")

#Variavel para armazenar as imagens
imagens =[]

#percorre a lista de arquivos
for arquivo in arquivos:
    #Abre a imagen
    img= Image.open("imagens/"+ arquivo)
    #adiciona a imagen na lista
    imagens.append(ImageTk.PhotoImage(img))

#Exibe os arquivos em um Label
#arquivos_label = Label(root, text=arquivos)
#arquivos_label.pack()
#img = Image.open('imagens/Egg.png')
#img_Tk = ImageTk.PhotoImage(img)

img_label = Label(root, image=imagens[0])

img_label.pack()

root.mainloop() 