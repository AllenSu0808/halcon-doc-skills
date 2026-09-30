# assign_at (Operator)

## Name

`assign_at` — Assignment of one or several values to one or several tuple elements.

## Signature

`assign_at( : : Index, Value : Result)`

## Description

`assign_at` assigns a single value to one or several
elements of a tuple, or it assigns a number of values elementwise to the
specified elements of the output tuple.
All other elements of the output tuple keep their values.
If the passed indices are out of the current range of the output tuple,
the tuple is increased and the new values are initialized to a
default value.

In the full text editor an `assign_at` operation is simply entered
with the help of the assignment operator symbol := and the
index access operator symbol [ ] following the output
variable.
The *`Index`* parameter can be any expression that evaluates to any
number of positive integer values.
The *`Value`* parameter must evaluate to exactly one value or to
the same number of indices that are provided via the *`Index`*
parameter, e.g.:

```
  Areas[Radius-1]    := Area
  Areas[0,4,|Rad|-1] := 0
  FileNames[0,2,4]   := ['f1','f2','f3']
```

The operator `assign_at` replaces and extends the modifying version
of the old [`insert`](insert.md) operator.

## Parameters

**`Index`** (input_control)  integer(-array) `→`  (integer)

Indices of the elements that have to be replaced by the new
value(s).

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6

Minimum increment:
1

**`Value`** (input_control)  tuple(-array) `→`  (integer / real / string)

Value(s) that is to be assigned.

Default:
1

**`Result`** (output_control)  tuple(-array) `→`  (real / integer / string)

Result tuple containing the assigned values.

## Result

If the expression is correct
`assign_at` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Alternatives

`assign`,
`tuple_replace`

## Module

Foundation
