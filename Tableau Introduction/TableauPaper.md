# Tableau Paper

Tableau is a powerful visualization tool that allows data to be rapidly visualized and dissected.  We use Tableau regularly at PNNL, both internally and for external clients, and find that it offers significant value when leveraged correctly.  This paper will outline some of the best practices we have found for utilizing Tableau.  Our goal is this will serve as both a guide for others and offer an understanding of the PNNL Tableau process.

It's tempting to jump right into Tableau, devil-may-care what the data looks like or what information you're trying to get out of it.  We've all done it.  It doesn't work.  It's not worth it.  In the end a good plan will take you further than just diving in and creating meaningless bubble charts.  Before you start playing with the data, go through the following steps.  It will take a bit of time but will be worth it in the long run.

## Step 1.  Understand the Problem Space

We often start with data but expect information.  Transforming data into information, however, requires us to understand of the problem in order to deduce what parts of the data are important.  Generally, we start by performing minimal literature reviews and conducting interviews or discussions with subject matter experts and the client.  This step normally takes a few hours; spending extra time here generally pays off with the final product.

Consider yourself forewarned!  In projects where we have failed to deliver an adequate visualization, this step has either been skipped or rushed.  

### Example
We were asked by a client to develop a visualization of "weather" information.  Weather is a sufficiently broad problem space, so we met with experts and our client to elicit what information they hoped to communicate.  This helped us determine what data we might need to be visualize.  From this elicitation, we learned the important weather metrics were primarily the temperature and humidity.  By digging into the problem space in more detail, we were able to develop a small list of must-have metrics for the final visualization.

We are certain that you will encounter similar issues when dealing with data in a world where more is kept than is necessary.  Remember that turning data into information requires an understanding of the underlying problem otherwise you may end up creating amazing visualizations correlating the sales of cheese with engineering graduation rates.

In taking the time to develop even a working understanding of the problem, we also give ourselves a place to begin when we start reviewing the data.  

#### Questions to ask
1) What metrics are you currently tracking with the data?
2) Of the data that you are collecting (or have stored), what do you think is the most valuable? Why does this data provide value?
3) What story does the data tell?  
4) What questions do you want to answer using the data?

## Step 2.  Understanding the Data

In the same way that a rock climber needs to find the first ledge on which to place hand, you need an starting point from which you will begin playing with the data and building your visualization.  There has to be the "first" metric that is plotted or reviewed and when staring at a list of 100's of data columns; we need a tangible place to start.  From our experience, it is best to do this side-by-side with the client.  This can be a daunting task and is something we were shy about at first, but Tableau is on your side.  With a few simple filters and chart types you will be able to rapidly create visualizations that rival excel and you will earn their trust.  As we work with the client to understand the data, we are also starting to know them and their expectations for the product.  This will also give you something to work from once you are away from the client.

Since most clients are comfortable with Excel, we use Excel to look at data structures and organization whenever possible.  If we're working with data from databases, we try to get an understanding of which tables are important.  In either case, we build entity relationship diagrams to map the data location and relationships.  These almost always become a valuable discussion tools later when we're building and refining the visualization.

It is important to keep an eye on related datasets.  Tableau will help blend different datasets as long as there is information to merge on.  Particularly be cautious of geographic data blending unless it is by an identification number.

{Insert Picture Here}

## Step 3.  Understanding the Client

The perfect visualization for one client might be completely unacceptable for the next.  For that reason, we try and understand what each specific client is looking for from the visualization.  Some clients require tables of data; others only want colored charts.  We have found that asking clients what they want is not effective; we have had more success asking to see their current reports as well as charts and other visualizations they find useful.  These examples are a good starting point for development of the visualization.

## Step 4.  Understanding the Question

Okay.  Now that you have all that background information (problem space, data, client!), you are ready to understand the question.  We developed the following table, which we complete iteratively with the client until we fully capture what question they are trying to answer.

EXAMPLE table

Use Case | Reasoning | Explanation
----

Have you made it this far?  We know, we're not even to the fun stuff yet.  But this next step is, possibly, the keystone in the arch that is your data analysis and visualization project.  

## Step 5.  Formatting the Data

Your viz will fail if your data is not formatted correctly.  Well, that's not entirely true.  Without formatting your data properly, you can probably get your viz to about 80% of where you want it before you end up having to go back and reformat the data anyway.  The better you format your data before you begin, the easier it will be to build the viz and the better your viz will be in the end.  Ideally, you will format your data exactly how it needs to be for your viz before you start building it.  But that doesn't always happen.  Even with practice and experience, you may get pretty far in building your viz and then realize you need to reformat your data.  That's okay.  Learn from your mistakes and make better choices next time.  Or learn from ours:

A stacked dataset will work well for Tableau visualizations like the following:

(SHOW DATA AND VIZ EXAMPLE)

If the clients require visualizations like <Insert Viz>, the data must be unstacked.

<insert example>

To get data in the format we need, we use open source extract, transform, and load (ETL) tools like BLAH BLAH BLAH to transform database data.  When using Excel data, we often develop macros to reformat uncooperative worksheets.  Whenever possible, we convert the data to both a stacked and unstacked (see code, example, etc) version so both are available.  When you are working with data from two data formats or multiple sources, you can use Tableau's native connection feature to blend and connect data seamlessly.

Example?

