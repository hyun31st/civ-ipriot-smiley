<style>

body {
    counter-reset: h2counter;
}

/* H1 - No numbering */
h1 {
    /* No counter reset or increment */
}

/* H2 - Level 1 numbering */
h2 {
    counter-reset: h3counter;
}

h2::before {
    counter-increment: h2counter;
    content: counter(h2counter) ". ";
}

/* H3 - Level 2 numbering */
h3 {
    counter-reset: h4counter;
}

h3::before {
    counter-increment: h3counter;
    content: counter(h2counter) "." counter(h3counter) " ";
}

/* H4 - Level 3 numbering (optional) */
h4 {
    counter-reset: h5counter;
}

h4::before {
    counter-increment: h4counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) " ";
}

</style>

# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## Required evidence

### Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```
![Example Running Code](docs/images/remote_settings.png)

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file

![Local Execution](docs/JJ_attachments/Local Execution.png)

If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name                    | value                                           |
   | ----------              |-------------------------|-------------------------------------------------|
   | built-in primitive type | dimmed                  | True                                            |
   | built-in composite type | WHITE<br/>GREEN<br/>RED | (255, 255, 255)<br/>(0, 255, 0)<br/>(255, 0, 0) |
   | user-defined type       | Y<br/>O                 | YELLOW<br/>BLANK                                |

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type  |
   | ------------             |-------|
   | self.pixels              | List  |
   | A member of self.pixels  | Tuple |
   | self                     | Happy |

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow | File      | First line | Line range |
   | ------------ |-----------|------------|------------|
   |  sequence    | smiley.py | WHITE = (255, 255, 255)         | 5-9        |
   |  selection   | happy.py  | self.pixels[pixel] = self.BLANK if wide_open else self.YELLOW          | 31-31      |
   |  iteration   | sad.py    | for pixel in eyes:        | 25-30      |

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used? | Example                                           |
   | ----------------------- |-------|---------------------------------------------------|
   | int                     | Yes   | eyes = [10,13,18,21]<br/>for **_pixel_** in eyes: |
   | float                   | Yes   | **_delay_** = 0.25                                |
   | str                     | No    | `__main__`                                        |
   | bool                    | Yes   | **_wide_open_** = True                            |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

> Your answer here
> <br/>Class variable is similar to global variable. It can be used in any class. However, instance variable is specific to the class.
> <br/>Due to the different levels which variables are defined, the description(wording) should reflect their purpose.
> <br/>WHITE, GREEEN, RED, YELOOW and BLANK each have unique RGB codes as tuples. These class variable ensure that other classes don't need to define them again.

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

   > Your answer here
   > <br/>When Happy class is initialized, draw_mouth() and draw_eyes() methods must be executed.

   2. What statement(s) does it execute (consider the `super` call), and what is the result?

   > Your answer here
   > <br/>In order to initialize the base class's attributes in the inherited class.

### Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:
   
> Your answer here
> <br/>They are "North Metro Software Python Coding Standards" based on PEP 8 style.
> <br/>One of method name "**def** _run_hat_gui_" is started with verb and using snake case.
> <br/>One of class name "**class** _SenseHat:_" is camel case

2. List three aspects of this convention you see applied in the code.

> Your answer here
> <br/>Constant - DEFAULT_RGB = [(255, 255, 255)] * 64
> <br/>Variable - self.led_matrix = [None] * 64
> <br/>Method - def draw_mouth(self):

3. Give two examples of organizational documentation in the code.

> Your answer here
> <br/> Introduction at the beginning of the code
> <br/>"""Mock SenseHAT class. If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of this one.)
To do that DELETE this file so that it will not shadow the sense_hat class installed in your system.
You do not need to understand this code to use it for the smiley exercise"""
import contextlib
> <br/> Comment
> <br/>time.sleep(1)  # Give the process some time to start

### Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s)  |
|------------|---------------|-------------------|
| NotReal    | Sub           | NotRealParent     |
| Smiley     | Super         | Real Parent       |
| Sad        | Sub           | Smiley            |
| Happy      | Sub           | Smiley, Blinkable |
| Blinkable  | Sub           | Abstract          |

2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

> Your answer here
> <br/> Abstraction is the most common concept in the project.
> <br/> The Smiley project involves turning on LEDs in a LED matrix. By using different patterns of on/off LEDs, we can display sad or happy faces.
> <br/> These patterns share a common feature. They are blinkable. This is why "Blinkable" is an abstract class. Each pattern is an individual class that can utilized the "Blinkable" feature.

