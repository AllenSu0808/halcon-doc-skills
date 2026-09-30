# assign (Operator)

## Name

`assign` — Assign a new value to a variable.

## Signature

`assign( : : Input : Result)`

## Description

`assign` assigns a new value to a variable.

In the full text editor, an assignment is simply entered with the help of the
assignment operator :=, e.g.:

```
  u := sin(x) + cos(y)
```

This is equivalent to the C syntax assignment:

```
  u = sin(x) + cos(y);
```

If the operator window is used for entering an assignment, `assign`
must be entered into the operator combo box as an operator name.
This opens the parameter area, where the parameter *`Input`* represents
the expression that has to be evaluated to one value and assigned to the
variable, i.e., this is the right side of the assignment.
The parameter *`Result`* gets the name of the variable, i.e., this
is the left side of assignment.

## Attention

In addition to the parameter type control, which is indicated in the
parameter description, `assign` also supports iconic variables
and vector variables. For an assignment, the parameter types of the
two parameters *`Input`* and *`Result`* must be identical.
For the assignment of iconic objects, the operator [`copy_obj`](copy_obj.md) is
used internally.

## Parameters

**`Input`** (input_control)  real(-array) `→`  (real / integer / string)

New value.

Default:
1

**`Result`** (output_control)  real(-array) `→`  (real / integer / string)

Variable that has to be changed.

## Example (HDevelop)

```
Tuple1 := [1,0,3,4,5,6,7,8,9]
Val := sin(1.2) + cos(1.2)
Tuple2 := []
```

## Result

If the expression is correct
`assign` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Alternatives

`insert`

## Module

Foundation
