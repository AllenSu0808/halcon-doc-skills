# insert (Operator)

## Name

`insert` — Assignment of a value to a tuple element.

## Warning

**`insert` is obsolete and is only provided for
reasons of backward compatibility.
The modifying version of the `insert` operator was replaced by the
operator [`assign_at`](assign_at.md).
This operator uses the same notation in the full text editor, so that it is
used automatically.
The non-modifying version of the `insert` operator is replaced by the
new operator [`tuple_replace`](tuple_replace.md).**

## Signature

`insert( : : Input, Value, Index : Result)`

## Description

`insert` assigns a single value to a specific element of a tuple.

In the full text editor an insert operation is simply entered with the help
of the assignment operator sign := and the index access
operator sign [ ] for the result variable, e.g.:

```
  Areas[Radius-1] := Area
```

If the operator window is used for entering the insert operator,
`insert` must be entered into the operator combo box as the
operator name.
This opens the parameter area, where the parameter *`Value`* represents
the expression that has to be evaluated to one value and assigned to the
element at position *`Index`* within the tuple *`Input`*.
The parameter *`Result`* gets the name of the variable where the result
has to be stored.

If the input tuple that is passed via the parameter *`Input`* and the
output tuple that is passed in *`Result`* are identical (and only in
that case), the `insert` operator is listed and can be written in the
full text editor in the above assignment notation.
In this case, the input tuple is modified and the correct operator notation
for above assignment would be:

```
   insert (Areas, Area, Radius-1, Areas)
```

If the *`Input`* tuple and the *`Result`* tuple differ, the input
tuple will not be modified.
In this case, within the program listing only the operator notation can be
used:

```
   insert (Areas, Area, Radius-1, Result)
```

This is the same as:

```
  Result := Areas
  Result[Radius-1] := Area
```

Please note that the operator `insert` will not increase the tuple
if the tuple already stores a value at the passed index.
Instead of that the element at the position *`Index`* will be replaced.
Hence, for the *`Value`* parameter exactly one single value (or an
expression that evaluates to one single value) must be passed.

If the passed *`Index`* parameter is beyond the current tuple size,
the tuple will be increased to the required size. The tuple elements
that were inserted between the hitherto last element and the new element
are undefined.

## Parameters

**`Input`** (input_control)  real(-array) `→`  (real / integer / string)

Tuple, where the new value has to be inserted.

Default:
[]

**`Value`** (input_control)  real `→`  (real / integer / string)

Value that has to be inserted.

Default:
1

Value range:
`0
≤
Value
≤
1000000`

**`Index`** (input_control)  integer `→`  (integer)

Index position for new value.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6

Minimum increment:
1

**`Result`** (output_control)  real(-array) `→`  (real / integer / string)

Result tuple with inserted values.

## Result

If the expression is correct
`insert` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Alternatives

`assign`

## Module

Foundation
