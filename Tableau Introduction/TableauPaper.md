# Tableau Paper

Tableau is a powerful visualization tool that allows data to be rapidly visualized and disected.  Here at PNNL we have used it in a variety of projects both internally and externally and have found it can offer significant value when leveraged correctly.  This paper will outline some of the best practices we have found for utilizing Tableau.  Our hope is this will serve as both a guide for others and offer an undersatnding of the Tableau process here at PNNL.


## Understanding the problem

Often we start with data and expect information.  Changing data into information requires an understanding of the problem to elicit the important parts.  Therefore, the first step in creating most visualizations is spending a few hours understanding the problem space.  Generally, this starts by perfoming minimal literature reviews followed by discussions with subject matter experts.  This portion of the process is not overly time consuming but spending extra time here generally pays off with the final product.

When evaluating failed visualization products, we have noticed this step has either been skipped or rushed.  

### Example
Tableau was leveraged in one project to visualize weather information.  This was a broad problem so we probbed into what needed to be visualized and the problem space.  From our elicitation we learned our clients were primarily interested in understanding the temperature and humidity information from a number of projected weather files across years.  By digging into the problem space in more detail we were able to develop a small list of must have metrics for the final visualization.


## Understanding the data

Having a cursory understading of the problem gives the designers something to look for in the dataset.  In the same way that a rock climber needs to find the first ledge for thier hand, a designer needs an initial place to start pulling and visualizing data.  This step is also performed in the presence of the clients to help refine the designers understanding of the dataset.

When available, we leverage existing excel documentation to look at data structures adnd organization.  If data is only stored within databases we construct entity relationship diagrams to map the data location and relationships.  These almost always become a valuable discussion tool later in the visualization workflow.



## Understanding the clients

The perfect visualization for one client might be completely unacceptable for the next.  For that reason, we try and understand what each specific client is looking for from the visualization.  Some people will require tables of data, others only want colored charts.  Asking clients what they want isn't generally effective so we instead ask to see current reports and charts they find useful.  These generally become a good starting point for our future development.


## Understanding the question

With the background in hand, it should now be possible to understand and engage the clients on the question they are trying to answer with the data.  A best practice is to fill out the following table 

Use Case | Reasoning | Explination
----

## Formatting Data

At this point we have a reasonable understading of the problem space, cursory understanding of the data, and examples of visualzations the clients already find useful.  This is the time to start thinking more about the data.

A stacked dataset will work well for Tableau visualzations like the following:

If the clients require visualizations like <Insert Viz> it must be unstacked.

Our team leverages open source ETL tools to transform database data or will use excel macros to reformat existing excel sheets.  The best practice is to convert the data to both a stacked and unstacked version when possible so both are available.  Tableau excels at data blending and can make the connection between the two data formats seamless.

Transforming data can always become a nightmare if the data becomes updated in the future.  For that reason, reformatting repeatability is extremely important.  This requires an understanding of all input files used, transformation techques, and outputs.  The outputs should also be clearly labeled with some type of documentation indicating their source and a processing date.

### Text vs xls vs db

Whenever possible a database works extremely well with Tableau.  When processing weather information for a client, an R script was developed to read the files into a local sqlite database for processing.  Once in a database, the records can easily be joined with other types of information.  

If data has been reformatted from excel or csv files and is relatively small, excel might be the best option for data storage format.  Tabeleau can connect live to excel sheets which makes updating and changing information extremely efficient for those used to the excel environment. 


## Creating visualization

Once a good data foundation is established the fun can begin.  There are numerous tutorials fully detailing the complexities of Tableau visualizations and thier possibilities.  Using the details from above we start constucting individual sheets to display the data.  These are generally higher level than appear to be useful at first but will become part of dashboards in the future.  

Actions and dashboard are created once the core visualization sheets are finished.  One or more core visualizations are placed on a sheet to tell a compelling story about the data.  Tableau differs from other tools because it works best wehn the visualizations are compartmentalized to dashboards.  Actions can be used to seamlessly transport the user between dashboards to visualize their data.  We have used this technique to show geographic relationships.  The client was interested in understanding information at the city level but also needed something for the entire country.  Our solution was to create a colored country map that linked to a state level dashboard highlighting each city.  This action was immediate and allowed us to show more detailed information regarding the state and the selected cities.  We followed a similar approach to show what resources were available in the city.


## Publication

There are three primary methods of distrubuting a Tableau visualiztion, each of which has benefits that others do not.

### 1 Tableau Public
	- When you are using data that is relatively small, less than 1,000,000 rows, and is not proprietary, Tableau public can be an excellent option.  Through their public server, Tableau will store your data and host the visualiztion.  This can be easily embedded into websites to quickly share insights.

	Tableau public also has some limitations on what can be done with the dashbaord.  When the dashbaord is created with the desktop version items like "view data" are available, these are not available in the public version so additional design considerations must be taken into account if the user would like to see all underlying data.

	Pros: Completely free, easily sharable, very fast
	Cons: Data must be made public, data sizes must be relatively small.


### 2 Tableau Reader
	- Often data is not public and the insights gained from them are for a specific subset of people.  Tableau reader is a great option for this group because it allows each of them to review the data on their own computer at their leaisure without an internet connection.  These workbooks don't have a true file size limit but in general, all data will be stored with the workbook so it is important to keep overall data size in mind.  We often describe this as an interactive PDF for a users data.
	Tableau reader has the same limitations as the public version with viewing all data.  This again should be taken into consideration when creating a workbook for other users.

	Pros: All data stored within documnet, no internet connection required, also completely free to view data
	Cons: Data is not automatically updated for each user's workbook.  This can be a major disadvantage when it comes to rapidly changing data.


### 3 Tableau Desktop

	This is the same program used to create the original visualizations.  The users will end up seeing the workbook in the same way as it was created.  This can sometimes be a disadvantage because users may be tempted to pull in additional data or visualizations.  At times, this results in a user creating a "personalized workbook" that doesn't reflect the current development state.  Consideration should be made to these users adn work in any features they have indepndently created into a fully deployed production version.

	Pros: Users will have the most control over the dashboard.  Anything that is done by the analyst can also be done by the end user.  Data can also be updated by the end user so this can be more easily used for rapidly changing datasets.
	Cons: Must pay the full license fee for any users who want to view the workbook.  This is generally $2k.  End users may also experience additional confusion with the workbook becuase they have more options.


### 4 Tableau Server
	When possible, Tableau server is the preferred deployment environment.  Once a user has access to Tableau server, they gain the ability to view data in nearly the same way as on the desktop version.  Their interface is generally a web browser but can also be through other devices such as an iPad.  When utilizing the web interface, the end user can also create comments and change portions of the dashboard.  This makes adding features far easier because comments can be shared between users rapidly.

	Pros: Automatic data updating.  Collaboration between groups
	Cons: High initial cost.  Additional fee for each new user



## Validation with use cases


- Creating a visualization with tableau public
- Ingesting excel data - best practices
