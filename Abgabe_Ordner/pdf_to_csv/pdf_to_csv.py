
""" PdfToCsv
    In this file the slides from the lecture PR1 by Jörn Fischer are read. 
    Then written to the text file pdfToText.txt.
    After that the Text File will be converted into the CSV file TextToCSV.CSV 
"""
import slate3k
import re
import csv

class PdfToCsv:

    def read_pdf_file(self):
        with open('PR1.pdf','rb') as f:
            #return all pages from pdf in Byte array
            extracted_text = slate3k.PDF(f)

        return extracted_text        

    def clean_extracted_text(self, extracted_text):
        temp = ""
        clean_extracted_text = {}
        #Iterate over extracted_text Array
        for i in extracted_text:
            # Split into key and content for the csv file==> 2 columns
            split_after_new_Line = i.split('\n\n')
            key_value = split_after_new_Line[0]+ ' ' + split_after_new_Line[1]
            content = repr(i)

            # Replace invalid characters and pages
            content = content.replace("\\x0c'", "").replace("\\uf06c", "").replace("\\x0c\"", "").replace("●","")
            m = re.search("((?<=')|(?<=\")|(?<=\n\n))(.*)", content)
            compare_with_footer = split_after_new_Line[0] + split_after_new_Line[1] + split_after_new_Line[2]

            if re.search("Jörn Fischer  -  j.fischer@hs-mannheim.de - Raum A112", compare_with_footer):
                continue


            #save key and values in a dictionary (assoziative array with key and value) 
            if m:
                if temp != key_value:
                    clean_extracted_text.update({key_value: m.group()})
                else:
                    clean_extracted_text.update({key_value: clean_extracted_text[key_value] + " " + m.group()})
            temp = key_value

        return clean_extracted_text

    def dict_to_csv(self, clean_extracted_text):
        with open('q&aLecturePr1.csv', 'w',  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('key', 'content'))
            for key, value in clean_extracted_text.items():
                writer.writerow([key, value])


obj = PdfToCsv()
extracted_text = obj.read_pdf_file()
clean_extracted_text = obj.clean_extracted_text(extracted_text)
obj.dict_to_csv(clean_extracted_text)