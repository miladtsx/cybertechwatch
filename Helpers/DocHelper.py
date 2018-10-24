from docx import Document
from docx.shared import Pt
from Model import  localNewsRepository
from Helper import getFileName

def saveToFile():
    try:
        if (len(localNewsRepository) < 1):
            print "[Info] Abort Saving report; no News found!"
            return
        localNewsRepository.sort(key=lambda x: x.title)
        
        doc = Document()
        for item in localNewsRepository:
            
            doc.add_heading(item.title, level=2)
            p = doc.add_paragraph('')
            p.add_run(str(item.date) + '\n').font.size=Pt(9)
            p.add_run(str(item.url)).font.size=Pt(8)
                                
        doc.save(getFileName())
        
        print "News File Generated (" + str(len(localNewsRepository)) + ")."
    except Exception,e:
        print '[Err] File operation failed!' + str(e)