Transforming data can always become a nightmare if the data becomes updated in the future.  For that reason, reformatting repeatability is extremely important.  This requires an understanding of all input files used, transformation techniques, and outputs.  The outputs should also be clearly labeled with some type of documentation indicating their source and a processing date.

If you take one thing from this section: Document the process and make it repeatable.  The only thing that is worse than having badly formatted data is to have the perfect data format with the perfect visualizations and then get a data update that you cannot process.

### Text vs xls vs db

Whenever possible, we like to use data from databases with Tableau.  When processing data in the weather example, we developed a script to read the raw weather files into a local sqlite database for processing.  Once in a database, we could easily join the with other types of information using Tableau's connection features.  These scripts are relatively simple and we provide an example at the conclusion to get you started.

If data has been reformatted from Excel or csv files and is relatively small, Excel might be the best option for data storage format.  Tabeleau can connect live to excel sheets, which makes updating and changing information extremely efficient for those used to the Excel environment. 


## Creating visualization

Finally!  We made it!  Once we've established a good data foundation, the fun can begin.  There are numerous tutorials fully detailing the complexities and possibilities of Tableau visualizations.  Using the details from above, we start constructing individual sheets to display the data.  These are generally higher level than appear to be useful at first but will become part of dashboards in the future.  

Actions and dashboard are created once the core visualization sheets are finished.  One or more core visualizations are placed on a sheet to tell a compelling story about the data.  Tableau differs from other tools because it works best when the visualizations are compartmentalized to dashboards.  Actions can be used to seamlessly transport the user between dashboards to visualize their data.  We have used this technique to show geographic relationships or to offer the ability for a user to "dig in".  In the geographic example, the client was interested in information at the city level but also needed something for the entire country.  Our solution was to create a colored country map that linked to a state level dashboard highlighting each city.  This action was immediate and allowed us to show more detailed information regarding the state and the selected cities.  We followed a similar approach to show what resources were available in the city.

<insert example gif>


## Publication

There are three primary methods of distributing a Tableau visualization, each of which has benefits that others do not.

### 1 Tableau Public
	- When you are using data that is less than 1,000,000 rows and is not proprietary, Tableau public can be an excellent option.  Through their public server, Tableau will store your data and host the visualization.  This can be easily embedded into websites to quickly share insights.

	However, there are limits to what can be done with the dashboard when you use Tableau public.  When the dashboard is created with the desktop version items like "view underlying data" are available; these are not available in the public version so additional design considerations must be taken into account if the user would like to see all underlying data.

	Pros: Completely free, easily sharable, very fast
	Cons: Data must be made public, data sizes must be relatively small.


### 2 Tableau Reader
	- Often data is not public and the insights gained from them are for a specific subset of people.  Tableau reader is a great option for this group because it allows each of them to review the data on their own computer, at their leisure, without an internet connection.  These workbooks don't have a true file size limit but in general, all data will be stored with the workbook so it is important to keep overall data size in mind.  We often describe this as an interactive PDF for a users data.
	Tableau reader has the same limitations as the public version with viewing all underlying data around a point.  This again should be taken into consideration when creating a workbook for other users.  Fortunately there is the ability to export data that is used to generate graphs and tables so users will still have some degree of access.

	Pros: All data stored within document, no internet connection required, also completely free to view data
	Cons: Data is not automatically updated for each user's workbook.  This can be a major disadvantage when it comes to rapidly changing data.


### 3 Tableau Desktop

	This is the same program used to create the original visualizations.  The users will end up seeing the workbook in the same way as it was created.  This can sometimes be a disadvantage because users may be tempted to pull in additional data or visualizations.  At times, this results in a user creating a "personalized workbook" that doesn't reflect the current development state.  These users may be able to add valuable insights if their workbook is reviewed often enough.

	Pros: Users will have the most control over the dashboard.  Anything that is done by the analyst can also be done by the end user.  Data can also be updated by the end user so this can be more easily used for rapidly changing datasets.
	Cons: Must pay the full license fee for any users who want to view the workbook.  This is generally $2k.  End users may also experience additional confusion with the workbook because they have more options.


### 4 Tableau Server
	When possible, Tableau server is the preferred deployment environment.  Once a user has access to Tableau server, they gain the ability to view data in nearly the same way as on the desktop version.  Their interface is generally a web browser but can also be through other devices such as an iPad.  When utilizing the web interface, the end user can also create comments and change portions of the dashboard.  This makes adding features far easier because comments can be shared between users rapidly.

	Pros: Automatic data updating.  Collaboration between groups
	Cons: High initial cost.  Additional fee for each new user



## Validation with use cases

The final step of any good visualization is to watch people interact with it who haven't seen it.  Often, after hours of creating graphs and understanding all of the background, things are understood that are not conveyed through the workbook.  We will use the set of questions that was developed at the beginning of the process with a fresh set of eyes to validate the logical nature of the workbook.  These sessions do not have to be long, most problems can be found within the first 15 minutes.

It is important to also validate with your final users.  It is possible that even with all of the prep work an erroneous assumption has been made.  Finding this before the visualization is fully deployed helps make sure others are able to get the information they need.

The results of this step drive the final step of refinements and then a dashboard can begin its life out in the wild.

## Endorsements and credits

Written by: Dan Skorski

This introduction has been read and edited by:


