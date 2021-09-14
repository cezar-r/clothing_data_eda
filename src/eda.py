import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

class EDA:

	def __init__(self, data, style = "dark_background"):
		plt.style.use(style)
		self.data = data


	def ratings_counts(self, show_total = True, show_avg = True):
		counts = self.data.rating.value_counts()
		plt.bar(counts.index.values, counts.values)
		title = 'Ratings'
		if show_total:
			title += f'\nTotal: {sum(counts.values)}'
		if show_avg:
			title += f'\nAverage: {round(np.mean(self.data.rating.values), 2)}'
		plt.title(title)
		plt.ylabel("Count")
		plt.xlabel("Rating")
		plt.tight_layout()
		plt.show()


	def _plotting_helper(self, show, grouping_column, title_text, xlabel, mean = True, reverse = False, sort = True, save_img = True):
		if reverse:
			item_ids = self.data[grouping_column].value_counts().index.values[::-1][:show]
		else:
			item_ids = self.data[grouping_column].value_counts().index.values[:show]
		x = []
		y = []

		items_group = self.data.groupby(grouping_column)
		for _id, table in items_group:
			if _id in item_ids:
				x.append(str(_id))
				if mean:
					y.append(table.rating.mean())
				else:
					y.append(table.rating.count())

		if sort:
			zipped_lists = zip(x, y)
			sorted_pairs = sorted(zipped_lists, key = lambda x: x[1])
			tuples = zip(*sorted_pairs)
			x, y = [list(tuple) for tuple in tuples]

		og_title_text = title_text

		title_text += f' ({len(x)})\nAverage - {round(np.mean(y), 2)}'
		if len(x) > 20:
			plt.figure(figsize = (len(x) / 3, 5))

		fig, ax = plt.subplots()
		ax.set_title(title_text)
		ax.set_xlabel(xlabel)
		ax.set_ylabel('Rating')
		ax.bar(x, y)
		ax.set_xticklabels(x, rotation = 45)
		plt.tight_layout()
		if save_img:
			plt.savefig(f'../images/{og_title_text.replace(" ", "_")}.png')
		else:
			plt.show()


	def _attributes_helper(self, grouped_column, scaled, title_text, save_img = True):
		feedback_dict = {}
		item_ids = list(self.data['fit'].value_counts().index.values)
		items_group = self.data.groupby(grouped_column)

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

		og_title_text = title_text


		fig, ax = plt.subplots() # had to instantiate plot this way to be able to edit xticks w strings
		ax.bar(x - width/2, list(feedback_dict.values())[0], width, label = list(feedback_dict.keys())[0])
		ax.bar(x + width/2, list(feedback_dict.values())[1], width, label = list(feedback_dict.keys())[1])
		ax.set_xticklabels(item_ids, rotation = 45)
		ax.set_title(title_text)
		ax.legend()
		ax.set_xlabel("Feedback")
		ax.set_ylabel("Counts")
		plt.tight_layout()
		if save_img:
			plt.savefig(f'../images/{og_title_text.replace(" ", "_")}.png')
		else:
			plt.show()


	def ratings_per_product_most_popular(self, show = 50):
		self._plotting_helper(show, 'item_id', title_text = 'Average Ratings per Product - Most Popular Products', xlabel = 'Product ID', mean = True, reverse = False)

	def ratings_per_product_least_popular(self, show = 50):
		self._plotting_helper(show, 'item_id', title_text = 'Average Ratings per Product - Least Popular Products', xlabel = 'Product ID', mean = True, reverse = True)

	def ratings_count_per_product_most_popular(self, show = 50):
		self._plotting_helper(show, 'item_id', title_text = 'Total Ratings per Product - Most Popular Products', xlabel = 'Product ID',  mean = False, reverse = False)

	def ratings_count_per_product_least_popular(self, show = 50):
		self._plotting_helper(show, 'item_id', title_text = 'Total Ratings per Product - Least Popular Products', xlabel = 'Product ID', mean = False, reverse = True)

	def ratings_per_category(self, show = 4):
		self._plotting_helper(show, 'category', title_text = 'Average Ratings per Category', xlabel = 'Category', mean = True, reverse = False)

	def rating_count_per_category(self, show = 4):
		self._plotting_helper(show, 'category', title_text = 'Total Ratings per Product', xlabel = 'Category', mean = False, reverse = False)

	def rating_per_year(self, show=10):
		self._plotting_helper(show, 'year', title_text = 'Average Rating per Year', xlabel = 'Year', mean = True, sort = False)

	def fit_feedback(self, show = 5):
		self._plotting_helper(show, 'fit', title_text = 'Total Fit Feedback', xlabel = 'Feedback', mean = False)

	def user_attributes(self, show = 2):
		self._plotting_helper(show, 'user_attr', title_text = 'Count of User Attributes', xlabel = 'Attributes', mean = False)

	def model_attributes(self, show = 2):
		self._plotting_helper(show, 'model_attr', title_text = 'Count of Model Attributes', xlabel = 'Attributes', mean = False)

	def fit_feedback_vs_model_attribute(self, scaled = False):
		self._attributes_helper("model_attr", scaled, title_text = 'Fit Feedback vs Model Attributes')

	def fit_feedback_vs_user_attribute(self, scaled = False):
		self._attributes_helper("user_attr", scaled, title_text = 'Fit Feedback vs User Attributes')