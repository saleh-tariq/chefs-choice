from sqlalchemy.sql import text

from app.models import (SCHEMA, Ingredient, Recipe, Step, StepIngredients, db,
                        environment)

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
    ## Recipe
    sunny = Recipe(
        name="Sunny Side Up Eggs",
        description="Sunny Side Up Eggs LMAOOOO",
        img="https://thebakermama.com/wp-content/uploads/2021/03/IMG_5169-scaled.jpg",
        user_id=1,
    )

    ## Ingredients
    eggs = Ingredient(
        name="Eggs",
        price_per_unit=25,
        amount_available=48,
        unit_of_measurement="eggs",
        img="https://www.shadygrovefertility.com/wp-content/uploads/2023/07/Egg-supply-blog.png",
        user_id=1,
    )
    butter = Ingredient(
        name="Butter",
        price_per_unit=129,
        amount_available=7,
        unit_of_measurement="sticks",
        img="https://www.realsimple.com/thmb/VvdPHiBwtcQgPl8MiRbOjSjNo4g=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/freeze-butter-GettyImages-466938239-b386cf1b961642089337ab851e40a87e.jpg",
        user_id=1,
    )

    ## STEPS
    sunny_step1 = Step(description="First, butter a pan on low heat", seconds=60,is_head =1)
    sunny_step1_ingred1 = StepIngredients(amount_needed=0.25)
    sunny_step1_ingred1.ingredient = butter
    sunny_step1.ingredients.append(sunny_step1_ingred1)

    sunny_step2 = Step(description="Then, add 5 eggs in and let cook", seconds=240)
    sunny_step2_ingred1 = StepIngredients(amount_needed=5)
    sunny_step2_ingred1.ingredient = eggs
    sunny_step2.ingredients.append(sunny_step2_ingred1)

    sunny_step3 = Step(
        description="Finally, once cooked to your liking, remove the eggs and enjoy",
        seconds=0,
    )

    sunny_step1.next_step = sunny_step2
    sunny_step2.next_step = sunny_step3

    sunny.steps.append(sunny_step1)
    sunny.steps.append(sunny_step2)
    sunny.steps.append(sunny_step3)
    db.session.add(sunny)

    ## Recipe
    vegetable_stir_fry = Recipe(
        name="Vegetable Stir-Fry",
        description="A quick and healthy vegetable stir-fry.",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/vegetable-stir-fry.jpg",
        user_id=1,
    )

    ## Ingredients
    bell_pepper = Ingredient(
        name="Bell Pepper",
        price_per_unit=50,
        amount_available=1000,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/bell-pepper.jpg",
        user_id=1,
    )
    broccoli = Ingredient(
        name="Broccoli",
        price_per_unit=40,
        amount_available=1000,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/broccoli.jpg",
        user_id=1,
    )
    carrot = Ingredient(
        name="Carrot",
        price_per_unit=30,
        amount_available=1000,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/carrot.jpg",
        user_id=1,
    )

    ## STEPS
    stir_fry_step1 = Step(description="Heat oil in a pan over medium heat.", seconds=60,is_head =1)
    oil = Ingredient(
        name="Vegetable Oil",
        price_per_unit=40,
        amount_available=500,
        unit_of_measurement="ml",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/vegetable-oil.jpg",
        user_id=1,
    )
    stir_fry_step1_ingred1 = StepIngredients(amount_needed=20)
    stir_fry_step1_ingred1.ingredient = oil
    stir_fry_step1.ingredients.append(stir_fry_step1_ingred1)

    stir_fry_step2 = Step(
        description="Add bell pepper, broccoli, and carrot and stir-fry for 5 minutes.",
        seconds=300,
    )
    stir_fry_step2_ingred1 = StepIngredients(amount_needed=300)
    stir_fry_step2_ingred1.ingredient = bell_pepper
    stir_fry_step2.ingredients.append(stir_fry_step2_ingred1)

    stir_fry_step2_ingred2 = StepIngredients(amount_needed=200)
    stir_fry_step2_ingred2.ingredient = broccoli
    stir_fry_step2.ingredients.append(stir_fry_step2_ingred2)

    stir_fry_step2_ingred3 = StepIngredients(amount_needed=100)
    stir_fry_step2_ingred3.ingredient = carrot
    stir_fry_step2.ingredients.append(stir_fry_step2_ingred3)

    stir_fry_step3 = Step(description="Serve hot with rice.", seconds=0)

    stir_fry_step1.next_step = stir_fry_step2
    stir_fry_step2.next_step = stir_fry_step3

    vegetable_stir_fry.steps.append(stir_fry_step1)
    vegetable_stir_fry.steps.append(stir_fry_step2)
    vegetable_stir_fry.steps.append(stir_fry_step3)

    db.session.add(vegetable_stir_fry)

    ## Recipe
    spaghetti_aglio_e_olio = Recipe(
        name="Spaghetti Aglio e Olio",
        description="A classic Italian pasta dish with garlic and olive oil.",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/spaghetti-aglio-e-olio.jpg",
        user_id=1,
    )

    ## Ingredients
    spaghetti_ingredient = Ingredient(
        name="Spaghetti",
        price_per_unit=150,
        amount_available=500,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/spaghetti.jpg",
        user_id=1,
    )

    garlic_ingredient = Ingredient(
        name="Garlic",
        price_per_unit=20,
        amount_available=100,
        unit_of_measurement="cloves",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/garlic.jpg",
        user_id=1,
    )

    olive_oil_ingredient = Ingredient(
        name="Olive Oil",
        price_per_unit=300,
        amount_available=1000,
        unit_of_measurement="ml",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/olive-oil.jpg",
        user_id=1,
    )

    chili_flakes_ingredient = Ingredient(
        name="Red Chili Flakes",
        price_per_unit=15,
        amount_available=100,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/red-chili-flakes.jpg",
        user_id=1,
    )

    ## STEPS
    aglio_e_olio_step1 = Step(
        description="Boil water and cook spaghetti until al dente.", seconds=600,is_head =1
    )
    aglio_e_olio_step1_ingred1 = StepIngredients(amount_needed=200)
    aglio_e_olio_step1_ingred1.ingredient = spaghetti_ingredient
    aglio_e_olio_step1.ingredients.append(aglio_e_olio_step1_ingred1)

    aglio_e_olio_step2 = Step(
        description="In a pan, heat olive oil and sauté garlic until golden.",
        seconds=120,
    )
    aglio_e_olio_step2_ingred1 = StepIngredients(amount_needed=50)
    aglio_e_olio_step2_ingred1.ingredient = olive_oil_ingredient
    aglio_e_olio_step2.ingredients.append(aglio_e_olio_step2_ingred1)

    aglio_e_olio_step2_ingred2 = StepIngredients(amount_needed=4)
    aglio_e_olio_step2_ingred2.ingredient = garlic_ingredient
    aglio_e_olio_step2.ingredients.append(aglio_e_olio_step2_ingred2)

    aglio_e_olio_step3 = Step(
        description="Add red chili flakes and cooked spaghetti; toss to combine.",
        seconds=60,
    )
    aglio_e_olio_step3_ingred1 = StepIngredients(amount_needed=5)
    aglio_e_olio_step3_ingred1.ingredient = chili_flakes_ingredient
    aglio_e_olio_step3.ingredients.append(aglio_e_olio_step3_ingred1)

    aglio_e_olio_step1.next_step = aglio_e_olio_step2
    aglio_e_olio_step2.next_step = aglio_e_olio_step3

    spaghetti_aglio_e_olio.steps.append(aglio_e_olio_step1)
    spaghetti_aglio_e_olio.steps.append(aglio_e_olio_step2)
    spaghetti_aglio_e_olio.steps.append(aglio_e_olio_step3)

    db.session.add(spaghetti_aglio_e_olio)

    ## Recipe
    chicken_curry = Recipe(
        name="Chicken Curry",
        description="A flavorful chicken curry with spices.",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/chicken-curry.jpg",
        user_id=1,
    )

    ## Ingredients
    chicken_ingredient = Ingredient(
        name="Chicken Breast",
        price_per_unit=200,
        amount_available=1000,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/chicken.jpg",
        user_id=1,
    )

    onion_ingredient = Ingredient(
        name="Onion",
        price_per_unit=15,
        amount_available=100,
        unit_of_measurement="units",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/onion.jpg",
        user_id=1,
    )

    tomato_ingredient = Ingredient(
        name="Tomato",
        price_per_unit=10,
        amount_available=500,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/tomato.jpg",
        user_id=1,
    )

    curry_powder_ingredient = Ingredient(
        name="Curry Powder",
        price_per_unit=50,
        amount_available=200,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/curry-powder.jpg",
        user_id=1,
    )

    ## STEPS
    curry_step1 = Step(
        description="Sauté chopped onion until translucent.", seconds=180,is_head =1
    )
    curry_step1_ingred1 = StepIngredients(amount_needed=1)
    curry_step1_ingred1.ingredient = onion_ingredient
    curry_step1.ingredients.append(curry_step1_ingred1)

    curry_step2 = Step(description="Add chicken and cook until browned.", seconds=300)
    curry_step2_ingred1 = StepIngredients(amount_needed=500)
    curry_step2_ingred1.ingredient = chicken_ingredient
    curry_step2.ingredients.append(curry_step2_ingred1)

    curry_step3 = Step(
        description="Add tomato and curry powder; simmer until cooked through.",
        seconds=600,
    )
    curry_step3_ingred1 = StepIngredients(amount_needed=200)
    curry_step3_ingred1.ingredient = tomato_ingredient
    curry_step3.ingredients.append(curry_step3_ingred1)

    curry_step3_ingred2 = StepIngredients(amount_needed=20)
    curry_step3_ingred2.ingredient = curry_powder_ingredient
    curry_step3.ingredients.append(curry_step3_ingred2)

    curry_step1.next_step = curry_step2
    curry_step2.next_step = curry_step3

    chicken_curry.steps.append(curry_step1)
    chicken_curry.steps.append(curry_step2)
    chicken_curry.steps.append(curry_step3)

    db.session.add(chicken_curry)

    ## Recipe
    caprese_salad = Recipe(
        name="Caprese Salad",
        description="A fresh salad with tomatoes, mozzarella, and basil.",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/caprese-salad.jpg",
        user_id=1,
    )

    ## Ingredients
    mozzarella_ingredient = Ingredient(
        name="Fresh Mozzarella",
        price_per_unit=300,
        amount_available=500,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/mozzarella.jpg",
        user_id=1,
    )

    tomato_ingredient = Ingredient(
        name="Tomato",
        price_per_unit=10,
        amount_available=500,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/tomato.jpg",
        user_id=1,
    )

    basil_ingredient = Ingredient(
        name="Fresh Basil",
        price_per_unit=50,
        amount_available=100,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/basil.jpg",
        user_id=1,
    )

    olive_oil_ingredient = Ingredient(
        name="Olive Oil",
        price_per_unit=300,
        amount_available=1000,
        unit_of_measurement="ml",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/olive-oil.jpg",
        user_id=1,
    )

    ## STEPS
    caprese_step1 = Step(description="Slice mozzarella and tomatoes.", seconds=120,is_head =1)
    caprese_step1_ingred1 = StepIngredients(amount_needed=250)
    caprese_step1_ingred1.ingredient = mozzarella_ingredient
    caprese_step1.ingredients.append(caprese_step1_ingred1)

    caprese_step1_ingred2 = StepIngredients(amount_needed=300)
    caprese_step1_ingred2.ingredient = tomato_ingredient
    caprese_step1.ingredients.append(caprese_step1_ingred2)

    caprese_step2 = Step(
        description="Layer mozzarella, tomato, and basil on a plate.", seconds=60
    )
    caprese_step2_ingred1 = StepIngredients(amount_needed=10)
    caprese_step2_ingred1.ingredient = basil_ingredient
    caprese_step2.ingredients.append(caprese_step2_ingred1)

    caprese_step3 = Step(description="Drizzle with olive oil and serve.", seconds=30)
    caprese_step3_ingred1 = StepIngredients(amount_needed=20)
    caprese_step3_ingred1.ingredient = olive_oil_ingredient
    caprese_step3.ingredients.append(caprese_step3_ingred1)

    caprese_step1.next_step = caprese_step2
    caprese_step2.next_step = caprese_step3

    caprese_salad.steps.append(caprese_step1)
    caprese_salad.steps.append(caprese_step2)
    caprese_salad.steps.append(caprese_step3)

    db.session.add(caprese_salad)

    ## Recipe
    omelette = Recipe(
        name="Omelette",
        description="A fluffy omelette with cheese and herbs.",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/omelette.jpg",
        user_id=1,
    )

    ## Ingredients

    cheese_ingredient = Ingredient(
        name="Cheddar Cheese",
        price_per_unit=200,
        amount_available=300,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/cheddar.jpg",
        user_id=1,
    )

    herbs_ingredient = Ingredient(
        name="Fresh Herbs",
        price_per_unit=50,
        amount_available=100,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/herbs.jpg",
        user_id=1,
    )

    ## STEPS
    omelette_step1 = Step(description="Whisk eggs in a bowl.", seconds=30,is_head =1)
    omelette_step1_ingred1 = StepIngredients(amount_needed=3)
    omelette_step1_ingred1.ingredient = eggs
    omelette_step1.ingredients.append(omelette_step1_ingred1)

    omelette_step2 = Step(
        description="Heat butter in a pan, pour in eggs, and cook.", seconds=300
    )
    omelette_step2_ingred1 = StepIngredients(amount_needed=0.25)
    omelette_step2_ingred1.ingredient = butter  # Reusing butter
    omelette_step2.ingredients.append(omelette_step2_ingred1)

    omelette_step3 = Step(
        description="Add cheese and herbs; fold and serve.", seconds=60
    )
    omelette_step3_ingred1 = StepIngredients(amount_needed=50)
    omelette_step3_ingred1.ingredient = cheese_ingredient
    omelette_step3.ingredients.append(omelette_step3_ingred1)

    omelette_step3_ingred2 = StepIngredients(amount_needed=5)
    omelette_step3_ingred2.ingredient = herbs_ingredient
    omelette_step3.ingredients.append(omelette_step3_ingred2)

    omelette_step1.next_step = omelette_step2
    omelette_step2.next_step = omelette_step3

    omelette.steps.append(omelette_step1)
    omelette.steps.append(omelette_step2)
    omelette.steps.append(omelette_step3)

    db.session.add(omelette)

    ## Recipe
    fried_rice = Recipe(
        name="Fried Rice",
        description="Delicious fried rice with vegetables and eggs.",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/fried-rice.jpg",
        user_id=1,
    )

    ## Ingredients
    rice_ingredient = Ingredient(
        name="Cooked Rice",
        price_per_unit=50,
        amount_available=1000,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/rice.jpg",
        user_id=1,
    )

    mixed_vegetables_ingredient = Ingredient(
        name="Mixed Vegetables",
        price_per_unit=80,
        amount_available=500,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/vegetables.jpg",
        user_id=1,
    )

    ## STEPS
    fried_rice_step1 = Step(
        description="Heat oil in a pan and add cooked rice.", seconds=120,is_head =1
    )
    fried_rice_step1_ingred1 = StepIngredients(amount_needed=200)
    fried_rice_step1_ingred1.ingredient = rice_ingredient
    fried_rice_step1.ingredients.append(fried_rice_step1_ingred1)

    fried_rice_step2 = Step(description="Add mixed vegetables and sauté.", seconds=180)
    fried_rice_step2_ingred1 = StepIngredients(amount_needed=100)
    fried_rice_step2_ingred1.ingredient = mixed_vegetables_ingredient
    fried_rice_step2.ingredients.append(fried_rice_step2_ingred1)

    fried_rice_step3 = Step(
        description="Add beaten eggs and stir until cooked.", seconds=300
    )
    fried_rice_step3_ingred1 = StepIngredients(amount_needed=2)
    fried_rice_step3_ingred1.ingredient = eggs  # Reusing eggs
    fried_rice_step3.ingredients.append(fried_rice_step3_ingred1)

    fried_rice_step1.next_step = fried_rice_step2
    fried_rice_step2.next_step = fried_rice_step3

    fried_rice.steps.append(fried_rice_step1)
    fried_rice.steps.append(fried_rice_step2)
    fried_rice.steps.append(fried_rice_step3)

    db.session.add(fried_rice)

    ## Recipe
    caprese_salad = Recipe(
        name="Caprese Salad",
        description="A fresh salad with tomatoes, mozzarella, and basil.",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/caprese-salad.jpg",
        user_id=1,
    )

    ## Ingredients

    mozzarella_ingredient = Ingredient(
        name="Mozzarella Cheese",
        price_per_unit=250,
        amount_available=300,
        unit_of_measurement="grams",
        img="https://www.acouplecooks.com/wp-content/uploads/2020/05/mozzarella.jpg",
        user_id=1,
    )

    ## STEPS
    caprese_step1 = Step(
        description="Slice tomatoes and mozzarella cheese.", seconds=120,is_head =1
    )
    caprese_step1_ingred1 = StepIngredients(amount_needed=200)
    caprese_step1_ingred1.ingredient = tomato_ingredient
    caprese_step1.ingredients.append(caprese_step1_ingred1)

    caprese_step2 = Step(
        description="Layer tomatoes, mozzarella, and basil on a plate.", seconds=180
    )
    caprese_step2_ingred1 = StepIngredients(amount_needed=150)
    caprese_step2_ingred1.ingredient = mozzarella_ingredient
    caprese_step2.ingredients.append(caprese_step2_ingred1)

    caprese_step2_ingred2 = StepIngredients(amount_needed=10)
    caprese_step2_ingred2.ingredient = basil_ingredient
    caprese_step2.ingredients.append(caprese_step2_ingred2)

    caprese_step3 = Step(description="Drizzle with olive oil and serve.", seconds=30)
    caprese_step3_ingred1 = StepIngredients(amount_needed=20)
    caprese_step3_ingred1.ingredient = olive_oil_ingredient
    caprese_step3.ingredients.append(caprese_step3_ingred1)

    caprese_step1.next_step = caprese_step2
    caprese_step2.next_step = caprese_step3

    caprese_salad.steps.append(caprese_step1)
    caprese_salad.steps.append(caprese_step2)
    caprese_salad.steps.append(caprese_step3)

    db.session.add(caprese_salad)

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
        db.session.execute(text("DELETE FROM ingredients"))
        db.session.execute(text("DELETE FROM steps"))
        db.session.execute(text("DELETE FROM step_ingredients"))

    db.session.commit()
