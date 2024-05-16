# boarding_school_funding

## Table of Contents

- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Tools](#tools)
- [Data Cleaning](#data-cleaning)
- [Data Analysis](#data-analysis)
- [Results](#results)
- [Recommendations](#recommendations)
- [Limitations and recommendations for future research](#limitations-and-recommendations-for-future-research)
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
The data collection required manually typing the statistics from government reports, and then creating UniqueIDs to track schools over time that frequently changed name, type (e.g. day vs. boarding, or contract status).  I also collected additional data on attendance and agency affiliation to facilitate additional analyses on the scope of the industry. The dataset includes the entirety of Alaska, B.C., Washington, Oregon, and California. However, I also included a filter for those schools located in the Northwest Coast (roughly, SE AK to Northern CA) for purposes of the analysis.

### Data Analysis

This analysis focuses on trends within the Northwest Coast, a subset of the entire dataset available. A summary table is presented of funding to distinct religious denominations in this period converted roughly into 2024 USD. Additionally, trends are analyzed for:
-funding to both government and church schools over time, by country
-total contract funding by province over time
-funding to Protestant v. Catholic churches over time, by country
-boarding school attendance over time, by country
-day school attendance over time, by country

Additional results are listed below for government land grants to church denominations on reservations in Washington, Oregon, and California.

### Results
![Screenshot from 2024-05-16 14-52-01](https://github.com/lucaskolson/boarding_school_funding/assets/91341415/412b4610-4a00-4f87-b8a1-4f67cc801bcb)


![Screenshot from 2024-04-22 22-11-33](https://github.com/lucaskolson/boarding_school_funding/assets/91341415/51cff5c2-3f6a-4afb-b5f4-8e457105d147)


![Screenshot from 2024-04-22 22-15-17](https://github.com/lucaskolson/boarding_school_funding/assets/91341415/dcfd580e-9fe7-4c72-8912-ce6288c99de2)


![Screenshot from 2024-04-22 22-44-07](https://github.com/lucaskolson/boarding_school_funding/assets/91341415/94b42e7a-eed9-4355-b6c3-92c1e3bc6d04)


![Screenshot from 2024-04-23 12-37-19](https://github.com/lucaskolson/boarding_school_funding/assets/91341415/d351312d-808a-4d45-8566-b2664a9b64eb)


![Screenshot from 2024-04-22 22-37-34](https://github.com/lucaskolson/boarding_school_funding/assets/91341415/80e92b5a-b938-45eb-af7e-c166113ddac2)

<img width="461" alt="Screenshot 2024-05-16 at 2 47 16 PM" src="https://github.com/lucaskolson/boarding_school_funding/assets/91341415/1a5a2fb5-b682-4a52-bc6a-e31d189bb3cd">

<img width="905" alt="Screenshot 2024-05-16 at 2 47 31 PM" src="https://github.com/lucaskolson/boarding_school_funding/assets/91341415/3ae18598-ed3b-4ff3-a79f-aceb274d8d77">


### Limitations and recommendations for future research
This study is limited in several dimensions. As a comparison of just one region along the Northwest Coast, it is unclear how many of these generalizations are accurate across the entirety of both countries. Additionally, only a limited time-period is covered within this region. While this period does encompass the peak of simultaneous church involvement in both countries, significant church activities with boarding and residential schools exists both before and after. Lastly, perhaps most glaringly, mission schools are largely excluded from this study when they are not actively receiving money from the government. These unfunded mission schools do not report statistics to the government and including them would require access to a much broader array of sources controlled by church denominations. 

However, these limitations point to areas for further research. Perhaps the lowest hanging fruit would be to expand analysis of contract schools across the entirety of the United States and Canada as well as up to the present. Doing so is not only feasible but would provide a much more comprehensive picture of church involvement in the industry, allowing for a more rigorous approach to tracking down available church archives. Additionally, collecting and harmonizing data on boarding schools in New Zealand and Australia would provide the simplest international comparison to the United States and Canada with a focus on former British colonies. This international approach would work towards a broad understanding of Indigenous boarding schools as a global phenomenon and the variations across different locations and time-periods. An expanded dataset would also allow for better causal analysis to explain the varying manifestations of Indigenous boarding schools across the world. 

### Selected References

S.1723 - Truth and Healing Commission on Indian Boarding School Policies Act. Accessed at: https://www.congress.gov/bill/118th-congress/senate-bill/1723

Adams, David Wallace. Education for Extinction: American Indians and the Boarding School Experience, 1875-1928. University Press of Kansas, 2501 W. 15th St., Lawrence, KS 66049, 1995.

Canada. Annual Report, 1880, Department of the Interior. "Report on Industrial Schools for Indians and Half-Breeds". Nicholas Flood Davin. 14th March, 1879. Accessed at: http://rschools.nan.on.ca/article/the-davin-report-1879-1120.asp 

Feir, D. L. (2016). The long‐term effects of forcible assimilation policy: The case of Indian boarding schools. Canadian Journal of Economics/Revue canadienne d'économique, 49(2), 433-480.

Gregg, M. T. (2018). The long-term effects of American Indian boarding schools. Journal of Development Economics, 130, 17-32.

NABSHC Digital Map, accessed at: https://boardingschoolhealing.org/digitalmap 

Native American Rights Fund, “Trigger Points,” November 2019. https://www.narf.org/nill/documents/trigger-points.pdf

Newland, Bryan Todd. Federal Indian boarding school initiative investigative report. United States Department of the Interior, Office of the Secretary, 2022.

Smith, A. "Indigenous peoples and boarding schools: A comparitive study. United Nations Permanent Forum on Indigenous Issues." (2009): 2009. Accessed at: https://www.un.org/esa/socdev/unpfii/documents/IPS_Boarding_Schools.pdf

Weber, Francis J. "A Missionary's Plea For Governmental Assistance." Records of the American Catholic Historical Society of Philadelphia 77, no. 4 (1966): 242-49. Accessed June 9, 2020. www.jstor.org/stable/44210640.



