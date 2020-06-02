# MODEL/DB FIELDS

### LISTING

id: INT
realtor INT (FOREIGN KEY [realtor])
title: STR
address: STR
state: STR
zipcode: STR
description: STR
price: INT
bedrooms: INT
bathrooms: INT
garage: INT
sqst: INT
lot_size: FLOAT
list_date: DATE
photo_main: STR
photo_1: STR
photo_2: STR
photo_3: STR
photo_4: STR
photo_5: STR
photo_6: STR


### REALTOR

id: INT
name: STR
photo: STR
description: TEXT
email: STR
phone: STR
is_mvp: BOOL [0]
hire_date: DATE


### CONTACT

id: INT
user_id: INT
listing: INT
listing_id: INT
name: STR
email: STR
phone: STR
message: TEXT
contact_date: DATE