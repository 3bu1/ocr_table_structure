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
When i did a quick test i got 95% accuracy in terms of character recognition. I Feel we can push it to 98% by fine tuning other parameters. 