# create_dict (Operator)

## Name

`create_dict` — Create a new empty dictionary.

## Signature

`def create_dict() -> HHandle`

## Description

`create_dict` creates a new empty dictionary and returns
it in *`dict_handle`*.

The dictionary serves as an associative array-like container allowing to
store an arbitrary number of values associated with unique keys (integers
or strings).
Each key can refer either to a tuple or to an iconic object.
These are stored in the dictionary using
[`set_dict_tuple`](set_dict_tuple.md) or [`set_dict_object`](set_dict_object.md),
respectively, from where they can be retrieved again using
[`get_dict_tuple`](get_dict_tuple.md) or [`get_dict_object`](get_dict_object.md).

The data stored in the dictionary is always a copy of the original
data, being it control parameters or objects.
The original data
can thus be reused immediately after the [`set_dict_tuple`](set_dict_tuple.md)
or [`set_dict_object`](set_dict_object.md) calls.
The following particularities apply:

- Objects: The copy is a reference, as in [`copy_obj`](copy_obj.md).
  In particular, changes made using the operators [`set_grayval`](set_grayval.md) or
  [`overpaint_region`](overpaint_region.md) affect the object stored in the dictionary as well.
- Handles: Storing any handle in the dictionary will copy the handle
  value, but not the resource behind the handle.

Multiple threads can add, retrieve and remove keys concurrently as long as
every thread accesses a different key. As an exception to this rule, multiple
threads can retrieve the same key from a dictionary simultaneously.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `create_dict`,
which can be used in an expression in the following syntax:

[`DictHandle := dict{`}](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`dict_handle`** (output_control)  dict `→` HHandle

Handle of the newly created dictionary.

Number of elements:
DictHandle == 1

## Example (HDevelop)

```
Dicts := []
for idx := 0 to 4 by 1
  create_dict (DictHandle)
  Dicts[idx] := DictHandle
endfor
* ...
```

## Result

Returns 2 (
H_MSG_TRUE)
unless a resource allocation error occurs.

## Possible Successors

`set_dict_tuple`,
`set_dict_object`

## See also

`set_dict_tuple`,
`get_dict_tuple`,
`set_dict_object`,
`get_dict_object`,
`get_dict_param`

## Module

Foundation
