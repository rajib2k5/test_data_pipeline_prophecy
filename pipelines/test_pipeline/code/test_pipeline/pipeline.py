from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test_pipeline.config.ConfigStore import *
from test_pipeline.udfs.UDFs import *
from prophecy.utils import *
from test_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/test_pipeline")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/test_pipeline")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
