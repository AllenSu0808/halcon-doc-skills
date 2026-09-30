# set_dict_object (Operator)

## Name

`set_dict_object` — Add a key/object pair to the dictionary.

## Signature

`def set_dict_object(object: HObject, dict_handle: HHandle, key: Union[str, int]) -> None`

## Description

`set_dict_object` stores an object associated with a key in the
dictionary.
The dictionary is denoted by the *`dict_handle`* parameter.

*`object`* is copied by the operation and can thus be
immediately reused.
Thereby the object data is copied in HALCON's object database,
meaning the new object contains a reference to *`object`*,
see [`copy_obj`](copy_obj.md).

Both an empty object or an object tuple are considered
as a valid value that can be associated with the key.
If any data (tuple or object) was already associated with given key
(*`key`*), the old data is destroyed by `set_dict_object`
and replaced by *`object`*.

The *`key`* has to be a string or an integer.
Strings are treated case sensitive.

The object data for the given key can be retrieved again from the dictionary
using [`get_dict_object`](get_dict_object.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `set_dict_object`,
which can be used in an expression in the following syntax:

- Dynamic syntax:

  [`DictHandle.['Key'] := Object`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)
- Static syntax:

  [`DictHandle.Key := Object`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- dict_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`object`** (input_object)  object(-array) `→` HObject

Object to be associated with the key.

**`dict_handle`** (input_control, state is modified)  dict `→` HHandle

Dictionary handle.

Number of elements:
DictHandle == 1

**`key`** (input_control)  string `→` Union[str, int]

Key string.

Number of elements:
Key == 1

Restriction:
`length(Key) > 0`

## Example (HDevelop)

```
create_dict (Dict)
read_image (Image, 'filename')
set_dict_object (Image, Dict, 'my_image')
```

## Result

If the operation succeeds, `set_dict_object` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key) or resource allocation error.

## Possible Predecessors

`create_dict`

## Possible Successors

`set_dict_object`,
`set_dict_tuple`

## Alternatives

`set_dict_tuple`

## See also

`create_dict`,
`set_dict_tuple`,
`get_dict_tuple`,
`get_dict_object`,
`remove_dict_key`,
`get_dict_param`

## Module

Foundation
