"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *
from sqlalchemy import and_, not_, or_

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
brand_query = Model.query.filter_by(id=8).one()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
chevy_corvette = Model.query.filter(and_(
                                          Model.brand_name=='Chevrolet', 
                                          Model.name=='Corvette')).all()

# Get all models that are older than 1960.
older_models = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
new_founded = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
cor_models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
not_discontinued = Brand.query.filter(and_(
                                          Brand.founded == 1903,
                                          Brand.discontinued == None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
old_discontinued = Brand.query.filter(or_(
                                          Brand.discontinued != None, 
                                          Brand.founded < 1950)).all()


# Get any model whose brand_name is not Chevrolet.
not_chevy = Model.query.filter(not_(Model.brand_name == 'Chevrolet')).all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models_of_the_year = Model.query.filter_by(year=year).all()

    for model in models_of_the_year:
        print "model name:", model.name
        print "brand name:", model.brand_name
        print "headquarters:", model.brands.headquarters
        print "\n"


def get_brands_summary(brand_name):
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_summary = Model.query.filter_by(brand_name=brand_name).all()

    for summary in brand_summary:
        print "Brand Name:", summary.brand_name
        print "Model Name:", summary.name
        print "\n"


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# A SQL query.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table is a way to diagram how two tables in SQL 
# are related to each other. It manages many to many relationships.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    brand_search = Model.query.filter_by(name=mystr).first()
    
    print brand_search.brand_name


def get_models_between(start_year, end_year):
    models_between = Model.query.filter(and_(
                                            Model.year >= start_year,
                                            Model.year < end_year)).all()
    for model in models_between:
        print model.year, model.name

