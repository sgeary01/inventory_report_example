'''
Copyright 2020 Flexera Software LLC
See LICENSE.TXT for full license text
SPDX-License-Identifier: MIT

Author : sgeary  
Created On : Fri Aug 07 2020
File : report_artifacts.py
'''

import logging

logger = logging.getLogger(__name__)

#--------------------------------------------------------------------------------#
def create_report_artifacts(reportData):
    logger.info("Entering create_report_artifacts")

    # Dict to hold the complete list of reports
    reports = {}

    textFile = generate_text_report(reportData)
    htmlFile = generate_html_report(reportData)
    
    reports["viewable"] = htmlFile
    reports["allFormats"] = [htmlFile, textFile]

    logger.info("Exiting create_custom_report")
    
    return reports 

#------------------------------------------------------------------#
def generate_text_report(reportData):
    logger.info("    Entering generate_text_report")
    
    reportName = reportData["reportName"]
    projectName = reportData["projectName"]
    projectOwner = reportData["ownerName"]
    
    textFile = reportName + "-" + projectName + ".txt"

    # Create a simple HTML file to display
    txt_ptr = open(textFile,"w")
    txt_ptr.write("%s\n" %reportName) 
    txt_ptr.write("\n")
    txt_ptr.write("Details for project: %s\n" %projectName) 
    txt_ptr.write("Project Owner: %s\n" %projectOwner) 
    txt_ptr.write("\n")

    txt_ptr.close() 

    logger.info("    Exiting generate_text_report")
    
    return textFile

#------------------------------------------------------------------#
def generate_html_report(reportData):
    logger.info("    Entering generate_html_report")

    reportName = reportData["reportName"]
    projectName = reportData["projectName"]

    htmlFile = reportName + "-" + projectName + ".html"

    # Create a simple HTML file to display
    html_ptr = open(htmlFile,"w")
    html_ptr.write("<html>\n") 
    html_ptr.write("<title>%s - %s</title>\n" %(reportName, projectName)) 
    html_ptr.write("<h1><center>%s</center></h1>\n" %reportName) 
    html_ptr.write("<p>\n") 
    html_ptr.write("<hr>\n") 
    html_ptr.write("<h1> Details for project: " + reportData["projectName"] + "</h1>\n") 
    html_ptr.write("<p>\n") 
    html_ptr.write("<h3> Project Owner: " + reportData["ownerName"] + "</h3>\n") 
    html_ptr.write("<p>\n") 
    html_ptr.write("<hr>\n") 
    html_ptr.write("</html>\n") 
    html_ptr.close() 

    logger.info("    Exiting generate_html_report")
    return htmlFile

