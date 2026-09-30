# dev_set_check (Operator)

## Name

`dev_set_check` — Specify the error handling in HDevelop.

## Signature

`dev_set_check( : : Mode : )`

## Description

`dev_set_check` specifies how HDevelop has to react in case of
an error, i.e., if the return state of an operator is not 2 (
H_MSG_TRUE)
.

If *`Mode`* has the value *'give_error'*---which is the
system default---an erroneous operator call will throw an exception,
that can be caught within the HDevelop program by the [`catch`](catch.md)
statement.
However, if there is no surrounding [`try`](try.md)-[`catch`](catch.md) block in the
HDevelop program and the program is executed within HDevelop, the
program execution stops at the erroneous operator and an error message box
is opened to display the error text.
In addition, the appropriate operator call is entered into the
*Operator Window*, so that the user can easily edit and possibly
correct the parameters of the erroneous operator call.
If the procedure was called from HDevEngine and the exception is
not caught within the HDevelop program, an `HDevEngineException`
object is thrown and the procedure is left.

If *`Mode`* is set to
*'~give_error'*, the error
will be ignored and the program continues with the next operator.
`dev_set_check('~give_error')`
is intended to be used in connection with
[`dev_error_var`](dev_error_var.md), which allows to check the result state that is
returned by the operator calls.

## Attention

Using the code export feature of HDevelop, the code that is generated
for this operator may have a different behavior than the related
HALCON operator.
For a detailed description of the code export of HDevelop graphics
operators into the different programming languages see in the
`“HDevelop User's Guide”` the chapter `Code Export`
-> `General Aspects of Code Generation`
-> `Graphics Windows`.

## Parameters

**`Mode`** (input_control)  string `→`  (string)

Mode of error handling.

Default:
'give_error'

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
* Now the program will stop with an exception
dev_set_check ('give_error')
read_image (Image, FileName)
```

## Result

If the values of the specified parameters are correct,
`dev_set_check` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_error_var`

## See also

`set_check`,
`try`,
`catch`,
`endtry`

## Module

Foundation
