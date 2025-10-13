# Grade Calculator

This is a project-based guide to some of Python's foundational features. Each step will give you a usable product, while also introducing one or more key concepts in the language.

For this guide, you'll need to create a blank Python file.

## V1: Outline

The first version will be the **minimum required** for a usable grade calculator. It will use **input/output** and **arithmetic**.

Input is how the user gives information to the program. This is usually done using the `input` function. For our program, the user needs to be able to input their grade, so add these two lines:

```python
current_grade = input("What is your current grade, as a percent? (Leave off '%') ")
current_grade = float(current_grade)
```

The first line will show a message to the user, then wait for them to put something in and store what they write in a variable.
The second line converts what they entered from a **string** (series of characters) into a **float** (deicmal number) so the program can use it in calculations later.

Our program will also need three more numbers from the user: `current_grade` (the user's current grade in the class), `desired_grade` (the grade the user wants in the class), and `final_share` (what percent of their grade the final will be). Add code for all three of those below what you have now.

Once you're done with that, we need to do math on those numbers. Add these lines below what you currently have:

```python
share_fraction = final_share / 100
final_needed = (desired_grade - current_grade * (1 - share_fraction)) / share_fraction
```

The first line converts `final_share` from a percent to a fraction.
The second is the mathematical formula we use to calculate the needed final.
Notice that Python follows the order of operations. The parentheses will be evaluated first, then the multiplication, and so on.

Finally, we need to show the user the result using output. In Python, this is usually done with the `print` function. Add the following line to the bottom of your code:

```python
print("You need a " + str(final_needed) + ".")
```

At this point, you can run your program to test it.

If something's not working, compare your code to below. It's okay if the `input` messages are different, but make sure they are surrounded by double quotes, and make sure they don't have any double quotes *inside* of them.

<details><summary>Show finished code</summary>

```python
current_grade = input("What is your current grade, as a percent? (Leave off '%') ")
current_grade = float(current_grade)
desired_grade = input("What grade do you want, as a percent? ")
desired_grade = float(desired_grade)
final_share = input("What percent of your grade is your final? ")
final_share = float(final_share)

share_fraction = final_share / 100
final_needed = (desired_grade - current_grade * (1 - share_fraction)) / share_fraction

print("You need a " + str(final_needed) + ".")
```
</details>

## V2: ...with grade-based messages

It would be nice to have messages showing what letter grade each final is.
We can't just do math since letter grades aren't numbers. Instead, we'll use **if statements** to make the program show a different message based on your type of grade. Add the following lines to the end of your program:

```python
if final_needed > 100:
    print("That's over 100%. Extra credit?")
```

`final_needed > 100` is the condition of the if statement. Everything inside the if statement will only happen if the condition is true. If the condition is false, those things will get skipped over. Something is "inside the if statement" - or anything other statement ending in a colon - if it is *one indentation level deeper* than the statement itself.

An **elif** statement is like an if statement, but it will only get checked if the if/elif statement just above it was skipped over. Add this code to the bottom of your program, unindented:

```python
elif final_needed >= 90:
    print("That's an A.")
```

If your needed grade *isn't* over 100, and *is* greater than equal to 90, this will give you a message saying that you need an A.
We'll want similar messages for B-D. Add elif statements for each of those below, but hold off on F for now.

For F, our job is a little easier. Instead of using if/elif statements, which need a condition, we can just say "as long as we got here, we know you only need an F." Add this **else statement** code to the bottom of your program, unindented:

```python
else:
    print("That's an F.")
```

This won't trigger if *any* of the blocks above it triggered, but if you got through all of them, it'll give you the right message.

<details><summary>Show finished code</summary>

```python
current_grade = input("What is your current grade? ")
current_grade = float(current_grade)
desired_grade = input("What grade do you want? ")
desired_grade = float(desired_grade)
final_share = input("What percent of your grade is your final? ")
final_share = float(final_share)

share_fraction = final_share / 100
final_needed = (desired_grade - current_grade * (1 - share_fraction)) / share_fraction

print("You need a " + str(final_needed) + ".")

if final_needed > 100:
    print("That's over 100%. Extra credit?")
elif final_needed >= 90:
    print("That's an A.")
elif final_needed >= 80:
    print("That's a B.")
elif final_needed >= 70:
    print("That's a C.")
elif final_needed >= 60:
    print("That's a D.")
else:
    print("That's an F.")
```
</details>

## V3: Packaging

The program is complicated. It's doing a lot of things: asking for input, doing math on it, writing a custom message, and giving output. We should probably package some of those to simplify it.

We're going to do that with **functions**, which take a large amount of code and give it a short name.

Delete the `share_fraction` and `final_needed` lines from your program. Those are the lines we're going to pack up. At the very top of your program, add the following :

```python
def calculate_final(current, desired, share):
    share_fraction = share / 100
    needed = (desired - current * (1 - share_fraction)) / share_fraction
    return needed
```

`calculate_final` is the name of the function. This is how we'll refer to it later.
`current`, `desired`, and `share` are its **parameters**: for programming reasons too complicated for this guide ("scope", for the curious), a function doesn't know what happens outside of it, so parameters are how we tell it the important context.
The middle two lines are the same arithmetic we did before.
The final line is a **return statement**: for similar programming reasons as before (still scope), the program *outside* a function doesn't know what happens *inside* of it, so return statements lets the function report back the important information. Notice how we are only returning `needed` and not `share_fraction` - that's because the rest of the program only needs to know the grade the user needs, not any specific details about how we calculated that grade.

In words, the `calculate_final` function **takes in** the user's grades and course details, **computes** the final they need for it, and **returns** (reports) the final grade they need.

Now that we've packaged those calculations, we can use them in your code by **calling** the function. Just above the first `print` function, add this line:

```python
final_needed = calculate_final(current_grade, desired_grade, final_share)
```

This wil call the `calculate_final` function and provide it your current and desired grades, as well as your final share, as the parameters.

Run the program and make sure it still works. If it does, try to package up the code that chooses a letter grade message. Give it the name `write_message`. It will take one `final_needed` parameter. Make sure to replace all the `print` functions with `return` statements. Once you're done, you should be able to replace the old code with just two lines:

```python
message = write_message(final_needed)
print(message)
```

<details><summary>Show finished code</summary>

```python
def calculate_final(current, desired, share):
    share_fraction = share / 100
    needed = (desired - current * (1 - share_fraction)) / share_fraction
    return needed

def write_message(final_needed):
    if final_needed > 100:
        return "That's over 100%. Extra credit?"
    elif final_needed >= 90:
        return "That's an A."
    elif final_needed >= 80:
        return "That's a B."
    elif final_needed >= 70:
        return "That's a C."
    elif final_needed >= 60:
        return "That's a D."
    else:
        return "That's an F."

current_grade = input("What is your current grade? ")
current_grade = float(current_grade)
desired_grade = input("What grade do you want? ")
desired_grade = float(desired_grade)
final_share = input("What percent of your grade is your final? ")
final_share = float(final_share)

final_needed = calculate_final(current_grade, desired_grade, final_share)
print("You need a " + str(final_needed) + ".")

message = write_message(final_needed)
print(message)
```
</details>

## V4: Loops

This one's a smaller change. We want the user to be able to enter as many grades as they like. We can use a **while loop** for that. While loops repeat a block of code until their condition is no longer true. Just above your first input function, add this line:

```python
while input("Do you want to calculate a grade? y/n ") != "n":
```

This will ask the user for input. If the input is "n", the program will skip the statements in the loop. Otherwise, the program will run all the statements. After it's done, it will ask for input *again* and check to make sure it's not "n". It will repeat the process until the user enters "n"; until then, it'll keep going forever.

Like if statements, while loops determine what's "inside" the statement using indentation. Highlight every line after the while line and hit tab. That will tell the program that the contents of the loop are inside it.

<details><summary>Show finished code</summary>

```python
def calculate_final(current, desired, share):
    share_fraction = share / 100
    needed = (desired - current * (1 - share_fraction)) / share_fraction
    return needed

def write_message(final_needed):
    if final_needed > 100:
        return "That's over 100%. Extra credit?"
    elif final_needed >= 90:
        return "That's an A."
    elif final_needed >= 80:
        return "That's a B."
    elif final_needed >= 70:
        return "That's a C."
    elif final_needed >= 60:
        return "That's a D."
    else:
        return "That's an F."

while input("Do you want to calculate a grade? y/n ") != "n":
    current_grade = input("What is your current grade? ")
    current_grade = float(current_grade)
    desired_grade = input("What grade do you want? ")
    desired_grade = float(desired_grade)
    final_share = input("What percent of your grade is your final? ")
    final_share = float(final_share)

    final_needed = calculate_final(current_grade, desired_grade, final_share)
    print("You need a " + str(final_needed) + ".")

    message = write_message(final_needed)
    print(message)
```
</details>


## V5: Remembering courses

Generally, once a program finishes a pass through a loop, it'll forget most of what happened inside it. To remember the final grades we calculate, we can store that information in a **list**: a sequence of things (numbers, strings, etc.) in a specific order.

Above the while statement, add the following:

```python
grades_needed = []
```

The square brackets indicate an empty list.

There are several useful things you can do to a list. One is **appending**, which adds something to the end. Below the final print statement, add this line (still indented):

```python
grades_needed.append(final_needed)
```

That will tack the most recently calculated final to the end of the list.

Another useful thing is **indexing**, which lets you get a specific item out of a list. Add the following lines to the bottom of your program, *not* indented:

```python
replayed_final = int(input("Which final do you want to see again, starting from 0?"))
print(grades_needed[replayed_final])
```

Indexing a list is **number-based** and gets the element with the number you put in the brackets. It also starts from zero, so if you want the first item you put into the list, you should enter "0".

A third useful thing is **iteration**, which goes through the entire list and does something for each element. This is done with a **for statement**. Add these lines to the bottom of the program:

```python
print("To recap, you need:")
for grade in grades_needed:
    print(str(grade) + ".", end=" ")
    message = write_message(grade)
    print(message)
```

`grade` is a temporary name referring to the **current item** that the for loop is looking at. For every single grade that you put into the list, this program will output the grade and add the messsage.

If you have a list, you can also **insert** items, **remove** items, **sort** the list, and more. Some useful operations, and their descriptions, are available at the [Python documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists). If you want to know the length of the list, you can get that using `len(grades_needed)` (or whatever the name of the list is).

<details><summary>Show finished code</summary>

```python
def calculate_final(current, desired, share):
    share_fraction = share / 100
    needed = (desired - current * (1 - share_fraction)) / share_fraction
    return needed

def write_message(final_needed):
    if final_needed > 100:
        return "That's over 100%. Extra credit?"
    elif final_needed >= 90:
        return "That's an A."
    elif final_needed >= 80:
        return "That's a B."
    elif final_needed >= 70:
        return "That's a C."
    elif final_needed >= 60:
        return "That's a D."
    else:
        return "That's an F."

grades_needed = []

while input("Do you want to calculate a grade? y/n ") != "n":
    current_grade = input("What is your current grade? ")
    current_grade = float(current_grade)
    desired_grade = input("What grade do you want? ")
    desired_grade = float(desired_grade)
    final_share = input("What percent of your grade is your final? ")
    final_share = float(final_share)

    final_needed = calculate_final(current_grade, desired_grade, final_share)
    print("You need a " + str(final_needed) + ".")

    message = write_message(final_needed)
    print(message)

    grades_needed.append(final_needed)

replayed_final = int(input("Which final do you want to see again, starting from 0?"))
print(grades_needed[replayed_final])

print("To recap, you need:")
for grade in grades_needed:
    print(str(grade) + ".", end=" ")
    message = write_message(grade)
    print(message)
```
</details>

## V6: Named courses

Lists only store items based on their order. If you want to get something out of the lists using something more informative, like the name of a particular item, you'll need a different tool.

A **dictionary** is like a list, but it stores its values based on names, not just order. Replace the `grades_needed` line with this:

```python
grades_needed = {}
```

The curly braces signal that this is an empty dictionary.

In order to remember classes based on names, we need to ask the user for a name, so add this line (still indented) right after the while statement:

```python
course_name = input("What is the course name? ")
```

Then, replace the `append` line with this:

```python
grades_needed[course_name] = final_needed
```

This will create a new entry in the dictionary with the **key** (name) that the user inputted and the **value** based on the final they need.

Unlike a list, you access the elements of a dictionary based on their keys, not their number. Can you guess how the `replayed_final` line should change? To make that work?

You can iterate over the items of a dictionary, but you'll usually want to do it a little differently. For example, the for loop for the dictionary in this program should have the following header (notice that there are two things between `for` and `in`, as well as `.items()` at the end):

```python
for course, grade in grades_needed.items():
```

In this loop, `course` will be the key - the name of the current course, and `grade` will be the value - the grade you needed for that course. Given that header, can you guess what the body of the loop could be?

For both tasks, you can look at the finished code to see the solution.

<details><summary>Show finished code</summary>

```python
def calculate_final(current, desired, share):
    share_fraction = share / 100
    needed = (desired - current * (1 - share_fraction)) / share_fraction
    return needed

def write_message(final_needed):
    if final_needed > 100:
        return "That's over 100%. Extra credit?"
    elif final_needed >= 90:
        return "That's an A."
    elif final_needed >= 80:
        return "That's a B."
    elif final_needed >= 70:
        return "That's a C."
    elif final_needed >= 60:
        return "That's a D."
    else:
        return "That's an F."

grades_needed = {}

while input("Do you want to calculate a grade? y/n ") != "n":
    course_name = input("What is the course name? ")
    current_grade = input("What is your current grade? ")
    current_grade = float(current_grade)
    desired_grade = input("What grade do you want? ")
    desired_grade = float(desired_grade)
    final_share = input("What percent of your grade is your final? ")
    final_share = float(final_share)

    final_needed = calculate_final(current_grade, desired_grade, final_share)
    print("You need a " + str(final_needed) + ".")

    message = write_message(final_needed)
    print(message)

    grades_needed[course_name] = final_needed

replayed_final = input("Which final do you want to see again? ")
print(grades_needed[replayed_final])

print("To recap, you need:")
for course, grade in grades_needed.items():
    print(str(grade) + " in " + course + ". ", end=" ")
    message = write_message(grade)
    print(message)
```
</details>

## More applications

Using what you learned in this guide, try the following, in order of difficulty:

- Let the user see as many finals again as they want.
- Write a new function, `bounded_input(message, minimum, maximum)`, that asks the user for input until they write something between the minimum and maximum values, then returns that input. Use this function to ask for numbers instead of plain `input` functions.
- Instead of calculating the user's final grades for each class right away, store the *information* for each class in a "dictionary of lists", then calculate each final at the end.
