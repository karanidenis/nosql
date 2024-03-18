### Nosql

- Nosql is a database that provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases.
- Nosql databases are increasingly used in big data and real-time web applications.
- Nosql systems are also sometimes called "Not only SQL" to emphasize that they may support SQL-like query languages or sit alongside SQL databases in polyglot-persistent architectures.
- Nosql databases are often very fast, do not require fixed table schemas, avoid join operations by storing denormalized data, and are designed to scale horizontally.
- The most popular Nosql databases are MongoDB, CouchDB, Redis, RavenDB, Cassandra, HBase, Neo4j, and Couchbase.

### MongoDB

- MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.
- MongoDB is a distributed database at its core, so high availability, horizontal scaling, and geographic distribution are built in and easy to use.
- MongoDB is free and open-source, published under the GNU Affero General Public License.

### MongoDB vs SQL

- SQL databases are primarily called as Relational Databases (RDBMS); whereas NoSQL database are primarily called as non-relational or distributed database.
- SQL databases are table based databases whereas NoSQL databases are document based, key-value pairs, graph databases or wide-column stores.
- SQL databases have a predefined schema whereas NoSQL databases have a dynamic schema for unstructured data.
- SQL databases are vertically scalable whereas the NoSQL databases are horizontally scalable.
- SQL databases uses SQL ( structured query language ) for defining and manipulating the data, which is very powerful. In NoSQL database, queries are focused on collection of documents.
- SQL database examples: MySql, Oracle, Sqlite, Postgres and MS-SQL. NoSQL database examples: MongoDB, BigTable, Redis, RavenDb, Cassandra, Hbase, Neo4j and CouchDb.
- For complex queries: SQL databases are good fit for the complex query intensive environment whereas NoSQL databases are not good fit for complex queries.
- For the type of data to be stored: SQL databases are not best fit for hierarchical data storage. But, NoSQL database fits better for the hierarchical data storage as it follows the key-value pair way of storing data similar to JSON data. NoSQL database are highly preferred for large data set (i.e for big data).
- For scalability: In most typical situations, SQL databases are vertically scalable. You can manage increasing load by increasing the CPU, RAM, SSD, etc, on a single server. On the other hand, NoSQL databases are horizontally scalable. You can just add few more servers easily in your NoSQL database infrastructure to handle the large traffic.
- For high transactional based application: SQL databases are best fit for heavy duty transactional type applications, as it is more stable and promises the atomicity as well as integrity of the data. While you can use NoSQL for transactions purpose, it is still not comparable and sable enough in high load and for complex transactional applications.
- For support: Support is one of the main issue with the NoSQL databases. There are very less support available for NoSQL compared to the well defined support available for SQL database.

### MongoDB Shell

- MongoDB shell is an interactive JavaScript interface to MongoDB, which provides a powerful interface for system administrators as well as a way for developers to test queries and operations directly with the database.

### MongoDB CRUD Operations

- CRUD stands for Create, Read, Update, and Delete. These are the four basic functions of persistent storage. Also, sometimes you may see U as a synonym for Retrieve, Read, or Select.
- MongoDB provides the following methods to perform CRUD operations:
  - db.collection.insertOne() - This method is used to insert a single document into a collection.
  - db.collection.insertMany() - This method is used to insert multiple documents into a collection.
  - db.collection.find() - This method is used to select documents in a collection and returns a cursor to the selected documents.
  - db.collection.updateOne() - This method is used to update a single document within the collection.
  - db.collection.updateMany() - This method is used to update multiple documents within the collection.
  - db.collection.deleteOne() - This method is used to delete a single document from a collection.
  - db.collection.deleteMany() - This method is used to delete multiple documents from a collection.

### MongoDB Data Types

