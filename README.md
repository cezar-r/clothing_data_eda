# Data Analysis on Ecommerce Clothing Dataset
- This project takes a deep analytical dive into a dataset from an ecommerce site that contains features about their customers and sales. More info on the dataset can be found [here](https://cseweb.ucsd.edu/~jmcauley/datasets.html#market_bias).

## Data Insights
- The dataset consisted of 66,960 rows of data, with features such as Item ID's, User ID's, Ratings, User Attributes, Model Attributes, and even feedback based on how the clothing fit.

## Looking at Ratings
- One of the most important things in business is customer satisfaction. One metric that can quantify this is ratings given by the customers. More positive ratings = better customer satisfaction. Here is a plot of the overall frequency of ratings across this webstore.

<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Ratings.png" width = 450 height = 333>
As you can see, this webstore overall has very positive feedback, with over half of their overall ratings being a 5 star rating. The average rating also shows this to be true, with an average rating of 4.28 stars. <br /> <br />

## Fit Feedback
- Something that may indicate this very positive customer feedback is the fit of the clothing. On the chart below, we can see that most customers are happy with how the clothing they purchased fits.

<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Total_Fit_Feedback.png" width = 450 height = 330>

## Average Annual Rating
We can also analyze how the ratings have been over the years. The chart below shows the average rating for each year, and we can see that the ratings have been somewhat stagnant, however they have been very positive throughout the past 10 years.

<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Average_Rating_per_Year.png" width = 450 height = 330>

## Annual Count of Ratings
To get a sense of how popular this website is over the past few years, we can analyze the number of ratings it got each year. Below, we can see that the website peaked in popularity between 2013-2016. Since then, it has gotten a lot less reviews and has struggled to get anywhere near its peak years

<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/%23_of_Ratings_Each_Year.png" width = 450 height = 330> 

## Ratings per Product
Another rating-based analysis we can look at is the average rating per product. This dataset consisted of 152 unique items, so plotting them all would be too crowded. Instead, we can look at the ratings for the most popular products, as well as the least popular products.

### Ratings per Most Popular Products
- In the graph below, we can see that the 30 most popular products have an average rating well above the overall average rating, which gives some insight as to why these products are so popular. Popularity amongst the products was calculated by the total count of ratings they recieved.
<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Average_Ratings_per_Product_-_Most_Popular_Products_(30).png" width = 450 height = 300>

### Ratings per Least Popular Products
- The graph below shows the ratings for the 30 least popular products, which we can see that these products have about the same average of ratings as the most popular products.
<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Average_Ratings_per_Product_-_Least_Popular_Products_(30).png" width = 450 height = 300>

## Ratings per Category
- This graph shows the average rating per category. As we can see, all categories have about the same average rating.
<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Average_Ratings_per_Category.png" width = 450 height = 300>

- We can see the popularity of these categories by looking at the count of ratings each category has recieved. From this graph, we can that the most popular categories, by far, are Tops and Dresses
<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Total_Ratings_per_Category.png" width = 450 height = 300>

## Category Popularity Over Time
- This graph analyzes the popularity of each category, year-by-year. This graph also shows us that the website peaked in traffic between 2013-2016, and has since gotten a lot less reviews. It also shows that the two most dominant categories have always been dominant on their store, however Bottoms had a big boom 2015 which almost made them the most popular category for that year.

<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Category_Popularity_per_Year.png" width = 450 height = 330>

## Most Popular Months
- This graph shows the most popular months, again based on number of ratings recieved that month. We can see that the store gets more traffic later in the year, around holiday season.

<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Most_Popular_Months.png" width = 450 height = 330>

## User and Model Attributes
- Below are two graphs that show the frequency of both user and model attributes. 

<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Count_of_User_Attributes.png" width = 450 height = 330>

<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Count_of_Model_Attributes.png" width = 450 height = 330>

## Fit Feedback vs User Attributes
- Using the user attributes, we can analyze the fit feedback for each of the user attributes. We can see that the user attribute doesn't give us much of an indication on if the feedback will be good or not.

<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Fit_Feedback_vs_User_Attributes.png" width = 450 height = 330>

## Fit Feedback vs Model Attributes
- We can do the same based on the model attributes. Here, we can see that the proportion of feedback that is "Just Right" is much better when the model attributes are both Small and Large.
 
<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Fit_Feedback_vs_Model_Attributes.png" width = 450 height = 330>

## Summary
This webstore recieves a lot of positive ratings, with an average rating score of 4.28 out of 5. The feedback given on the clothes is also very positive, with just over 80% of the feedback saying the clothes fit just right. The best fit feedback is given when the model attributes are both small & large, most likely due to inclusivity. However, this store has not seen any increase in its ratings over the years and has also seen major dips in traffic since 2016. Now in terms of popularity within the store, its Tops and Dresses products are by far the most popular. This is also historically accurate, with these two categories being the most popular categories 7 out of the last 10 years. <br/> <br/>
This webstore should focus on its Tops and Dresses collections, especially right before September, and use models that are both small and large for the best feedback. Of course, it should first focus on getting much more overall traffic to its website.

## Technologies
- Pandas
- Numpy
- Matplotlib
