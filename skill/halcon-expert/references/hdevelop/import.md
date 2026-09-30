# import (Operator)

## Name

`import` — Import one or more external procedures.

## Signature

`import( : : ProcedureSource : )`

## Description

The `import` statement can be used to import additional external
procedures from within a HDevelop program. The imported procedures become
only available for the procedure that contains the `import` statement
but not for other procedures.

`import` statements may occur in any line of a procedure. The imported
procedures become only available below the `import` statement and may
be overruled by later `import` statements.

```
  proc()
  * unresolved procedure call

  import ./the_one_dir
  proc()
  * resolves to ./the_one_dir/proc.hdvp

  import ./the_other_dir
  proc()
  * resolves to ./the_other_dir/proc.hdvp
```

The parameter *`ProcedureSource`* points to the source
of the external procedures. It can either be the path of a directory that
contains the procedures and/or the procedure libraries to be used or
directly the file name of a procedure library. In both cases, the path may
either be absolute or relative. In the latter case, HDevelop interprets
the path as being relative to the file location of the procedure that
contains the `import` statement.
Thus, the location of this procedure can be included with *'.'*.
The path has to be in quotes if it
contains one or more spaces, otherwise the program line will become invalid.

Contrary to system, user-defined, and session directories HDevelop looks
only in the directory specified by an `import` statement for external
procedures but not recursively in its subdirectories.

Note, that an `import` statement is never
executed and, therefore, *`ProcedureSource`* has to be evaluated
already at the procedure's loading time. Therefore, *`ProcedureSource`*
has to be a constant expression, and, in particular, it is not possible
to pass a string variable to *`ProcedureSource`*.

However, *`ProcedureSource`* may also contain environment variables,
which HDevelop resolves accordingly. Environment variables, regardless of
the platform actually used, must always be denoted in Windows syntax, i.e.,
%VARIABLE%.

`import` neither tests whether the path *`ProcedureSource`*
exists nor whether it points to a procedure library or a directory that
contains procedures at all. Therefore, `import`
statements with nonexistent or pointless paths nonetheless stay valid
program lines, in any case.

Import paths are listed separately in HDevelop's procedure settings.
Of course, these paths can't be modified or deactivated from within the
procedure settings. Furthermore, procedures that are available only via
an `import` statement are marked with a special icon.

In the program listing, import statements are displayed and must
be entered without parenthesis in order to emphasize that the line is a
declaration and not an executable operator.

## Parameters

**`ProcedureSource`** (input_control)  string `→`  (string)

File location of the external procedures to be loaded:
either a directory or a procedure library

## Result

`import` is never executed.

## Module

Foundation
