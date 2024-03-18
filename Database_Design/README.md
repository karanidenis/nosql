#### MongoDB

-You have been hired as a database administrator for a new startup called "TechShop". TechShop is an online marketplace for tech products where users can buy and sell various tech items such as laptops, smartphones, and accessories.

-Your task is to design and implement a NoSQL database for TechShop using MongoDB. The database should store information about users, products, and transactions.

-You will need to create a database called "techshop" and implement the following collections:

1. users - This collection should store information about users such as name, email, and password.
2. products - This collection should store information about products such as name, description, and price.
3. transactions - This collection should store information about transactions such as the user who made the purchase, the product that was purchased, and the date of the transaction.

The database should be designed to support the following operations:

1. Add a new user to the database.
2. Add a new product to the database.
3. Record a new transaction in the database.
4. Retrieve all products in the database.
5. Retrieve all transactions for a given user.
6. Retrieve all transactions for a given product.
7. Find the top 5 most popular products in the database.

You should also implement the following constraints:

1. Users should have a unique email address.
2. Transactions should have a unique transaction ID.

You should also implement the following indexes:

1. An index on the email field of the users collection.
2. An index on the name field of the products collection.
3. An index on the transaction ID field of the transactions collection.

You should also implement the following validation rules:

1. The email field of the users collection should be required and should be a valid email address.
2. The name field of the products collection should be required and should be a string with a maximum length of 100 characters.
3. The transaction ID field of the transactions collection should be required and should be a string with a length of 24 characters.

Indexes:

- Create an index on the name field of the Users collection to speed up queries.
  Aggregation:
- Use MongoDB's aggregation framework to count the number of products

Draw a diagram to visualize the schema.
The diagram looks like this:

```javascript
    {
        users: {
            _id: ObjectId,
            name: String,
            email: String,
            password: String
        },
        products: {
            _id: ObjectId,
            name: String,
            description: String,
            price: Double
        },
        transactions: {
            _id: ObjectId,
            user: ObjectId,
            product: ObjectId,
            date: Date
        }
    }
```

    ```javascript
    db.createCollection("users", {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                required: ["name", "email", "password"],
                properties: {
                    name: {
                        bsonType: "string",
                        description: "must be a string and is required"
                    },
                    email: {
                        bsonType: "string",
                        description: "must be a string and is required"
                    },
                    password: {
                        bsonType: "string",
                        description: "must be a string and is required"
                    }
                }
            }
        }
    })
    db.users.createIndex({ email: 1 }, { unique: true })

    db.createCollection("products", {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                required: ["name", "description", "price"],
                properties: {
                    name: {
                        bsonType: "string",
                        description: "must be a string and is required"
                    },
                    description: {
                        bsonType: "string",
                        description: "must be a string and is required"
                    },
                    price: {
                        bsonType: "double",
                        description: "must be a double and is required"
                    }
                }
            }
        }
    })
    db.products.createIndex({ name: 1 })

    db.createCollection("transactions", {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                required: ["user", "product", "date"],
                properties: {
                    user: {
                        bsonType: "objectId",
                        description: "must be an objectId and is required"
                    },
                    product: {
                        bsonType: "objectId",
                        description: "must be an objectId and is required"
                    },
                    date: {
                        bsonType: "date",
                        description: "must be a date and is required"
                    }
                }
            }
        }
    })
    db.transactions.createIndex({ transactionId: 1 })
    ```

<!-- ![database schema](Database_schema.png) -->

<img src="Database_schema.png" alt="database schema" width="300" height="200">
