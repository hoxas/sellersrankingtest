# Dev Test - Sellers Ranking Logic

## Introduction
Sellers Ranking & Registration Logic Prototype\

Made with:
>Python 3 - Script\
>Sqlite - Database

The database already comes populated with a few sales and 5 registered sellers with the following names:
> Helo\
> Mark\
> Sable\
> Richie\
> Lana

So when registering a sale if the seller name doesn't match any of these it will ask for another name.

## Requirements
> Python 3.8 >=\
> Git (to clone the repo)

***All the modules used are Python built-ins.***

## Installation
Cloning the repository
```
git clone https://github.com/hoxas/sellersrankingtest
```

## Running
Entering repo directory
```
cd sellersrankingtest
```
Running script
```
python3 logic.py
```

## Usage
```
python3 logic.py [arg]
python logic.py [arg]
```
**Leave with no arg for default registration process.**
### Arguments:
| Command | Description |
| ------- | ----------- |
| -h --help | Display help string and exit |
| -s --skip | Skips sale registration process and outputs list |
| -l --list |  Lists registered sellers and exit |
          
## Demo
By running the command below without any changes to the database in the repo
```
python3 logic.py -s
```
We will skip the registration process to see if the output list ranking is working properly\
And the output should be:
```
Opening Sale Registration
Connecting to DB... 
Connection established!
Skipping registration process
All sales, sorted by sellers with most sales, descending:
{'customer': 'Alice', 'date': 1666407323.223167, 'item': 'T-shirt', 'price': 200.5, 'seller_name': 'Helo'}
{'customer': 'Alice', 'date': 1666407471.064199, 'item': 'Expensive Ring', 'price': 100000, 'seller_name': 'Helo'}
{'customer': 'Quazar', 'date': 1666407947.098727, 'item': 'Item', 'price': 999, 'seller_name': 'Helo'}
{'customer': 'Fred', 'date': 1666555714.750558, 'item': 'Queue', 'price': 500, 'seller_name': 'Sable'}
{'customer': 'Kay', 'date': 1666561285.366115, 'item': 'Pants', 'price': 149.99, 'seller_name': 'Sable'}
{'customer': 'Alice', 'date': 1666407385.863182, 'item': '200 Dollars', 'price': 500, 'seller_name': 'Mark'}
```
We can see in the output above that it ranked in descending order by the seller with most sales registered, being:
> **Helo** the number one with **three** sales\
> **Sable** number two with **two** sales\
> **Mark** number three with **one** sale

The other two sellers **Richie** and **Lana** have no **sales** registered so they don't show up. 

You are free to play around with the script and register more sales to check the output.

### Aditional Info

**date column is stored as a Unix Timestamp**