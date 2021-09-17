#!/usr/bin/env python
# coding: utf-8

'''
File containing the EDA object, which contains several methods for various analytics
Most analytics are done through two private functions: _plotting_helper() and _attributes_helper
'''

import numpy as np 
import matplotlib.pyplot as plt 


class EDA:
	"""Object that is used for the main data analytics"""

	def __init__(self, data, save_images = True, style = "dark_background"):
		plt.style.use(style)
		self.data = data
		self.save_img = save_images


	def ratings_counts(self, show_total = True, show_avg = True):
		"""Plots count of each rating

		Parameters
		----------
		show_total: bool 		display total ratings along with title
		show_avg: bool 			display average rating along with title
		"""
		counts = self.data.rating.value_counts()
		title = 'Ratings'
		og_title_text = title
		if show_total:
			title += f'\nTotal: {sum(counts.values)}'
		if show_avg:
			title += f'\nAverage: {round(np.mean(self.data.rating.values), 2)}'

		fig, ax = plt.subplots()

		ax.bar(counts.index.values, counts.values)
		ax.set_title(title)
		ax.set_ylabel("Count")
		ax.set_xlabel("Rating")
		plt.tight_layout()
		if self.save_img:
			plt.savefig(f'../images/{og_title_text.replace(" ", "_")}.png')
		else:
			plt.show()


	def _sort_two_lists(self, arr_idx, x, y):
		"""Helper function that sorts two list based on the order of one list

		Parameters
		----------
		arr_idx: int 			the array who's sorted order is going to dictate the order of the other array
		x: arr 					one of the arrays being sorted
		y: arr 					one of the arrays being sorted
		"""
		zipped_lists = zip(x, y)
		sorted_pairs = sorted(zipped_lists, key = lambda x: x[arr_idx])
		tuples = zip(*sorted_pairs)
		x, y = [list(tuple) for tuple in tuples]
		return x, y


	def _plotting_helper(self, show, grouping_column, title_text, xlabel = '', mean = True, reverse = False, sortx = False, sorty = True):
		"""Helper function that handles most of the plotting

		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		grouping_column: str 	column that is being analyzed
		title_text: str 		title for the graph
		xlabel: str 			label for x-axis
		mean: bool 				if true, the mean of the y-values will be plotted. otherwise, the count will be plotted
		reverse: bool 			if true, the values for the x-axis are flipped. mainly used for least_popular_product methods
		sortx: bool				if true, bars will be sorted based on x-values
		sorty: bool 			if true, bars will be sorted based on y-values
		"""
		if reverse:
			item_ids = self.data[grouping_column].value_counts().index.values[::-1][:show]
		else:
			item_ids = self.data[grouping_column].value_counts().index.values[:show]

		x = []
		y = []

		items_group = self.data.groupby(grouping_column)
		for _id in item_ids:
			for _item_id, table in items_group:
				if _id == _item_id:
					x.append(str(_id))
					if mean:
						ylabel = 'Rating'
						y.append(table.rating.mean())
					else:
						ylabel = 'Count'
						y.append(table.rating.count())

		if sorty:
			x, y, = self._sort_two_lists(1, x, y)
		elif sortx:
			x, y, = self._sort_two_lists(0, x, y)

		og_title_text = title_text
		if len(x) > 2:
			title_text += f'\nAverage - {round(np.mean(y), 2)}'
		if len(x) > 20:
			fig, ax = plt.subplots(figsize = (len(x) / 3, 5))
		else:
			fig, ax = plt.subplots()

		if xlabel == '':
			xlabel = str(grouping_column.title())

		ax.set_title(title_text)
		ax.set_xlabel(xlabel)
		ax.set_ylabel(ylabel)
		ax.bar(x, y)
		ax.set_xticklabels(x, rotation = 45)
		plt.tight_layout()
		if self.save_img:
			plt.savefig(f'../images/{og_title_text.replace(" ", "_")}.png')
		else:
			plt.show()


	def _attributes_helper(self, grouping_column, title_text, scaled = False):
		"""Helper function that handles multi-bar plotting

		Parameters
		----------
		grouping_column: str 	column that is being analyzed
		title_text: str 		title for the graph
		scaled: bool 			if true, the two bar plots will be scaled based on their maximum values
		"""
		feedback_dict = {}
		item_ids = list(self.data['fit'].value_counts().index.values)
		items_group = self.data.groupby(grouping_column)

		for _id, table in items_group:
			fit_counts = table['fit'].value_counts()
			for count in fit_counts:
				if _id in feedback_dict:
					feedback_dict[_id].append(count)
				else:
					feedback_dict[_id] = [count]

		if scaled:
			for k in feedback_dict:
				feedback_dict[k] = [i/max(feedback_dict[k]) for i in feedback_dict[k]]

		x = np.arange(len(item_ids))
		width = .35
		item_ids.insert(0, item_ids[0])

		fig, ax = plt.subplots() # had to instantiate plot this way to be able to edit xticks w strings
		ax.bar(x - width/2, list(feedback_dict.values())[0], width, label = list(feedback_dict.keys())[0])
		ax.bar(x + width/2, list(feedback_dict.values())[1], width, label = list(feedback_dict.keys())[1])
		ax.set_xticklabels(item_ids, rotation = 45)
		ax.set_title(title_text)
		ax.legend()
		ax.set_xlabel("Feedback")
		ax.set_ylabel("Counts")
		plt.tight_layout()
		if self.save_img:
			plt.savefig(f'../images/{title_text.replace(" ", "_")}.png')
		else:
			plt.show()


	def _month_to_string(self, x):
		"""Converts string between 01 - 12 to month

		Parameters
		----------

		x: str 					string to be converted to month
		"""
		month_hash = {'01' : 'January',
					'02' : 'February',
					'03' : 'March',
					'04' : 'April',
					'05' : 'May',
					'06' : 'June',
					'07' : 'July',
					'08' : 'August',
					'09' : 'September',
					'10' : 'October',
					'11' : 'Novemeber',
					'12' : 'December'}
		return month_hash[x]


	def category_popular_per_year(self):
		"""Plots the number of ratings each category got each year"""
		categories_dict = {}
		x = []
		grouped_categories = self.data.groupby('category')
		grouped_years = self.data.groupby('year')
		for cat, cat_table in grouped_categories:
			for year, year_table in grouped_years:
				if cat in categories_dict:
					categories_dict[cat].append(year_table['category'][year_table['category'] == cat].count())
				else:
					categories_dict[cat] = [year_table['category'][year_table['category'] == cat].count()]
				if year not in x:
					x.append(year)
		
		fig, ax = plt.subplots(figsize = (12, 6))
		ax.set_title('Category Popularity per Year')
		ax.set_xlabel('Year')
		ax.set_ylabel('Count')
		for k in categories_dict:
			ax.plot(x, categories_dict[k], label = k)
		plt.legend()

		if self.save_img:
			plt.savefig('../images/Category_Popularity_per_Year.png')
		else:
			plt.show()


	def most_popular_months(self):
		"""Plots the most popular months, on average"""
		copy = self.data 
		copy['timestamp'] = copy['timestamp'].apply(lambda x : x[5:7])
		months_grouped = copy.groupby('timestamp')
		del copy

		x = []
		y = []
		for month, month_table in months_grouped:

			x.append(self._month_to_string(month))
			y.append(month_table.rating.count())

		fig, ax = plt.subplots(figsize = (12, 5))
		ax.set_title('Most Popular Months')
		ax.set_xlabel('Month')
		ax.set_xticklabels(x, rotation = 45)
		ax.set_ylabel('Count of Ratings')
		ax.bar(x, y)
		plt.tight_layout()

		if self.save_img:
			plt.savefig('../images/Most_Popular_Months.png')
		else:
			plt.show()


	def ratings_per_product_most_popular(self, show = 30):
		"""Plots average rating for each of the 30 most popular products (in terms of rating counts)
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'item_id', title_text = f'Average Ratings per Product - Most Popular Products ({show})', xlabel = 'Product ID', sorty = False)


	def ratings_per_product_least_popular(self, show = 30):
		"""Plots average rating for each of the 30 least popular products (in terms of rating counts)
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'item_id', title_text = f'Average Ratings per Product - Least Popular Products ({show})', xlabel = 'Product ID', reverse = True, sorty = False)


	def ratings_count_per_product_most_popular(self, show = 30):
		"""Plots number of ratings for the 30 most popular products (in terms of rating counts)
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'item_id', title_text = f'Total Ratings per Product - Most Popular Products ({show})', xlabel = 'Product ID',  mean = False, sorty = False)


	def ratings_count_per_product_least_popular(self, show = 30):
		"""Plots number of ratings for the 30 least popular products (in terms of rating counts)
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'item_id', title_text = f'Total Ratings per Product - Least Popular Products ({show})', xlabel = 'Product ID', mean = False, reverse = True)


	def ratings_per_category(self, show = 4):
		"""Plots average rating per product category
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'category', title_text = 'Average Ratings per Category')


	def rating_count_per_category(self, show = 4):
		"""Plots number of ratings per category
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'category', title_text = 'Total Ratings per Category', mean = False)


	def rating_per_year(self, show=10):
		"""Plots average rating year by year
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'year', title_text = 'Average Rating per Year', sortx = True, sorty = False)


	def rating_count_per_year(self, show = 10):
		"""Plots the number of ratings year by year

		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'year', '# of Ratings Each Year', mean = False, sortx = True, sorty = False)


	def fit_feedback(self, show = 5):
		"""Plots count of different fit feedbacks
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'fit', title_text = 'Total Fit Feedback', xlabel = 'Feedback', mean = False)


	def user_attributes(self, show = 2):
		"""Plots count of different user attribute
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'user_attr', title_text = 'Count of User Attributes', xlabel = 'Attributes', mean = False)


	def model_attributes(self, show = 2):
		"""Plots count of different model attributes
		
		Parameters
		----------
		show: int 				number of bars to be displayed on chart
		"""
		self._plotting_helper(show, 'model_attr', title_text = 'Count of Model Attributes', xlabel = 'Attributes', mean = False)


	def fit_feedback_vs_model_attribute(self, scaled = False):
		"""Plots the fit feedback based on the two different model attributes
		
		Parameters
		----------
		scaled: bool			if true, the two bar plots will be scaled based on their maximum values
		"""
		self._attributes_helper("model_attr", title_text = 'Fit Feedback vs Model Attributes', scaled = scaled)


	def fit_feedback_vs_user_attribute(self, scaled = False):
		"""Plots the fit feedback based on the two different user attributes
		
		Parameters
		----------
		scaled: bool 			if true, the two bar plots will be scaled based on their maximum values
		"""
		self._attributes_helper("user_attr", title_text = 'Fit Feedback vs User Attributes', scaled = scaled)
