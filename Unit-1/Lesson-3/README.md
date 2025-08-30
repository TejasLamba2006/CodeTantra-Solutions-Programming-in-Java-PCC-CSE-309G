# Unit 1 - Lesson 3 - Basics of Java Syntax – Comment Lines, Identifiers, Statements, Braces, Parenthesis

## 3.1. Basics of Java Syntax

### 3.1.1. Java program structure

A Java program is usually composed of multiple lines. Each line is composed of one or a combination of the below three input elements:

1. Comments
2. Whitespace characters
3. Tokens

A comment is a sequence of non-executable characters. There are three types of comments in Java which we will learn later.

#### Whitespace characters in Java

- Space ’ ’ (ASCII SP) produced by pressing spacebar
- Tab ’\t’ (ASCII HT) produced by pressing the tab key
- Form Feed character ’\f’ (ASCII FF) usually used as the page separator char between lines/paragraphs
- Line Terminator chars (used to separate two lines) – produced by pressing Enter key:
  - Line Feed - ’\n’ (ASCII LF also called NL - New Line) - used in all Unix and Mac OS X systems
  - Carriage Return - ’\r’ (ASCII CR) – used in MAC OS 9 and below
  - Carriage Return followed by Line Feed- ’\r\n’ (ASCII CRLF) – used in Windows systems

All other input elements other than comments and whitespace are called tokens. Tokens are further classified as:

- **Identifiers**: Names used to refer or identify (variables, methods, classes)
- **Keywords**: Reserved words in Java (e.g., public, new, for, if)
- **Literals**: Fixed values assigned in source code (primitive, String, null)
- **Operators**: 38 different operators (e.g., =, >, <, ==, >=)
- **Separators**: 12 separators (e.g., (), {}, [], ;, ,, ., ... , @, ::)

#### Example Code

```java
public class Test {
    public int sum(int num1, int num2) {
        return num1 + num2;
    }
}
```

#### Correct Statements

- The token `Test` which is the name of the class is called an Identifier.
- The token `sum` which is the name of the method is called an Identifier.

#### Incorrect Statements

- The tokens `num1` and `num2` are **not** Keywords; they are Identifiers.
- The open brace `{` and the close brace `}` are **not** Operators; they are Separators.

### 3.1.2. Usage of Spaces and Tabs

**Spaces** and **Tabs** are very important for code formatting in Java.

- An empty space is used as a separator between two tokens.
- A tab is used only to indent lines.

Whenever a new block of code starts after the opening brace `{`, the lines inside that block should be indented by one level (one tab) compared to the line which contains the opening brace.

**Note:** Usually after an opening brace `{`, pressing ENTER moves to the next line, where a tab is automatically inserted for indentation.

Below example shows the usage of spaces and tabs:

```java
package q35949;

public class SpacesAndTabsDemo {
  public static void main(String[] args) {
   for (int i = 0; i < 5; i++) {
    System.out.println("i = " + i);
   }
  }
}
```

- Orange borders mark spaces
- Pink borders mark tabs

Type the above example code in the provided Editor and observe the output.

**Note:** Please don't change the package name.

### 3.1.3. Three types of comments in Java

In Java, there are three types of comments:

1. **End-of-line comment**: Starts with `//` and the content following `//` till the end of that line is a comment. Also called single-line comment.
2. **Traditional comment**: Starts with `/*` and ends with `*/`, the content between is a comment. Also called multi-line comment.
3. **Java Doc comment**: Starts with `/**` and ends with `*/`, the content between contains Java documentation information.

Below code example shows all three types of comments:

```java
package q35952;
/*
  =====================================================
  Code by Tejas
  =====================================================
*/

/**
 * This class has an example code for the addition operator
 * @author James Gosling
 **/
public class TestAddition {
    
    public int sum(int num1, int num2) {
         //This is an example of a traditional comment,
           //also called a star-comment or multi-line comment
        
        return num1 + num2;
    }//end of the method sum
    
    public static void main(String[] args) {
        TestAddition example = new TestAddition();
        int num1 = 5;
        int num2 = 10;
        int result = example.sum(num1, num2);
        System.out.println("Sum: " + result);
    }
}


```

