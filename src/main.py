#!/usr/bin/env python
# coding: utf-8

'''
Main file from which data visualization is done.
'''

from data_loader import Data
from eda import EDA


def main():
	d = Data()
	df = d.dataframe
	# or
	# d = Data(auto_load = False)
	# df = d.load_data()
	
	eda = EDA(df)
	eda.ratings_counts()
	# eda.ratings_counts()

	'''
	# plots average rating for each of the 30 most popular products (in terms of rating counts)
	eda.ratings_per_product_most_popular()

	# plots average rating for each of the 30 least popular products (in terms of rating counts)
	eda.ratings_per_product_least_popular()

	# plots number of ratings for the 30 most popular products (in terms of rating counts)
	eda.ratings_count_per_product_most_popular()

	# plots number of ratings for the 30 least popular products (in terms of rating counts)
	eda.ratings_count_per_product_least_popular()

	# plots average rating per product category
	eda.ratings_per_category()

	# plots number of ratings per category
	eda.rating_count_per_category()

	# plots average rating year by year
	eda.rating_per_year()

	# plots count of different fit feedbacks
	eda.fit_feedback()

	# plots count of different user attributes
	eda.user_attributes()

	# plots count of different model attributes
	eda.model_attributes()

	# plots the fit feedback based on the two different model attributes
	eda.fit_feedback_vs_model_attribute()

	# plots the fit feedback based on the two different user attributes
	eda.fit_feedback_vs_user_attribute()
	'''

if __name__ == '__main__':
	main()
