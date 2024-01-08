from fastapi import  File, UploadFile, APIRouter, Query, Response, Request
from fastapi.responses import FileResponse
from PIL import Image
import pytesseract
import io
from typing import Optional

router = APIRouter(prefix='/convert', tags=['OCR'])

@router.post('/Img2Text', summary='Read text from an image')
async def ocr(image: UploadFile = File(...)):
   file_content = await image.read()
   read_file_bytes = Image.open(io.BytesIO(file_content))
   img_to_text = pytesseract.image_to_string(read_file_bytes, lang='eng')
   formated_text = ' '.join(img_to_text.split())
   return formated_text
   
   
@router.post('/Img2pdf', summary='Read text from an image')
async def ocr(req : Request, 
              rename: Optional[str] = Query(None, description="Want to rename your file?"), 
              image: UploadFile = File(...)):
   file_content = await image.read()
   read_file = Image.open(io.BytesIO(file_content))
   img_to_text = pytesseract.image_to_pdf_or_hocr(read_file, lang='eng')
   if req.query_params:
      file_name = f'{rename}.pdf'
   else:
      file_name= "img.pdf"
   file_path = f'files/{file_name}'
   with open(file_path, "wb") as pdf_file:
            pdf_file.write(img_to_text)

   return FileResponse(file_path, media_type='application/pdf', filename=file_name)
   
      