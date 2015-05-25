# Simple Data processing using PIG
This tutorial builds off of a hello world tutorial written by hortonworks.  Their original tutorial can be found here: http://hortonworks.com/hadoop-tutorial/hello-world-an-introduction-to-hadoop-hcatalog-hive-and-pig/.

I have taken their tutorial and made a few modifications so it is correct with their sandbox v 2.2.  I have also added a few additional analyses and explinations that I believe will make the concepts a bit easier to understand.


## Download the Sandbox
There are a number of great tutorials for installing the sandbox so I won't go into much detail.  The important bits are that you'll need some type of VM.  I use virtualbox because it works and because it is free.
https://www.virtualbox.org/wiki/Downloads

Then download the hortonworks sandbox.  I'm using version 2.2 for this tutorial.
http://hortonassets.s3.amazonaws.com/2.2.4/Sandbox_HDP_2.2.4.2_VirtualBox.ova


## Read in the csv file
*Note: This portion of the tutorial is taken almost directly from hortonworks.  I don't believe in re-inventing the wheel.*

### Grabbing some data
Hortonworks has a sample set of NYSE data located on amazonAWS.  You can download it through this link:
https://s3.amazonaws.com/hw-sandbox/tutorial1/NYSE-2000-2001.tsv.gz 

You can download the file directly onto the VM or onto the machine which is running the VM.  Hue (this is a front end that I will not cover in this totorial) gives you some very nice options for uploading data.

### Add the data to the system
Navigate you web browser of choice to 127.0.0.1:8000
Username: 'Hue'
Password: '1111'

Go to the File Browser at this address: 
http://127.0.0.1:8000/filebrowser/

You can also click on the icon in the menu bar.

### Upload the file to your user directory


### Bring the file into the catalog

We navigate over to HCatalog and create a new table for our data.  We have the option to name the table and stipulate where the data will come from.  

I've named the table nysedata but you can name it anything else as long as you change the reference on the first line of the PIG code below. 

Significantly more information regarding this process is on the hortonworks tutorial.  It is a useful read as the web interface allows you to see other things like table schema, previews, and databases in a clean area.  

## Create the PIG Script
The pig script can be created within the webframework but I prefer to use the command line.  It is just as easy, give more output, and offers more interactivity within the results.  Critically, it will allow you to describe each of the data objects as you define them to make sure you know what you are working with.

If you are using the sandbox simply login using putty 

	'127.0.0.1:2222' username 'root' password 'hadoop'.

Once you are at a command line you can start pig with the following command:

	'pig -useHCatalog'.

The option of useHCatalog is important because it will allow pig to use the catalogs that have been defined through the data import.  Without that option, the first line to load the dataset will fail.


### Load the dataset
I named the dataset nyse data.  You can confirm what you have named it by going to 127.0.0.1:8000 -> 

	dataset = LOAD 'nysedata' USING org.apache.hive.hcatalog.pig.HCatLoader();

running a describe on the dataset should show:

	dataset: {exchange: chararray,stock_symbol: chararray,date: chararray,stock_price_open: double,stock_price_high: double,stock_price_low: double,stock_price_close: double,stock_volume: long,stock_price_adj_close: double}

### Subset the data
When working with large datasets, it makes sense to subset as quickly as possible.  Our usecase is simply to find the average trade volume for each stock symbol so we'll subset immediately with the following code.

	subsetDataset = FOREACH dataset GENERATE stock_symbol, stock_volume;

Again, if we describe we should see the following:
	subsetDataset: {stock_symbol: chararray,stock_volume: long}

### Group the data by symbols
	
	groupedDataset = GROUP subsetDataset BY stock_symbol;

Results of describe:

	groupedDataset: {group: chararray,subsetDataset: {(stock_symbol: chararray,stock_volume: long)}}

Note how this data is stored.  There is a group with the individual stock_symbol and then all of the resulting data that applies to the group.  If we were to look at the head of the groupedDataset we should see something like the following:

	{group: AAPL, 
		subsetDataset: 
			{(stock_symbol: APPL, stock_volume: 23423), 
			(stock_symbol: APPL, stock_volume: 553345), 
			(stock_symbol: APPL, stock_volume: 456477), 
			(stock_symbol: APPL, stock_volume: 664522), 
			(stock_symbol: APPL, stock_volume: 36321)}}

### Iterate to get average
This is referred to as a Nested Projection.  We iterate over the groupedDataset but need to reach into the subsetDataset to find the stock volumes to average.  To reach into a subset we use . notation.  
It is important to know which stock symbol we have calculated the average for so we add the group to the end.  This is the same group that is shown in the describe of the step above.

	outputDataset = FOREACH groupedDataset GENERATE AVG(subsetDataset.stock_volume), group;

Results of Describe:

	outputDataset: {double,group: chararray}

### Wrapping up with PIG
At this point the output can be dumped to the screen.  The following command will actually run the complete job.

	dump outputDataset;

This will show all of the results to the screen as well as a log of what is going on with the file.

It is more likely that we would want this file someplace else so we could work with it.  

	STORE outputDataset INTO '/user/nyseaverages.csv' USING CSVExcelStorage(',', 'NO_MULTILINE', 'WINDOWS');

At this point, we can follow the same import procedure as above to get the file into the HCatalog so we could query the data with our favorite analysis program (R, Tableau, Python, etc.).

Note that if the outputDataset is dumped, it cannot also be stored.  You'll have to switch the order if you would like to do both operations.

## Conclusion

This seems like a ton of work to do something that could be done in R or Python in a few minutes but remember, this is SCALABLE.  This dataset only has 800,000 rows.  What if we had all of the data for all years?  Increasing the data by multiple orders of magnitude doesn't require any changes to the code.  This gives us the best of both worlds, a small test environment as well as a fully scalable solution that doesn't require any changes to our process.