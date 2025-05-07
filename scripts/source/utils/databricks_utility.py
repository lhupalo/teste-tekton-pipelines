import IPython
from pyspark.sql import SparkSession


class DatabricksUtility:
    """
    A utility class for managing Spark sessions and DBUtils in Databricks environments.
    """

    @staticmethod
    def get_spark() -> SparkSession:
        """
        Get or create a SparkSession.

        Returns
        -------
        SparkSession
            The SparkSession instance.
        """
        return SparkSession.builder.getOrCreate()

    @staticmethod
    def get_dbutils():
        """
        Get the DBUtils object in Databricks or IPython's `dbutils` in other environments.

        Returns
        -------
        DBUtils or IPython.db
            The DBUtils object or IPython's `dbutils`.
        """
        spark = DatabricksUtility.get_spark()
        if spark.conf.get("spark.databricks.service.client.enabled") == "true":
            from pyspark.dbutils import DBUtils

            return DBUtils(spark)
        else:
            return IPython.get_ipython().user_ns["dbutils"]
