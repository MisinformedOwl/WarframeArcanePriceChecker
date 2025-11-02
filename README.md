# WarframeArcanePriceChecker
Checks the warframe marketplace for each arcane price which can be dissolved by loid.

## How it works
So essencially I use docker to run airflow. 

And using the dags it will run the python files located in ``./dags/warframeArcanePricing/collectArcanes.py`` This then creates a csv. which can be used by a power BI application, seen as a ``.pbix`` file.

## How to run it
I'm not gonna go into detail about how to run it so i'm going to assume you have knowledge and can just follow these generic instructions as it's late and i'm getting tired. Use docker, to run the docker file. It will create an airflow application at ``localhost:8080``. You then go to dags and search for warframe and enable it or trigger it to run once.

If you want to not go through this, simply run collect Arcanes.py and it will get the new prices and update the CSV for you to use in power BI, or whatever visualisation tool of your choice.

### Whats the point of EstablishXMLArcanes.py
Well it's actually creating the json file in the same area. I started using XML, didn't realise you cant have integers. So i switched.
Anyways, this file creates that file. It establishes the arcanes available by loid to roll for. Aswell as their dropchances displayed on the warframe wiki.
