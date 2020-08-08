'''
Copyright 2020 Flexera Software LLC
See LICENSE.TXT for full license text
SPDX-License-Identifier: MIT

Author : sgeary  
Created On : Fri Aug 07 2020
File : report_data.py
'''

import logging
import CodeInsight_RESTAPIs.project.get_project_inventory

logger = logging.getLogger(__name__)

#-------------------------------------------------------------------#
def gather_data_for_report(domainName, port, projectID, authToken, reportName):
    logger.debug("Entering gather_data_for_report")

    try:
        projectInventoryResponse = CodeInsight_RESTAPIs.project.get_project_inventory.get_project_inventory_details(domainName, port, projectID, authToken)
    except:
        logger.error("    No project ineventory response!")
        print("No project inventory response.")
        return -1

    projectName = projectInventoryResponse["projectName"]
    projectOwner = projectInventoryResponse["ownerName"]
    inventoryItems = projectInventoryResponse["inventoryItems"] 

    reportData = {}
    reportData["reportName"] = reportName
    reportData["projectName"] = projectName
    reportData["ownerName"] = projectOwner
    reportData["projectID"] = projectID
    


    logger.debug("Exiting gather_data_for_report")

    return reportData


