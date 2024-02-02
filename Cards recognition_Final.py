# First you have to install the Following libraries in your cmd or terminal 
## pip install easyocr 
## pip install Pillow 
## pip install json 



# Importing the necessarie libraries
import json
import numpy as np
from PIL import Image 
from typing import List
import easyocr
import io 
import requests 
from tkinter import filedialog





# Convert the JSON data to a NumPy array
with open('your json file' , encoding="utf8" ) as f:
    data = json.load(f)
data = np.array(data)
def extract_text_with_easyocr(image_path , language ='en'):
    reader = easyocr.Reader([language])
    result = reader.readtext(image_path)
    extracted_text =""
    for detection in result :
        text = detection[1]
        extracted_text += text + ' '
    return extracted_text.strip()


        

imag = Image.open(filedialog.askopenfilename(title="Select a file"))
 # Add The Path oof the Image that you wanna recognize 
imag_croped = imag.crop(box=(160,10 , 600 , 200))
image_path = np.array(imag_croped)
# Specify the language (e.g., 'en' for English)
language = 'en'
extracted_text = extract_text_with_easyocr(image_path, language)  
if len(extracted_text) == 0 :     
    flipped_image = imag.transpose(Image.ROTATE_90)
    croped = flipped_image.crop(box=(150, 600 , 400 , 680))
    croped_arr = np.array(croped)
    extracted_text= extract_text_with_easyocr(croped_arr , language)
    print(extracted_text)
else :
    
    print(extracted_text)

def info_print():

    
    print("id : {}".format(data[i]["productId"])) # Display the Proudct id 
    print(data[i]['name']) # Display the Name 
    print(data[i]['skus'][0]['abbr']) # Display the Language 
    response = requests.get(data[i]['image']) # Display The Image 
    image = Image.open(io.BytesIO(response.content))
    image.show()


#Display the the Other information of the Image 
for i in range(1774) : 
    if extracted_text in data[i]['name'] : # The First search 
        info_print() 
        
        
              
        break    
        
if extracted_text not in data[i]['name'] : 
    for i in range(1774):
        if extracted_text.split()[0] in data[i]['name'] : # The second search
                info_print()  
        
         
                break
if extracted_text.split()[0] not in data[i]['name'] :
    for i in range(1774):
        if extracted_text.split()[0:3] in data[i]['name'] : # The second search
             info_print()
             break


        

