'''
Copyright 2020 Flexera Software LLC
See LICENSE.TXT for full license text
SPDX-License-Identifier: MIT

Author : sgeary  
Created On : Mon Aug 10 2020
File : common_html.py
'''

import os
import logging
from datetime import datetime
import base64

logger = logging.getLogger(__name__)

#----------------------------------------------------------#
def create_html_head_block(html_ptr, reportName):
    logger.info("Entering create_html_header for %s" %reportName)

    scriptDirectory = os.path.dirname(os.path.realpath(__file__))
    logger.debug(scriptDirectory)

    cssFile =  os.path.join(scriptDirectory, "css/revenera_common.css")

    html_ptr.write("    <head>\n")

    html_ptr.write("        <!-- Required meta tags --> \n")
    html_ptr.write("        <meta charset='utf-8'>  \n")
    html_ptr.write("        <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'> \n")

    html_ptr.write(''' <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.1/css/bootstrap.min.css" integrity="sha384-VCmXjywReHh4PwowAiWNagnWcLhlEJLA5buUprzK8rxFgeH0kww/aWY76TfkUoSX" crossorigin="anonymous">\n''')
    html_ptr.write('''    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.20/css/dataTables.bootstrap4.min.css">\n''')
  
    html_ptr.write("        <style>\n")

    # Add the contents of the css file to the head block
    try:
        f_ptr = open(cssFile)
        for line in f_ptr:
            html_ptr.write("            %s" %line)
        f_ptr.close()
    except:
        logger.error("Unable to open %s" %cssFile)
        print("Unable to open %s" %cssFile)
    
    html_ptr.write("        </style>\n")  
    html_ptr.write("        <title>%s</title>\n" %reportName)
    html_ptr.write("    </head>\n") 

#----------------------------------------------------------#
def create_html_banner(html_ptr, reportName):
    logger.info("Entering create_html_banner")
    
    # Grab the current date/time for report date stamp
    now = datetime.now().strftime("%B %d, %Y at %H:%M:%S")

    
    scriptDirectory = os.path.dirname(os.path.realpath(__file__))
    imageFile =  os.path.join(scriptDirectory, "images\\logo.svg")

    try:
        with open(imageFile,"rb") as image:
            encodedLogoImage = base64.b64encode(image.read())
    except:
        logger.debug("Unable to open %s" %imageFile)

    # Put the image and date in a table for organizational purposes

    html_ptr.write("<div class='row'>\n")
    html_ptr.write("    <div class='col align-self-end'>\n")
    html_ptr.write("    	<img src='data:image/svg+xml;base64, {}'>\n".format(encodedLogoImage.decode('utf-8')))
    html_ptr.write("    </div>\n")
    html_ptr.write("    <div class='col text-center align-self-end'>\n")
    html_ptr.write("       <h2>%s</h2>" %reportName)
    html_ptr.write("    </div>\n")
    html_ptr.write("    <div class='col text-right align-self-end'>\n")
    html_ptr.write("       Generated on: %s\n" %now)
    html_ptr.write("    </div>\n")
    html_ptr.write("</div>\n")


    html_ptr.write("        <p>\n")  
    html_ptr.write("        <hr class='medium'>\n")  

#--------------------------------------------------------------------------------------
def add_javascript_cdns(html_ptr):
    logger.info("Entering add_javascript_cdns")

    html_ptr.write("<script src=\"https://code.jquery.com/jquery-3.5.1.slim.min.js\" integrity=\"sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj\" crossorigin=\"anonymous\"></script>\n")

    html_ptr.write("<script src=\"https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js\" integrity=\"sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN\" crossorigin=\"anonymous\"></script>\n")

    html_ptr.write("<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.1/js/bootstrap.min.js\" integrity=\"sha384-XEerZL0cuoUbHE4nZReLT7nx9gQrQreJekYhJD9WNWhH8nEW+0c5qq7aIo2Wl30J\" crossorigin=\"anonymous\"></script>\n")    
