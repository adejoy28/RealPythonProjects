# install and import Python Modules
# PyPDF2
# pyttsx3
import PyPDF2
import pyttsx3


Engine = pyttsx3.init()
PDF_Reader = PyPDF2.PdfFileReader(open("../What is python.pdf", "rb"))

for Page_num in range(PDF_Reader.numPages):
    Text = PDF_Reader.getPage(Page_num).extractText()
    # Engine.getProperty("voices")
    Engine.say(Text)
    Engine.runAndWait()

