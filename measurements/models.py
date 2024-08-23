import ast
import os
import re
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import pandas as pd
from cars.models import Car
from ckeditor.fields import RichTextField
    
class Measurement(models.Model):
    date = models.DateTimeField(default=timezone.now)
    csv_file = models.FileField(upload_to="files")
    slug = models.SlugField(default="", blank=True, null=True, unique=True, db_index=True, editable=False)
    txt_file = models.FileField(upload_to="files",null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="measurements")
    
    #The new name of the file is generated based on the date and time information in the 'date' field.
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.date.strftime('%Y-%m-%d-%H-%M-%S'))
            slug = base_slug
            num = 1
            while Measurement.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug

        if self.csv_file:
            filename, file_extension = os.path.splitext(self.csv_file.name)
            new_filename = self.date.strftime('%Y-%m-%d-%H-%M-%S') + file_extension
            self.csv_file.name = os.path.join('files/csv', new_filename)

        super().save(*args, **kwargs)

    #If there is a file in the 'csv_file' field, the path to the file is taken and the CSV file is read using the pandas library.
    def read_csv(self):
        if self.csv_file:
            file_path = self.csv_file.path  
            df = pd.read_csv(file_path)
            return df
        return None
    
    def read_txt(self):
        if self.txt_file:
            file_path = self.txt_file.path
            with open(file_path, 'r') as file:
                content = file.read()
                
                # Extract DTC (Diagnostic Trouble Codes) using regex
                dtc_pattern = r"DTC:\s*(\[\(.*?\)\])"
                dtc_match = re.search(dtc_pattern, content, re.DOTALL)
                
                if dtc_match:
                    dtc_str = dtc_match.group(1)
                    try:
                        # Convert the string to a Python list
                        dtc_list = ast.literal_eval(dtc_str)
                        return dtc_list
                    except Exception as e:
                        print(f"Error converting DTC to list: {e}")
                        return None
                else:
                    print("No DTC found in the txt file.")
                    return None
        return None


class FileUploadModel(models.Model):
    file = models.FileField(upload_to="uploads")