from data_loader import Data
from eda import EDA


def main():
	d = Data()
	df = d.dataframe
	# d = Data(auto_load = False)
	# df = d.load_data()
	
	eda = EDA(df)
	eda.ratings_per_product_most_popular()
	eda.ratings_per_product_least_popular()
	eda.ratings_count_per_product_most_popular()
	eda.ratings_count_per_product_least_popular()
	eda.ratings_per_category()
	eda.rating_count_per_category()
	eda.rating_per_year()
	eda.fit_feedback()
	eda.user_attributes()
	eda.model_attributes()
	eda.fit_feedback_vs_model_attribute()
	eda.fit_feedback_vs_user_attribute()



if __name__ == '__main__':
	main()
