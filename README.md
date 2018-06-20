### HHchurch

This repo contains data and code for an assignment from the coursera course **Applied Data Science with Python**.

## The Assignment 

This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **religious events or traditions** (see below) for the region of **Hamburg, Hamburg, Germany**, or **Germany** more broadly.

You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Hamburg, Hamburg, Germany** to Ann Arbor, USA. In that case at least one source file must be about **Hamburg, Hamburg, Germany**.

You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.

Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!

As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.

Here are the assignment instructions:
  * State the region and the domain category that your data sets are about (e.g., **Hamburg, Hamburg, Germany** and **religious events or traditions**).
  * You must state a question about the domain category and region that you identified as being interesting.
  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.

What do we mean by **religious events or traditions**?  For this category you might consider calendar events, demographic data about religion in the region and neighboring regions, participation in religious events, or how religious events relate to political events, social movements, or historical events.

## Tips
 * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
 * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
 * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
 * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!


## My solution 
I decided to look into the amount of people with christian affiliations (protestants and catholics) in Hamburg, the development of these numbers over the past years and how this compares to the average in Germany. 

In this repository you will find the underlying data that I used, which I received from these websites: 
Data for Hamburg: http://www.kirchenaustritt.de/hamburg
Data for entire Germany: http://www.kirchenaustritt.de/statistik

Further you will find the python script to transform these data and make a nice figure using matplotlib. The figure can also be found in the repository. 
