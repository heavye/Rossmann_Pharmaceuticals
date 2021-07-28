import numpy as np
import pandas as pd
from helper import MyHelper


class MyCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
        print('Cleaning ...')

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df.drop_duplicates(inplace=True)

        return df

    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert column to datetime
        """

        df['start'] = pd.to_datetime(
            df['start'])
        df['end'] = pd.to_datetime(
            df['end'])

        return df

    def drop_columns_with_null_values(self, df: pd.DataFrame, threshold_in_percent=30) -> pd.DataFrame:
        Helper = MyHelper()

        null_percent_df = pd.DataFrame(columns=['column', 'null_percent'])
        columns = df.columns.values.tolist()

        null_percent_df['column'] = columns
        null_percent_df['null_percent'] = null_percent_df['column'].map(
            lambda x: Helper.percent_missing_for_col(df, x))

        columns_to_be_dropped = null_percent_df[null_percent_df['null_percent']
                                                > threshold_in_percent]['column'].to_list()
        df = self.__drop_columns(df, columns_to_be_dropped)

        return df

    def drop_rows_with_null_values(self, df: pd.DataFrame, threshold_in_percent=1) -> pd.DataFrame:
        Helper = MyHelper()

        null_percent_df = pd.DataFrame(columns=['column', 'null_percent'])
        columns = df.columns.values.tolist()

        null_percent_df['column'] = columns
        null_percent_df['null_percent'] = null_percent_df['column'].map(
            lambda x: Helper.percent_missing_for_col(df, x))
        
        columns_subset = null_percent_df[null_percent_df['null_percent']
                                         < threshold_in_percent]['column'].to_list()

        df = df.dropna(subset=columns_subset)

        return df

    def handle_missing_qantitative_data_with_mean(self, df: pd.DataFrame, method="mean"):

        numeric_data = ['int16', 'int32', 'int64',
                        'float16', 'float32', 'float64']

        all_cols = df.columns.to_list()
        num_cols = [c for c in all_cols if df[c].dtypes in numeric_data]

        if (method == "mean"):

            for col in num_cols:
                df[col] = df[col].fillna(df[col].mean())

            return df

        elif method == "ffill":

            for col in num_cols:
                df[col] = df[col].fillna(method='ffill')

            return df

        elif method == "bfill":

            for col in num_cols:
                df[col] = df[col].fillna(method='bfill')

            return df
        else:
            print("Method unknown")
            return df
    
    def handle_missing_categorical_data_with(self, df: pd.DataFrame, method="ffill"):

        numeric_data = ['int16', 'int32', 'int64',
                        'float16', 'float32', 'float64']

        all_cols = df.columns.to_list()
        num_cols = [c for c in all_cols if not df[c].dtypes in numeric_data]
        
        if method == "ffill":

            for col in num_cols:
                df[col] = df[col].fillna(method='ffill')

            return df

        elif method == "bfill":

            for col in num_cols:
                df[col] = df[col].fillna(method='bfill')

            return df
        else:
            print("Method unknown")
            return df

    def handle_outliers(self, df, col):
        df = df.copy()
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        lower_bound = q1 - ((1.5) * (q3 - q1))
        upper_bound = q3 + ((1.5) * (q3 - q1))

        df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
        df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])

        return df

    #Treating the outliers 
    # a function for replacing outliers with the median, used when there's too many outliers in a feature
    def replace_outlier_with_median(dataFrame, feature):
        Q1 = dataFrame[feature].quantile(0.25)
        Q3 = dataFrame[feature].quantile(0.75)
        median = dataFrame[feature].quantile(0.50)

        IQR = Q3 - Q1

        upper_whisker = Q3 + (1.5 * IQR)
        lower_whisker = Q1 - (1.5 * IQR)

        dataFrame[feature] = np.where(dataFrame[feature] > upper_whisker, median, dataFrame[feature])
        dataFrame[feature] = np.where(dataFrame[feature] < lower_whisker, median, dataFrame[feature])
        return 
        
    def __drop_columns(self, df, columns=[]):

        return df.drop(columns, axis=1)