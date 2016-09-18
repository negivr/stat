from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,KeepTogether,tables
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.units import inch,cm,mm
from reportlab.pdfgen import canvas

PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]
styles = getSampleStyleSheet()
style = styles["Normal"]

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',15)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-38, 'Title 1')
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-58, 'Title 2')

    NormalStyle = tables.TableStyle([
        ('BOX',(0,0),(-1,-1),0.45,colors.blue),
        ('ALIGN',(0,0),(-1,-1),'LEFT'),
        ('BACKGROUND',(0,0),(-1,-1),colors.lightblue)
        ])

    mytable = tables.Table([('test','test'),('test2','test2'),('test3','test3')],
    colWidths = 1* inch,rowHeights= 0.25 * inch,style = NormalStyle)

    mytable.wrapOn(canvas,PAGE_WIDTH ,PAGE_HEIGHT)
    mytable.drawOn(canvas,(doc.width/2)-20,700)

    doc.afterPage()
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.restoreState()

doc = SimpleDocTemplate("myreport.pdf",
                        leftMargin = 0.75*inch,
                        rightMargin = 0.75*inch,
                        topMargin = 1*inch,
                        bottomMargin = 1*inch)

data = "".join(['this is a test' for i in range(200)])
mydata = Paragraph(data,style)
Story = [Spacer(2.5,0.75*inch)]
Story.append(mydata)

doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)