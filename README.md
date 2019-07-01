## OCR for table structured text
This program helps in converting image to text using tesseract package. But the problem is tesseract is poor when it comes to pick from table formated data like in the image 41.jpg.

So what we need to do is break the boxes in to tiny pices and then make tesseract read them in this way you wont get junk chars. 

## How to break the box? 
1. Detect Verticle lines like in image verticle_lines.jpg
2. Detect Horiziontal lines like in image horizontal_lines.jpg
3. Merge These to images to get shape of table like in image img_final_bin.jpg
4. Detect boxes in img_final_bin.jpg
5. save these box images like in ```./Cropped/```
6. Run tesseract against these cropped images. Job Done.

## Result
When i did a quick test i got 13 character recognition mistakes including digits, special char, small & big alphabets out of 1000 characters. 98.7% accuracy in terms of character recognition.
Just to have a quick look i have added '*' after every mistake in results.txt file
I Feel it can be push to 99.9% by using tensorflow datasets. 
But you will find order of text is completly out of order. This can be handled using opencv shape detection algos. 

To get this right what we can do is, while tesract is detecting text from boxes, concat HTML ```<table><tr><td>``` code to the text so to match the image img_final_bin.jpg. Resultant when executed in the browser will match the pdf table.