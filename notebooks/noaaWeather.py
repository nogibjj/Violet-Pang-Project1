# Databricks notebook source
import pyspark.pandas

# COMMAND ----------

from azureml.opendatasets import NoaaIsdWeather

# COMMAND ----------

from datetime import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta

# COMMAND ----------

# Set start_date and end_date.
# Start a new instance of NoaaIsdWeather
# Call to_pandas_dataframe() method to get a pandas DataFrame.
start_date = parser.parse('2021-1-1')
end_date = parser.parse('2021-2-28')
isd = NoaaIsdWeather(start_date, end_date)
isd.to_pandas_dataframe().info()
print('isd done')

# COMMAND ----------

df = isd.to_pandas_dataframe()


# COMMAND ----------

display(df.head(4))

# COMMAND ----------

