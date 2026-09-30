# dev_error_var (Operator)

## Name

`dev_error_var` — Define or undefine an error variable.

## Signature

`dev_error_var( : : ErrorVar, Mode : )`

## Description

`dev_error_var` defines an error variable, i.e., a variable which
contains the result state of the last operator call.
*`ErrorVar`* will be 2 (
H_MSG_TRUE)
if no error had occurred.
The parameter *`Mode`* specifies whether the error variable should be
used (*1*) or not (*0*).
If an error variable is active it will be updated each time an operator
execution is finished. Thus a value is only valid until the next
call of an operator. The value can be saved by assigning it to
another variable (see example)
or by calling `dev_error_var(ErrorVar,0)`.

## Parameters

**`ErrorVar`** (input_control)  integer `→`  (integer)

Name of the variable which shall contain the error status.

Default:
'ErrorVar'

**`Mode`** (input_control)  integer `→`  (integer)

Switch the error variable on or off.

Default:
1

List of values:
0, 1

## Example (HDevelop)

```
dev_close_window ()
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
dev_error_var (Error, 1)
dev_set_check ('~give_error')
FileName := 'wrong_name'
read_image (Image, FileName)
ReadError := Error
if (ReadError != H_MSG_TRUE)
  write_string (WindowHandle, 'wrong file name: '+FileName)
endif
```

## Result

If the values of the specified parameters are correct,
`dev_error_var` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`dev_set_check`

## Possible Successors

`dev_set_check`,
`if`,
`elseif`,
`else`,
`assign`

## See also

`dev_set_check`,
`set_check`

## Module

Foundation
