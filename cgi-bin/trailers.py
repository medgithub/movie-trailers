import media

civil_war = media.Movie("Captain America: Civil War",
                        "Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                        "https://www.youtube.com/watch?v=dKrVegVI0Us")

independence_day = media.Movie("Independence Day: Resurgence",
                               "Two decades after the first Independence Day invasion, Earth is faced with a new extra-Solar threat. But will mankind's new space defenses be enough?",
                               "https://upload.wikimedia.org/wikipedia/en/5/58/Independence-Day-2-poster.jpg",
                               "https://www.youtube.com/watch?v=LbduDRH2m2M")

ghostbusters = media.Movie("Ghostbusters",
                           "30 years after Ghostbusters took the world by storm, the beloved franchise makes its long-awaited return. Director Paul Feig brings his fresh take to the supernatural comedy, joined by some of the funniest actors working today.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d0/Ghostbusters_2016_film_poster.jpg",
                           "https://www.youtube.com/watch?v=w3ugHP-yZXw")

finding_dory = media.Movie("Finding Dory",
                           "The friendly-but-forgetful blue tang fish reunites with her loved ones, and everyone learns a few things about the real meaning of family along the way.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
                           "https://www.youtube.com/watch?v=3JNLwlcPBPI")

suicide_squad = media.Movie("Suicide Squad",
                            "A secret government agency recruits imprisoned supervillains to execute dangerous black ops missions in exchange for clemency.",
                            "https://upload.wikimedia.org/wikipedia/en/a/ac/Suicide_Squad_%28film%29_Poster.jpg",
                            "www.youtube.com/watch?v=fyJH39ZbPAg")

stb = media.Movie("Star Trek Beyond",
                  "Where no man has gone before?",
                  "https://upload.wikimedia.org/wikipedia/en/b/ba/Star_Trek_Beyond_poster.jpg",
                  "https://www.youtube.com/watch?v=XRVD32rnzOw")

movies = [civil_war, independence_day, ghostbusters, finding_dory, suicide_squad, stb]

def getMovies():
  return movies