#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
# Tkinter (Tk/Ttk) Progressbar widget example
#
# Written by Yu-Jie Lin
# This code is placed in Public Domain
#
# Gist: https://gist.github.com/livibetter/6850443
# Clip: https://www.youtube.com/watch?v=rKr8wjKuhBY
#
# References:
#
#   * http://docs.python.org/2/library/ttk.html#progressbar
#   * http://docs.python.org/3/library/tkinter.ttk.html#progressbar
#
# Backstory:
#
# I wrote this script because one [1] of my videos got some hits with
# irrelevant keywords. I understand that would be frustrating when the searcher
# wants to find a progress bar in Tk, but gets a video hit about progress bar
# in terminal. So I did some reading and coding to produce this code.
#
# [1]: https://www.youtube.com/watch?v=goeZaYERNnM


try:
  import Tkinter              # Python 2
  import ttk
  import winsound
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk

def main():
	root = Tkinter.Tk()
	ft = ttk.Frame(height=100)
	
	ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
	winsound.PlaySound('sonic.wav', winsound.SND_FILENAME)


	pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')
	pb_hd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
	pb_hd.start(500)
	root.wm_geometry("1000x200")

	entree = Tkinter.Entry(root, textvariable="Entrer le mot de passe", width=30)
	entree.pack()
	win = Tkinter.PhotoImage(file="win.gif")
	fail = Tkinter.PhotoImage(file="fail.gif")
	def end(endType):
		canvas = Tkinter.Canvas(root, width=800, height=450)
		if endType == "win":
			canvas.create_image(0, 0, anchor=Tkinter.NW, image=win)
		else:
			canvas.create_image(0, 0, anchor=Tkinter.NW, image=fail)
		canvas.pack()

		pb_hd.stop()
		pb_hd.pack_forget()
		entree.pack_forget()
		btn.pack_forget()
		root.wm_geometry("1000x500")

	def callback(event):
		if entree.get() == "aston":
			end("win")
		else:
			futur = pb_hd['value'] + 10
			if futur >= 99:
				end("fail")
			else:
				pb_hd.step(10)

	btn = Tkinter.Button(root, text ='Valider')
	btn.bind("<Button-1>", callback)
	btn.pack(side=Tkinter.BOTTOM, padx=5, pady=5)

	def task():
		ft.winfo_toplevel().title("Téléchargement dans " + str(int(pb_hd['value']))+"%")
		root.after(500, task)
		if pb_hd['value'] >= 99:
				end("fail")

	root.after(500, task)
	root.mainloop()

if __name__ == '__main__':
	main()