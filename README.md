# Rossmann Pharmaceuticals Sales Prediction

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann is concerned with predicting their daily sales for up to six weeks in advance.

This project builds an end-to-end product that delivers the predictions and serves it on web application dashboard. 

### The deployed web application dashboard can be found ...

### The data and feature description for this challenge can be found [here](https://www.kaggle.com/c/rossmann-store-sales/data).

## Folder Structure
The notebooks folder contains notebooks for explanatory data-analysis and modelling respectively. The source code for the web application dashboard can be found in web_dashboard folder.

## Clonning and Running
1. Clone the repository
2. You can run the notebooks on jupyter notebook or cloud services like Google Colab.
3. Follow the following steps to run the web dashboard.

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/flask-boilerplate-dashboard-argon.git
$ cd flask-boilerplate-dashboard-argon
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=app.py
$ (Powershell) $env:FLASK_APP = ".\app.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```
## Procedure
The project uses seasonal decomposition and visualizations to understand the historical sales of Rossmann Stores. LinearRegression and RandomForrestRegressor were used to make predictions for future sales. The predictions are served on a web application dashboard built using Flask and deployed on Heroku.

## Evaluation
The project uses GridSearchCV for hyper-parameter tuning and model comparison with a scoring of r-squared. RandomForest turned out to be the best performer.  

## Data fields
Most of the fields are self-explanatory.

The following are descriptions for those that
aren't.

- Id - an Id that represents a (Store, Date) duple within the test set

- Store - a unique Id for each store

- Sales - the turnover for any given day (this is what you are predicting)
- Customers - the number of customers on a given day
- Open - an indicator for whether the store was open: 0 = closed, 1 = open
- StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are
- closed on state holidays. Note that all schools are closed on public holidays and
- weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
- SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public
- schools
- StoreType - differentiates between 4 different store models: a, b, c, d
- Assortment - describes an assortment level: a = basic, b = extra, c = extended. Read more
- about assortment here
- CompetitionDistance - distance in meters to the nearest competitor store
- CompetitionOpenSince[Month/Year] - gives the approximate year and month of the
- time the nearest competitor was opened
- Promo - indicates whether a store is running a promo on that day
- Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is
- not participating, 1 = store is participating
- Promo2Since[Year/Week] - describes the year and calendar week when the store
- started participating in Promo2
- PromoInterval - describes the consecutive intervals Promo2 is started, naming the
months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts
in February, May, August, November of any given year for that store
