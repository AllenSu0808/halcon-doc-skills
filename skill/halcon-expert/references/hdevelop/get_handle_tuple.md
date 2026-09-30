# get_handle_tuple (Operator)

## Name

`get_handle_tuple` — Retrieve a tuple associated with a key from a handle.

## Signature

`get_handle_tuple( : : Handle, Key : Tuple)`

## Description

`get_handle_tuple` retrieves a tuple associated with the *`Key`*
from *`Handle`* and returns it in *`Tuple`*.
The list of keys supported by a handle can be queried with
[`get_handle_param`](get_handle_param.md).

Note that this operator is provided only for implementing generic
debug and inspection mechanisms.
The keys returned for certain handle types can change without notice.
Additionally, some handle types might not be supported by this operator.
Also, this operator is not optimized for performance.
To obtain more reliable information about a handle in a program, it is
strongly recommended to use the operators specialized for the particular
handle type, such as [`get_object_model_3d_params`](get_object_model_3d_params.md),
[`get_generic_shape_model_param`](get_generic_shape_model_param.md) etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Handle`** (input_control)  handle `→`  (handle)

Handle of which to get the key.

**`Key`** (input_control)  string `→`  (string / integer)

Key to get.

Number of elements:
Key == 1

Restriction:
`length(Key) > 0`

**`Tuple`** (output_control)  tuple(-array) `→`  (string / integer / real)

Control value of the key.

## Result

If the parameters are valid, the operator `get_handle_tuple`
returns the value 2 (
H_MSG_TRUE)
.
If the handle is invalid or does not support the given key, or if the
key references an iconic object instead of a tuple, an exception is raised.

## Possible Predecessors

`get_handle_param`

## Alternatives

`get_handle_object`

## See also

`get_handle_param`,
`get_handle_object`

## Module

Foundation
