import requests
import os
from bs4 import BeautifulSoup

GS_TRI_THUC_URL = "https://docs.google.com/document/d/e/2PACX-1vT1YqDoJ6oQo5fuZs-maN6MJ2i82zk_DeX6dW1_S7d5DLgVNHt66Y6QRr3o4qRQK-RsgbdcDqsASJAi/pub"

def get_init_txt():
  # Get the directory where the script is located
  script_dir = os.path.dirname(os.path.abspath(__file__))

  # Specify the filename to delete
  filename = "init_class.txt"

  # Construct the full file path
  file_path = os.path.join(script_dir, filename)

  # Check if the file exists
  if os.path.exists(file_path):
      # Delete the file
      os.remove(file_path)
      print(f"File '{filename}' deleted successfully.")
  else:
      print(f"File '{filename}' does not exist.")
  response = requests.get(GS_TRI_THUC_URL)

  soup = BeautifulSoup(response.text,'lxml')
  tags = soup.find_all('p')
  
  with open('init_class.txt','w', encoding="utf-8") as file:
    for tag in tags:
      file.write(tag.text+'\n')
  file.close()

def get_new_txt():
   # Get the directory where the script is located
  script_dir = os.path.dirname(os.path.abspath(__file__))

  # Specify the filename to delete
  filename = "new_class.txt"

  # Construct the full file path
  file_path = os.path.join(script_dir, filename)

  # Check if the file exists
  if os.path.exists(file_path):
      # Delete the file
      os.remove(file_path)
      print(f"File '{filename}' deleted successfully.")
  else:
      print(f"File '{filename}' does not exist.")
  response = requests.get(GS_TRI_THUC_URL)

  soup = BeautifulSoup(response.text,'lxml')
  tags = soup.find_all('p')
  
  with open('new_class.txt','w', encoding="utf-8") as file:
    for tag in tags:
      file.write(tag.text+'\n')
  file.close()

def compare_files(file1, file2):
    with open(file1, "r",encoding="utf-8") as f1, open(file2, "r",encoding="utf-8") as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    if len(file1_lines) != len(file2_lines):
        return False

    for line1, line2 in zip(file1_lines, file2_lines):
        if line1.strip() != line2.strip():
            return False

    return True

def replace_file(file1, file2):
    try:
        # Read the contents of file2.txt
        with open(file2, "r",encoding="utf-8") as f2:
            new_content = f2.read()

        # Replace the contents of file1.txt
        with open(file1, "w",encoding="utf-8") as f1:
            f1.write(new_content)
        print(f"File '{file1}' has been replaced successfully.")

        # Delete file2.txt
        os.remove(file2)
        print(f"File '{file2}' has been deleted successfully.")
    except OSError as e:
        print(f"Error processing files: {e}")

      

