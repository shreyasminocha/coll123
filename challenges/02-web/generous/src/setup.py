import sqlite3
import random

top_50_twitch_streamers = [
    ("ninja",),
    ("auronplay",),
    ("rubius",),
    ("ibai",),
    ("xqc",),
    ("tfue",),
    ("thegrefg",),
    ("shroud",),
    ("juansguarnizo",),
    ("pokimane",),
    ("sodapoppin",),
    ("myth",),
    ("heelmike",),
    ("tommyinnit",),
    ("adinross",),
    ("timthetatman",),
    ("nickmercs",),
    ("elspreen",),
    ("riot games",),
    ("elmariana",),
    ("sypherpk",),
    ("dream",),
    ("alanzoka",),
    ("amouranth",),
    ("summit1g",),
    ("esl_csgo",),
    ("clix",),
    ("arigameplays",),
    ("elded",),
    ("mongraal",),
    ("fortnite",),
    ("quackity",),
    ("loltyler1",),
    ("bugha",),
    ("robleis",),
    ("tubbo",),
    ("georgenotfound",),
    ("montanablack88",),
    ("moistcr1tikal",),
    ("dakotaz",),
    ("wilbursoot",),
    ("slakun10",),
    ("drlupo",),
    ("fresh",),
    ("drdisrespect",),
    ("ranboolive",),
    ("nickeh30",),
    ("daequanwoco",),
    ("philza",),
    ("squeezie",),
]

if __name__ == "__main__":
    db = sqlite3.connect("database.db")
    db.cursor().execute(
        "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, subscribed INTEGER)"
    )
    db.cursor().execute(
        "INSERT INTO users VALUES ('admin', ?, 1)", (random.randbytes(10).hex(),)
    )

    db.cursor().execute("CREATE TABLE IF NOT EXISTS streamers (name TEXT)")
    db.cursor().executemany(
        "INSERT INTO streamers VALUES (?)",
        top_50_twitch_streamers,
    )
    db.commit()
