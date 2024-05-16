# boarding_school_funding

## Table of Contents

- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Tools](#tools)
- [Data Cleaning](#data-cleaning)
- [Data Analysis](#data-analysis)
- [Results](#results)
- [Recommendations](#recommendations)
- [Limitations](#limitations)
- [References](#references)


### Project Overview
This project analyzes trends in U.S. and Canadian funding in the Northwest Coast for Indigenous boarding and residential schools for the period 1876-1909. The primary focus of the dataset is to track funding received by specific church denominations over time in this period. This period covers the early evolution of the boarding school industry for Indigenous peoples in this region, particularly when church denominations were simultanously active in both countries. Afterwards, as the data shows, church involvement in the U.S. tapers off while increasing in Canada.

This dataset is used as the basis for the first chapter of my doctoral dissertation at the University of Washington: "Penitential Pilgrims: Indigenous Truth Commissions in the Northwest Coast"

### Data Sources
This dataset is based on annual reports of the US Commissioner of Indian Affairs, the Alaska General Agent of Education, and the Canadian Annual Report on Indian Affairs. The beginning of the time period aligns with the earliest simultaneous reporting of school financial statistics by the US and Canadian governments for California, Oregon, Washington, British Columbia, and Alaska. This beginning also aligns well with the end of Grant’s presidency in the US and just before 1879, which marked a number of key events including the Davin Report, the opening of Carlisle Indian School, and the establishment of the Bureau of Catholic Indian Missions. The end of the dataset coincides with the 1908 U.S. Supreme Court Case Quick Bear v. Leupp that ended the model of church contracting commonly used beforehand. Consequently, the dataset allows for a comparative approach of the early establishment of the boarding and residential school industry in the US and Canada at a time when church denominations in both countries were actively receiving government funding.

## Tools
The data for each year is saved in a .csv file, which I uploaded into a MySQL server. The code is written in python using VScode to access the MySQL server and then conduct the analysis. Specific libraries in python include:

-mysql.connector
-numpy
-pandas
-matplotlib.pyplot
-tabulate


### Data Cleaning
The data collection required manually typing the statistics from government reports, and then creating UniqueIDs to track schools over time that frequently changed name, type (e.g. day vs. boarding, or contract status).  I also collected additional data on attendance and agency affiliation to facilitate additional analyses on the scope of the industry. The dataset includes the entirety of Alaska, B.C., Washington, Oregon, and California. However, I also included a filter for those schools located in the NOrthwest Coast (roughly, SE AK to Northern CA) for purposes of the analysis.

### Data Analysis



### Results



![image](https://github.com/lucaskolson/boarding_school_funding/assets/91341415/22ced2ca-1448-4884-b0d9-c9c27d2a6236)







### Recommendations


### Limitations


### References
