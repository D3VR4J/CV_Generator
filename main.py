import os
from unicodedata import name
from fpdf import FPDF

run = True
while run:
    fname = input("Input Your Filename= ")
    fname = f"./output/{fname}.pdf"
    print("Your output location is:", fname)

    if os.path.isfile(fname) and os.stat(fname).st_size != 0:
        print ("Already Present in the directory")
        continue

    else:
        print ("This is PC Builder")
        name = input("Enter Your name: ")
        pno = '+91' + input("Enter Your Mobile no.: ")
        email = input("Enter your email: ")
        adres = input("Enter your addrress: ")
        dob = input("Enter your date of birth(dd/mm/yyyy): ")
        objective = """To Secure a challenging position in a reputable organization to expand my learnings, knowledge, and skills Seeking an entry-level position to begin my career in a high-level professional environment."""
        run = False

class PDF(FPDF):
    #for header this will incluse on every page
    '''def header(self):
        self.set_draw_color(0,0,0)
        self.image('pdflearning/image.jpg', 165, 15, 35, )
        self.ln(8)'''

    def footer(self):
        self.set_y(-15)
        self.set_x(100)
        self.set_font('helvetica', '', 10)
        self.set_text_color(100,50,100)
        self.cell(10, 5, f'Page {self.page_no()}', align='c')
        '''

    def objective(self, name):
        with open(name, 'rb') as fh:
            txtfile = fh.read().decode('latin-1')
            self.set_font('helvetica', '', 16)
            self.multi_cell(190, 8, f'{txtfile}')'''

pdf = PDF('P', 'mm', 'A4') #(Orientation= 'L=Landscape','P=Potrait')

#add a page
pdf.add_page()

#add a font
pdf.set_font('helvetica', 'b', 21) #(Font, style, size)

#add ac color
pdf.set_text_color(162,0,37)

#add a image
iname = input("Input Your Profile Image Name(eg- image.png)= ")
iname = f"./image/{iname}"
if os.path.isfile(iname):
    pdf.image(iname, 165, 15, 35, )
else:
    iname = 'yourimage.jpg'
    pdf.image(f'./image/{iname}', 165, 15, 35, )
pdf.ln(8)

#create a cell
pdf.cell(40, 10, f'Name: {name}', ln= True)
pdf.set_text_color(0,0,0)
pdf.set_font('helvetica', '', 16)
pdf.cell(100, 8, f'DOB: {dob}', ln=1)
pdf.cell(100, 8, f'Email: {email}', ln=1)
pdf.cell(100, 8, f'Mobile.No.: {pno}', ln=1)
pdf.cell(100, 8, f'Address: {adres}', ln=1)
pdf.ln(10)


#objective
pdf.set_font('helvetica', 'b', 21)
pdf.set_fill_color(134, 198, 244)
pdf.cell(40, 9,'Objective' , fill=1, border=0, ln= True)
pdf.set_font('helvetica', '', 16)
pdf.multi_cell(190, 8, f'{objective}', border=0)
pdf.ln()


#Qualification
pdf.ln()
pdf.set_font('helvetica', 'b', 21)
pdf.set_fill_color(134, 198, 244)
pdf.cell(55, 9, 'Qualifications' , fill=1, border=0, ln= True)

user = int(input("How many Qualifications do you have?= "))
dquali = {}
for i in range(1, user+1):
    instring = f"Qualification{i} = "
    quali = "quali%d" % i
    dquali[quali] = f'{i}. ' + input(instring)

for i in range(1, user+1):
    damn = "quali%d" %i
    quali = dquali[damn]
    print(quali)

    pdf.set_font('helvetica', '', 16)
    pdf.multi_cell(190, 8, f'{quali}', border=0)


#Skills
pdf.ln()
pdf.set_font('helvetica', 'b', 21)
pdf.set_fill_color(134, 198, 244)
pdf.cell(25, 9, 'Skills' , fill=1, border=0, ln= True)
user = int(input("how many skills do you have?= "))
dskill = {}
for i in range(1, user+1):
    instring = f"Skill{i} = "
    skill = "skill%d" % i
    dskill[skill] = f'{i}. ' + input(instring)

for i in range(1, user+1):
    damn = "skill%d" %i
    skill = dskill[damn]
    print(skill)

    #Skills
    pdf.set_font('helvetica', '', 16)
    pdf.multi_cell(190, 8, f'{skill}', border=0)


#Hobbies
pdf.ln()
pdf.set_font('helvetica', 'b', 21)
pdf.set_fill_color(134, 198, 244)
pdf.cell(35, 9, 'Hobbies' , fill=1, border=0, ln= True)

user = int(input("How many Hobbies do you have?= "))
dhobby = {}
for i in range(1, user+1):
    instring = f"Hobby{i} = "
    hobby = "hobby%d" % i
    dhobby[hobby] = f'{i}. ' + input(instring)

for i in range(1, user+1):
    damn = "hobby%d" %i
    hobby = dhobby[damn]
    print(hobby)

    pdf.set_font('helvetica', '', 16)
    pdf.multi_cell(180, 8, f'{hobby}', border=0)


#Strengh
pdf.ln()
pdf.set_font('helvetica', 'b', 21)
pdf.set_fill_color(134, 198, 244)
pdf.cell(35, 9, 'Strength' , fill=1, border=0, ln= True)

user = int(input("How many Strength do you have?= "))
dstrength = {}
for i in range(1, user+1):
    instring = f"Strength{i} = "
    strength = "strength%d" % i
    dstrength[strength] = f'{i}. ' + input(instring)

for i in range(1, user+1):
    damn = "strength%d" %i
    strength = dstrength[damn]
    print(strength)

    pdf.set_font('helvetica', '', 16)
    pdf.multi_cell(190, 8, strength, border=0)

#pdf.cell(40, 8, f'{txtfile}', ln= True)
print("File Created at location: ", fname)
pdf.output(fname)