# dash-covid-measures

###

* App is currently running on Heroku: https://dash-covid-measures.herokuapp.com/ 

### Team

* This dashboard is created by the research group [AIDA](https://aida.ugent.be) of Ghent University
 led by Professor dr. ir. Tijl De Bie. Contributors of this work are:

 - [Dieter De Witte](https://biblio.ugent.be/person/802000451589) (data analysis & python dashboard)
 - [Maarten Buyle](https://telefoonboek.ugent.be/nl/people/802002919534) (data analysis & python data prep)
 - [Tijl De Bie](https://biblio.ugent.be/person/9797BDFE-BE0B-11E4-9A6A-FB22B5D1D7B1) (supervision)

### data sources

* Excess mortality data: [mortality.org](https://mortality.org)
  - used to calculate R0
  - used to calculate IFR (infection fatality rates)
* COVID19 data from [Our world in data](https://ourworldindata.org/coronavirus-data-explorer)
* [COVID19 datahub](https://storage.covid19datahub.io/) for the covid measures data per country


### dash_heroku_deployment

* Have a look [here](https://github.com/drdwitte/dash-heroku-test)


* For a full tutorial on how to deploy your app, 
go right here: 
https://towardsdatascience.com/how-to-deploy-your-dash-app-with-heroku-a4ecd25a6205



* Actual deployment: 
    - go to folder with all the files in this template (app, requirements, Procfile)
    - note: requirements.txt is the output of pip freeze > requirements.txt and is kept in sync
    in pycharm

1. heroku create `unique-app-name`
2. git push heroku master
3. heroku ps:scale web=1

your app should be available from: https://`unique-app-name`.herokuapp.com

## Issues

* Start project => create project => from VCS
* Heroku crashes during startup => **gunicorn**: command not found => put in requirements file!