- MongoDB supports many data types. Some of the most commonly used data types are:
  - String: This is the most commonly used datatype to store the data. String in MongoDB must be UTF-8 valid.
  - Integer: This type is used to store a numerical value. Integer can be 32 bit or 64 bit depending upon your server.
  - Boolean: This type is used to store a boolean (true/ false) value.
  - Double: This type is used to store floating point values.
  - Min/ Max keys: This type is used to compare a value against the lowest and highest BSON elements.
  - Arrays: This type is used to store arrays or list or multiple values into one key.
  - Timestamp: Timestamp is used to store current date time.
  - Object: This datatype is used for embedded documents.
  - Null: This type is used to store a Null value.
  - Symbol: This datatype is used identically to a string; however, it's generally reserved for languages that use a specific symbol type.
  - Date: This datatype is used to store the current date or time in UNIX time format. You can specify your own date time by creating object of Date and passing day, month, year into it.
  - Object ID: This datatype is used to store the document’s ID.
  - Binary data: This datatype is used to store binary data.
  - Code: This datatype is used to store JavaScript code into the document.
  - Regular expression: This datatype is used to store regular expression.

### MongoDB Indexing

- Indexes support the efficient resolution of queries. Without indexes, MongoDB must perform a collection scan, i.e. scan every document in a collection, to select those documents that match the query statement. If an appropriate index exists for a query, MongoDB can use the index to limit the number of documents it must inspect.
- MongoDB supports several types of indexes:
  - Single Field: This index is used to create an index on a single field.
  - Compound Index: This index is used to create an index on multiple fields.
  - Multikey Index: This index is used to index the content stored in arrays.
  - Text Index: This index is used to index the content stored in string fields.
  - Hashed Index: This index is used to hash the value of the indexed field.

### MongoDB Aggregation

- Aggregation operations process data records and return computed results. Aggregation operations group values from multiple documents together, and can perform a variety of operations on the grouped data to return a single result.
  - $project: This is used to select some specific fields from a collection.
  - $match: This is a filtering operation and thus this can reduce the amount of documents that are given as input to the next stage.
  - $limit: This is used to limit the number of documents.
  - $skip: This is used to skip a number of documents.
  - $unwind: This is used to unwind document that are using arrays.
  - $group: This is used to group documents.
  - $sort: This is used to sort documents.
  - $geoNear: This is used to return an ordered list of documents based on the proximity to a geospatial point.
  - $out: This is used to write the result of the aggregation query to a new collection or view.
  - $lookup: This is used to perform a left outer join to another collection in the same database to filter in documents from the "joined" collection for processing.
  - $facet: This is used to process multiple aggregation pipelines within a single stage on the same set of input documents.
  - $graphLookup: This is used to perform a recursive search on a collection.
  - $addFields: This is used to add new fields to the document.
  - $replaceRoot: This is used to replace the input document with the specified document.

### MongoDB Sharding

- Sharding is a method for distributing data across multiple machines. MongoDB uses sharding to support deployments with very large data sets and high throughput operations.
- Sharding is the process of storing data records across multiple machines and is MongoDB’s approach to meeting the demands of data growth. As the size of the data increases, a single machine may not be sufficient to store the data nor provide an acceptable read and write throughput. Sharding solves the problem with horizontal scaling. With sharding, you add more machines to support data growth and the demands of read and write operations.
  - Shard: This is the server that stores the data.
  - Mongos: This is the routing service for the sharded cluster. It routes the client requests to the appropriate shard.
  - Config Server: This is the server that stores the metadata of the sharded cluster.
  - Shard Key: This is the key that is used to distribute the data across the shards.
  - Chunk: This is the range of data that is stored in a shard.
  - Balancer: This is the process that balances the data across the shards.
  - Zone: This is the range of data that is stored in a shard.
  - Tag: This is the label that is used to tag the data.
  - Hashed Sharding: This is the sharding method that uses a hashed shard key.

### MongoDB Replication

- Replication is the process of synchronizing data across multiple servers. Replication provides redundancy and increases data availability. With multiple copies of data on different database servers, replication provides a level of fault tolerance against the loss of a single database server.
  - Primary: This is the main server that receives all write operations.
  - Secondary: This is the server that replicates the data from the primary server.
  - Arbiter: This is the server that is used to break the tie in the election of the primary server.
  - Oplog: This is the log that records all the operations that are performed on the primary server.
  - Replica Set: This is the group of servers that maintain the same data set.
  - Read Preference: This is the way to specify from which server to read the data.
  - Write Concern: This is the way to specify the number of servers that must confirm the write operation.

