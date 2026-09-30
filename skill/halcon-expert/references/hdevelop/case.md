# case (Operator)

## Name

`case` — Jump label that starts a branch within a [`switch`](switch.md) block.

## Signature

`case( : : Constant : )`

## Description

`case` defines a jump label within a [`switch`](switch.md) block.
It starts a branch that is executed if the value of the control expression
of the [`switch`](switch.md) statement matches the constant integer expression
that is defined in *`Constant`*.
For this parameter only constant integer expressions are accepted.
Variable expressions and other data types are not allowed.

As in the programming languages C, C++, and C# the `case` statement
does not open a block that is automatically left at the next `case`
or [`default`](default.md) statement.
In contrast, it works just like a goto label that is accessed if the label
matches.
In order to leave a `case` branch and continue execution after the
end of the [`switch`](switch.md) block, the [`break`](break.md) statement can be used
anywhere within the [`switch`](switch.md) block.

## Parameters

**`Constant`** (input_control)  integer `→`  (integer)

Constant integer expressions that determines for which value of
the switch control expression the branch is accessed.

Default:
1

## Result

`case` (as an operator) always returns 2 (
H_MSG_TRUE)
.

## Alternatives

`elseif`

## See also

`switch`,
`default`,
`endswitch`,
`if`

## Module

Foundation
