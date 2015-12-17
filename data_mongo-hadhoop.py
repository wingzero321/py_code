# data_mongo-hadhoop.py

from pyspark import SparkContext, SparkConf


def main():
    conf = SparkConf().setAppName("pyspark test")
    sc = SparkContext(conf=conf)

    # Create an RDD backed by the MongoDB collection.
    # MongoInputFormat allows us to read from a live MongoDB instance.
    # We could also use BSONFileInputFormat to read BSON snapshots.
    rdd = sc.newAPIHadoopRDD(
        inputFormatClass='com.mongodb.hadoop.MongoInputFormat',
        keyClass='org.apache.hadoop.io.Text',
        valueClass='org.apache.hadoop.io.MapWritable',
        conf={
            'mongo.input.uri': 'mongodb://localhost:27017/db.collection'
        }
    )

    # Save this RDD as a Hadoop "file".
    # The path argument is unused; all documents will go to "mongo.output.uri".
    rdd.saveAsNewAPIHadoopFile(
        path='file:///this-is-unused',
        outputFormatClass='com.mongodb.hadoop.MongoOutputFormat',
        keyClass='org.apache.hadoop.io.Text',
        valueClass='org.apache.hadoop.io.MapWritable',
        conf={
            'mongo.output.uri': 'mongodb://localhost:27017/output.collection'
        }
    )

    # We can also save this back to a BSON file.
    rdd.saveAsNewAPIHadoopFile(
        path='hdfs://localhost:8020/user/spark/bson-demo',
        outputFormatClass='com.mongodb.hadoop.BSONFileOutputFormat',
        keyClass='org.apache.hadoop.io.Text',
        valueClass='org.apache.hadoop.io.MapWritable'
    )


if __name__ == '__main__':
    main()