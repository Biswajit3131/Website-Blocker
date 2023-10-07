#import module
from tkinter import*

host_path='C:\Windows\System32\drivers\etc\hosts'
ip_address='127.0.0.1'


def block():
    website_lists = enter_Website.get(1.0,END)
    Website=list(website_lists.split(","))
    with open(host_path,'r+')as host_file:
    	file_content = host_file.read()
    	for web in Website:
    		if web in file_content:
    			display=Label(window,text='Already Blocked',font='arial')
    			display.place(x=200,y=200)
    	else:
    			host_file.write(ip_address+" "+web+'\n')
    			Label(window,text="Blocked",font='arial').place(x=230,y=200)	
def unblock():
    website_lists = enter_Website.get(1.0,END)
    Website=list(website_lists.split(","))
    with open(host_path,'r+')as host_file:
    	file_content = host_file.readlines()
    	for web in Website:
    		if web in website_lists:
    			with open(host_path,'r+') as f:
    				for line in file_content:
    					if line.strip(',')!= website_lists:
    						f.write(line)
    						Label(window,text="UnBlocked",font='arial').place(x=350,y=200)
    					else:
    						display=Label(window,text='Already UnBlocked',font='arial')
    						display.place(x=350,y=200)	
    		
    	else:
    			host_file.write(ip_address+""+web+'\n')
    			Label(window,text="Blocked",font='arial').place(x=230,y=200)	
def close():
    window.destroy()

#to make a window
window=Tk()

#set size of window
window.geometry('650x400')
window.maxsize(750,600)
window.minsize(550,300)

#set title of window
window.title('WEBSITE BLOCKER')

#set Header
l1=Label(window,text='WEBSITE BLOCKER',font=('bold',15),fg='purple')
l1.pack()
l2=Label(window,text='Developed By @BISWAJIT',font=('bold',12),fg='purple')
l2.pack(side=BOTTOM)

l3=Label(window,text='Enter website :')
l3.place(x=100,y=50)
enter_Website=Text(window,font=(10),width=30,height=1)
enter_Website.place(x=200,y=48)

b1=Button(window,text='Block',font=('bold',10),bg='blue',fg='red',command=block)
b1.place(x=150,y=100)
b2=Button(window,text='Un Block',font=('bold',10),bg='green',fg='orange',command=unblock)
b2.place(x=270,y=100)
b3=Button(window,text='Exit',font=('bold',10),bg='yellow',fg='black',command=close)
b3.place(x=400,y=100)
window.mainloop()