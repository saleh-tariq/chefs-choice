from app.models import db, Ingredient, environment, SCHEMA
from sqlalchemy.sql import text

salt = Ingredient(
    name="Salt",
    price_per_unit="125",
    amount_available="10.75",
    unit_of_measurement="cups",
    img="https://assets.clevelandclinic.org/transform/1dbde386-78f5-41ad-8103-f8463950b0ea/spoonful-salt-sitting-tabletop-1051727580",
    userId=1,
)
pepper = Ingredient(
    name="Pepper",
    price_per_unit="300",
    amount_available="3.92",
    unit_of_measurement="cups",
    img="https://i5.walmartimages.com/asr/275e080a-321f-4214-9d1c-9695abdbcad5.5bd08980ff6bb69eb26247026db37570.jpeg",
    userId=1,
)
eggs = Ingredient(
    name="Eggs",
    price_per_unit=25,
    amount_available=48,
    unit_of_measurement="eggs",
    img="https://www.shadygrovefertility.com/wp-content/uploads/2023/07/Egg-supply-blog.png",
    userId=1,
)
rice_krispies = Ingredient(
    name="Rice Krispies",
    price_per_unit=345,
    amount_available=3,
    unit_of_measurement="boxes",
    img="https://m.media-amazon.com/images/I/91laxLarjYL._AC_UF894,1000_QL80_.jpg",
    userId=1,
)
marshmallows = Ingredient(
    name="Marshmallows",
    price_per_unit=250,
    amount_available=5,
    unit_of_measurement="cups",
    img="https://nuts.com/images/rackcdn/ed910ae2d60f0d25bcb8-80550f96b5feb12604f4f720bfefb46d.ssl.cf1.rackcdn.com/09669a3bdb119241-XKMdPBRT-large.jpg",
    userId=1,
)
butter = Ingredient(
    name="Butter",
    price_per_unit=129,
    amount_available=7,
    unit_of_measurement="sticks",
    img="https://www.realsimple.com/thmb/VvdPHiBwtcQgPl8MiRbOjSjNo4g=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/freeze-butter-GettyImages-466938239-b386cf1b961642089337ab851e40a87e.jpg",
    userId=1,
)
potatoes = Ingredient(
    name="Potatoes",
    price_per_unit=66,
    amount_available=500,
    unit_of_measurement="potats",
    img="https://131299103.cdn6.editmysite.com/uploads/1/3/1/2/131299103/s620857546626214343_p354_i1_w2560.jpeg",
    userId=1,
)
lemon_juice = Ingredient(
    name="Lemon Juice",
    price_per_unit=75,
    amount_available=4,
    unit_of_measurement="cups",
    img="https://i5.walmartimages.com/seo/ReaLemon-100-Lemon-Juice-2-48-oz-Bottles_cc77f650-0272-4c90-a042-b3a8cd3b0b99.83b27bbbc58da7faaf534cccc197e06d.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF",
    userId=1,
)
tuna = Ingredient(
    name="Tuna",
    price_per_unit=25,
    amount_available=30,
    unit_of_measurement="cans",
    img="https://m.media-amazon.com/images/I/61gYUL02VvL._AC_UF894,1000_QL80_.jpg",
    userId=1,
)
cheese_singles = Ingredient(
    name="Cheese Singles",
    price_per_unit=15,
    amount_available=400,
    unit_of_measurement="singles",
    img="https://m.media-amazon.com/images/I/41uKz1OUlsL._AC_UF894,1000_QL80_.jpg",
    userId=1,
)


# Adds a demo user, you can add other users here if you want
def seed_ingredients():
    db.session.add(salt)
    db.session.add(pepper)
    db.session.add(eggs)
    db.session.add(rice_krispies)
    db.session.add(marshmallows)
    db.session.add(butter)
    db.session.add(potatoes)
    db.session.add(lemon_juice)
    db.session.add(tuna)
    db.session.add(cheese_singles)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_ingredients():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.ingredients RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM ingredients"))

    db.session.commit()
