# get_dict_object (Operator)

## Name

`get_dict_object` — Retrieve an object associated with the key from the dictionary.

## Signature

`get_dict_object( : Object : DictHandle, Key : )`

## Description

`get_dict_object` retrieves an object associated with the *`Key`*
from the dictionary denoted by the *`DictHandle`*.
The object has to be previously stored to the dictionary using
[`set_dict_object`](set_dict_object.md).

The operator returns the data in the parameter *`Object`*. The
iconic object is copied by the operation. Therefore, clearing or reusing
the dictionary object afterwards will not have any side-effect on the
returned iconic object.

If the given *`Key`* is not present in the dictionary or if the data
associated with the key is not an object, `get_dict_object` fails.
Presence of keys and information about the data associated with the key can
be verified using [`get_dict_param`](get_dict_param.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `get_dict_object`,
which can be used in an expression in the following syntax:

- Dynamic syntax:

  [`Object := DictHandle.['Key']`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)
- Static syntax:

  [`Object := DictHandle.Key`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Object`** (output_object)  object(-array) `→` object

Object value retrieved from the dictionary.

**`DictHandle`** (input_control)  dict `→`  (handle)

Dictionary handle.

Number of elements:
DictHandle == 1

**`Key`** (input_control)  string `→`  (string / integer)

Key string.

Number of elements:
Key == 1

Restriction:
`length(Key) > 0`

## Example (HDevelop)

```
* ...
get_dict_param (Dict, 'key_exists', ['simple_string','foo','my_image'], \
                KeysPresence)
get_dict_param (Dict, 'key_data_type', ['simple_string','my_image'], \
                KeysType)
get_dict_object (Image, Dict, 'my_image')
```

## Result

If the operation succeeds, `get_dict_object` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key), the required key not found in the
dictionary or other than object data associated with given key.

## Possible Predecessors

`set_dict_object`

## Possible Successors

`get_dict_object`

## Alternatives

`get_dict_tuple`

## See also

`create_dict`,
`set_dict_tuple`,
`get_dict_tuple`,
`set_dict_object`,
`remove_dict_key`,
`get_dict_param`

## Module

Foundation
