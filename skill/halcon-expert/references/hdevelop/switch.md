# switch (Operator)

## Name

`switch` — Starts a multiway branch block.

## Signature

`switch( : : ControlExpression : )`

## Description

`switch` starts a block that allows to control the program flow
via a multiway branch.
The parameter *`ControlExpression`* must result in an integer value.
This value determines to what [`case`](case.md) label the execution jumps.
Every [`case`](case.md) statement includes one integer constant.
If the integer constant of a [`case`](case.md) statement is equal to the
calculated value of the parameter *`ControlExpression`*, the program
execution continues there.
In addition, an optional [`default`](default.md) statement can be defined as
the last jump label within a `switch` block.
The program execution jumps to this [`default`](default.md) label, if no
[`case`](case.md) constant matches the calculated *`ControlExpression`*
value.

As in the programming languages C, C++, and C#, the [`case`](case.md)
statement is a jump label and---in contrast to [`elseif`](elseif.md)---not the
begin of an enclosed block that is automatically left at the next
[`case`](case.md) or [`default`](default.md) statement.

In order to leave the `switch` block after the execution of the
code lines of a [`case`](case.md) branch, as in C or C++ a [`break`](break.md)
statement must be inserted at the end of the [`case`](case.md) branch.
[`break`](break.md) statements can be used anywhere within a
`switch` block.
This causes the program execution to continue after the closing
[`endswitch`](endswitch.md) statement.
Without a [`break`](break.md) statement at the end of a branch the program
execution “falls through” to the statements of the following
[`case`](case.md) or [`default`](default.md) branch.

If the same statements have to be executed in different cases, i.e.,
for multiple control values, several [`case`](case.md) statements with different
constant expressions can be listed one below the other.

## Parameters

**`ControlExpression`** (input_control)  integer `→`  (integer)

Integer expression that determines at which case
label the program execution is continued.

## Example (HDevelop)

```
TestStr := ''
for Index := 1 to 8 by 1
  TestStr := TestStr + '<'
  switch (Index)
  case 1:
    TestStr := TestStr + '1'
    break
  case 2:
    TestStr := TestStr + '2'
    * intentionally fall through to 3
  case 3:
    TestStr := TestStr + '3'
    * intentionally fall through to 4
  case 4:
    TestStr := TestStr + '4'
    break
  case 5:
  case 6:
    * common case branch for 5 and 5
    TestStr := TestStr + '56'
    break
  case 7:
    * continue for loop
    TestStr := TestStr + '7'
    continue
  default:
    TestStr := TestStr + 'd'
    break
  endswitch
  TestStr := TestStr + '>'
endfor
```

## Result

If the condition is correct,
`switch` (as an operator) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code is returned.

## Alternatives

`if`,
`elseif`,
`else`

## See also

`case`,
`default`,
`endswitch`,
`if`

## Module

Foundation
