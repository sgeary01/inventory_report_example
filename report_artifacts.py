'''
Copyright 2020 Flexera Software LLC
See LICENSE.TXT for full license text
SPDX-License-Identifier: MIT

Author : sgeary  
Created On : Fri Aug 07 2020
File : report_artifacts.py
'''

import logging
import html_assets.common_html

logger = logging.getLogger(__name__)

#--------------------------------------------------------------------------------#
def create_report_artifacts(reportData):
    logger.info("Entering create_report_artifacts")

    # Dict to hold the complete list of reports
    reports = {}

    htmlFile = generate_html_report(reportData)
    
    reports["viewable"] = htmlFile
    reports["allFormats"] = [htmlFile]

    logger.info("Exiting create_report_artifacts")
    
    return reports 


#------------------------------------------------------------------#
def generate_html_report(reportData):
    logger.info("    Entering generate_html_report")

    reportName = reportData["reportName"]
    projectName = reportData["projectName"]
    projectOwner = reportData["ownerName"]
    inventoryComponents = reportData["inventoryComponents"]
    

    htmlFile = reportName + "-" + projectName + ".html"

    # Create a simple HTML file to display
    html_ptr = open(htmlFile,"w")
    html_ptr.write("<html>\n")
    html_assets.common_html.create_html_head_block(html_ptr, reportName)

    html_ptr.write("<body>\n")
    html_ptr.write("    <div class='container'>\n")

    html_assets.common_html.create_html_banner(html_ptr, reportName)

    html_ptr.write("<h1> Inventory Details for project: %s</h1>\n" %projectName) 
    html_ptr.write("<p>\n") 

    html_ptr.write("<table id=\"reportData\" class=\"table table-condensed table-striped table-bordered table-sm\" style=\"width:100%\">\n")

    html_ptr.write("<colgroup>\n")
    html_ptr.write("<col span=\"1\" style=\"width: 30%;\">\n")
    html_ptr.write("<col span=\"1\" style=\"width: 15%;\">\n")
    html_ptr.write("<col span=\"1\" style=\"width: 15%;\">\n")
    html_ptr.write("<col span=\"1\" style=\"width: 40%;\">\n")
    html_ptr.write("</colgroup>\n")

    html_ptr.write("<thead>\n")
    html_ptr.write("<tr>\n")
    html_ptr.write("<th style=\"vertical-align:middle\" class=\"vertical-align:middle text-center\">Component</th>\n")
    html_ptr.write("<th style=\"vertical-align:middle\" class=\"text-center\">Version</th>\n")
    html_ptr.write("<th style=\"vertical-align:middle\" class=\"text-center\">License</th>\n")
    html_ptr.write("<th style=\"vertical-align:middle\" class=\"text-center\">URL</th>\n")
    html_ptr.write("</tr>\n")
    html_ptr.write("</thead>\n")
    html_ptr.write("<tbody>\n")

    for component in inventoryComponents:

        html_ptr.write("        <tr>\n")
        html_ptr.write("            <td>%s</td>\n" %inventoryComponents[component]["componentName"])
        html_ptr.write("            <td>%s</td>\n" %inventoryComponents[component]["componentVersionName"])
        html_ptr.write("            <td>%s</td>\n" %inventoryComponents[component]["selectedLicenseName"])
        html_ptr.write("            <td>%s</td>\n" %inventoryComponents[component]["componentUrl"])
        html_ptr.write("        </tr>\n")


    html_ptr.write("</tbody>\n")
    html_ptr.write("</table>\n")

    html_ptr.write("<p>\n") 
 

    # Write javascript cdns
    html_assets.common_html.add_javascript_cdns(html_ptr)
    html_ptr.write("<hr class='small'>\n") 
    html_ptr.write("</div>\n")

    html_ptr.write('''   <script src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>  \n''')

    html_ptr.write('''

            <script type="text/javascript">


            $(document).ready(function() {
                $('#reportData').dataTable( {
                "order": [[ 3, "desc" ]],
                "aLengthMenu": [[25, 50, 100, -1], [25, 50, 100, "All"]],
                "pageLength": 100
                } );
            } );

            </script> 
            ''')




    html_ptr.write("</body>\n")
    html_ptr.write("</html>\n")

    html_ptr.close() 

    logger.info("    Exiting generate_html_report")
    return htmlFile

