#!/usr/bin/env python

import media
import fresh_tomatoes

# Create instances of favorite movies
empire_strikes_back = media.Movie("Empire Strikes Back",
                                  "Luke continues on his his to become a Jedi",
                                  "https://t1.gstatic.com/images?q=tbn:ANd9G" +
                                  "cTtXwQAEDxEY3E9Nn78H96VZCjlV6hZWPlDd5IpVN" +
                                  "yeuzO2vT17",
                                  "https://www.youtube.com/watch?v=JNwNXF9Y6kY")


blade_runner = media.Movie("Blade Runner",
                           "Description",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/B" +
                           "lade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=JMyz9bnKITY")


gladiator = media.Movie("Gladiator",
                        "Description",
                        "https://t3.gstatic.com/images?q=tbn:ANd9GcRuhegCaGH" +
                        "fcQc-Owpib9vGSO0hUlSUMTojO2s4ih8oXqHBw2ks",
                        "https://www.youtube.com/watch?v=w5rVtxWTq8w")


up = media.Movie("Up",
                 "Description",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_" +
                 "film%29.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")


the_martian = media.Movie("Blade Runner",
                          "Description",
                          "https://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7E" +
                          "IOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")


interstellar = media.Movie("Interstellar",
                           "Description",
                           "https://t1.gstatic.com/images?q=tbn:ANd9GcRf61mk" +
                           "er2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

movies = [empire_strikes_back,
          blade_runner,
          gladiator,
          up,
          the_martian,
          interstellar]

fresh_tomatoes.open_movies_page(movies)