#### Important Points Regarding Comments

- There should not be a space between `//` in end-of-line comment and between `/*`, `/**`, and `*/` in standard and Java Doc comments.
- Comments do not nest. For example, `/*` and `*/` have no special meaning inside a `//` comment, and vice versa.
- Do not write comments inside character literals. Comments inside String literals are part of the String's content.

**Note:** Please don't change the package name.

### 3.1.4. Correct the Error

In English, we use a period (.) to terminate a statement. In Java, a semicolon (;) is used to terminate a statement.

For example:

```java
int x = 3;
int y = x + 4;
System.out.println("Holla!");
```

If we miss the semicolon at the end of a statement, it is a syntax error and the Java compiler will flag an error.

#### Example with Error

```java
package q10800;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello") // Missing semicolon here
    }
}
```

#### Corrected Code

```java
package q10800;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello"); // Semicolon added
    }
}
```

**Note:** Please don't change the package name.

### 3.1.5. Correct the Error in Syntax

Identify the error and correct it.

**Note:** Please don't change the package name.

#### Error

- The statement `String text4 = ", I am learning Java"` is missing a semicolon at the end.

#### Corrected Code

```java
package q10801;
public class PrintHello {
    public static void main(String[] args) {
        String text1 = "He";
        String text2 = "llo";
        String text3 = text1 + text2;
        String text4 = ", I am learning Java";
        String text5 = text3 + text4;
        System.out.println("text5 = " + text5);
    }
}
```

### 3.1.6. Missing Parenthesis

In Java, a method call is followed by an open `(` and close `)` parenthesis. The arguments that the method accepts are passed in between these parenthesis.

For example:

```java
System.out.println("Good Morning");
```

#### Error

- The code is missing a closing parenthesis in the method call.

#### Corrected Code

```java
package q10802;
public class Test {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

**Note:** Please don't change the package name.

### 3.1.7. Correct the Error

Identify the error in the given code and correct it.

**Note:** Please don't change the package name.

#### Error

- There is an extra closing parenthesis in the method call.

#### Corrected Code

```java
package q10803;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

### 3.1.8. Correct the Error

Find the error and correct the code.

**Note:** Please don't change the package name.

#### Error

- The statement `System.out.println("Hello, I am learning Java!"` is missing a closing parenthesis and a semicolon.

#### Corrected Code

```java
package q10804;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

### 3.1.9. Understanding usage of braces

In Java, code statements are written in code blocks. A code block starts with an open brace `{` and ends with a close brace `}`.

For example:

```java
public class A {
    int x = 2;
    public static void main(String[] args) {
        System.out.println("Holla!");
    }
}
```

#### Error

- The code is missing a closing brace for the `main` method and the class.

#### Corrected Code

```java
package q10805;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

**Note:** Please don't change the package name.

### 3.1.10. Correct the Error

Find the error and correct it in the code.

**Note:** Please don't change the package name.

#### Error

- The code is missing closing braces for the `main` method and the class.

#### Corrected Code

```java
package q10806;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

### 3.1.11. Correct the Error in Syntax

Find the error and correct it in the code.

**Note:** Please don't change the package name.

#### Error

- The class and method declarations are missing braces `{}`.

#### Corrected Code

```java
package q10807;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

---

### 3.1.12. Correct the Error in Syntax

Find the errors in the given code and correct it.

**Note:** Please don't change the package name.

#### Errors

- The string assignment for `text2` is missing a closing quote and semicolon.

#### Corrected Code

```java
package q10808;
public class PrintHello {
    public static void main(String[] args) {
        String text1 = "He";
        String text2 = "llo";
        String text3 = text1 + text2;
        System.out.println("text3 = " + text3);
    }
}
```
