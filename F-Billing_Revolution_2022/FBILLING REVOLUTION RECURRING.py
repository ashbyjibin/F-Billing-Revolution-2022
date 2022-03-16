# from ossaudiodev import SOUND_MIXER_SPEAKER
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# from PIL import ImageTk, Image
# import pandas as pd
# from tkinter.messagebox import showinfo
from prettytable import PrettyTable
import tkinter.scrolledtext as scrolledtext
import tkinter.scrolledtext as st
# from tkinter.filedialog import askopenfilename
import subprocess # for system calculator
# from borb.pdf.document import Document 
# from borb.pdf.page.page import Page
from reportlab.pdfgen import canvas
from tkcalendar import Calendar
import datetime
# from datetime import timedelta
from tkcalendar import DateEntry
# import os
# import webbrowser

# from tkcalendar import Calendar
# from tkcalendar import DateEntry
# from datetime import date
from tkinter import filedialog
import tkinter as tk
from tkinter.tix import ComboBox, Tree
from typing_extensions import Self
# import MySQLdb
# con = MySQLdb.connect(host="localhost", user="root", password="", database="fbilldb")
from models import *


root=Tk()
root.geometry("1360x730")
root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)

s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
tabControl.pack(expand = 1, fill ="both")




selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")


photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")



#--------------------TAB-4  RECURRING-ASHBY---------------------


  
    
# def generate_recurring():  
#    messagebox.showinfo("F-Billing Revolution 2022", "1 new invoice successfully created.")
 #generate recurring invoice popups
def generate_recurring_noinvoice(): 
  #  if result=='ok': 
   messagebox.showinfo("F-Billing Revolution 2022", "No recurring invoices are ready today")


#print invoice
  
def print_invoice_recurring():

  def property1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 28, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy Count:").place(x=55, y=95)
      nocopy = Spinbox(propert1,from_=0,to=100000000, width=28).place(x=150, y=95)    

      btn=Button(propert1,text="OK", width=10,).place(x=390, y=425)
      btn=Button(propert1,text="Cancel", width=10,).place(x=490, y=425) 




      okbtn=Button(propert1,text="OK", width=10,).place(x=390, y=425)
      canbtn=Button(propert1,text="Cancel", width=10,).place(x=490, y=425)  
      
      
   
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=property2).place(x=450, y=370)
    btn=Button(property_Frame,text="OK", width=10,).place(x=390, y=410)
    btn=Button(property_Frame, text="Cancel", width=10,).place(x=490, y=410)  


    
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1, text="Ok", width=10).place(x=460, y=370)
      canbtn=Button(print1, text="Cancel", width=10).place(x=560, y=370)
      


#email
      
def email_invoice_recurring():
  mailDetail=Toplevel()
  mailDetail.title("Invoice E-Mail")
  mailDetail.geometry("1080x550")
  mailDetail.resizable(False, False)
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)

  messagelbframe=LabelFrame(email_Frame,text="Message", height=500, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1,command=addacnt).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)



  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)

  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings",command=savesettings).place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)


def addacnt():  
   messagebox.showinfo("F-Billing Revolution 2022", "No sender email address.\nPlease fill Your company email address textfield under the Account tab.")

def savesettings():  
   messagebox.showinfo("F-Billing Revolution 2022", "Your E-mail configuration settings has been saved.")


def printpreviewinvoice_recurring():
  # root = Tk()
  # root = Toplevel()
  # root.title("F-Billing Revolution Invoice Report ")
  # p2= PhotoImage(file = "images/fbicon.png")
  # root.iconphoto(False, p1)
  # root.geometry("1800x1800+0+0")
  # canvas = Canvas(root)
  # canvas.place(relwidth=1, relheight=1,x=250,y=10) 
 
  # paperheigth = root.winfo_fpixels('1m') * 297
  # paperwidth = root.winfo_fpixels('1m') * 210

  # ws  = Tk()
  # ws.title('PythonGuides')
  # ws.geometry('300x400')

  # root = Tk()
  # lst = [('', 'INVOICE', 'PRICE', 'QUANTITY'),
  #     (1, 1003, '500', 1),
  #     (2, 1003, '500', 1)] 
  # total_rows = len(lst)
  # total_columns = len(lst[1])
  # for i in range(total_rows):      
  #   for j in range(total_columns):    
  #     e = Entry(
  #         root,
  #         width = 20,
  #         fg = 'blue',
  #         font = ('Arial', 16, 'bold'))
  #     e.grid(row=i, column=j)
  #     e.insert(0, lst[i][j])
   
  # root = Tk()
  # # var = StringVar()
  # root.maxsize(1360,740)       # Sets max size of window
  # root.minsize(320,240)

  # canvas_height = 800
  # canvas_width = 800

  # w = Canvas(root, width=canvas_width, height=canvas_height)
  # w.create_rectangle(5, canvas_height, canvas_width, 2,   fill="#ffffff")  
  # # la = Label(root, text='hai', relief=RAISED ).place(x=5,y=20)



  
  ws = Tk()
  ws.title('F-Billing Revolution 2022 - invoice')
  ws.maxsize(1360,740)       # Sets max size of window
  ws.minsize(1360,740)
  ws['bg']='#999999'

  style = ttk.Style(root)
  style.theme_use("clam")
  style.theme_use("default")
  # style.configure("Treeview.Heading", background="#ffad33")

  # tree=ttk.Treeview(master,style="mystyle.Treeview")
 
  tv = ttk.Treeview(ws, style="mystyle.Treeview")
  tv["show"]='headings'
  tv['columns']=('Id/sku', 'Product/Service', 'Quantity','Unit Price','Price')
  tv.column('Id/sku', anchor=CENTER, width=100 )
  tv.column('Product/Service', anchor=CENTER, width=300)
  tv.column('Quantity', anchor=CENTER, width=100)
  tv.column('Unit Price', anchor=CENTER, width=100)
  tv.column('Price', anchor=CENTER, width=100)

  tv.heading('Id/sku', text='ID/SKU', anchor=CENTER)
  tv.heading('Product/Service', text='Product/Service - Description', anchor=CENTER)
  tv.heading('Quantity', text='Quantity', anchor=CENTER)
  tv.heading('Unit Price', text='Unit Price', anchor=CENTER)
  tv.heading('Price', text='Price', anchor=CENTER)

  # tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
  # tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
  # tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
  # tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
  # tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
  fbcursor.execute('SELECT * FROM Productservice')
  j = 0
  for i in fbcursor:
    tv.insert(parent='', index='end', iid=i, text=' ', values=(i[0],i[5],i[7],i[12],i[9]))
    j += 1


  tv.pack()


  ws.mainloop()

    



def search_recur():
  sear = searchvar.get()
  for record in rtree.get_children():
    rtree.delete(record)
  searchtop.destroy()
  
  fb = mysql.connector.connect(
      host="localhost", user="root", password="", database="fbilldb", port="3306"
  )
  fcursor = fb.cursor()
  
  sql = "select * from invoice where businessname = %s "
  val = (sear, )
  fcursor.execute(sql, val)
  records = fcursor.fetchall()
  
  count=0
  for i in records:
    if True:
      rtree.insert(parent='', index='end', iid=i, text='rtree', values=('', i[0], i[26], i[24], i[27], i[18], i[8]))
    else:
      pass
  count += 1
  
  fb.commit()
  fb.close()

