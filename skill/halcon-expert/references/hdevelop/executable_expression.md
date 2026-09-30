# executable_expression (Operator)

## Name

`executable_expression` — Execute a stand-alone operation.

## Signature

`executable_expression( : : Expression : )`

## Description

The HDevelop language contains a few operations that are executed
stand-alone, i.e., not as an expression within another operator call.
The operator `executable_expression` allows to enter such stand-alone
operations into the operator window of HDevelop.
In the full text editor however, those operations are entered verbatim.

Currently, the following modifying vector operations are stand-alone and can
only be used in an executable expression:

- `.clear()`
- `.insert()`
- `.remove()`

For further details about these operations please refer to the HDevelop
User's Guide.

Even though *`Expression`* formally is presented as a control parameter,
nonetheless it is also possible to execute stand-alone operations with
iconic vectors.

## Parameters

**`Expression`** (input_control)  number-vector `→`  (real / integer / string)

Operation to be executed.

## Example (HDevelop)

```
read_image (Image1, 'fin1')
read_image (Image2, 'fin2')
ImageVector.insert(1, Image1).insert(2, Image2)
* process vector
ImageVector.clear()
```

## Result

If the values of the specified parameters are correct,
`executable_expression` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Module

Foundation
