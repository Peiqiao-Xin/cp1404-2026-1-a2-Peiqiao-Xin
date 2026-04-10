# cp1404-2026-1-a2-Peiqiao-Xin
# Project Reflection

## What I learned about coding in this project

This project helped me understand object-oriented programming much more clearly than before. In Assignment 1, I stored each place as a list and accessed values by index. That approach worked, but it was not very flexible or easy to read. In this assignment, I changed the program to use a `Place` class and a `PlaceCollection` class. This made the code much easier to organise because each place became an object with meaningful attributes such as `name`, `country`, `priority` and `is_visited`.

One of the most useful things I learned was how classes improve readability and reuse. For example, instead of writing code like `place[0]` or `place[3]`, I could use `place.name` and `place.is_visited`. This made the program easier to understand and reduced mistakes. I also learned that methods such as `mark_visited()`, `mark_unvisited()` and `is_important()` make the logic more natural because the behaviour belongs to the object itself.

Another important thing I learned was how one data model can support different interfaces. After I finished the classes, I reused them in both the console program and the GUI program. This showed me why the assignment required classes first. Once the data model was working properly, it became much easier to build the GUI around it. The GUI did not need a completely different logic structure, because it could use the same `Place` and `PlaceCollection` classes.

I also improved my understanding of file handling by changing from CSV to JSON. JSON was more suitable for storing structured data because it matched the object attributes more directly. Implementing `load_places()` and `save_places()` in `PlaceCollection` helped me see how file I/O can be separated from the main program logic.

The GUI part was the most challenging part of the assignment. I learned how to separate the visual layout in `app.kv` from the program logic in `main.py`. I also learned how to dynamically create widgets, especially the place buttons on the right side of the app. This was different from the console program because the interface had to update after every user action. I had to make sure that pressing a button changed the visited status, updated the button colour, refreshed the count at the top, and displayed the correct status message at the bottom.

Error handling was another area where I improved. In the console program, I had already used exception handling for invalid numeric input, but in the GUI I had to think more carefully about how to validate input fields and display useful messages to the user. I implemented checks for blank fields, invalid priority values and priorities less than 1. This helped me understand that robust programs should not only work when the user gives correct input, but should also respond clearly when the input is wrong.

## What I learned about my development process

The most important lesson about my development process was that the order of development really matters. At first, it was tempting to focus on the GUI because it is the most visible part of the project. However, I realised that building the classes first was the right approach. Once `Place` and `PlaceCollection` were tested and working, the rest of the project became much easier. This showed me that good planning saves time later.

Writing simple test files for `Place` and `PlaceCollection` was also helpful. Even though the tests were basic, they gave me confidence that the classes were working before I used them in the console and GUI. This reduced debugging later because I could isolate problems more easily. I learned that testing early is much better than waiting until the whole program is finished.

Another important lesson was the value of incremental development. Instead of trying to finish the whole assignment in one large step, I worked on smaller parts: class methods first, then tests, then console functionality, then GUI layout, then GUI behaviour. This made the project more manageable and made it easier to find the cause of problems when something did not work.

I also learned that user interface work often takes more time than expected. Even after the main logic was working, I still had to spend time adjusting layout, button text, colours and status messages. This reminded me that software quality is not only about whether the program runs, but also about whether the interface is clear and user-friendly.

Finally, this project showed me the importance of version control as part of the development process. Commits are not just for backup; they also show how the project was built step by step. A better commit history reflects a better development process. In future projects, I would like to be even more disciplined about making smaller, more regular commits with clear messages from the beginning.

## What I would improve next time

If I were to improve this project further, I would make the GUI look even closer to the demo by refining the visual styling and spacing. I would also add more automated tests instead of relying mainly on simple printed test results. In addition, I would plan my commit history more carefully from the start so that the full development process is documented more clearly.

Overall, this assignment helped me move from writing a working script to designing a more structured program with reusable classes, testing, file persistence and a graphical user interface. It was the most useful project so far for helping me understand how different parts of a Python application fit together.