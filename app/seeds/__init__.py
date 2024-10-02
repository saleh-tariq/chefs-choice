from flask.cli import AppGroup
from .users import seed_users, undo_users
from .ingredients import seed_ingredients, undo_ingredients
from .recipes import seed_recipes, undo_recipes

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup("seed")


# Creates the `flask seed all` command
@seed_commands.command("all")
def seed():
    undo_recipes()
    undo_ingredients()
    undo_users()
    seed_users()
    seed_ingredients()
    seed_recipes()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command("undo")
def undo():
    undo_recipes()
    undo_ingredients()
    undo_users()
    # Add other undo functions here
