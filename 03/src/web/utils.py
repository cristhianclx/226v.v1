import docx
from pypdf import PdfReader
import re


def getText(filename):
    if filename.name.endswith(".docx"):
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)
    if filename.name.endswith(".pdf"):
        reader = PdfReader(filename)
        number_of_pages = len(reader.pages)
        fullText = []
        for number_page in range(0, number_of_pages):
            page = reader.pages[number_page]
            fullText.append(page.extract_text())
        return '\n'.join(fullText)
    

def wrangler(raw):
    # 1. Solo letras
    letras = re.sub("[^a-zA-ZáóéíúñÑ]", " ", raw)
    # 2. convertir a minusculas
    letras = letras.lower()
    letras = letras.replace("á", "a")
    letras = letras.replace("é", "e")
    letras = letras.replace("í", "i")
    letras = letras.replace("ó", "o")
    letras = letras.replace("ú", "u")
    words = letras.split()
    # 2.1. reemplazar tildes
    # 3. convertir a set ya que es más rapido
    # stops = set(stopwords.words("spanish"))
    # 4. Quitar stop words
    # meaningful_words = [w for w in words if not w in stops]
    # 5. Unir las palabras,
    return( " ".join( words ))