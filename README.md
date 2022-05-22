# Description
Simple price monitoring service accross a couple of supported sites.

The price monitoring service was created because the I love the offers and discounts. So, instead of searching manually and monitoring a couple of items every day I decided to automate this process and create a service.

This is a project will be built using VS Code. Drawio plugin for VS Code will be helpful so you can view the flowcharts.

### State

This project is in progress. The base structure is being defined.

### Design Overview

The project will include a backend and a frontend service. The backend will be built in Django which will be responsible for the user handling and will provide REST API endpoints that extract information about the price monitoring URLs of each user. The frontend will be built using React and it will fetch the information from the backend using API calls.

The flow of this service will be split into different distinct blocks. The first one would be to match the product that the user is looking for to specific URLs from each store. The second part of this flow will be to extract the information from this URLs and start tracking it. Initially, the service will include simple solutions in both blocks mostly because I want to build the core and experiment with React and then start iterating on it. 

