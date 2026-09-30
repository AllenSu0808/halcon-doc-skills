# global (Operator)

## Name

`global` — Declare a global variable.

## Signature

`global( : : Declaration : )`

## Description

The `global` statement can be used to declare a global variable.
By declaring a variable as global the variable becomes visible to all other
procedures that also declare the same variable explicitly as global.

If a variable is not explicitly declared as
global inside a procedure, the variable is local within that procedure
even if there is a global variable with the same name.

The parameter *`Declaration`* contains the variable declaration
that consists of the optional keyword *'def'*, the type *'object'*
or *'tuple'*, the optional keyword *'vector'* (followed by the
desired dimension in round brackets), and the variable name.

Setting the type to *'object'* an iconic variable is declared, by
setting it to *'tuple'* a control variable is declared.

The keyword *'def'* allows to mark one declaration explicitly as the
place where the variable is defined.
In most cases this will not be necessary because in HDevelop the variable
instance is created as soon as it is declared somewhere.
However, if several procedures are exported to a programming language and if
the procedures are not exported into one output file that contains all
procedures together but into separate output files it will become necessary
to mark one of the global variable declarations
as the place where the variable is defined.
A set of procedure export files that are linked to one library
or application must contain exactly one definition of each global variable
in order to avoid both undefined symbols and multiple definitions.

In the program listing, global variable declarations are displayed and must
be entered without parenthesis in order to emphasize that the line is a
declaration and not an executable operator. The syntax is as follows:

```
  global [def] {object|tuple} [vector(<Dimension>)] <Variable Name>
```

## Parameters

**`Declaration`** (input_control)  string `→`  (string)

Global variable declaration: optional keyword *'def'*,
type, and variable name

Suggested values:
'object', 'tuple', 'def object', 'def tuple', 'object vector(1)', 'tuple vector(1)', 'def object vector(1)', 'def tuple vector(1)'

## Result

`global` is never executed.

## Module

Foundation
