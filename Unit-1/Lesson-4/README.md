````markdown
# Unit 1 - Lesson 4 - Syntax of main(), Command-line arguments, and `println()`

### 4.1.1. Introduction to main method

- The Java program execution starts at a special method named `main`.
- The `main` method must have the exact signature to be recognized by the JVM: `public static void main(String[] args)`.
- `public` allows the JVM to call it from outside, `static` means it belongs to the class, and `void` indicates no return value.
- `String[] args` is an array containing command-line arguments supplied when the program runs.
- If the `main` signature is different (missing `static`, wrong parameter type, or different name), the JVM will not run the program even if it compiles.

Example (correct `main`):
```java
package q10755;
public class PrintHello {
 public static void main(String[] args) {
  System.out.println("Hello, I am learning Java!");
 }
}
```

### 4.1.2. Error in main method syntax (Fix and explanation)

Identify the error and correct the code. The common mistakes are:
- Wrong capitalization (`Public` instead of `public`)
- Wrong parameter type (`String args` instead of `String[] args`)
- Missing semicolon after `System.out.println(...)`

Problem (example from CodeTantra):
```java
package q10756;
public class PrintHello{
    Public static void main(String[] args){
        System.out.println("Hello, I am learning Java!")
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10756;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

Explanation:
- `Public` is not valid — Java keywords are lowercase; use `public`.
- The `main` parameter must be an array: `String[] args`.
- Every statement must end with a semicolon (`;`).

### 4.1.3. Error in main method syntax (CodeTantra question `q10757`)

Problem (as given):
```java
package q10757;
public class PrintHello {
    public static VOID main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10757;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

What was wrong and why:
- `VOID` is not a Java keyword — Java is case-sensitive; the correct keyword is `void` (all lowercase).
- The rest of the code is fine (package name must not be changed as requested).

Quick notes for submission:
- Keep the `package q10757;` line unchanged.
- Ensure the file is saved as `PrintHello.java` inside the folder matching the package (e.g., `q10757`).

### 4.1.4. Error in main method syntax (CodeTantra question `q10758`)

Problem (as given):
```java
package q10758;
public class PrintHello {
    puublic sstatic vooid mmmmain(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10758;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

What was wrong and why:
- Several identifiers were misspelled: `puublic` → `public`, `sstatic` → `static`, `vooid` → `void`, and `mmmmain` → `main`.
- Java is case-sensitive and requires exact keywords; misspellings cause compilation errors.
- The package line must remain `package q10758;` as requested.

Quick notes for submission:
- Save this as `PrintHello.java` inside a folder named `q10758` and compile with `javac q10758\PrintHello.java`.

### 4.1.5. Error in main method syntax (CodeTantra question `q10759`)

Problem (as given):
```java
package q10759;
public class PrintHello {
    public static void main(STRING[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10759;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

What was wrong and why:
- `STRING` (all uppercase) is not the correct type name — Java type names are case-sensitive; the standard type is `String` with an initial capital and the rest lowercase.
- The rest of the code is correct; keep the `package q10759;` line unchanged per the instruction.

Quick notes for submission:
- Save this file as `PrintHello.java` inside a folder named `q10759` and compile with:
```powershell
javac q10759\PrintHello.java
java -cp . q10759.PrintHello
```

### 4.1.6. Error in main method syntax (CodeTantra question `q10760`)

Problem (as given):
```java
package q10760;
public class PrintHello {
    p s v m   (S[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10760;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

What was wrong and why:
- The method line was missing the full keywords and correct identifiers. The JVM expects the exact `public static void main(String[] args)` signature.
- `p s v m` appears to be fragmented keywords: `public static void main`.
- `(S[] args)` uses `S` instead of `String` and is missing the parameter name — correct is `String[] args`.
- Keep the `package q10760;` line unchanged per instructions.

Quick notes for submission:
- Save this file as `PrintHello.java` inside a folder named `q10760` and compile with:
```powershell
javac q10760\PrintHello.java
java -cp . q10760.PrintHello
```

### 4.1.8. Error in main method syntax (CodeTantra question `q10790`)

Problem (as given):
```java
package q10790;
public class PrintHello {
    main() {
        System.out.println("Hello, I am learning Java!");
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10790;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

What was wrong and why:
- The `main` method is missing the required signature. It must be declared as `public static void main(String[] args)` for the JVM to locate the entry point.
- `main()` with no parameters and no return type will not be recognized at runtime.

Quick notes for submission:
- Save this file as `PrintHello.java` inside a folder named `q10790` and compile with:
```powershell
javac q10790\PrintHello.java
java -cp . q10790.PrintHello
```

### 4.1.9. Fill in the missing code (CodeTantra question `q10791`)

Problem (as given):
```java
package q10791;
public class PrintHello {
    (){
        System.out.println("Hello, I am learning Java!");
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10791;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

What was missing and why:
- The code was missing the `main` method signature entirely — it showed an anonymous/empty parentheses block. The JVM requires `public static void main(String[] args)` as the program entry point.

Quick notes for submission:
- Save this file as `PrintHello.java` inside a folder named `q10791` and compile with:
```powershell
javac q10791\PrintHello.java
java -cp . q10791.PrintHello
```

### 4.1.7. Error in main method syntax (CodeTantra question `q10785`)

Problem (as given):
```java
package q10785;
public class PrintHello {
     main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10785;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello, I am learning Java!");
    }
}
```

What was wrong and why:
- The method declaration is missing the access modifier and return type. The entry point must be `public static void main(String[] args)`.
- Without `public static void`, the JVM will not recognize `main` as the program entry point.

Quick notes for submission:
- Save this file as `PrintHello.java` inside a folder named `q10785` and compile with:
```powershell
javac q10785\PrintHello.java
java -cp . q10785.PrintHello
```

### 4.1.10. Introduction to main method (command-line arguments)

The Java programs can be passed arguments on the command line while executing. These arguments are made available in a `String` array, which is passed into the `main` method.

Consider the following code snippet that demonstrates the usage of command-line arguments:

```java
public class CommandLineArgumentsDemo {
    public static void main(String[] args) {
        System.out.println("args.length : " + args.length);
        System.out.println("args[0] : " + args[0]);
        System.out.println("args[1] : " + args[1]);
        System.out.println("args[2] : " + args[2]);
        System.out.println("args[3] : " + args[3]);
    }
}
```

Assume that the program is executed with four command-line arguments.

Question: What is the purpose of the `main` method in the given code?

- Correct answer: It serves as the entry point of the program and executes the code.

Explanation:
- The `main` method is the JVM entry point. When you run `java ClassName`, the JVM calls `public static void main(String[] args)` to start execution.
- In this snippet `main` prints the number of arguments (`args.length`) and the first four arguments — that is the work it performs after being invoked by the JVM.
- The other options are specific behaviors or effects (for example, printing `args.length`), but the primary role of `main` is to act as the program's entry point and execute code.

Edge-case / safety note:
- If the program is run with fewer than four arguments, accessing `args[0]`..`args[3]` will throw `ArrayIndexOutOfBoundsException`. Always check `args.length` before indexing.

Safer version (prints up to 4 arguments only if present):

```java
public class CommandLineArgumentsDemoSafe {
    public static void main(String[] args) {
        System.out.println("args.length : " + args.length);
        for (int i = 0; i < args.length && i < 4; i++) {
            System.out.println("args[" + i + "] : " + args[i]);
        }
    }
}
```

Run example (PowerShell):
```powershell
javac CommandLineArgumentsDemoSafe.java
java CommandLineArgumentsDemoSafe one two three four
```

### 4.1.11. Understanding Arguments (CodeTantra question `q10793`)

The below code demonstrates how command line arguments are passed to a class called `CommandLineArgumentDemo`:

```text
>> java CommandLineArgumentDemo Red Blue Green
```

In the above code:
1. the first argument `Red` can be accessed as `args[0]`
2. the second argument `Blue` can be accessed as `args[1]`
3. the third argument `Green` can be accessed as `args[2]`

Assume that three command line arguments will be passed to the below class with name `CommandLineArgumentDemo`.
Write code in the `main(String[] args)` method to print only the second argument.

Problem (as given):
```java
package q10793;
public class CommandLineArgumentDemo {
    public static void main(String[] args) {
        //Write the code fragment in the below println(     ) method to print only the second argument
        System.out.println(    );
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10793;
public class CommandLineArgumentDemo {
    public static void main(String[] args) {
        // the second argument is at index 1
        System.out.println(args[1]);
    }
}
```

Explanation:
- Command-line arguments are zero-indexed: the first argument is `args[0]`, the second is `args[1]`.
- The code prints only the second argument as requested.

Quick notes for submission:
- Save this file as `CommandLineArgumentDemo.java` inside a folder named `q10793` and compile with:
```powershell
javac q10793\CommandLineArgumentDemo.java
java -cp . q10793.CommandLineArgumentDemo Red Blue Green
```

### 4.1.12. Understanding Command line arguments (CodeTantra question `q10794`)

Assume that five command line arguments will be passed to the below class with name `CommandLineArgumentDemo`.
Write code in the `main(String[] args)` method to print only the fourth argument.

Problem (as given):
```java
package q10794;
public class CommandLineArgumentDemo {
    public static void main(String[] args) {
        //Write the code fragment in the below println(     ) method to print only the fourth argument
        System.out.println(    );
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10794;
public class CommandLineArgumentDemo {
    public static void main(String[] args) {
        // the fourth argument is at index 3
        System.out.println(args[3]);
    }
}
```

Explanation:
- Command-line arguments are zero-indexed: the first argument is `args[0]`, so the fourth is `args[3]`.

Quick notes for submission:
- Save this file as `CommandLineArgumentDemo.java` inside a folder named `q10794` and compile with:
```powershell
javac q10794\CommandLineArgumentDemo.java
java -cp . q10794.CommandLineArgumentDemo a b c d e
```

### 4.1.13. Understanding Command line arguments (CodeTantra question `q10795`)

Assume that five command line arguments will be passed to the below class with name `CommandLineArgumentDemo`.
Write code in the `main(String[] args)` method to print only the first argument.

Problem (as given):
```java
package q10795;
public class CommandLineArgumentDemo {
    public static void main(String[] args) {
        //Write the code fragment in the below println(     ) method to print only the first argument
        System.out.println(    );
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10795;
public class CommandLineArgumentDemo {
    public static void main(String[] args) {
        // the first argument is at index 0
        System.out.println(args[0]);
    }
}
```

Explanation:
- Command-line arguments are zero-indexed: the first argument is `args[0]`.

Quick notes for submission:
- Save this file as `CommandLineArgumentDemo.java` inside a folder named `q10795` and compile with:
```powershell
javac q10795\CommandLineArgumentDemo.java
java -cp . q10795.CommandLineArgumentDemo a b c d e
```

### 4.1.14. Understanding Command line arguments (CodeTantra question `q10796`)

Assume that five command line arguments will be passed to the below class with name `CommandLineArgumentDemo`.
Write code in the `main(String[] args)` method to print only the fifth argument.

Problem (as given):
```java
package q10796;
public class CommandLineArgumentDemo {
    public static void main(String[] args) {
        //Write the code fragment in the below println(     ) method to print only the fifth argument
        System.out.println(    );
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10796;
public class CommandLineArgumentDemo {
    public static void main(String[] args) {
        // the fifth argument is at index 4
        System.out.println(args[4]);
    }
}
```

Explanation:
- Command-line arguments are zero-indexed: the first argument is `args[0]`, so the fifth is `args[4]`.

Quick notes for submission:
- Save this file as `CommandLineArgumentDemo.java` inside a folder named `q10796` and compile with:
```powershell
javac q10796\CommandLineArgumentDemo.java
java -cp . q10796.CommandLineArgumentDemo a b c d e
```

## 4.2. Syntax of println method

### 4.2.1. Example for printing Hello

Problem (CodeTantra `q35959`):
```java
package q35959;
public class PrintHello {
    public static void main(String[] arg) {
        system.outprintln("Java");
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q35959;
public class PrintHello {
    public static void main(String[] arg) {
        System.out.println("Java");
    }
}
```

What was wrong and why:
- Java is case-sensitive: `system` should be `System` (capital S).
- The print method must be `System.out.println(...)` — the original used `outprintln` without the dot between `out` and `println`.
- The corrected line `System.out.println("Java");` prints the text `Java` followed by a newline.

Quick notes for submission:
- Keep the `package q35959;` line unchanged.
- Save this as `PrintHello.java` inside a folder named `q35959` and run:
```powershell
javac q35959\PrintHello.java
java -cp . q35959.PrintHello
```

### 4.2.2. Correct the Error

Problem (CodeTantra `q10762`):
```java
package q10762;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println(Hello);
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10762;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

What was wrong and why:
- String literals must be enclosed in double quotes. `Hello` without quotes is treated as an identifier (variable/class) and will cause a compilation error.

Quick notes for submission:
- Keep the `package q10762;` line unchanged.
- Save as `PrintHello.java` inside a folder named `q10762` and run:
```powershell
javac q10762\PrintHello.java
java -cp . q10762.PrintHello
```

### 4.2.3. Correct the Error

Problem (CodeTantra `q10763`):
```java
package q10763;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello")
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10763;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

What was wrong and why:
- The statement was missing a terminating semicolon (`;`) after the `System.out.println("Hello")` call. Every Java statement must end with a semicolon.
- Also ensure parentheses and quotes are balanced; the corrected line is `System.out.println("Hello");`.

Quick notes for submission:
- Keep the `package q10763;` line unchanged.
- Save as `PrintHello.java` inside a folder named `q10763` and run:
```powershell
javac q10763\PrintHello.java
java -cp . q10763.PrintHello
```

### 4.2.4. Correct the Error

Problem (CodeTantra `q10764`):
```java
package q10764;
public class PrintHello {
    public static void main(String[] args) {
        system.out.println("Hello");
    }
}
```

Corrected code (copy-paste this into the platform):
```java
package q10764;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

What was wrong and why:
- Java is case-sensitive: `system` (lowercase) is not the `System` class. The JVM needs the `System` class (capital `S`) to access `out` and `println`.
- Correct form: `System.out.println("Hello");`.

Quick notes for submission:
- Keep the `package q10764;` line unchanged.
- Copy-paste the corrected code into the platform's editor for `q10764` and submit.

### 4.2.5. Understanding the difference between `print` and `println`

Explanation and examples:
- `System.out.print(...)` prints the text but does not add a newline at the end. The next output will continue on the same line.
- `System.out.println(...)` prints the text and then adds a newline, so subsequent output appears on the next line.

Example (CodeTantra `q10765`):
```java
package q10765;
public class PrintVsPrintln {
    public static void main(String[] args) {
        System.out.print("Hello");
        System.out.print(" ");
        System.out.print("World");
        System.out.println("!");
        System.out.println("Next line");
    }
}
```

Expected output:
```
Hello World!
Next line
```

Why this matters:
- Use `print` when you want to continue printing on the same line (for formatted output or building a line gradually).
- Use `println` when you want to finish a line and move to the next one (common for simple messages and logs).

Quick notes for submission:
- Keep the `package q10765;` line unchanged.
- Save as `PrintVsPrintln.java` inside a folder named `q10765` and run:
```powershell
javac q10765\PrintVsPrintln.java
java -cp . q10765.PrintVsPrintln
```

### 4.2.6. Correct the Error

Problem (CodeTantra `q10766`):
```java
package q10766;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Value = " + 10 + 20);
    }
}
```

Question: What will this print? If it's not the intended result `Value = 30`, fix the code so it prints `Value = 30`.

Explanation and corrected code (copy-paste this into the platform):
- The expression `"Value = " + 10 + 20` is evaluated left-to-right. First `"Value = " + 10` becomes the string `"Value = 10"`, then `+ 20` concatenates to produce `"Value = 1020"`.
- To get arithmetic before concatenation, parenthesize the addition: `"Value = " + (10 + 20)`.

Corrected code:
```java
package q10766;
public class PrintHello {
    public static void main(String[] args) {
        System.out.println("Value = " + (10 + 20));
    }
}
```

Expected output:
```
Value = 30
```

Quick notes for submission:
- Keep the `package q10766;` line unchanged.
- Save as `PrintHello.java` inside a folder named `q10766` and run:
```powershell
javac q10766\PrintHello.java
java -cp . q10766.PrintHello
```

