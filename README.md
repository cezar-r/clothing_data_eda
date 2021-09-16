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

## Ratings per Product
Another rating-based analysis we can look at is the average rating per product. This dataset consisted of 152 unique items, so plotting them all would be too crowded. Instead, we can look at the ratings for the most popular products, as well as the least popular products.

### Ratings per Most Popular Products
- In the graph below, we can see that the 30 most popular products have an average rating well above the overall average rating, which gives some insight as to why these products are so popular. Popularity amongst the products was calculated by the total count of ratings they recieved.
<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Average_Ratings_per_Product_-_Most_Popular_Products_(30).png" width = 450 height = 300>

### Ratings per Least Popular Products
- The graph below shows the ratings for the 30 least popular products, which we can see that these products have a lower average of ratings compared to the overall average rating, which also gives some insight as to why these products are less popular.
<img src = "https://github.com/cezar-r/clothing_data_eda/blob/main/images/Average_Ratings_per_Product_-_Least_Popular_Products_(30).png" width = 450 height = 300>

## Ratings per Category