### MongoDB Security

- MongoDB provides several features to secure your data:
  - Authentication: This is the process of verifying the identity of a client.
  - Authorization: This is the process of verifying what operations a client is allowed to perform.
  - Encryption: This is the process of converting the data into a code to prevent unauthorized access.
  - Auditing: This is the process of recording the operations that are performed on the database.
  - Role-Based Access Control: This is the process of controlling the access of the users to the database based on their role.
  - SSL: This is the protocol that is used to secure the data that is transmitted over the network.
  - Kerberos: This is the network authentication protocol that is used to provide strong authentication for client/server applications by using secret-key cryptography.

### MongoDB Backup

- MongoDB provides the following methods to backup your data:
  - mongodump: This is the command-line utility for creating a binary export of the contents of a database.
  - mongorestore: This is the command-line utility for restoring the binary export created by mongodump.
  - Filesystem Snapshots: This is the method of creating a snapshot of the filesystem that the database files are stored on.
  - Cloud Manager: This is the service that provides the backup and monitoring of the MongoDB deployments.
  - Ops Manager: This is the service that provides the backup and monitoring of the MongoDB deployments.

### MongoDB Aggregation Pipeline

- The aggregation pipeline is a framework for data aggregation modeled on the concept of data processing pipelines. Documents enter a multi-stage pipeline that transforms the documents into an aggregated result. The most basic pipeline stages provide filters that operate like queries and document transformations that modify the form of the output document.

### MongoDB Data Modeling

- Data modeling is the process of creating a data model for the data to be stored in a database. This data model is a conceptual representation of Data objects, the associations between different data objects, and the rules. Data modeling helps in the visual representation of data and enforces business rules, regulatory compliances, and government policies on the data.
  - Embedded Data Model: This is the data model that embeds one document inside another.
  - Normalized Data Model: This is the data model that stores the data in multiple collections and links the documents using references.
  - Data Model References: This is the way to reference the documents in another collection.
  - Data Model Relationships: This is the way to define the relationship between the documents.

### MongoDB Performance

- MongoDB provides the following methods to improve the performance of your database:
  - Indexing: This is the process of creating an index on a field in the collection.
  - Covered Query: This is the query that can be satisfied by scanning the index and does not have to examine any documents.
  - Query Plan Cache: This is the cache that stores the query plans.
  - Write Operations: This is the process of inserting, updating, and deleting the documents.
  - Read Operations: This is the process of reading the documents.
  - Profiler: This is the tool that provides the statistics of the operations that are performed on the database.
  - Sharding: This is the process of distributing the data across multiple servers.
  - Replication: This is the process of synchronizing the data across multiple servers.
  - Aggregation: This is the process of processing the data records and returning the computed results.
  - Data Modeling: This is the process of creating a data model for the data to be stored in the database.

### MongoDB Scalability

- MongoDB provides the following methods to scale your database:
  - Sharding: This is the process of storing the data records across multiple machines.
  - Replication: This is the process of synchronizing the data across multiple servers.
  - Indexing: This is the process of creating an index on a field in the collection.
  - Aggregation: This is the process of processing the data records and returning the computed results.
  - Data Modeling: This is the process of creating a data model for the data to be stored in the database.

### MongoDB Monitoring

- MongoDB provides the following methods to monitor your database:
  - mongostat: This is the command-line utility that provides a quick overview of the status of a currently running mongod or mongos instance.
  - mongotop: This is the command-line utility that provides a method to track the amount of time a read or write operation takes to complete.
  - Database Profiler: This is the tool that provides the statistics of the operations that are performed on the database.
  - mongod.log: This is the log file that records all the events that are performed on the database.
  - mongos.log: This is the log file that records all the events that are performed on the sharded cluster.
  - System Resource Monitoring: This is the process of monitoring the system resources that are used by the database.
