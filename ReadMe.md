## Working with SQLAlchemy

### Instalation

pip install sqlalchemy

### Overview

SQLAlchemy is the Python SQL toolkit and ORM that gives developers the full power of SQL. This library facilitates the communication between Python programs and databases. SQLAlchemy is used as an ORM (Object Relational Mapping) tool that translates Python classes to tables on the relational databases and automatically converts function calls to SQL statements.

SQLAlchemy can be used with or without the ORM features. Configurations with various application software stacks and backend databases can be done depending on what type of application you build. SQLAlchemy has two modes ORM and Core. Core has more of a schema-centric view like traditional SQL which is focused around tables, keys and index structures.

### Features Learned
- DBAPI : Database API works with a wide variety of databases. ie: Psycopg2 (DBAPI) is default for PostgreSQL (database). Another would be PyMySQL  (DBAPI) for MySQL (database).

- create_engine : This Engine function is the starting point for the application. It creates a dialect and a connection pool. This is how we interact with the database. The Dialect refers to the name of the database. 

- declarative_base : used to create a base class. 

- sessionmaker : A session establishes and mainains all conversations between your program and the databases. Its commonly known as the "holding zone".

- Column - Defines the column datatype in the table of Db

- String : Defines the string datatype in the table of Db

- Integer : Defines the integer datatype in the table of Db.




