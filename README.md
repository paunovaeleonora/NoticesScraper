# NoticesScraper

This Scrapy Project collects all romanian notices for a particular day from http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1.

The script collects the following information for a chosen day:
  - Date,
  - Notice Number,
  - Tender Name,
  - Procedure State,
  - Contract Type,
  - Type of Procurement,
  - Estimated Value.

You should follow the website link. Then you filter notices for specific day by filling only the two fields of the filter form: "Publication date".
then press filter:
  - Right click and "Inspect". Go to Network. Then search for "GetCNoticeList/",
  - Right click on it and copy as Curl (bash),
  - Open Postman and go to File / Import / , select raw text and paste, then press Continue and Import. Click on the </> icon to view the generated python script,
  - Copy payload and headers and replace the existing ones into spiders/notices.py file.


The scripts has one start links. Collects all the tender notices for the chosen day from the website API, based on the total items and page size calculates the total number of pages. 
After that collects all the notices following the pages ahead and if the validation passes, it collects the required information and adds it to the database table.


Database:

  - The data is stored in SQLite database,
  - every time when the script is ran it adds only the tender notices that do not exist already in the database,
  - database relations need further modification,
  - notice_number is set as primary key

Project Requirements:
   - Python on you device, if not already installed,
   - clone this repository to a local repository on your machine,
   - open cmd (for Windows) or Linux terminal,
   - navigate to main folder of the project,
   - pip install requirements.txt,
   - to run the project run "scrapy crawl notices".

To see the collected information you can to go to: https://sqliteonline.com/ and upload your database.
If you use Pycharm you can see the db file directly in the IDE by double clicking notices.db file and set the conection. 
