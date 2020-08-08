'''
Copyright 2020 Flexera Software LLC
See LICENSE.TXT for full license text
SPDX-License-Identifier: MIT

Author : sgeary  
Created On : Fri Aug 07 2020
File : create_report.py
'''

import sys
import logging
import argparse
import zipfile

import report_data
import report_artifacts

###################################################################################
# Test the version of python to make sure it's at least the version the script
# was tested on, otherwise there could be unexpected results
if sys.version_info <= (3, 5):
    raise Exception("The current version of Python is less than 3.5 which is unsupported.\n Script created/tested against python version 3.8.1. ")
else:
    pass

###################################################################################
#  Set up logging handler to allow for different levels of logging to be capture
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S', filename="_template_report.log", filemode='w',level=logging.DEBUG)
logger = logging.getLogger(__name__)

####################################################################################
# Create command line argument options
parser = argparse.ArgumentParser()
parser.add_argument('-pid', "--projectID", help="Project ID")
parser.add_argument("-rid", "--reportID", help="Report ID")
parser.add_argument("-authToken", "--authToken", help="Code Insight Authorization Token")
parser.add_argument("-domainName", "--domainName", help="Code Insight Core Server Domain Name")
parser.add_argument("-port", "--port", help="Code Insight Core Server Port")


#----------------------------------------------------------------------#
def main():

	reportName = "Template Example Report"

	logger.info("Creating %s" %reportName)
	print("Creating %s" %reportName)

	# See what if any arguments were provided
	args = parser.parse_args()
	projectID = args.projectID
	reportID = args.reportID
	authToken = args.authToken
	port = args.port
	domainName = args.domainName
	
	logger.debug("Custom Report Provided Arguments:")	
	logger.debug("    projectID:  %s" %projectID)	
	logger.debug("    reportID:   %s" %reportID)	
	logger.debug("    domainName:  %s" %domainName)	
	logger.debug("    port:  %s" %port)
	logger.debug("    authToken:  %s" %authToken)	

	try:
		reportData = report_data.gather_data_for_report(domainName, port, projectID, authToken, reportName)
		print("    Report data has been collected")
	except:
		print("Error encountered while collecting report data.  Please see log for details")
		logger.error("Error encountered while collecting report data.")
		return -1
	
	try:
		reports = report_artifacts.create_report_artifacts(reportData)
		print("    Report artifacts have been created")
	except:
		print("Error encountered while creating report artifacts.  Please see log for details")
		logger.error("Error encountered while creating report artifacts.")
		return -1

	logger.debug("Reports: %s" %reports)


	logger.info("Completed %s" %reportName)
	print("Completed %s" %reportName)


#----------------------------------------------------------------------#    
if __name__ == "__main__":
    main()  