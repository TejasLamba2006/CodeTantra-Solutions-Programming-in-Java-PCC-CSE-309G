# Lesson 2: Java Program Life Cycle

# Topic 1: Java Program Execution and JDK /JRE

## Question

**2.1.1. Java Program Life Cycle**

Click on the below Live Demo button to learn the steps involved in writing and executing a Java program.

After learning from the Live Demo, select all correct statements given below:

## Step-by-step Explanation

- Java source code is written and saved in a file with a `.java` extension.
- The Java compiler uses the Java source file and generates a file with `.class` extension.
- The file with `.class` extension is called a Java class file.
- The Java class file contains the Java bytecode, which is executed by the Java Virtual Machine (JVM).

## Key Java Concepts Used

- **Source Code**: Written in `.java` files.
- **Compiler**: Converts `.java` files to `.class` files (bytecode).
- **JVM**: Executes bytecode from `.class` files.
- **Bytecode**: Intermediate code for platform independence.

## Correct Statements

- The Java compiler uses the Java source file and generates file with `.class` extension.
- The file with `.class` extension is called as Java class file.
- The Java class file contains the Java bytecode, which is executed by the Java Virtual Machine (JVM).

The statement "Java source code is written and saved in a file with .class extension." is incorrect. Java source code is saved in a file with a `.java` extension.

---

## Question 2

**2.1.2. What is Java Runtime Environment?**

JRE stands for Java Runtime Environment.

Java Runtime Environment (JRE) is the essential piece of software required to run any Java program on an operating system.

JDK (Java Development Kit) contains JRE along with other tools like compilers needed during development.

JRE contains only those tools and libraries essential for running a Java program.

JDK and JRE are available as separate downloads. Installing JDK also installs JRE, but installing JRE alone does not provide compilers and other development tools.

To write and compile Java programs, JDK is needed. To run compiled Java programs, JRE is sufficient.

JRE includes:

- JVM (Java Virtual Machine)
- Browser plugin for running Java Applets
- Java class libraries (standard Java classes used during execution)

### Correct Statement

- Java class libraries contain the class files of standard Java classes required for running Java Applications or Applets.

The other statements are incorrect:

- JRE is not used for compiling Java source code to class files (JDK is needed for compilation).
- Browser plugin does not contain the Java Compiler.
- Java code cannot be run without a JVM.

# Topic 2: Syntax of simple Class

## 2.2.1. How to write an Empty Student Class?

This is how a simple class is written in Java. We will learn more about classes in detail in later sections.

- The keywords `public` and `class` are always written in lowercase.
- The class name, such as `Student`, should always start with a capital letter.
- Keywords are words with special meaning in Java, and all are lowercase.

### Example (Corrected Code)

```java
package q10737;
public class Student {
    public static void main(String args[]) {
        try {
            Class<?> clazz = Class.forName("q10737.Student");
            System.out.println("class Student found");
        } catch(ClassNotFoundException cnfe) {
            try {
                Class<?> badClazz = Class.forName("q10737.student");
                System.out.println("class student found");
            } catch(ClassNotFoundException cnfe1) {
                System.out.println("class Student not found");
            }
        }
    }
}
```

#### Key Points

- Use `class` (not `Class`) keyword in lowercase.
- Class names should start with a capital letter.
- Package name should match the folder structure.
- This example demonstrates an empty class with a main method for testing class existence.

## 2.2.2. Error in Spelling

Identify the error and correct the code.

**Note:** Please don't change the package name.

### Error

- The keyword `Public` is incorrectly capitalized. In Java, all keywords are lowercase.

### Corrected Code

```java
package q10751;
/*
  =====================================================
  Code by Tejas
  =====================================================
*/

public class Student {

}
```

#### Key Point

- Use `public` (not `Public`) in lowercase for the class declaration.

## 2.2.3. Error in case

Identify the error in the case used in the name of the class and correct it.

**Note:** Please don't change the package name.

### Error

- The class name `student` should start with a capital letter. In Java, class names should follow PascalCase (first letter capitalized).

### Corrected Code

```java
package q10754;
public class Student {

}
```

#### Key Point

- Always start class names with a capital letter (PascalCase).

## 2.2.4. Error in the spelling of a keyword

Below code contains an empty class declaration with class name `Test`.

However there is an error in the code below, identify and correct the error.

**Note:** Please don't change the package name.

### Error

- The keyword `Class` is incorrectly capitalized. In Java, all keywords are lowercase.

### Corrected Code

```java
package q11602;
public class Test {

}
```

#### Key Point

- Use `class` (not `Class`) in lowercase for the class declaration.
