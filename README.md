
# Classification Model for Water Pumps in Tanzania

Our goal for this project is to build a model to classify water pumps in Tanzania as functional or needs repair.

## TABLE OF CONTENTS

Our home repository contains the project environment and information about our project.

### Final Report

[Final Report Notebook](Final_Report.ipynb)


### EDA

[Exploratory Data Analysis](eda) 

### Data

[Raw Data](data)


### Images

[Visualizations](images)


### SRC

[Custom Functions](src)

### README

[Read Me](README.md)


## Project Goal and Background

We used the Cross-Industry Standard Process for Data Mining(CRISP-DM) approach to this project. 

#### Business Understanding: 

We began this project by taking the time to understand what the problem is, who will be using the model we build, how the model will be used, and how this helps the goals of the stakeholders of the organization.

The **problem this project is addressing** is access to water by way of wells. Access to water is an important issue that has reverberations in the social and economic aspects of a society. The [World Health Organization writes](https://www.who.int/news-room/fact-sheets/detail/drinking-water#:~:text=Safe%20and%20readily%20available%20water,contribute%20greatly%20to%20poverty%20reduction.), “Safe and readily available water is important for public health, whether it is used for drinking, domestic use, food production or recreational purposes. Improved water supply and sanitation, and better management of water resources, can boost countries’ economic growth and can contribute greatly to poverty reduction.” 

The water pumps we are looking at in our modeling are meant to provide potable water. If these water pumps fail, that community’s availability of drinking water is impacted. Reduced availability of working water pumps means an increased use of the functional ones, which could mean a reduction in that water pumps lifespan before it needs repairs. Being able to know which pumps are on the point of failing can help repair them before they become broken and have a minimal interruption of service to the community.

This model **will be used by** the Tanzanian Ministry of Water to assess which water pumps will fall into disrepair first and be prepared to repair them before they become non-functional. This model **helps the goals** of the Tanzanian Ministry of Water to provide access to water to its citizens. By knowing which water pumps will fail, the Ministry of Water can implement better maintenance. Moreover, this model and implementation of outcomes can help towards [The Tanzanian Development Vision 2025](https://mof.go.tz/mofdocs/overarch/vision2025.htm) to have universal access to safe water by the year 2025.

#### Data Understanding:

The **data comes from** [Taarifa](http://taarifa.org/) who sources it from the [Tanzanian Ministry of Water](https://www.maji.go.tz/). The datasets were downloaded from [Driven Data’s “Pump it Up: Data Mining the Water Table”](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/23/) competition.

Our target is to classify the water pumps into functional or needs repair(functional needs repair and non functional.The data is currently classified as:
1. `functional` - the waterpoint is operational and there are no repairs needed
2. `functional needs repair` - the waterpoint is operational, but needs repairs
3. `non functional` - the waterpoint is not operational

This overview map shows functional water points in green and ones that need repair in orange. There are many other orange points that overlap with and are underneath the green ones and are difficult to distinguish at this zoomed out view, but with this map we want to showcase that there are many areas where there is only orange—meaning that these areas have a pump that needs repair, many areas without any working pumps nearby. 

![Image of Tableau Map](https://github.com/MWilliamson96/Tanzania_Well_Competition/blob/master/images/Map.png)

## Modeling

When building our first model we wanted to focus on physical features that all the wells would be subject to and would contribute to their eventual mechanical failure. Narrowing the focus of our features will help the Tanzanian Ministry of Water better allocate resources to fixing the appropriate wells that are peppered throughout their developing country.

After attempting several models, we found that the 'functional-needs repair' class was exceptionally difficult to predict due to
it being severly underrepresented in the data set. We tried to remedy this problem by using upsampling techniques like SMOTE,
but found that the results were still unsatisfactory. We decided that both the class 'functional-needs repair' and the class
'non-functional' were top priority as these classes will have the most significant impact on the health and well being of
the people using these wells. In order to more reliably predict these categories we combined them into one category 'needs repair'.
This eliminated the problem of having a significant minority class and increased our recall score for the new category significantly over the recall score for 'functional-needs repair'.

![Image of confusion matrix initial](https://github.com/MWilliamson96/Tanzania_Well_Competition/blob/master/images/confusion_matrix_tert.png)

## Evaluation
After running our model, we retrieved the features that had the most importance when it came to classifying functional vs non-functioning or wells that need repair. And as we suspected the features that played the biggest role came down to physical attributes dealing with the mechanism involved with retrieval, how long its been in use, the quality of the water in the well, and most importantly the well altitude. 

This last feature we feel most likely relates to access to the well, both by the populations using it, and to the maintenance crews or installers who service these wells. Wells at higher altitudes are most likely harder to get to, especially if they are located in a mountainous region. 

![Image of Tableau graph](https://github.com/MWilliamson96/Tanzania_Well_Competition/blob/master/images/top%20features.png)

# Conclusion
Our final model was able to predict whether or not a well is in need of repair with an accuracy of 80.8%. The most important features in determining which class a well would fall into were the well altitude (gps_height in the data), the water point type, the contsruction year, and the size of the population that relies on that well. We think there is potential for improvement in our model by a small margin if we perhaps drop some of the least important features and adjust our pre-processing strategy to reduce data leakage, but we’ll likely only see a small increase in accuracy and recall as the data itself seems to have a significant bit of random noise.

![Image of confusion matrix binary](https://github.com/MWilliamson96/Tanzania_Well_Competition/blob/master/images/confusion_matrix_binary.png)

# Potential Next Steps
Our next step is to of course increase our ability to better classify which wells are functional and non functional. By improving our model we hope to help Tanzania better determine what characteristics lead to failing wells, that way after they bring more wells back online, so they continually meet Tanzania’s water needs.
 
Another  step forward is that we would like to get additional data that helps inform the usage as well as look at the findings with regards to population, and also who is using the water well, be it for urban or agricultural needs. Making these determinations can help inform the Ministry of Water which wells to prioritize for immediate repair, and which wells are not worth the cost of repairing and maintaining.
