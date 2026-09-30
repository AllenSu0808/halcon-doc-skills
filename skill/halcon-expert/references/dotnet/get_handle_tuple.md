# GetHandleTuple (Operator)

## Name

`GetHandleTuple` — Retrieve a tuple associated with a key from a handle.

## Signature

`static void HOperatorSet.GetHandleTuple(HTuple handle, HTuple key, out HTuple tuple)`

## Description

`GetHandleTuple` retrieves a tuple associated with the *`key`*
from *`handle`* and returns it in *`tuple`*.
The list of keys supported by a handle can be queried with
[`GetHandleParam`](get_handle_param.md).

Note that this operator is provided only for implementing generic
debug and inspection mechanisms.
The keys returned for certain handle types can change without notice.
Additionally, some handle types might not be supported by this operator.
Also, this operator is not optimized for performance.
To obtain more reliable information about a handle in a program, it is
strongly recommended to use the operators specialized for the particular
handle type, such as [`GetObjectModel3dParams`](get_object_model_3d_params.md),
[`GetGenericShapeModelParam`](get_generic_shape_model_param.md) etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`handle`** (input_control)  handle `→` [HHandle](HHandle.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of which to get the key.

**`key`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Key to get.

Number of elements:
Key == 1

Restriction:
`length(Key) > 0`

**`tuple`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Control value of the key.

## Result

If the parameters are valid, the operator `GetHandleTuple`
returns the value 2 (
H_MSG_TRUE)
.
If the handle is invalid or does not support the given key, or if the
key references an iconic object instead of a tuple, an exception is raised.

## Possible Predecessors

`GetHandleParam`

## Alternatives

`GetHandleObject`

## See also

`GetHandleParam`,
`GetHandleObject`

## Module

Foundation
