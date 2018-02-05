# C195 Database Seeder

This program is intended to seed the test database that students are provided
in order to complete WGU's C195 Software II course.

All tables are loaded except for:

* `reminder`
* `incrementtypes`
* `user`

According to the FAQ document provided by Course Mentors, `reminder` and
`incrementtypes` aren't _needed_ to complete the project. The `user` table
is intentionally left out in order to let students figure out how they want
to load it, and what user records they would like in it. You'll **need** to add
at least 1 user to the `user`s table in order for this script to work properly.

## Steps for Installing and Running

1. Install Python 3.6 and Pip3
2. Download or clone this repo to your computer
3. Create *at least* 1 user in the `user` table and add auto_increment to `address`, `appointment`, `city`, `country`, `customer`
4. Open a a terminal and navigate to where you cloned this repo
5. Enter `pip3 install -r requirements.txt` to install dependencies
6. Go into [settings.py](/settings.py) and
   * set the DB connection info
   * set the desired number of records for each table
   * set the UTC offset for your timezone. [Here is a list of UTC offsets](https://en.wikipedia.org/wiki/List_of_UTC_time_offsets).
7. Enter `python3 main.py` and wait for the script to complete
