#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
from Tkinter import *
import time

class ProgressBar(Canvas):
    
    def __init__(self,parent,largeur,hauteur,color, mdp, inert):
        
        global root,valeur,larg,haut,coul,txt,old,rainbow,inertie
        
        root=parent
        larg=largeur
        coul=color
        haut=hauteur
        rainbow=False
        mdp=mdp
        inertie=inert
                
        Canvas.__init__(self)

        self.configure(height=hauteur,width=largeur+40)
        self.create_rectangle(0,0,largeur,hauteur,fill="Tan",outline="AntiqueWhite")
        old=self.create_rectangle(3,3,3,18,fill=color,outline=color)
        txt=self.create_text(largeur+20,hauteur/2,text="0 %")

        valeur=0

    def SetValue(self,consigne):
        
        global root,valeur,larg,color,txt,old,rainbow,haut,inertie

        while (int(valeur*100+.5)!=int(consigne*100+.5)):
            if (valeur<consigne):
                valeur=valeur+(float(consigne-valeur)/50)
                float (valeur)
                self.delete(old)
                self.delete(txt)
                txt=self.create_text(larg+20,haut/2,text=str(int(valeur))+" %")
                longueur=(valeur/100)*larg
                
                if (rainbow==False):
                    couleur=coul
                else:
                    if (valeur<51):
                        col=5.11*valeur
                        if len(hex(int(col))[2:])==2:
                            code=str(hex(int(col))[2:])+"ff00"
                        elif len(hex(int(col))[2:])==1:
                            code="0"+str(hex(int(col))[2:])+"ff00"
                        elif len(hex(int(col))[2:])==1 and int(valeur)==0:
                            code="00ff00"
                        else:
                            code="ffff00"

                    elif (valeur>50):
                        col=255-5.11*(valeur-50)
                        if len(hex(int(col))[2:])==2:
                            code="ff"+str(hex(int(col))[2:])+"00"
                        elif len(hex(int(col))[2:])==1:
                            code="ff0"+str(hex(int(col))[2:])+"00"
                        else:
                            code="ff0000"
                        
                    couleur="#"+code
                    
                old=self.create_rectangle(2,2,longueur,haut-2,fill=couleur,outline=couleur)
                root.update()
                time.sleep(inertie) #Définie l'inertie de l'aiguille (Timer)
                
                
            elif(valeur>consigne):
                valeur=valeur+(float(consigne-valeur)/50)
                float (valeur)
                self.delete(old)
                self.delete(txt)
                txt=self.create_text(larg+20,haut/2,text=str(int(valeur))+" %")
                longueur=(valeur/100)*larg
                
                if (rainbow==False):
                    couleur=coul
                else:
                    if (valeur<51):
                        col=5.11*valeur
                        if len(hex(int(col))[2:])==2:
                            code=str(hex(int(col))[2:])+"ff00"
                        elif len(hex(int(col))[2:])==1:
                            code="0"+str(hex(int(col))[2:])+"ff00"
                        elif len(hex(int(col))[2:])==1 and int(valeur)==0:
                            code="00ff00"
                        else:
                            code="ffff00"

                    elif (valeur>50):
                        col=255-5.11*(valeur-50)
                        if len(hex(int(col))[2:])==2:
                            code="ff"+str(hex(int(col))[2:])+"00"
                        elif len(hex(int(col))[2:])==1:
                            code="ff0"+str(hex(int(col))[2:])+"00"
                        else:
                            code="ff0000"
                        
                    couleur="#"+code
                    

                old=self.create_rectangle(2,2,longueur,haut-2,fill=couleur,outline=couleur)
                root.update()
                time.sleep(inertie) #Définie l'inertie de l'aiguille (Timer)
            
                
            else:
                float (valeur)
                self.delete(old)
                self.delete(txt)
                txt=self.create_text(larg+20,haut/2,text=str(int(valeur))+" %")
                longueur=(valeur/100)*larg
                
                if (rainbow==False):
                    couleur=coul
                else:
                    if (valeur<51):
                        col=5.11*valeur
                        if len(hex(int(col))[2:])==2:
                            code=str(hex(int(col))[2:])+"ff00"
                        elif len(hex(int(col))[2:])==1:
                            code="0"+str(hex(int(col))[2:])+"ff00"
                        elif len(hex(int(col))[2:])==1 and int(valeur)==0:
                            code="00ff00"
                        else:
                            code="ffff00"

                    elif (valeur>50):
                        col=255-5.11*(valeur-50)
                        if len(hex(int(col))[2:])==2:
                            code="ff"+str(hex(int(col))[2:])+"00"
                        elif len(hex(int(col))[2:])==1:
                            code="ff0"+str(hex(int(col))[2:])+"00"
                        else:
                            code="ff0000"
                        
                    couleur="#"+code
                    
                txt=self.create_text(larg+20,haut/2,text=str(int(valeur))+" %")
                old=self.create_rectangle(2,2,longueur,haut-2,fill=couleur,outline=couleur)
                root.update()
                time.sleep(inertie) #Définie l'inertie de l'aiguille (Timer)

    def OnRainbow(self):
            
        global rainbow

        rainbow=True

    def SetColor(self,couleur):

        global rainbow,color

        rainbow=False
        color=couleur

    def SetBackgroundColor(couleur):

        global haut,larg

        self.create_rectangle(0,0,larg,haut,fill=couleur,outline=couleur)

    def changeInertie(intertValue):
    	inertie = intertValue

fenetre = Tk()

def callback(event):
    print "clicked at", event.x, event.y

btn = Button(fenetre, text ='Bouton 1')
btn.bind("<Button-1>", callback)
btn.pack(side=BOTTOM, padx=5, pady=5)

pg = ProgressBar(fenetre,1000,100,"red", "aston", 3)

pg.pack()
pg.SetValue(100)


fenetre.mainloop()