3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

> Your answer here
> <br/> INHERITANCE
> <br/> It is to reduce writing code. The Happy and Sad classes are very similar. They only differ in their patterns to turning on LEDs.
> For example, LED colour and turning on/off LED are common methods. Once the full LED pattern for a face has been defined in Smiley class, the other classes only need to adjust the relevant LEDs.
> <br/> Using inheritance in this project significantly reduces the need to rewrite code.


### Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > Your answer here
   > <br/> The **draw_mouth** method is the key difference because it has unique pattern.
   > <br/> Sad class makes positions [49, 54, 42, 43, 44, 45] blank, while the Happy class makes positions [41, 46, 50, 51, 52, 53] blank.
2. What are the key similarities?
   > Your answer here
   > <br/> The **draw_eyes** method is the key similarity and also both classes are inherited from Smiley class.
3. What difference stands out the most to you and why?
   > Your answer here
   > <br/> The if statement. The Sad class uses a traditional way for the if statement but the Happy class defines it in a single line.
   > <br/> At first, it's hard to read it from happy class but once I get used to it, it becomes much simpler and easier to read.
4. How does this difference affect the functionality of these classes
   > Your answer here
   > <br/> I don't think there is any functionality difference between if statements.

### Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   > Your answer here
   > <br/> The Smiley class directly utilize the functionality of the SenseHat class.
   > <br/> However, The Happy and Sad class inherit from the Smiley class and include super().__init__(). They also utilize the SenseHat class.

2. Which of these classes directly interact with the SenseHat functionalities?
   > Your answer here
   > <br/>**Smiley()**
3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > Your answer here
   >

### Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.

> Your answer here
> <br/> Yes, every Smiley face (Sad or Happy) should be able to blink because blinking is an LED feature not limited a certain face type.
> <br/> Blinking a face can add emphasis for people. It can be interpreted as making the expression even happier or sadder.

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.

> Your answer here
> <br/> No, it depends on the situation or occasion.
> <br/> If the Smiley is working on an advertising sign, the interval can remain the same while the program is running.
> <br/> However, if the Smiley interacts with other features such as music or reels(short videos on YouTube or TikTok), the blinking interval will vary.

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.

> Your answer here
> <br/> The blink method is defined in both Happy and Sad classes. This method has a same feature but can behave differently depending on where it's running. For example, the Happy class sets the interval 0.25 seconds while the Sad class can set it differently. 

4. How is inheritance used in the blink method, and why is it important for polymorphism?

> Your answer here
> <br/>The blink method in Blinkable class is an abstract method not just a regular method.
> The Blinkable class cannot be instantiated by itself. It must be inherited by another class. Since it's inherited, its behavior depends on how the subclass implements it.

1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python
   def blink(self, delay=0.25):
       pass  # Replace 'pass' with your implementation
   ```

2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

![Sad Smiley Blinking](docs/JJ_attachments/main code sad blinking.png)
![Sad Smiley Blinking](docs/JJ_attachments/Sad code blinking.png)

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

  > Your answer here
  >  <br/>Adding the method was pretty easy. At this stage, the blink method is exactly same as in the Happy class. However, it can behave differently if the delay is different or if other loop conditions are  added.
  >  <br/>The main function needed to be adjusted because it was only executing the Happy class. I only changed it to instantiate the Sad class.

  ### If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

     > Your answer here
      <br/>The Blinkable  class is a subclass and also abstract class because it's inherited from the ABC(abstract) class.
      <br/>The abstraction class cannot be instantiated by itself but it used only to define a blueprint for other classes. 

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.

  > Your answer here
  > <br/>Abstract Base Class

  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

  > Your answer here
  > <br/>Abstration - It's important to find what is the most basic element from the project. The abstraction will define the element and simplify the code in the project.

  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

  > Your answer here
  > <br/>I think Python program is very powerful and also flexible. Even if the blinking feature is defined in the Blinkable class, the Sad class can have "blink" method without inheriting the Blinkable abstract class.
  > <br/>However, it's good practice and have benefit for team members to use the Blinkable class from the Sad class.

  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

  > Your answer here

  ***

  ## Refactoring

  ### Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > Your answer here
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > Your answer here
     3. Add the color blue to the appropriate class using the appropriate format and values.

  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > Your answer here

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > Your answer here

  Here's a revised version of the "Flexible Colors – Step 1" section for the smiley project, incorporating your specifications for formatting and content updates:

  ### Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.

  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.

  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

  ![Bulk Rename](screenshots/bulk_rename.png)

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***
