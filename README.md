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
to load it, and what user records they would like in it.

## Requirements

In order to run this script on your machine, you'll need the following
installed on your machine:

* Python (this program was written/tested using Python 3.6.1), and
* Pip3, the package manager for Python 3

In order to install the necessary dependencies for the program, enter the
following in your terminal:

```bash
$ pip install -r requirements.txt
```

It is also **required** that you update your tables so that the primary keys auto-increment.

## Before Running the Program

Go into [settings.py](/settings.py) and set the database connection info and how many of each
type of record you would like.
