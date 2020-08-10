
  

# sca-codeinsight-reports-template

  
  

The sca-codeinsight-reports-template repository is a simple example report for Revenera's Code Insight product. A user should be able to clone this project and then modify the contents to create a custom report with the desired data they wish to collect and present.

  

## Usage

  

This report is executed directly from within Revenera's Code Insight product. From the summary page of each Code Insight project it is possible to *generate* the **Template Example Report** via the Custom Report Framework

  

The Code Insight Custom Report Framework will provide the following to the custom report when initiated:

- Project ID

- Report ID

- Authorization Token

  

For this example report these three items are passed on to a batch or sh file which will in turn execute a python script. This script will then:

  

- Collect data for the report via REST API using the Project ID and Authorization Token

- Take the collected data and 
	- create a simple html document with details about the project - The *"viewable"* file
	- create a simple text document with details about the project

- Create a zip file of this html document - The *"downloadable"* file

- Create a zip file with the viewable file and the downloadable file

- Upload this combined zip file to Code Insight via REST API

- Delete the report artifacts that were created as the script ran

  

### Registering the Report

  

Prior to being able to call the script directly from within Code Insight it must be registered. The registration.py file can be used to directly register the report once the contents of this repository have been copied into the custom_report_script folder at the base Code Insight installation directory.

To register this report:

    python registration.py -reg

To unregister this report:

    python registration.py -unreg

  
  

  

## License

  

[MIT](LICENSE.TXT)