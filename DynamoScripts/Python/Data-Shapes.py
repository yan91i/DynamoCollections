#Copyright (c) mostafa el ayoubi ,  2016
#Data-Shapes www.data-shapes.net , elayoubi.mostafa@gmail.com

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Point
from System.Windows.Forms import Application, Button, Form, Label, TextBox, CheckBox, FolderBrowserDialog, OpenFileDialog, DialogResult, ComboBox, FormBorderStyle
from System.Collections.Generic import *


clr.AddReference('RevitAPIUI')
from  Autodesk.Revit.UI import Selection

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

#getting screen resolution and creating resolution factor to handle high res screens
import ctypes
user32 = ctypes.windll.user32
resolutionX = user32.GetSystemMetrics(0)
resolutionY = user32.GetSystemMetrics(1)
resfactX = resolutionX/1920
resfactY = resolutionY/1080



class MultiTextBoxForm(Form):


    def __init__(self):
        self.Text = 'Data-Shapes | Multi Input UI'
        self.output = []
        self.values = []

    def setclose(self, sender, event):
    	cbindexread = 0
    	for f in self.output:
    		if f.GetType() == TextBox:
    			self.values.append(f.Text)
    		if f.GetType() == CheckBox:
    			self.values.append(f.Checked)
    		if f.GetType() == Button:
    			if f.Tag == None :
    				self.values.append(f.Text)
    			else:
    				self.values.append(f.Tag)
    		if f.GetType() == ComboBox:
    			self.values.append(globals() ['dict%d'%(cbindexread)][f.Text])
    			cbindexread += 1
    	self.Close()

    def reset(self, sender, event):
		pass

    def openfile(self, sender, event):
		ofd = OpenFileDialog()
		dr = ofd.ShowDialog()
		if dr == DialogResult.OK:
			sender.Text = ofd.FileName

    def opendirectory(self, sender, event):
		fbd = FolderBrowserDialog()
		dr = fbd.ShowDialog()
		if dr == DialogResult.OK:
			sender.Text = fbd.SelectedPath

    def pickobjects(self, sender, event):
		sel = uidoc.Selection.PickObjects(Selection.ObjectType.Element,'')
		selelem = [doc.GetElement(s.ElementId) for s in sel]
		sender.Tag = (selelem)

    def pickfaces(self, sender, event):
		selface = uidoc.Selection.PickObjects(Selection.ObjectType.Face,'')
		faces = [uidoc.Document.GetElement(s).GetGeometryObjectFromReference(s).ToProtoType(True) for s in selface]
		sender.Tag = [i for f in faces for i in f]

    def pickedges(self, sender, event):
		seledge = uidoc.Selection.PickObjects(Selection.ObjectType.Edge,'')
		edges = [uidoc.Document.GetElement(s).GetGeometryObjectFromReference(s).AsCurve().ToProtoType(True) for s in seledge]
		sender.Tag = edges

    def topmost(self):
		self.TopMost = True



form = MultiTextBoxForm()
form.topmost()

xlabel = 25*resfactX
xinput = 125*resfactX
y = 10*resfactY
fields = []
error = 0
cbindex = 0
inputheight = 20*resfactY
inputwidth = 150*resfactX
#Input form

if isinstance(IN[0],list):
	inputnames = IN[0]
else:
	inputnames = [IN[0]]

if isinstance(IN[1],list):
	inputtypes = IN[1]
else:
	inputtypes = [IN[1]]

for i,j in zip(inputnames,inputtypes):
	label = Label()
	label.Location = Point(xlabel,y+4*resfactY)
	label.Height = 20*resfactY
	label.Width = 80*resfactX
	label.Text = str(i)
	form.Controls.Add(label)
	if isinstance(j,list):
		cb = ComboBox()
		cb.Location = Point(xinput,y)
		cb.Width = 150*resfactX
		globals()['dict%d'%(cbindex)] = {}
		try :
			for k in j:
				globals()['dict%d'%(cbindex)][k.Name] = k
				cb.Items.Add(k.Name)
		except :
			for k in j:
				try:
					globals()['dict%d'%(cbindex)][str(k)] = k
				except:
					globals()['dict%d'%(cbindex)][k.encode('utf-8').decode('utf-8')] = k
				cb.Items.Add(k)
		form.Controls.Add(cb)
		form.output.append(cb)
		cbindex += 1
	elif j == 's':
		tb = TextBox()
		tb.Text = 'Default'
		tb.Width = inputwidth
		tb.Height = inputheight
		tb.Location = Point(xinput,y)
		form.Controls.Add(tb)
		form.Controls.Add(label)
		form.output.append(tb)
	elif j == 'bool':
		yn = CheckBox()
		yn.Location = Point(xinput,y)
		yn.Text = 'Yes/No'
		form.Controls.Add(yn)
		form.output.append(yn)
	elif j == 'fp':
		fp = Button()
		fp.Width = inputwidth
		fp.Height = inputheight
		fp.Text = 'FilePath'
		fp.Location = Point(xinput,y)
		form.Controls.Add(fp)
		fp.Click += form.openfile
		form.output.append(fp)
	elif j == 'dp':
		dp = Button()
		dp.Width = inputwidth
		dp.Height = inputheight
		dp.Text = 'DirectoryPath'
		dp.Location = Point(xinput,y)
		form.Controls.Add(dp)
		dp.Click += form.opendirectory
		form.output.append(dp)
	elif j == 'se':
		se = Button()
		se.Width = inputwidth
		se.Height = inputheight
		se.Text = 'Select model element(s)'
		se.Location = Point(xinput,y)
		form.Controls.Add(se)
		se.Click += form.pickobjects
		form.output.append(se)
	elif j == 'sf':
		sf = Button()
		sf.Width = inputwidth
		sf.Height = inputheight
		sf.Text = 'Select face(s)'
		sf.Location = Point(xinput,y)
		form.Controls.Add(sf)
		sf.Click += form.pickfaces
		form.output.append(sf)
	elif j == 'sed':
		sed = Button()
		sed.Width = inputwidth
		sed.Height = inputheight
		sed.Text = 'Select Edge(s)'
		sed.Location = Point(xinput,y)
		form.Controls.Add(sed)
		sed.Click += form.pickedges
		form.output.append(sed)

	else :
		error = 'One or more input types are invalid, visit www.data-shapes.net for more informations'
	y+= 30*resfactY


button = Button()
button.Text = 'Set values'
button.Width = inputwidth
button.Height = inputheight
button.Location = Point (100*resfactX,y+30*resfactY)
button.Click += form.setclose
form.Controls.Add(button)

form.MaximizeBox = False
form.MinimizeBox = False
form.FormBorderStyle = FormBorderStyle.FixedSingle

form.Width = 300*resfactX
form.Height = y + 120*resfactY


if error == 0 and IN[2] == True:
	Application.Run(form)
	result = form.values
	OUT = result,True

elif IN[2] == False:
	result = "Set toggle to true!"
	OUT = result,False