def recur_cust_search():
    global searchvar, searchtop
    searchtop = Toplevel()  
    searchtop.title("Find Text")
    searchtop.geometry("520x200+390+250")
    
    findwhat1=Label(searchtop,text="Find What:",pady=5,padx=10)
    findwhat1.place(x=5,y=20)
    searchvar = StringVar() 
    findwhat = ttk.Combobox(searchtop, width = 50, textvariable = searchvar)
    findwhat.place(x=80,y=25) 
    

    findButton = Button(searchtop, text ="Find next",width=10, command=search_recur)
    findButton.place(x=420,y=20)
    
    findin1=Label(searchtop,text="Find in:",pady=5,padx=10)
    findin1.place(x=5,y=47)
    n = StringVar() 
    findIN = ttk.Combobox(searchtop, width = 37, textvariable = n ) 
    # Adding combobox drop down list 
    findIN['values'] = ('Invoice#',  
                              ' Next Invoice', 
                              ' Recurring Period', 
                              ' Stop After', 
                              ' Customer Name', 
                              ' Invoice Total',  
                              ' <<All>>') 
      
    findIN.place(x=80,y=54) 
    findIN.current(0)

    closeButton = Button(searchtop, text ="Close",width=10, command=lambda : searchtop.destroy())
    closeButton.place(x=420,y=50)

    match1=Label(searchtop,text="Match:",pady=5,padx=10)
    match1.place(x=5,y=74)
    n = StringVar() 
    match = ttk.Combobox(searchtop, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    match['values'] = ('From Any part',' Whole Field',  
                              ' From the beginning of the field')
      
    match.place(x=80,y=83) 
    match.current(0)

    search1=Label(searchtop,text="Search:",pady=5,padx=10)
    search1.place(x=5,y=102)
    n = StringVar() 
    search = ttk.Combobox(searchtop, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    search['values'] = ('All', 'up', 
                              'Down')
      
    search.place(x=80,y=112) 
    search.current(0)


    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(searchtop,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=60,y=141)

    checkvarStatus5=IntVar()
   
    Button5 = Checkbutton(searchtop,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button5.place(x=270,y=141)

# def recur_refresh():
   
  
   

#convert to invoice
def convert():
  if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
        messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
  else:
      messagebox.destroy()
  

#search in invoice 
# def search_invoice_recurring():  
#     top = Toplevel()     
#     top.title("Find Text")   
#     top.geometry("600x250+390+250")
#     findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
#     n = StringVar()
#     findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
#     findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
#     n = StringVar()
#     findIN = ttk.Combobox(top, width = 30, textvariable = n )
#     findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
#     findIN.place(x=90,y=54)
#     findIN.current(0)

#     findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
#     closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
#     match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
#     n = StringVar()
#     match = ttk.Combobox(top, width = 23, textvariable = n )   
#     match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                    
#     match.place(x=90,y=83)
#     match.current(0)

#     search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
#     n = StringVar()
#     search = ttk.Combobox(top, width = 23, textvariable = n )
#     search['values'] = ('All', 'up',' Down')
#     search.place(x=90,y=112)
#     search.current(0)
#     checkvarStatus4=IntVar()  
#     Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
#     Button4.place(x=90,y=141)
#     checkvarStatus5=IntVar()   
#     Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
#     Button5.place(x=300,y=141)

#-------------------------view/edit invoice---------------------------

#--------------------------calculator-recurring----------------------

def calculator_recurring():
  subprocess.Popen('C:\\Windows\\System32\\calc.exe')


#edit/view invoice in recurring 

def view_invoice_recurring():
  try:
    itemid = rtree.item(rtree.focus())["values"][0]
    pop=Toplevel(midFrame)
    global dateentry
    expdate=StringVar()
    pop.title("Invoice")
    pop.geometry("950x690+150+0")


    #select customer
    def customer_invoice_recurring():
      cuselection=Toplevel()
      cuselection.title("Select Customer")
      cuselection.geometry("930x650+240+10")
      cuselection.resizable(False, False)

    
      def create1():
        ven=Toplevel(midFrame)
        global checkvar1,checkvar2,cnotes,custid,bname,baddress,cat,sname,saddress,contp,cemail,ctel,cfax,cmob,scontp,scemail,sctel,scfax,ccountry,ccity,taxentry,discoutentry
        ven.title("Add new vendor")
        ven.geometry("930x650+240+10")
        checkvar1=IntVar()
        checkvar2=IntVar()
        radio=IntVar()
        createFrame=Frame(ven, bg="#f5f3f2", height=650)
        createFrame.pack(side="top", fill="both")
        labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        labelframe1.place(x=10,y=5,width=910,height=600)
        text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        custid=Entry(labelframe1,width=25)
        custid.place(x=150,y=10)
        
        text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        cat=ttk.Combobox(labelframe1,width=25,value="Default")
        cat.place(x=460 ,y=10)
        text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        
        labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        labelframe2.place(x=5,y=40,width=420,height=150)
        name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        sname = Entry(labelframe2,width=28)
        sname.place(x=130,y=5)
        addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        saddress = Entry(labelframe2,width=28)
        saddress.place(x=130,y=40,height=80)
        
        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

        labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        labelframe3.place(x=480,y=40,width=420,height=150)
        name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        bname = Entry(labelframe3,width=28)
        bname.place(x=130,y=5)
        addr = Label(labelframe3, text="AddSress:",bg="#f5f3f2").place(x=5,y=40)
        baddress = Entry(labelframe3,width=28)
        baddress.place(x=130,y=40,height=80)
        
        labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe4.place(x=5,y=195,width=420,height=150)
        name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        contp = Entry(labelframe4,width=28)
        contp.place(x=130,y=5)
        email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        cemail = Entry(labelframe4,width=28)
        cemail.place(x=130,y=35)
        tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        ctel = Entry(labelframe4,width=11)
        ctel.place(x=130,y=65)
        fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        cfax = Entry(labelframe4,width=11)
        cfax.place(x=280,y=65)
        sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        cmob = Entry(labelframe4,width=15)
        cmob.place(x=248,y=95)      

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

        
        labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
        labelframe5.place(x=480,y=195,width=420,height=125)
        name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        scontp = Entry(labelframe5,width=28)
        scontp.place(x=130,y=5)
        email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        scemail = Entry(labelframe5,width=28)
        scemail.place(x=130,y=35)
        tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        sctel = Entry(labelframe5,width=11)
        sctel.place(x=130,y=65)
        fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        scfax = Entry(labelframe5,width=11)
        scfax.place(x=280,y=65)

        labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe6.place(x=5,y=350,width=420,height=100)
        Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        taxentry = Entry(labelframe6,width=10)
        taxentry.place(x=290,y=5)
        discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        discoutentry = Entry(labelframe6,width=10)
        discoutentry.place(x=100,y=35)

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe7.place(x=480,y=330,width=420,height=100)
        country= Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        ccountry = Entry(labelframe7,width=28)
        ccountry.place(x=130,y=5)
        city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        ccity = Entry(labelframe7,width=28)
        ccity.place(x=130,y=35)

        labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
        labelframe8.place(x=5,y=460,width=420,height=100)
        R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
        labelframe9.place(x=480,y=430,width=420,height=150)
        cnotes = Entry(labelframe9)
        cnotes.place(x=10,y=10,height=100,width=390)

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK",command=rec_cust_reg).place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
                

      enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(cuselection, width=20).place(x=110, y=10)
      text=Label(cuselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(cuselection, width=20).place(x=450, y=10)
      
      global custree

      custree=ttk.Treeview(cuselection, height=27)
      custree["columns"]=["1","2","3", "4"]
      custree.column("#0", width=35, )
      custree.column("1", width=160)
      custree.column("2", width=160)
      custree.column("3", width=140)
      custree.column("4", width=140)
      custree.heading("#0",text="")
      custree.heading("1",text="Customer/Ventor ID")
      custree.heading("2",text="Customer/Ventor Name")
      custree.heading("3",text="Tel.")
      custree.heading("4",text="Contact Person")
      custree.place(x=5, y=45)
      
      fbcursor.execute('SELECT * FROM Customer;') 
      j = 0
      for i in fbcursor:
        custree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))
        j += 1


      ctegorytree=ttk.Treeview(cuselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      scrollbar = Scrollbar(cuselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=tree.yview )

      btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60, command=treefthcng).place(x=15, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=create1).place(x=250, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=create1).place(x=435, y=610)
      btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   
  



    # def customer_reg():# Storing values into db (user)
    #    businessname =  bname.get()
    #    sql=('INSERT INTO Customer (businessname) VALUES(%s)')
    #    val=(businessname)
    #    fbcursor.execute(sql,val)
    #    fbilldb.commit()
    #    messagebox.showinfo('Registration successfull')  

    

    #add new line item
    def newline_recurring():
      newselection=Toplevel()
      newselection.title("Product/Services")
      newselection.geometry("930x650+240+10")
      newselection.resizable(False, False)

      

      #add new product
      def product():  
        top = Toplevel()
        global codeentry,nameentry,country,desentry,unitentry,pcsentry,costentry,priceentry,stockentry,lowentry,wareentry,txt,checkvarStatus,checkvarStatus2,checkvarStatus3
        top.title("Add a new Product/Service")
        p2 = PhotoImage(file = 'images/fbicon.png')
        top.iconphoto(False, p2)
      
        top.geometry("700x550+390+15")
        tabControl = ttk.Notebook(top)
        s = ttk.Style()
        s.theme_use('default')
        s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
      
        tabControl.add(tab1,compound = LEFT, text ='Product/Service')
        tabControl.add(tab2,compound = LEFT, text ='Product Image')
      
        tabControl.pack(expand = 1, fill ="both")
      
        innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
        innerFrame.pack(side="top",fill=BOTH)

        Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
        Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

        code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
        code1.place(x=20,y=0)
        codeentry = Entry(Customerlabelframe,width=35)
        codeentry.place(x=120,y=8)

        checkvarStatus=IntVar()
        status1=Label(Customerlabelframe,text="Status:")
        status1.place(x=500,y=8)
        Button1 = Checkbutton(Customerlabelframe,
                          variable = checkvarStatus,text="Active",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                        
                          width = 10)

        Button1.place(x=550,y=5)

        category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
        category1.place(x=20,y=40)
        n = StringVar()
        country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
        
        country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
        
        country.place(x=120,y=45)
        country.current(0)


        name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
        name1.place(x=20,y=70)
        nameentry = Entry(Customerlabelframe,width=60)
        nameentry.place(x=120,y=75)

        des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
        des1.place(x=20,y=100)
        desentry = Entry(Customerlabelframe,width=60)
        desentry.place(x=120,y=105)

        uval = IntVar(Customerlabelframe, value='$0.00')
        unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        unit1.place(x=20,y=130)
        unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
        unitentry.place(x=120,y=135)

        pcsval = IntVar(Customerlabelframe, value='$0.00')
        pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        pcs1.place(x=320,y=140)
        pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
        pcsentry.place(x=410,y=140)

        costval = IntVar(Customerlabelframe, value='$0.00')
        cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
        cost1.place(x=20,y=160)
        costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
        costentry.place(x=120,y=165)

        priceval = IntVar(Customerlabelframe, value='$0.00')
        price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
        price1.place(x=20,y=190)
        priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
        priceentry.place(x=120,y=195)

        checkvarStatus2=IntVar()
      
        Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                          text="Taxable Tax1rate",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                          height=2,
                          width = 12)

        Button2.place(x=415,y=170)


        checkvarStatus3=IntVar()
      
        Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                          text="No stock Control",
                          onvalue =1 ,
                          offvalue = 0,
                          height=3,
                          width = 15)

        Button3.place(x=40,y=220)


        stockval = IntVar(Customerlabelframe, value='0')
        stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
        stock1.place(x=90,y=260)
        stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
        stockentry.place(x=150,y=265)

        lowval = IntVar(Customerlabelframe, value='0')
        low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        low1.place(x=300,y=260)
        lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
        lowentry.place(x=495,y=265)

      
        ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
        ware1.place(x=60,y=290)
        wareentry = Entry(Customerlabelframe,width=50)
        wareentry.place(x=150,y=295)

        text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        text1.place(x=20,y=330)

        txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
        txt.place(x=32,y=358)




        okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60,command=rec_pro_insert)
        okButton.pack(side=LEFT)

        cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
        cancelButton.pack(side=RIGHT)

        imageFrame = Frame(tab2, relief=GROOVE,height=580)
        imageFrame.pack(side="top",fill=BOTH)

        browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        browseimg.place(x=15,y=35)

        browsebutton=Button(imageFrame,text = 'Browse')
        browsebutton.place(x=580,y=30,height=30,width=50)
        
        removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
        removeButton.place(x=400,y=450)
                      
      enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(newselection, width=20).place(x=110, y=10)
      text=Label(newselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(newselection, width=20).place(x=450, y=10)

      cusventtree=ttk.Treeview(newselection, height=27)
      cusventtree["columns"]=["1","2","3", "4","5"]
      cusventtree.column("#0", width=35,  anchor="center")
      cusventtree.column("1", width=160,  anchor="center")
      cusventtree.column("2", width=160,  anchor="center")
      cusventtree.column("3", width=140,  anchor="center")
      cusventtree.column("4", width=70,  anchor="center")
      cusventtree.column("5", width=70,  anchor="center")
      cusventtree.heading("#0",text="")
      cusventtree.heading("1",text="ID/SKU")
      cusventtree.heading("2",text="Product/Service Name")
      cusventtree.heading("3",text="Unit price")
      cusventtree.heading("4",text="Service")
      cusventtree.heading("5",text="Stock")
      cusventtree.place(x=5, y=45)


      def selectpro():
        selected =  cusventtree.focus()
        global valuep
        valuep=  cusventtree.item(selected)["values"][0]
        # messagebox.showinfo("",valuep)

        sql = "SELECT * FROM productservice  WHERE productserviceid= %s"
        i=(valuep,)
        fbcursor.execute(sql,i)
        
        j = 0
        for i in fbcursor:
         tree.insert(parent='', index='end', iid=i, text='', values=(i[2],i[4],i[5],i[7],i[13],i[8],i[10],(i[7]*i[13])))
        j += 1


      fbcursor.execute('SELECT * FROM Productservice;') 
      j = 0
      for i in fbcursor:
        cusventtree.insert(parent='', index='end', iid=i, text=' ', values=(i[0],i[4],i[7],i[12],i[13]))
        j += 1


     
      ctegorytree=ttk.Treeview(newselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)
      
      scrollbar = Scrollbar(newselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=tree.yview )
    
    
      btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60, command=selectpro).place(x=15, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
      btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)

      # fbcursor.execute('SELECT Productservice.Productserviceid, Productservice.name, Productservice.description, Productservice.unitprice, Productservice.sku,invoice.tax1,invoice.invoicetot FROM Productservice, invoice WHERE Productservice.Productserviceid = invoice.Productserviceid')
      # j = 0
      # for i in fbcursor:
      #   tree.insert(parent='', index='end', iid=i, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
      #   j += 1
    
      #---------------------------------------------------------
      



    # #preview message if customer  is not
    # def previewline():
    #   messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


    
    #sms notification
    def sms_recurring():
      send_SMS=Toplevel()
      send_SMS.geometry("700x480+240+150")
      send_SMS.title("Send SMS notification")

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      sms_Notebook = ttk.Notebook(send_SMS)
      SMS_Notification = Frame(sms_Notebook, height=470, width=700)
      SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
      sms_Notebook.add(SMS_Notification, text="SMS Notification")
      sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
      sms_Notebook.place(x=0, y=0)

      numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
      numlbel.place(x=10, y=10)
      numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
      stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
      stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
      
      dclbel=Label(SMS_Notification, text="Double click to insert into text")
      dclbel.place(x=410, y=60)
      dcl=Entry(SMS_Notification, width=30)
      dcl.place(x=400, y=85,height=200)
      
      smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
      smstype.place(x=10, y=223)
      snuvar=IntVar()
      normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
      unicode_rbtn.place(x=190, y=5)
      tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
      tiplbf.place(x=10, y=290)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
      tiplabl.place(x=5, y=5)

      btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
      btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
      btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
      

      smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
      smstype.place(x=10, y=5)
      snumvar=IntVar()
      normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
      unicode_rbtn.place(x=290, y=5)

      sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
      sms1type.place(x=10, y=80)
      name=Label(sms1type, text="Username").place(x=10, y=5)
      na=Entry(sms1type, width=20).place(x=100, y=5)
      password=Label(sms1type, text="Password").place(x=10, y=45)
      pas=Entry(sms1type, width=20).place(x=100, y=45)
      combo=Label(sms1type, text="Route").place(x=400, y=5)
      n = StringVar()
      combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
      btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

      
      tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
      tiplbf.place(x=10, y=190)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
      tiplabl.place(x=0, y=5)
      tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
      tiplabl1.place(x=0, y=60)
      tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
      tiplabl2.place(x=0, y=100)
      tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
      tiplabl3.place(x=0, y=140)
      checkvar1=IntVar()
      chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 

    #mark invoice
    def markinvoice_recurring():
      mark_inv=Toplevel()
      mark_inv.geometry("700x480+240+150")
      mark_inv.title("Record Payement for Invoice")
      checkvar=IntVar()
      checkvar1=IntVar()
      checkvar2=IntVar()

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      mark_Notebook = ttk.Notebook(mark_inv)
      Mark_Invoice = Frame(mark_Notebook, height=470, width=750)
      mark_Notebook.add(Mark_Invoice, text="Mark Invoice")
      mark_Notebook.place(x=0, y=0)

      involbel=Label(Mark_Invoice, text="Invoice Balance")
      involbel.place(x=10, y=10)
      numentry=Entry(Mark_Invoice, width=45).place(x=130, y=10)

      labelframe5 = LabelFrame(Mark_Invoice,text="Payement Record Details",bg="#f5f3f2")
      labelframe5.place(x=10,y=60,width=670,height=250)
      e1 = Entry(labelframe5,width=28).place(x=30,y=45)
      pdate = Label(labelframe5, text="Payement Date:",bg="#f5f3f2").place(x=250,y=20)
      e2 = Entry(labelframe5,width=28).place(x=220,y=45)
      payd = Label(labelframe5, text="Paid By:",bg="#f5f3f2").place(x=450,y=20)
      drop = ttk.Combobox(labelframe5, value="Hello")
      drop.place(x=450,y=45)
      involbel=Label(labelframe5, text="Description")
      involbel.place(x=30, y=80)
      numentry=Entry(labelframe5, width=100).place(x=30, y=120)
      Checkbutton(labelframe5,text="Paid in full and close invoice",variable=checkvar,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=30 ,y=150)
      pl = Label(labelframe5,text="Payement Reciepts",bg="#f5f3f2")
      pl.place(x=300,y=145)
      Checkbutton(labelframe5,text="Send Payement Reciept",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=170)
      Checkbutton(labelframe5,text="Attach updated invoice",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=200)

      okbtn=Button(Mark_Invoice,compound = LEFT,image=tick , text="Save payement", width=100).place(x=10, y=350)
      canbtn=Button(Mark_Invoice,compound = LEFT,image=cancel, text="Cancel", width=100).place(x=500, y=350)

      
    #voidinvoice
    def voidinvoice_recurring():
      messagebox.askyesno("F-Billing Revolution","Are you sure to avoid this invoice?\nAll products will be placed back into stock and all payemnts will be voided.")
    
    #delete line item  
    # def delete_recurring():
    #   messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")
      
    def delete_recur_item():
      #  messagebox.askyesno("Delete invoice", "Are you sure to delete this invoice?")
      #  selected_item = tree.selection()[0]
      #  tree.delete(selected_item)  
      selected_item = tree.selection()[0]
      tree.delete(selected_item)

  # def updateorder():
  #   cmbodto4=ordercombo.get()
  #   addrsfrm4=sctxt.get('1.0', 'end-1c')
  #   sptto4=ship.get()
  #   adrsto4=addi.get('1.0', 'end-1c')
  #   emlfrm4=emi.get()
  #   smsfrm4=smsr.get()
  #   invid4=invo.get()
  #   orddatein4=invdate.get_date()
  #   ordduein4=invduedate.get_date()
  #   trmsin4=termsco.get()
  #   refin4=refco.get()
  #   extracstnme4=extra4.get()
  #   discountrte4=disr.get()
  #   extracst4=extrac.get()
  #   taax4=tax4.get()
  #   tplts4=tem4.get()
  #   slzprzn4=sa4.get()
  #   ctgryy4=cat4.get()
  #   bc4="Draft"
  #   idorder4= osdata[0]


  #   for line in vwedttree1.get_children():
  #     idsave=vwedttree1.item(line)['values'][0]

  #     sql1= 'SELECT * FROM  Productservice WHERE Productserviceid = %s'
  #     val=(idsave,)
  #     # print(val)
  #     fbcursor.execute(sql1,val,)
  #     child=fbcursor.fetchone()
  #     # print(child)
  #     # sql2= 'UPDATE storingproduct SET Productserviceid=%s,orderid=%s,sku=%s,category=%s,name=%s,description=%s,status=%s,unitprice=%s,peices=%s,cost=%s,taxable=%s,priceminuscost=%s,serviceornot=%s,stock=%s,stocklimit=%s,warehouse=%s,privatenote=%s'
  #     # val1=(child[0],sctxt,child[2],child[3],child[4],child[5],child[6],child[7],child[8],child[9],child[10],child[11],child[12],child[13],child[14],child[15],child[16])
  #     # fbcursor.execute(sql2,val1,)
  #     # fbilldb.commit()

  #   sql3='UPDATE Invoice SET invoiceid=%s,order_date=%s,due_date=%s,businessname=%s,status=%s,extra_cost_name=%s,extra_cost=%s,template=%s,sales_person=%s,discount_rate=%s,tax1=%s,category=%s,businessaddress=%s,shipname=%s,shipaddress=%s,cpemail=%s,cpmobileforsms=%s WHERE orderid=%s'
  #   val2=(ordrid,orddatein,ordduein,cmbodto,bc,extracstnme,extracst,tplts,slzprzn,discountrte,taax,ctgryy,addrsfrm,sptto,adrsto,emlfrm,smsfrm,idorder)
  #   fbcursor.execute(sql3,val2,)
  #   fbilldb.commit()

  #   for k in vwedttree1.get_children():
  #     pricetotl=vwedttree1.item(k)['values'][7]
  #     print(pricetotl)   

    firFrame=Frame(pop, bg="#f5f3f2", height=60)
    firFrame.pack(side="top", fill=X)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=customer_invoice_recurring)
    create.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=addnew,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=newline_recurring)
    add.pack(side="left", pady=3, ipadx=4)

    dele= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=delete,bg="#f5f3f2", fg="black", height=55, bd=1, width=55, command=delete_recur_item)
    dele.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    prev= Button(firFrame,compound="top", text="Preview\nInvoice",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printpreviewinvoice_recurring)
    prev.pack(side="left", pady=3, ipadx=4)

    prin= Button(firFrame,compound="top", text="Print \nInvoice",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=print_invoice_recurring)
    prin.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    mail= Button(firFrame,compound="top", text="Email\nInvoice",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
    mail.pack(side="left", pady=3, ipadx=4)

    sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms_recurring)
    sms1.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    mark= Button(firFrame,compound="top", text="Mark invoice\nas 'Paid'",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=57,command=markinvoice_recurring)
    mark.pack(side="left", pady=3, ipadx=4)

    void= Button(firFrame,compound="top", text="Void\ninvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=56,command=voidinvoice_recurring)
    void.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=calculator_recurring)
    calc.pack(side="left", pady=3, ipadx=4)

    fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
    fir1Frame.pack(side="top", fill=X)
  

    # opts = StringVar()
    global cus_var
    labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
    labelframe1.place(x=10,y=5,width=640,height=160)
    # options =[]
    # sql = "select businessname from Customer"
    # fbcursor.execute(sql,)
    # ids = fbcursor.fetchall()
    # print(ids)
    # cus_var = StringVar()
    # for i in ids:
    #   options.append(str(i[0])+"-"+i[1])
    # print(ids)

    # def look(event):
    #    print(ordercombo.get())

    # opts = StringVar()

  # #----------------------Recurring Finctions-----------------------------------------------  

    global recurentry1, recurentry2,checkvarStatus6,period2, current_var, month_var,stopcheck,btn
    def isChecked():
        if checkvarStatus6.get()==0:
          recurentry1['state'] = DISABLED 
          # recurentry2['state'] = DISABLED  
          period2['state'] = DISABLED
          #  month_var['state'] = DISABLED
        else:
            recurentry1['state'] = NORMAL
            # recurentry2['state'] = NORMAL
            period2['state'] = NORMAL
    

    def stopcheck():
        if checkvarStatus7.get()==0:
          recurentry2['state'] = DISABLED  
        else:
            recurentry2['state'] = NORMAL

    def duecheck():
        if checkvarStatus5.get()==0:
          invduedate['state'] = DISABLED  
        else:
          invduedate['state'] = NORMAL

    # def dueChecked():
    #     if checkvarStatus5.get()==0:
    #       e3['state'] = DISABLED 

    #     else:
    #       e3['state'] = NORMAL
    
                
    

    def recalculator():  
      date_1 = invdate.get_date()
      print(date_1)
      
      if period2.get() == "Month(s)":
        end_date = date_1 + datetime.timedelta(3*365/12)

      elif period2.get() == "Day(s)":
        end_date = date_1 + datetime.timedelta(days=int(period1.get()))
      
      
      print(end_date)
      recurentry1.delete(0,'end')
      recurentry1.insert(0, end_date.strftime('%m/%d/%y'))
      # recurentry2.config(f"ndate: {end_date.strftime('%m/%d/%Y')}")

    
    def updaterecur():# Edit recurring values into db (user)
      itemid = rtree.item(rtree.focus())["values"][1]
      recurring_period = month_var.get()
      recurring_period_month = current_var.get()
      next_invoice = recurentry1.get_date() 
      stop_invoice = recurentry2.get_date()
      sql='UPDATE invoice set recurring_period=%s,recurring_period_month=%s,next_invoice=%s,stop_recurring=%s where invoiceid=%s'
      val=(recurring_period,  recurring_period_month, next_invoice, stop_invoice, itemid)
      fbcursor.execute(sql,val)
      fbilldb.commit()
    
    global treefthcng

    def treefthcng():
      itemid = custree.item(custree.focus())["values"][0]
      sql = "select * from Customer where customerid = %s"
      val = (itemid, )
      fbcursor.execute(sql, val)
      cusvent = fbcursor.fetchone()
      ordercombo.delete(0,'end')
      ordercombo.insert(0, cusvent[3])
      sctxt.delete('1.0','end')
      sctxt.insert('1.0', cusvent[4])
      ship.delete(0,'end')
      ship.insert(0, cusvent[5])
      addi.delete('1.0','end')
      addi.insert('1.0', cusvent[6])
      emi.delete(0,'end')
      emi.insert(0, cusvent[8])
      smsr.delete(0,'end')
      smsr.insert(0,cusvent[11])
  # #----------------------End Recurring Finctions-----------------------------------------------  

   

    # def customerlist():
    #   cus["values"] = ids

    sql = "select businessname from Customer"
    fbcursor.execute(sql,)
    ids = fbcursor.fetchall()
    print(ids)
    cus_var = StringVar()

    
    itemid = rtree.item(rtree.focus())["values"][1]
    sql = "select * from invoice where invoiceid = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    recurdata = fbcursor.fetchone()
    print(recurdata[17])
     
  
    
    order = Label(labelframe1, text="Invoice to").place(x=10,y=5)
    ordercombo = ttk.Combobox(labelframe1, value=ids,width=28)
    ordercombo.place(x=80,y=5)
    ordercombo.delete(0,'end')
    ordercombo.insert(0, recurdata[18])
    # ordercombo = ttk.Combobox(labelframe1, textvariable=opts,width=28).place(x=80,y=5)
    # cus=ttk.Combobox(labelframe1,width=20, values=ids,textvariable=cus_var)
    # cus.place(x=80,y=5)
    # ordercombo = ttk.Combobox(labelframe1, value=ids,width=28).place(x=80,y=5)
    # ordercombo['values'] = options
    # ordercombo.current(0)
    # ordercombo.bind("<<ComboboxSelected>>", look)

    address=Label(labelframe1,text="Address").place(x=10,y=30)
    sctxt = scrolledtext.ScrolledText(labelframe1,width=23)
    sctxt.place(x=80,y=30,height=70)
    sctxt.delete('1.0','end')
    sctxt.insert('1.0', recurdata[19])
    ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
    ship=Entry(labelframe1,width=30)
    ship.place(x=402,y=3)
    ship.delete(0,'end')
    ship.insert(0, recurdata[20])
    address1=Label(labelframe1,text="Address").place(x=340,y=30)
    addi=scrolledtext.ScrolledText(labelframe1,width=23)
    addi.place(x=402,y=30,height=70)
    
    # e4= scrolledtext.ScrolledText(labelframe1, undo=True,width=23)
    addi.delete('1.0','end')
    addi.insert('1.0', recurdata[21])
    btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
    
    labelframe2 = LabelFrame(fir1Frame,text="")
    labelframe2.place(x=10,y=130,width=640,height=42)
    email=Label(labelframe2,text="Email").place(x=10,y=5)
    emi=Entry(labelframe2,width=30)
    emi.place(x=80,y=5)
    emi.delete(0,'end')
    emi.insert(0, recurdata[5])
    sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
    smsr=Entry(labelframe2,width=30)
    smsr.place(x=402,y=5)
    smsr.delete(0,'end')
    smsr.insert(0, recurdata[7])  
    labelframe = LabelFrame(fir1Frame,text="Invoice",font=("arial",15))
    labelframe.place(x=652,y=5,width=290,height=170)
    order=Label(labelframe,text="Invoice#").place(x=5,y=5)
    invo=Entry(labelframe,width=25)
    invo.place(x=100,y=5,)
    invo.delete(0,'end')
    invo.insert(0, recurdata[0])
    orderdate=Label(labelframe,text="Invoice date").place(x=5,y=33)
    invdate=DateEntry(labelframe,width=20)
    invdate.place(x=150,y=33,)
    invdate.delete(0,'end')
    invdate.insert(0, recurdata[2].strftime('%m/%d/%y'))
    checkvarStatus5=IntVar()
    checkvarStatus5.set(0)
    duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =1 ,offvalue = 0, command=duecheck).place(x=5,y=62)
    invduedate=DateEntry(labelframe,width=20)
    invduedate.place(x=150,y=62,)
    invduedate['state'] = DISABLED 
    invduedate.delete(0,'end')
    invduedate.insert(0, recurdata[3].strftime('%m/%d/%y'))
    terms=Label(labelframe,text="Terms").place(x=5,y=92)
    termsco=ttk.Combobox(labelframe, value="",width=25)
    termsco.place(x=100,y=92)
    ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
    refco=Entry(labelframe,width=27)
    refco.place(x=100,y=118)

    fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
    fir2Frame.pack(side="top", fill=X)
    listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
    
    tree=ttk.Treeview(listFrame)
    tree["columns"]=["1","2","3","4","5","6","7","8"]

    tree.column("#0", width=40)
    tree.column("1", width=80)
    tree.column("2", width=190)
    tree.column("3", width=190)
    tree.column("4", width=80)
    tree.column("5", width=60)
    tree.column("6", width=60)
    tree.column("7", width=60)
    tree.column("8", width=80)
    
    tree.heading("#0")
    tree.heading("1",text="ID/SKU")
    tree.heading("2",text="Product/Service")
    tree.heading("3",text="Description")
    tree.heading("4",text="Unit Price")
    tree.heading("5",text="Quality")
    tree.heading("6",text="Pcs/Weight")
    tree.heading("7",text="Tax1")
    tree.heading("8",text="Price")
    
    tree.pack(fill="both", expand=1)
    listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    new_value = tk.StringVar()
      
    def edit_window_box(val):
      
        edit_window = Toplevel(root)
        edit_window.title("Edit the value or cancel")
        edit_window.geometry("400x200")
        label_edit = tk.Label(edit_window , text='Enter value to edit', 
        font = ("Times New Roman", 12)).place(x=68,y=60)
        #create edit box
        edit_box = tk.Entry(edit_window)
        edit_box.insert(0,val)
        edit_box.place(x=200,y=63)
        #auto select edit window 
        edit_window.focus()


        def value_assignment(event):
          printing = edit_box.get()
          new_value.set(printing)
          #only destroy will not update the value (perhaps event keeps running in background)
          #quit allows event to stop n update value in tree but does not close the window in single click 
          #rather on dbl click shuts down entire app 
          edit_window.quit()
          edit_window.destroy()
      
        edit_window.bind('<Return>', value_assignment )

        B1 = tk.Button(edit_window, text=" Okay ")
        B1.bind('<Button-1>',value_assignment)
        B1.place(x=70,y=130)
        
        B2 = tk.Button(edit_window, text="Cancel", command = edit_window.destroy).place(x=276,y=130)
        edit_window.mainloop()
        
    #will explain
    #variable to hold col value (col clicked)
    shape1 = tk.IntVar()
    #tracks both col , row on mouse click
    def tree_click_handler(event):
        cur_item = tree.item(tree.focus())
        col = tree.identify_column(event.x)[1:]
        rowid = tree.identify_row(event.y)[1:]
        #updates list
        shape1.set(col)
        try:
            x,y,w,h = tree.bbox('I'+rowid,'#'+col)
        except:pass
        #tree.tag_configure("highlight", background="yellow")
        return(col)

    #code linked to event    
    tree.bind('<ButtonRelease-1>', tree_click_handler)

    #edit a value in a clicked cell
    def edit(event):
        try:
            selected_item = tree.selection()[0]
            temp = list(tree.item(selected_item , 'values'))
            tree_click_handler
            col_selected = int(shape1.get())-1
            edit_window_box(temp[col_selected])
            #do not run if edit window is open
            #use edit_window.mainloop() so value assign after window closes
            temp[col_selected] = new_value.get()
            tree.item(selected_item, values= temp)
            # prstree.insert(prstree.selection()[0])
        except: pass
    #binding allows to edit on screen double click
    tree.bind('<Double-Button-1>' , edit)

    fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
    fir3Frame.place(x=0,y=490)
  #----------------------------------------------

  


  #----------------------------------------------------------------------------------------
    # fbcursor.execute('SELECT * FROM invoice')
    # j = 0
    # for i in fbcursor:
    #   tree.insert(parent='', index='end', iid=i, text='', values=(
        
    #     i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    #   j += 1
  #-------------------------------------------------------------------------------------------
  

    tabStyle = ttk.Style()
    tabStyle.theme_use('default')
    tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
    myNotebook=ttk.Notebook(fir3Frame)
    invoiceFrame = Frame(myNotebook, height=200, width=800)
    recurFrame = Frame(myNotebook, height=200, width=800)
    payementFrame = Frame(myNotebook, height=200, width=800)
    headerFrame = Frame(myNotebook, height=200, width=1500)
    commentFrame = Frame(myNotebook, height=200, width=800)
    termsFrame = Frame(myNotebook, height=200, width=800)
    noteFrame = Frame(myNotebook, height=200, width=800)
    documentFrame = Frame(myNotebook, height=200, width=800)
    
    myNotebook.add(invoiceFrame,compound="left", text="Invoice")
    myNotebook.add(recurFrame,compound="left", text="Recurring")
    myNotebook.add(payementFrame,compound="left", text="Payments")
    myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
    myNotebook.add(commentFrame,compound="left",  text="Comments")
    myNotebook.add(termsFrame,compound="left", text="Terms")
    myNotebook.add(noteFrame,compound="left",  text="Private notes")
    myNotebook.add(documentFrame,compound="left",  text="Documents")
    myNotebook.pack(expand = 1, fill ="both")  

    itemid = rtree.item(rtree.focus())["values"][1]
    sql = "select * from invoice where invoiceid = %s "
    val = (itemid, )
    fbcursor.execute(sql, val)
    orbtdata = fbcursor.fetchone()
    print(orbtdata[4])

    labelframe1 = LabelFrame(invoiceFrame,text="",font=("arial",15))
    labelframe1.place(x=1,y=1,width=800,height=170)
    cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
    extra4=ttk.Combobox(labelframe1, value="",width=20)
    extra4.place(x=115,y=5)
    extra4['values']= ["Shipping and handling", "Postage and handling", "Delivery cost"] 
    extra4.delete(0,'end')
    extra4.insert(0, orbtdata[11])

    rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
    disr=Spinbox(labelframe1,width=6,  from_=0, to=100, font="italic 10")
    disr.place(x=460,y=5)
    disr.delete(0,'end')
    disr.insert(0, orbtdata[31]) 

    cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
    extrac=Entry(labelframe1,width=10)
    extrac.place(x=115,y=35)
    extrac.delete(0,'end')
    extrac.insert(0, orbtdata[12])
    tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
    tax4=Entry(labelframe1,width=7)
    tax4.place(x=460,y=35)
    tax4.delete(0,'end')
    tax4.insert(0, orbtdata[16]) 
    template=Label(labelframe1,text="Template").place(x=37,y=70)
    tem4=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
    sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
    sa4=Entry(labelframe1,width=18)
    sa4.place(x=115,y=100)
    sa4.delete(0,'end')
    sa4.insert(0, orbtdata[14])
    category=Label(labelframe1,text="Category").place(x=300,y=100)
    cat4=Entry(labelframe1,width=22)
    cat4.place(x=370,y=100)
    cat4.delete(0,'end')
    cat4.insert(0, orbtdata[17])
   
    
    statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
    statusfrme.place(x=540,y=0,width=160,height=160)
    draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
    on1=Label(statusfrme, text="Emailed on:").place( y=50)
    nev1=Label(statusfrme, text="Never").place(x=100,y=50)
    on2=Label(statusfrme, text="Printed on:").place( y=90)
    nev2=Label(statusfrme, text="Never").place(x=100,y=90)

   
  #------------------------------recurring edit ---------------------------------------------
    # itemid = tree.item(tree.focus())["values"][]
    # sql = "select * from invoice where invoiceid = %s"
    # val = (itemid, )
    # fbcursor.execute(sql, val)
    # psdata = fbcursor.fetchone()

  #-----------------------------------------------------------------
    global recurentry1, recurentry2,checkvarStatus6,period2, current_var, month_var
    recureframe = LabelFrame(recurFrame,text="",font=("arial",15))
    recureframe.place(x=1,y=1,width=800,height=170)
    checkvarStatus6=IntVar()
    current_var = StringVar()
    month_var = StringVar()
    checkvarStatus6.set(0)
    
    Checkbutton(recureframe,variable = checkvarStatus6,text="Recurring", offvalue=0, onvalue=1, command=isChecked).place(x=5,y=5)
    # Checkbutton(ws, text="accept T&C", variable=cb, onvalue=1, offvalue=0, command=isChecked).pack()
    period=Label(recureframe,text="Recurring period(interval)").place(x=65,y=35)
    # period1=Entry(recureframe,width=13, textvariable=month_var)
    # period1.place(x=240,y=35)
    period1 = Spinbox(recureframe, from_=1, to=10000, font="italic 10", width=9, text="Months(s)" ,textvariable=month_var)
    period1.place(x=240,y=35)
    period1.delete(0,'end')
    period1.insert(0, recurdata[24]) 

    
    # period1.delete(0,'end')
    # period1.insert(0, psdata[20])
                                
    nextinvo=Label(recureframe,text="Next Invoice").place(x=240,y=65)
    recurentry1=DateEntry(recureframe,width=20, )
    recurentry1.place(x=325,y=65)
    recurentry1['state'] = DISABLED 
    recurentry1.delete(0,'end')
    recurentry1.insert(0, recurdata[26].strftime('%m/%d/%y'))
    

    recalc = Button(recureframe, text="Recalculate", command=recalculator)
    recalc.place(x=490,y=65)
  
    saverec= Button(recureframe, text="Save" , command=updaterecur).place(x=570,y=65)
    
    checkvarStatus7=IntVar()
    checkvarStatus7.set(0)
    stoprecur=Checkbutton(recureframe,variable = checkvarStatus7,text="Stop recurring after",onvalue =1 ,offvalue = 0, command=stopcheck).place(x=180,y=95)
    recurentry2=DateEntry(recureframe, value="",width=20)
    recurentry2.place(x=325,y=95)
    recurentry2['state'] = DISABLED 
    recurentry2.delete(0,'end')
    recurentry2.insert(0, recurdata[27].strftime('%m/%d/%y'))

    def month():
      period2["values"] = ["Month(s)", "Days(s)"] 
    period2=ttk.Combobox(recureframe,width=20, 
                              values=["Month(s)", "Day(s)"],textvariable=current_var)
    # period2=Entry(recureframe,width=13, textvariable=current_var)
 
    period2.place(x=325,y=35)
    period2.delete(0,'end')
    period2.insert(0, recurdata[25])
    period2['state'] = DISABLED 
    
    print(current_var)
    btn1=Button(payementFrame,height=2,width=3,text="+").place(x=5,y=10)
    btn2=Button(payementFrame,height=2,width=3,text="-").place(x=5,y=50)
    cusventtree=ttk.Treeview(payementFrame, height=5)
    cusventtree["columns"]=["1","2","3","4","5"]
    cusventtree.column("#0", width=20, anchor="center")
    cusventtree.column("1", width=140, anchor="center")
    cusventtree.column("2", width=140, anchor="center")
    cusventtree.column("3", width=110, anchor="center")
    cusventtree.column("4", width=140, anchor="center")
    cusventtree.column("5", width=110, anchor="center")
    cusventtree.heading("#0",text="", anchor=W)
    cusventtree.heading("1",text="Payement ID")
    cusventtree.heading("2",text="Payement date")
    cusventtree.heading("3",text="Paid by")
    cusventtree.heading("4",text="Description")
    cusventtree.heading("5",text="Amount")      
    cusventtree.place(x=50, y=45)

    text1=Label(headerFrame,text="Title text").place(x=50,y=5)
    e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
    text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
    e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
    text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
    e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

    text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

    e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

    e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

    btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
    btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
    text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    cusventtree=ttk.Treeview(documentFrame, height=5)
    cusventtree["columns"]=["1","2","3"]
    cusventtree.column("#0", width=20)
    cusventtree.column("1", width=250)
    cusventtree.column("2", width=250)
    cusventtree.column("2", width=200)
    cusventtree.heading("#0",text="", anchor=W)
    cusventtree.heading("1",text="Attach to Email")
    cusventtree.heading("2",text="Filename")
    cusventtree.heading("3",text="Filesize")  
    cusventtree.place(x=50, y=45)
    

    fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
    fir4Frame.place(x=740,y=520)
    summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
    summaryfrme.place(x=0,y=0,width=200,height=170)
    discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
    discount1=Label(summaryfrme, text="$0.00").place(x=130 ,y=0)
    sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
    sub1=Label(summaryfrme, text="$0.00").place(x=130 ,y=21)
    tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
    tax1=Label(summaryfrme, text="$0.00").place(x=130 ,y=42)
    cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
    cost=Label(summaryfrme, text="$0.00").place(x=130 ,y=63)
    order=Label(summaryfrme, text="Order total").place(x=0 ,y=84)
    order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)
    total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
    total1=Label(summaryfrme, text="$0.00").place(x=130 ,y=105)
    balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
    balance1=Label(summaryfrme, text="$0.00").place(x=130 ,y=126)

    fir5Frame=Frame(pop,height=38,width=210)
    fir5Frame.place(x=735,y=485)
    btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
    btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)

   
    



    # val = ttk.Combobox.get()

    # print(val)
    # customerid = cus_var.get()
    # print(customerid)
    # recurring_period = month_var.get()
    # recurring_period_month = current_var.get()
    # print(recurring_period)
    # next_invoice = recurentry1.get_date() 
    # stop_invoice = recurentry2.get_date() 
    # # inv = 'SELECT invoiceid FROM invoice'
    # # print(inv)
    # sql='INSERT INTO invoice (recurring_period, recurring_period_month, next_invoice, stop_recurring) VALUES (%s,%s,%s, %s)'  #adding values into db
    # val=(recurring_period,  recurring_period_month, next_invoice, stop_invoice)
    # fbcursor.execute(sql,val)
    # fbilldb.commit()

   


    
          
    
  # import datetime

  # some_date = datetime.date.today()
  # three_months = datetime.timedelta(3*365/12)
  # print (some_date + three_months).isoformat()

  # def isChecked():
  #     if checkvarStatus6.get() == 1:

  #         btn['state'] = NORMAL
  #         btn.configure(text='Awake!')
  #     elif checkvarStatus6.get() == 0:
  #         btn['state'] = DISABLED
  #         btn.configure(text='Sleeping!')
  #     else:
  #         messagebox.showerror('Something went wrong!')

  #------------------------------------------------------------------------------------------


  # def generate_recurring():  
  #   con = MySQLdb.connect(host="localhost", user="root", password="", database="fbilldb")
  #   cur = con.cursor()
  #   cur.execute('SELECT * FROM invoice;')
  #   i = 0
  #   for ro in cur:
  #     tree.insert(parent='', index='end', iid=i, text='hello', values=('', i[0], i[1], i[2], i[3], i[4], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]))
  #     i += 1
  # #     # messagebox.showinfo("F-Billing Revolution 2022", "1 new invoice successfully created.")
  #     con = MySQLdb.connect(host="localhost", user="root", password="", database="fbilldb")

  #     cur = con.cursor()

  #     cur.execute("SELECT Recurring.recurringid, invoice.invoive_number, Recurring.next_invoice, Recurring.recurring_period, Recurring.stop_recurring, Customer.businessname, invoice.invoicetot FROM Recurring  JOIN invoice ON Recurring.invoiceid = invoice.invoiceid JOIN Customer ON Recurring.customerid = Customer.customerid")
    
  #     rows = cur.fetchall()    

  #     for row in rows:

  #         print(row) 

  #         tree.insert("", tk.END, values=row)        

  #     con.close() 

  # tree = ttk.Treeview(columns = (1,2,3,4,5,6,7,8), height = 15, show = "headings")
  # tree.pack(side = 'top')
  # scrollbar = Scrollbar()
  # scrollbar.place(x=1004+300+25, y=360, height=195)
  # scrollbar.config( command=tree.yview )
  # tree.heading(1)
  # tree.heading(2, text="Product/Service ID",)
  # tree.heading(3, text="Name")
  # tree.heading(4, text="Description")
  # tree.heading(5, text="Price")
  # tree.heading(6, text="QTY")
  # tree.heading(7, text="Tax1")
  # tree.heading(8, text="Line Total")   
  # tree.column(1, width = 40)
  # tree.column(2, width = 250)
  # tree.column(3, width = 270)
  # tree.column(4, width = 300)
  # tree.column(5, width = 130)
  # tree.column(6, width = 100)
  # tree.column(7, width = 100)
  # tree.column(8, width = 190)

  except:
    try:
      pop.destroy()
    except:
      pass
      messagebox.showerror('F-Billing Revolution', 'Select a record to edit.')   

      

    #---------------------------- Buttons--------------------------------------

