from . import Database

# This dict will contain information for each table that should exist as well as some startup data as needed,
# like creation scripts and initial data for populating these tables
db_setup = {
    "Users": {
        "createScript": """
            CREATE TABLE Users (
                userId varchar(255) UNIQUE PRIMARY KEY,
                username varchar(255),
                hash varchar(255),
                salt varchar(255),
                firstName varchar(255),
                lastName varchar(255),
                phoneNumber varchar(11),
                activeCart varchar(255),
                FOREIGN KEY (activeCart) REFERENCES Carts(cartId),
            );
        """,
    },
    "Addresses": {
        "createScript": """
            CREATE TABLE Addresses (
                addressId varchar(255) UNIQUE PRIMARY KEY,
                addressLine1 varchar(255),
                addressLine2 varchar(255),
                city varchar(255),
                stateCode char(2),
                zipCode char(5),
            );
        """,
    },
    
}

res = Database.cursor.execute("SELECT name FROM sqlite_master")

currentDbs = res.fetchall()