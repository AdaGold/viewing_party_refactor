# Viewing Party Refactor

In this activity we will be representing Viewing Party data with objects. Note that the instructions are intentionally vague at points! It will be up to you to decide how to name methods and variables, and to make various design decisions.

## Setup
ONLY ONE PERSON should fork the repo and add their partner as a collaborator. Both should then clone the repository.

Both partners should make a virtual environment, activate it, and install the dependencies.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Part 1

Begin implmenting the Person class. It should be able to be initialized with a name of the person. It should also have an instance variable that holds a collection of other people that are friends with this person. There should be an instance method that adds a new person to the friends. The new friend should only be added if the person is not already friends with them.

Write tests to verify this functionality and run them.

## Part 2

Begin implementing the Movie class. It should be able to be initialized with the name of the movie, the genre, and a rating on a scale of 1 to 5.

Write tests to verify this functionality and run them. (There may not be very many tests needed for this class at this point)

## Part 3

Add an instance variable to the Person class that keeps tracks of a "watchlist" - movies the person is interested in watching but has not yet watched. Write an instance method on the Person class that adds a movie to their watchlist. The movie should only be added if it is not already in the watchlist.

Write tests to verify this functionality and run them.

## Part 4

Add an instance variable to the Person class that keeps track of what movies they have already watched. Write an instance method on the Person class that represents the person watching a movie. This should add the movie to the person's collection of watched movies if it has not been watched by this person before. If the movie is on the person's "watchlist" (they were interested in watching it), it should be removed from the "watchlist" (because now they have watched it).

## Part 5 (OPTIONAL)

What can you add to the Person or Movie classes? Can you recreate more of the logic from the Viewing Party project, like finding the movies a Person has watched that their friends haven't? Can you add a release year to the Movie class and add an instance method that returns how many years have passed since the movie was released? Explore your curiosity! 