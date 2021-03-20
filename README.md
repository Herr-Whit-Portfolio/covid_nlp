# covid_nlp
Sentiment prediction using covid-relevant tweets

## Background

Using machine learning it is possible to leverage patterns in signals (language, images, etc.) and make decisions 
accordingly. However, as these patterns are change due to real-world developments, machine learning models must adapt. 
The covid-crisis resembles a particularly abrupt shift in economic, social and cultural patterns. This project will 
analyse and predict sentiments towards events and experiences related to covid based on twitter posts.

## Dataset

The dataset, which will be used for this project ist a collection of ~45.000 twitter posts collected and annotated with 
sentiment in five categories ranging from "extremely negative" to "extremely positive".

## Project

The primary aim of this project is to develop a classification model to predict the sentiment associated with a tweet 
about corona-related tweets. 

### Vocabulary
A secondary aim is to develop insight into corona-specific vocabulary and how otherwise neutral words as for example 
"supermarket" may be associated more with certain sentiments in this context (as for example supermarkets being 
associated with stressful experiences in a pandemic due to low stocks of hygiene products).

### Transfer Learning
Another secondary aim is to study how well classifiers, trained before the corona pandemic can be adapted to deal with 
the new context of corona. Therefore, this project will compare transfer learning methods with developing classifiers 
from scratch. 
