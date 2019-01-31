from cerebralcortex.cerebralcortex import CerebralCortex
from cerebralcortex.core.datatypes.datastream import DataStream
from cerebralcortex.core.metadata_manager.stream.metadata import Metadata, DataDescriptor, ModuleMetadata

from pprint import pprint
import pandas as pd
import json

CC = CerebralCortex("../../conf/")

filepath = '/Users/hnat/md2k/software/CerebralCortex-Kernel/cerebralcortex/examples/datafiles/accel.csv'
metadatapath = '/Users/hnat/md2k/software/CerebralCortex-Kernel/cerebralcortex/examples/datafiles/accel.json'

with open(metadatapath) as f:
    metadata = Metadata().from_json_file(f.read())

headers = ['timestamp']
headers.extend([dd.name.replace(' ','_') for dd in metadata.data_descriptor])

data = pd.read_csv(filepath, names=headers, index_col=False)
df = CC.sparkSession.createDataFrame(data)
datastream = DataStream(df, metadata)

CC.save_stream(datastream)