mainFrame=Frame(tab4, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

invoiceLabel = Button(midFrame,compound="top", text="Generate recurring\n invoices",relief=RAISED, image=video,bg="#f8f8f2", fg="black", height=55, bd=1, width=95, command=generate_recurring_noinvoice)
invoiceLabel.pack(side="left", pady=3, ipadx=4)


w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

orderLabel = Button(midFrame,compound="top", text="View/Edit\nInvoice",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=view_invoice_recurring) 
orderLabel.pack(side="left")


w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

previewLabel = Button(midFrame,compound="top", text="Print Preview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=printpreviewinvoice_recurring)
previewLabel.pack(side="left")

purchaseLabel = Button(midFrame,compound="top", text="Print Invoice",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=print_invoice_recurring)
purchaseLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

expenseLabel = Button(midFrame,compound="top", text=" E-mail \nInvoice",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=email_invoice_recurring)
expenseLabel.pack(side="left")


w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Search in\nInvoices",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=recur_cust_search)
productLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Refresh\nInvoices list",relief=RAISED, image=photo8,bg="#f8f8f2",fg="black", height=55, bd=1, width=75)#, command=recur_refresh
productLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Show totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=lambda: label.place())
productLabel.pack(side="left")

productLabel = Button(midFrame,compound="top", text="Hide totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=lambda: label.place_forget())
productLabel.pack(side="left")

label = Label(mainFrame, text = "$500")
label.place(x= 100 , y = 120)


invoilabel = Label(mainFrame, text="Recurring invoices", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))




    #------------------------------End Buttons-----------------------------------------------


# Recurring invoice table and scrollbars


# class MyApp1:
#   def __init__(self, parent):
    
#     self.myParent = parent 

#     self.myContainer1 = Frame(parent) 
#     self.myContainer1.pack()
    
#     self.top_frame = Frame(self.myContainer1) 
#     self.top_frame.pack(side=TOP,
#       fill=BOTH, 
#       expand=YES,
#       )  

#     self.left_frame = Frame(self.top_frame, background="white",
#       borderwidth=5,  relief=RIDGE,
#       height=250, 
#       width=2000, 
#       )
#     self.left_frame.pack(side=LEFT,
#       fill=BOTH, 
#       expand=YES,
#       )

    
rtree = ttk.Treeview(tab4, selectmode='browse')
rtree.pack(side = 'top')
rtree["columns"] = ("1","2","3","4","5","6","7")
rtree["show"]='headings'
rtree["height"]='15'
rtree.heading(1)
rtree.heading(2, text="Invoice#")
rtree.heading(3, text="Next Invoice")
rtree.heading(4, text="Recurring Period")
rtree.heading(5, text="Stop After")
rtree.heading(6, text="Customer Name")
rtree.heading(7, text="Invoice Total")  
rtree.column(1, width = 40, anchor="center")
rtree.column(2, width = 200, anchor="center")
rtree.column(3, width = 200, anchor="center")
rtree.column(4, width = 200, anchor="center")
rtree.column(5, width = 200, anchor="center")
rtree.column(6, width = 340, anchor="center")
rtree.column(7, width = 190, anchor="center")
  

   
  
# fbcursor.execute('SELECT  invoice.invoiceid, invoice.next_invoice, invoice.recurring_period, invoice.stop_recurring, Customer.businessname, invoice.invoicetot FROM invoice, customer WHERE invoice.customerid = customer.customerid')
# j = 0
# for i in fbcursor:
#     tree.insert(parent='', index='end', iid=i, text='hello', values=('',i[0], i[1], i[2], i[3], i[4], i[5]))
#     j += 1

sql = "select * from invoice  where recurring_period_month =%s OR recurring_period_month =%s"
val = ('month(s)', 'day(s)', )
fbcursor.execute(sql,val)
pdata = fbcursor.fetchall()

j = 0
for i in pdata:
  rtree.insert(parent='', index='end', iid=i, text='hello', values=('',i[0], i[26], i[24], i[27], i[18], i[8], i[7], i[13], i[14], i[11],i[16],i[3]))
  j += 1    


# scrollbar = Scrollbar(self.left_frame)

# scrollbar.place(x=1008+300+25, y=0, height=300+20)
# scrollbar.config( command=tree.yview )

inverticalbar=ttk.Scrollbar()
inverticalbar.place(x=1019+300+25, y=142, height=336+20)
    
    


tabControl = ttk.Notebook(tab4)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoice Items')
tabControl.add(tab2,image=photo11,compound = LEFT, text ='Invoice Private Notes')
tabControl.add(tab3,image=smslog,compound = LEFT, text ='SMS log')
tabControl.add(tab4,image=photo11,compound = LEFT, text ='Documents')
tabControl.pack(expand = 1, fill ="both")
    
  
tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
tree.pack(side = 'top')
tree.heading(1)
tree.heading(2, text="Product/Service ID",)
tree.heading(3, text="Name")
tree.heading(4, text="Description")
tree.heading(5, text="Price")
tree.heading(6, text="QTY")
tree.heading(7, text="Tax1")
tree.heading(8, text="Line Total")   
tree.column(1, width = 40, anchor="center")
tree.column(2, width = 250, anchor="center")
tree.column(3, width = 270, anchor="center")
tree.column(4, width = 300, anchor="center")
tree.column(5, width = 130, anchor="center")
tree.column(6, width = 100, anchor="center")
tree.column(7, width = 100, anchor="center")
tree.column(8, width = 190, anchor="center")

fbcursor.execute('SELECT Productservice.Productserviceid, Productservice.name, Productservice.description, Productservice.unitprice, Productservice.sku,invoice.tax1,invoice.invoicetot FROM Productservice, invoice WHERE Productservice.Productserviceid = invoice.Productserviceid')
j = 0
for i in fbcursor:
  tree.insert(parent='', index='end', iid=i, text='hello', values=('',i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
  j += 1

note1=Text(tab2, width=170,height=10).place(x=10, y=10)

note1=Text(tab3, width=170,height=10).place(x=10, y=10)

tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
tree.pack(side = 'top')
tree.heading(1)
tree.heading(2, text="Attach to Email",)
tree.heading(3, text="Filename")
tree.column(1, width = 30)
tree.column(2, width = 310)
tree.column(3, width = 1000)

# scrollbar = Scrollbar(self.left_frame)
# scrollbar.place(x=1004+300+25, y=360, height=195)
# scrollbar.config( command=tree.yview )

expverticalbar=ttk.Scrollbar()
expverticalbar.place(x=995+350,y=500,height=199)

       
# myapp = MyApp1(tab4)


def rec_cust_reg():# Storing values into db (user)contp,cemail,ctel,cfax,cmob,scontp,scemail,sctel,scfax,ccountry,ccity
  customerid = custid.get()
  businessname = bname.get()
  businessaddress = baddress.get()
  category= cat.get()
  shipname= sname.get()
  shipaddress = saddress.get()
  contactperson= contp.get()
  cpemail = cemail.get()
  cptelno = ctel.get()
  cpfax = cfax.get()
  cpmobileforsms = cmob.get()
  shipcontactperson= scontp.get()
  discount=discoutentry.get()
  specifictax1=taxentry.get()
  shipcpemail= scemail.get()
  shipcptelno= sctel.get()
  shipcpfax = scfax.get()
  country= ccountry.get()
  city = ccity.get()
  notes= cnotes.get()
  status= checkvar1.get()
  taxexempt= checkvar2.get()   
  sql='INSERT INTO customer (customerid,businessname,businessaddress,category,status,shipname,shipaddress,contactperson,cpemail,cptelno,cpfax,cpmobileforsms,shipcontactperson,shipcpemail,shipcptelno,shipcpfax,taxexempt,country,city,notes,discount,specifictax1) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
  val=(customerid,businessname,businessaddress,category,status,shipname,shipaddress,contactperson,cpemail,cptelno,cpfax,cpmobileforsms,shipcontactperson,shipcpemail,shipcptelno,shipcpfax,taxexempt,country,city,notes,discount,specifictax1)
  fbcursor.execute(sql,val)
  fbilldb.commit()
  messagebox.showinfo("F-Billing Revolution 2022",'Registration successfull')


  

def rec_pro_insert():# Storing values into db (user)
  sku = codeentry.get()
  category = country.get()
  name = nameentry.get()
  description = desentry.get()
  unitprice = unitentry.get()
  peices = pcsentry.get()
  cost = costentry.get()
  priceminuscost = priceentry.get()
  stock = stockentry.get()
  stocklimit = lowentry.get()
  warehouse = wareentry.get()
  privatenote = txt.get("1.0",'end-1c')
  status = checkvarStatus.get()
  taxable = checkvarStatus.get()
  serviceornot = checkvarStatus.get()
  sql='INSERT INTO Productservice (sku,category,name,description,unitprice,peices,cost,priceminuscost,stock,stocklimit,warehouse,privatenote,status,taxable,serviceornot) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
  val=(sku,category,name,description,unitprice,peices,cost,priceminuscost,stock,stocklimit,warehouse,privatenote,status,taxable,serviceornot)
  fbcursor.execute(sql,val)
  fbilldb.commit()
  messagebox.showinfo("F-Billing Revolution 2022","Successfully added product")
  


    

root.mainloop()
