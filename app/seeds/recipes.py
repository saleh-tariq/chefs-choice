from app.models import db, Recipe, RecipeIngredients, environment, SCHEMA
from sqlalchemy.sql import text
from .ingredients import (
    eggs,
    rice_krispies,
    marshmallows,
    butter,
    potatoes,
    lemon_juice,
    tuna,
    cheese_singles,
)

sunny = Recipe(
    name="Sunny Side Up Eggs",
    description="Sunny Side Up Eggs LMAOOOO",
    img="https://thebakermama.com/wp-content/uploads/2021/03/IMG_5169-scaled.jpg",
    user_id=1,
)
rice_crispy_treats = Recipe(
    name="Rice Crispy Treats",
    description="Soft yet crispy home-made rice crispies to make any kids party a blast",
    img="https://images.kglobalservices.com/www.ricekrispies.com/en_us/recipe/kicrecipe-1605/recip_img-7547527_recip_img-7547527_recip_img-7547527.jpg",
    user_id=1,
)
roasted_potatoes = Recipe(
    name="Classic Roasted Potatoes",
    description="A simple yet flavor packed recipe to bring your entire family together",
    img="https://www.foodnetwork.com/content/dam/images/food/fullset/2011/2/2/0/BXSP01H_rosemary-roasted-potatoes_s4x3.jpg",
    user_id=1,
)
tuna_melt = Recipe(
    name="Tuna Melts",
    description="A classic recipe for any picnic",
    img="https://www.seriouseats.com/thmb/h3BPsOL0qqqBPYN4aivT3xEAZG4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/20240214-TunaMelt-SEA--Peyton-Beckworth-1f500549fa8f48499e436fa3c2a0ca0e.jpg",
    user_id=1,
)


# Adds a demo user, you can add other users here if you want
def seed_recipes():
    sunny_egg = RecipeIngredients(amount_needed=5)
    sunny_egg.ingredient = eggs
    sunny_butter = RecipeIngredients(amount_needed=0.25)
    sunny_butter.ingredient = butter
    sunny.ingredients.append(sunny_egg)
    sunny.ingredients.append(sunny_butter)

    db.session.add(sunny)

    treat_krispies = RecipeIngredients(amount_needed=1)
    treat_krispies.ingredient = rice_krispies
    treat_butter = RecipeIngredients(amount_needed=0.5)
    treat_butter.ingredient = butter
    treat_marshmallows = RecipeIngredients(amount_needed=2)
    treat_marshmallows.ingredient = marshmallows
    rice_crispy_treats.ingredients.append(treat_krispies)
    rice_crispy_treats.ingredients.append(treat_butter)
    rice_crispy_treats.ingredients.append(treat_marshmallows)
    db.session.add(rice_crispy_treats)

    roasted_potatoes_potatoes = RecipeIngredients(amount_needed=10)
    roasted_potatoes_potatoes.ingredient = potatoes
    roasted_potatoes_lemon_juice = RecipeIngredients(amount_needed=0.25)
    roasted_potatoes_lemon_juice.ingredient = lemon_juice
    roasted_potatoes.ingredients.append(roasted_potatoes_potatoes)
    roasted_potatoes.ingredients.append(roasted_potatoes_lemon_juice)
    db.session.add(roasted_potatoes)

    tuna_melt_tuna = RecipeIngredients(amount_needed=3)
    tuna_melt_tuna.ingredient = tuna
    tuna_melt_butter = RecipeIngredients(amount_needed=0.25)
    tuna_melt_butter.ingredient = butter
    tuna_melt_cheese_singles = RecipeIngredients(amount_needed=6)
    tuna_melt_cheese_singles.ingredient = cheese_singles
    tuna_melt.ingredients.append(tuna_melt_tuna)
    tuna_melt.ingredients.append(tuna_melt_butter)
    tuna_melt.ingredients.append(tuna_melt_cheese_singles)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_recipes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipes"))
        db.session.execute(text("DELETE FROM recipe_ingredients"))

    db.session.commit()
