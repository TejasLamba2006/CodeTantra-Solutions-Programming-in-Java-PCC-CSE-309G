# Unit 1 - Lesson 1 - Introduction to Java - History, Java program Structure

## Question 1

**1.1.1. What is a computer programming language?**

## Step-by-step Explanation

- A language is a way to communicate or interact.
- In this course, we use English to communicate instructions to learners.
- Computers also need instructions, and we use special languages called computer programming languages for this purpose.
- Programming languages help us represent data (like numbers, text, images) and instructions to manipulate that data.
- There are many types of programming languages. In this course, we focus on Java.
- Java is an Object-oriented programming language, which means it models data as Objects and instructions as Methods.
- Other Object-oriented languages include C++ and C#.
- Just like saying "Hello!" in English or "Holla!" in Spanish, we use programming languages to instruct computers to display messages or perform tasks.
- Example: In Java, to display "Hello!", we write a program using Java's grammar and vocabulary.

## Key Java Concepts Used

- **Source Code**: The instructions written in a programming language.
- **Java Program Structure**: Consists of classes and methods.
- **Object-oriented Programming**: Data is modeled as objects, and actions as methods.
- **Printing Output**: Using `System.out.println()` to display messages.

## Correct Statement

- The sequence of instructions (in the form of source code) written in a computer programming language is called a computer program.

## Question 2

**1.1.2. A simple program in Java**

Below is an example of a simple program written in Java programming language.

Change the text in the below code to make the program print "Hello Java" instead of "Hello C".

We will learn more about the other aspects of the below code in the later sections.

**Note:** Please don't change the package name.

## Step-by-step Explanation

- The program defines a class called `FirstProgram`.
- Inside the class, the `main` method is defined. This is the entry point for Java programs.
- The statement `System.out.println("Hello Java");` prints the text "Hello Java" to the screen.
- Only the text inside the quotes needs to be changed from "Hello C" to "Hello Java".
- The rest of the code structure remains the same.

## Key Java Concepts Used

- **Class**: Blueprint for creating objects. Here, `FirstProgram` is the class name.
- **main method**: The starting point of execution in Java.
- **System.out.println()**: Used to print output to the console.
- **String**: Sequence of characters, enclosed in double quotes.

## Correct Output

```
Hello Java
```

## Question 3

**1.1.3. What is Java?**

Java programming language was created by Sun Microsystems (now part of Oracle Inc) in 1995.

Java can be used to develop many types of software applications: games, desktop apps, web apps, embedded apps (like in watches or pens), and more.

To develop Java applications, we need JDK (Java Development Kit), which contains tools like the compiler. The compiler converts source code (.java files) into bytecode (.class files). The JVM (Java Virtual Machine) interprets bytecode and generates output. This process is called compilation.

JRE (Java Runtime Environment) contains all tools and libraries needed to execute compiled Java code.

Java became popular because compiled Java code can run on any operating system (Windows, Linux, Mac) as long as JRE is installed.

**Note:** Code written in Java is compiled using the Java compiler, which is part of JDK.

### Correct Statements

- Compiled Java code can run on any Operating System provided that OS has JRE installed on it.
- JDK is used for developing applications using Java language. It contains tools like the compiler which is used during development.

## Question 4

**1.1.4. Understanding Structure of a Java Program**

A Java program consists of one or more classes. A class is the top most building block which is given a name.

A class usually consists of data (encapsulates data) and methods which operate on that data.

The class from where execution starts contains a special method called `main()`.

General structure of a Java class (.java file):

1. License statement in comments detailing ownership
2. Package statement
3. Import statements
4. Documentation comment
5. Class or Interface definition

### Brief Notes

- **License statement**: Contains copyright and ownership info.
- **Package statement**: Declares the package/folder structure for the class. Optional, but used in large projects.
- **Import statements**: Used to include predefined classes/packages. Optional, but written before class definition.
- **Documentation comment**: Describes purpose, author, and details of the class.
- **Class/Interface definition**: Main body of Java source code. Classes use `class` keyword, interfaces use `interface` keyword.

The `main()` method is optional, but when present, acts as the starting point of execution. It instantiates objects and manages communication between them. The program ends when `main()` finishes.

### Example (Corrected Code)

```java
package q10734;
public class FirstJavaProgram {
    public static void main(String[] args) {
        System.out.println("India got its independence in 1947");
    }
}
```
