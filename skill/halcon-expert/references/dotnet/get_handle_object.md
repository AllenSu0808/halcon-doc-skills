# GetHandleObject (Operator)

## Name

`GetHandleObject` — Retrieve an object associated with a key from a handle.

## Signature

`static void HOperatorSet.GetHandleObject(out HObject objectVal, HTuple handle, HTuple key)`

## Description

`GetHandleObject` retrieves an iconic object associated with the
*`key`* from *`handle`* and returns it in *`objectVal`*.
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

**`objectVal`** (output_object)  object(-array) `→` [HObject](HObject.md)

Iconic value of the key.

**`handle`** (input_control)  handle `→` [HHandle](HHandle.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of which to get the key.

**`key`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Key to get.

## Result

If the parameters are valid, the operator `GetHandleObject`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Alternatives

`GetHandleTuple`

## See also

`GetHandleParam`

## Module

Foundation
