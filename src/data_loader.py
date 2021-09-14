import pandas as pd 
from error_messages import *
import warnings


class Data:

	def __init__(self, auto_load = True) -> None:
		if auto_load:
			self.load_data()


	def load_data(self, 
				filename = '../data/modcloth_data.txt', 
				fill_na = False, 
				fill_symbol = None, 
				drop_na = True, 
				ignore_na = False, 
				column_drop_rate = .5,
				drop_cols = []) -> pd.DataFrame():
		# column_drop_rate = max ratio of NaN/Whole data in column needed to drop said column, between 0-1

		if (fill_na or drop_na or ignore_na) is not True:
			raise ArgumentError(f"At least one NaN argument must be true:\nfill_na = {fill_na}  drop_na = {drop_na}   ignore_na = {ignore_na}")
		if (fill_na and drop_na):
			raise ArgumentError(f"Both fill_na and drop_na arguments cannot be simultaneously true")

		if ignore_na:
			if drop_na:
				warnings.warn("Overriding drop_na as False, change ignore_na to False to avoid this\n")
			elif fill_na:
				warnings.warn("Overriding fill_na as False, change ignore_na to False to avoid this\n")
			drop_na = False
			fill_na = False

		try:
			self.dataframe = pd.read_csv(filename)
		except FileNotFoundError:
			raise FileNotFoundError(f"Could not locate {filename}")

		self._drop_columns(column_drop_rate, drop_cols)

		if drop_na:
			self.dataframe.dropna(inplace = True)
		elif fill_na:
			self.dataframe.fillna(fill_symbol, inplace = True)

		self.dataframe.reset_index(inplace = True)
		self.dataframe.drop('index', axis = 1, inplace = True)
		return self.dataframe

	def _drop_columns(self, rate, drop_cols):
		max_non_nans = 0
		for column in drop_cols:
			try:
				self.dataframe.drop(column, axis = 1, inplace = True)
			except KeyError:
				print((f"Couldn't find '{column}' column, continuing\n"))
				
		for column in self.dataframe.columns.values:
			if len(self.dataframe) - self.dataframe[column].isna().sum() > max_non_nans:
				max_non_nans = len(self.dataframe) - self.dataframe[column].isna().sum()
		for column in self.dataframe.columns.values:
			if self.dataframe[column].isna().sum() / max_non_nans > rate:
				self.dataframe.drop(column, axis = 1, inplace = True)
