# for (Operator)

## Name

`for` — Starts a loop block that is usually executed for a fixed number of
iterations.

## Signature

`for( : : Start, End, Step : Index)`

## Description

Syntax in HDevelop: `for Index := Start to End by Step`

The `for` statement starts a loop block that is usually executed
for a fixed number of iterations.
The `for` block ends at the corresponding [`endfor`](endfor.md) statement.

The number of iterations is defined by the *`Start`* value, the
*`End`* value, and the increment value *`Step`*.
All of these parameters can be initialized with expressions or variables
instead of constant values.
Please note that these loop parameters are evaluated only once, namely,
immediately before the `for` loop is entered.
They are not re-evaluated after the loop cycles, i.e., any modifications of
these variables within the loop body will have no influence on the number
of iterations.

The passed loop parameters must be either of type `integer` or
`real`.
If all input parameters are of type `integer`, the *`Index`*
variable will also be of type `integer`.
In all other cases the *`Index`* variable will be of type `real`.

At the beginning of each iteration the loop variable *`Index`* is
compared to the *`End`* parameter.
If the increment value *`Step`* is positive, the `for` loop
is executed as long as the *`Index`* variable is less than or
equal to the *`End`* parameter.
If the increment value *`Step`* is negative, the `for` loop
is executed as long as the *`Index`* variable is greater than or
equal to the *`End`* parameter.

**Attention:** If the increment value *`Step`* is set to a
value of type `real`, it may happen that the last loop cycle is
omitted owing to rounding errors in case the *`Index`* variable is
expected to match the *`End`* value exactly in the last cycle.
Hence, on some systems the following loop is not executed---as
expected---for four times (with the *`Index`* variable set to 1.3,
1.4, 1.5, and 1.6), but only three times because after three additions the
index variable is slightly greater than 1.6 due to rounding errors.

```
  I:=[]
  for Index := 1.3 to 1.6 by 0.1
    I := [I,Index]
  endfor
```

After the execution of the loop body, i.e., upon reaching
the corresponding [`endfor`](endfor.md) statement or a [`continue`](continue.md) statement,
the increment value (as initialized at the beginning of the `for`
loop) is added to the current value of the loop counter *`Index`*.
Then, the loop condition is re-evaluated as described above.
Depending on the result the loop is either executed again or finished
in which case execution continues with the first statement after the
corresponding [`endfor`](endfor.md) statement.

A [`break`](break.md) statement within the loop---that is not covered by
a more internal block---leaves the loop immediately and execution continues
after the corresponding [`endfor`](endfor.md) statement.
In contrast, the [`continue`](continue.md) statement is used to ignore the rest of
the loop body in the current cycle and continue execution with adapting the
*`Index`* variable and re-evaluating the loop condition.

**Attention:** It is recommended to avoid modifying the
*`Index`* variable of the `for` loop within its body.

If the `for` loop is stopped, e.g., by a [`stop`](stop.md) statement or by
pressing the `Stop` button, and if the PC is placed manually by the
user, the `for` loop is continued at the current iteration as long as
the PC remains within the `for` body or is set to the [`endfor`](endfor.md)
statement.
If the PC is set on the `for` statement (or before it) and executed
again, the loop is reinitialized and restarts at the beginning.

## Parameters

**`Start`** (input_control)  number `→`  (integer / real)

Start value of the loop variable.

Default:
1

**`End`** (input_control)  number `→`  (integer / real)

End value of the loop variable.

Default:
5

**`Step`** (input_control)  number `→`  (integer / real)

Increment value of the loop variable.

Default:
1

**`Index`** (output_control)  number `→`  (integer / real)

Loop variable.

## Example (HDevelop)

```
read_image (Image, 'fabrik')
threshold (Image, Region, 128, 255)
connection (Region, ConnectedRegions)
select_shape (ConnectedRegions, SelectedRegions, 'area', 'and', 150, 99999)
area_center (SelectedRegions, Area, Row, Column)
dev_close_window ()
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
dev_display (Image)
dev_display (SelectedRegions)
dev_set_color ('white')
for Index := 0 to |Area| - 1 by 1
  set_tposition (WindowHandle, Row[Index], Column[Index])
  write_string (WindowHandle, 'Area=' + Area[Index])
endfor
```

## Result

If the values of the specified parameters are correct,
`for` (as an operator) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code is returned.

## Alternatives

`while`,
`until`

## See also

`repeat`,
`break`,
`continue`,
`endfor`

## Module

Foundation
