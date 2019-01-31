from cerebralcortex.cerebralcortex import CerebralCortex
from cerebralcortex.core.datatypes.datastream import DataStream
from cerebralcortex.core.metadata_manager.stream.metadata import Metadata, DataDescriptor, ModuleMetadata

from pyspark.sql.functions import lit, hash, col

from pprint import pprint
import pandas as pd

CC = CerebralCortex("../../conf/")

#INPUTS
filepath = '/Users/hnat/md2k/software/CerebralCortex-Kernel/cerebralcortex/examples/datafiles/accel.csv'
metadatapath = '/Users/hnat/md2k/software/CerebralCortex-Kernel/cerebralcortex/examples/datafiles/accel.json'

#UUID is needed
user_uuid = 'ca4a8adc-7b64-4ba3-84a3-45c023660f38' # CC.get_user_id('test_user_1')

# The localtime offset is needed and data should be broken up by segments or the offset below needs to be applied
# differently
localtime_offset = -6 * 3600000

# Open the metadata file and pass it to the Metadata parser
with open(metadatapath) as f:
    metadata = Metadata().from_json_file(f.read())


# Header specification: [timestamp, value_0, value_1, ... value_n]
# and value_n is derived from the data_descriptor in the metadata object
# <spaces> are not allow and should be replaced with _s
headers = ['timestamp']
headers.extend([dd._name.replace(' ', '_') for dd in metadata.data_descriptor])

# Use pandas to read the CSV file with associated headers
data = pd.read_csv(filepath, names=headers, index_col=False)

# Use Spark to create a dataframe
df = CC.sparkSession.createDataFrame(data)

# Extend the data frame with the necessary columns to fit into Cerebral Cortex
# Add a 'localtime' column based on the offsets
# add the user column

# TODO: Can this be done automatically within the `save_stream` method or otherwise as part of CC
df = df.withColumn('localtime', col('timestamp') + localtime_offset).withColumn('user', lit(user_uuid))

# Create a datastream based on the Spark dataframe and metadata objects
datastream = DataStream(df, metadata)

# Store this data in the system
CC.save_stream(datastream)
