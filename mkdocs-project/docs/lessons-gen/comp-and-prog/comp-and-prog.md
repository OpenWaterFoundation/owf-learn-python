# Lesson / Computers, Data, and Programs #

**Level:  Basic**

**Estimated Time:  30 minutes**

* [Lesson Introduction](#lesson-introduction)
* [Prerequisites](#prerequisites)
* [Background](#background)
* [The Difference Between Data and Information](#the-difference-between-data-and-information)
* [Computer Program Input](#computer-program-input)
* [Program Logic](#program-logic)
* [Software Program as a State Machine](#software-program-as-a-state-machine)

-----------------------

## Lesson Introduction ##

This lesson provides basic information about computers, data, and programs.
There is no hands on programming in this lesson.

## Prerequisites ##

There are no prerequisites for this lesson.

## Background ##

A "computer" is ["one who computes" (see Wikipedia)](https://en.wikipedia.org/wiki/Computer_(job_description)).
For the purpose of this documentation, computers are defined as electronic devices that perform analysis
to provide useful information and/or automate tasks.

In basic terms, a computer makes decisions (creates output) based on input and a set of rules that
define how input is evaluated in order to generate output.
Input is typically provided from sensors, or data in files or databases.
Rules are typically provided by software code (a program).

Human computers use their brains to process input and make decisions, based on the experience that they have gained in life.
Electronic computers use input from sensors and data storage, along with program logic, to make decisions.

The term ["artificial intelligence" (AI) (see Wikipedia)"](https://en.wikipedia.org/wiki/Artificial_intelligence) 
refers to intelligence demonstrated by machines.
The reality is that most machines and computer programs perform tasks by following a sequence of commands
and evaluating decision points ("If A, do X, else do Y...") based on "decision trees" that match
processes defined by humans.
Even creating simple programs is a challenge and therefore true AI is a major challenge.

## The Difference Between Data and Information ##

According to [Wikipedia](https://en.wikipedia.org/wiki/Data):

*Data (singular datum) are individual units of information.
A datum describes a single quality or quantity of some object or phenomenon.
In analytical processes, data are represented by variables.*

*Although the terms "data", "information" and "knowledge" are often used interchangeably,
each of these terms has a distinct meaning.
In popular publications, data is sometimes said to be transformed into information when it is viewed in context or in post-analysis.*

It is also now common that "data" is used for single or plural.
Therefore "data is" and "data are" are generally both acceptable as plural.

For example, the current air temperature may be a single data value (21 degrees Celcius).
Is this hot or cold?  Obviously, it is comfortable to humans (21 degrees Celsius is about 70 degrees Fahrenheit).
However, it is not high enough to cook food and it may be too hot for the stability of some chemicals.
Therefore, it is important to consider context in order to translate data into information,
which can then be used for decisions.

The term "data-driven decisions" means that decisions are based on data and science,
not only feelings or "gut decision".
As will be shown in this documentation, it is important that software programs provide transparency and consistency so that complex
data and decisions are verified and presented in ways that can be trusted.

This documentation generally uses the term "data" when discussing software input,
but programs can also generate output data files, in order to process data using a sequence of programs.

## Computer Program Input ##

Computer program input must be represented in basic form that a computer program can understand, for example:

* **Information that is stored on media such as hard drives and USB flash drives** - In its most basic form,
data can be stored in binary form, which are zeros and ones that when considered in sequence represent data.
A "bit" is a single binary value 0 or 1.
A "byte" is a group of bits that represents a larger unit of information,
for example, a letter found on a keyboard.
See ["Units of information" (Wikipedia)"](https://en.wikipedia.org/wiki/Units_of_information) for more information.
64-bit operating systems are now common and use a design with [64-bit data unit size (see Wikipedia)](https://en.wikipedia.org/wiki/64-bit_computing).

* **Information is stored in a form that is human-readable** -  For example, the letters, numbers and other characters and symbols that are
used in written languages and on keyboards are represented in computers using bytes and other representations.
Whereas humans may be familiar with the written characters (such as those that you are are now reading),
computers also recognize other forms such as hexadecimal and octal codes.
See ["ASCII" (Wikipedia)](https://en.wikipedia.org/wiki/ASCII) information.
Unfortunately, the large number of human-spoken and corresponding written languages makes it difficult to 
universally integrate with computers and programs.
English and its character set are typically used to write code,
with language-specific characters used to interface with software users, for example to display information
in user interfaces.

* **Information is stored in a form that is machine-readable** - Human-readable text files can be read by software.
However, it may not be efficient to store or process.
For example, the text on this page contains the word "the" many times.
To save space in storing and transmitting this document, it might be reformatted into a form where the word "the"
is represented by a "lookup" value that is smaller than the original pattern.
Compression and decompression of information is a common computer science technique
to improve the speed of communication.

The data that are used by software programs need to be well understood by software.
For example, data must be stored as files on media (hard drive, USB thumb drive, etc.) and communicated between devices
over the internet.
Reading and writing data are some of the main functions of a program.
The term "encoding" is used to describe formatting data before it is written to a file or communicated.
The terms "decoding" and "parsing" are used to describe conversion of data as it is received or read from a file.

A "specification" is a document that describes a data format, so that it is clear how the data should be encoded and decoded.
An ["application programming interface" (API)](https://en.wikipedia.org/wiki/Application_programming_interface)
is a specification to help integrate data and software components.
For example, a specification may exist describing how to format a date,
and an API may exist describing how to provide a date to a website to request the weather forecast for a day.

Unfortunately, even simple things can become complicated, which is why there are many standard specifications.
For example, see the [ISO 8601 specification (Wikipedia)](https://en.wikipedia.org/wiki/ISO_8601) for dates and times.
It is generally best to use data specifications that are relevant, rather than inventing new ones.
However, there are certainly cases where clear standards don't exist or are difficult to adhere to,
thus requiring additional work and definition of new specifications.

## Program Logic ##

Program logic is coded as instructions that describe the rules for making decisions,
and can be defined in various forms, for example:

* **Firmware stored in devices** - Instructions for devices can be saved 
as ["firmware" (see Wikipedia)](https://en.wikipedia.org/wiki/Firmware),
for example for devices such as televisions, mobile phones, and other devices.
The implementation of [internet of things (IOT) (see Wikipedia)](https://en.wikipedia.org/wiki/Internet_of_things)
may result in many "smart" devices that rely on firmware.
Firmware is typically loaded before a device is shipped and can be updated later if necessary,
such as when a major bug is discovered in the firmware.
* **Program code** - Program code can be written and translated into forms that
computers and devices use to make decisions,
which is a topic of this documentation.
* **Instructions in Data** - Programs can be written in a way that expect additional instructions in data.
For example, Microsoft Excel worksheets can be created that use formulas that are defined by
users and saved in the Excel file (`*.xlsw`).
In this case, the computer program allows users to provide analysis logic, not just pure data.

Computer programming requires selecting a programming language, of which there are many.
However, most programming languages support common programming constructions, for example:

* variables to hold data values
* "if" statements to perform comparisons
* loop statements to repeat logic
* reading and writing data

The result of creating a program is to use the programming language's capabilities to manipulate
data with programming logic, in order to produce information that is useful.

## Software Program as a State Machine ##

A ["state machine" (see Wikipedia)](https://en.wikipedia.org/wiki/Finite-state_machine)
is a mathematical model of computation that can have a specific state at a point in time.
"State variables" are fundamental values that describe the essence of an entity.
For example, for a river basin, the state variables might include the water levels at different locations,
land use, air temperature, amount of snow, etc.
Software is like a state machine in that it can have only one state at each time while running the program.
A program that models river basins would therefore contain program code variables that represent the state variables.

Software programs manage data that is stored in files and data that is in computer memory.
The computer's memory is "addressed" by assigning an integer address to each chunk of memory.
For 64-bit computers, the chunks are aligned at 64-bit intervals.
For example:

```
var integer i = 10
```

Is a general statement that defines a variable of type `integer`, named `i`, with a value of `10`.
The computer memory address for the variable is actually a large number, and typically shown as a hexadecimal number such as `0x11110000`
(see ["Memory address" (Wikipedia)](https://en.wikipedia.org/wiki/Memory_address).
The software programmer generally does not worry about such things
but instead lets the programming tools handle the complexities.

A software program as a state machine involves defining variables that represent the "state" of a conceptual model,
with programming logic to change the state based on input, as follows:

1. The state is initialized by "hard coding" initial conditions in program code
(for example set variables to reasonable initial values).
2. The program may then further be initialized by reading data files.
3. The state is then changed by running the program over some period of time,
with input read and/or calculations performed at each time increment.
In some cases time may be irrelevant and changes to state can occur based on other inputs,
such as processing a group of data records.

Software should be repeatable, meaning that running the software with same initial state and input should result in the
same state at each step, and same output.

Implementing a software program as a state machine therefore involves conceptualizing:

* model states (variables that describe the problem)
* model input (data that drives changes in the analysis)
* model output (results from states changing due to input)
