
### Vertical Search Engine for Coventry University's School of Economics, Finance, and Accounting<br />
This project developed a vertical search engine for Coventry University's School of Economics, Finance, and Accounting. The search engine incorporated web scraping, inverted index, and query processor using Beautiful Soup and Flask. The web scraper was deployed on Azure Function for efficient scaling, cost optimization, and scheduled automation of web scraping. Scraped data was stored securely and reliably on Azure Blob storage. The web application was successfully deployed on Azure cloud as a Web App for seamless availability and scalability.<br />

**The website can be accessed at the following link:**
coventryfinan.azurewebsites.net

Components
The following are the main components of the vertical search engine:<br />

Web scraper: The web scraper uses Beautiful Soup to extract data from the websites of Coventry University's School of Economics, Finance, and Accounting. The scraped data is stored in a JSON file.<br />
Inverted index: The inverted index is a data structure that stores the terms in the scraped data and their corresponding document IDs. This allows for efficient search queries.<br />
Query processor: The query processor takes a user query and searches the inverted index for matching documents. The results of the search are then presented to the user.<br />
Azure Function: The Azure Function is used to deploy the web scraper. This allows for efficient scaling and cost optimization of the web scraper.<br />
Azure Blob storage: Azure Blob storage is used to store the scraped data. This ensures that the data is stored securely and reliably.<br />
Azure Web App: The Azure Web App is used to deploy the web application. This ensures that the web application is available and scalable.<br />
