# get_dict_tuple (Operator)

## Name

`get_dict_tuple` — Retrieve a tuple associated with the key from the dictionary.

## Signature

`def get_dict_tuple(dict_handle: HHandle, key: MaybeSequence[Union[str, int]]) -> Sequence[Union[int, float, str]]`

`def get_dict_tuple_s(dict_handle: HHandle, key: MaybeSequence[Union[str, int]]) -> Union[int, float, str]`

## Description

`get_dict_tuple` retrieves a tuple associated with the *`key`*
from the dictionary denoted by the *`dict_handle`*.
The tuple has to be previously stored to the dictionary using
[`set_dict_tuple`](set_dict_tuple.md).

The operator returns the data in the parameter *`tuple`*.
The data including strings is copied by the operation, the dictionary can
thus be immediately reused.

If the given *`key`* is not present in the dictionary or if the data
associated with the key is not a tuple, `get_dict_tuple` fails.
Presence of keys and information about the data associated with the key
can be verified using [`get_dict_param`](get_dict_param.md).

Obtaining the values for multiple keys at once is only possible if for each
of those keys, the dictionary contains a tuple with a single element.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `get_dict_tuple`,
which can be used in an expression in the following syntax:

- Dynamic syntax:

  [`Tuple := DictHandle.['Key']`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)
- Static syntax:

  [`Tuple := DictHandle.Key`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_dicts_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dict_handle`** (input_control)  dict `→` HHandle

Dictionary handle.

Number of elements:
DictHandle == 1

**`key`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int]]

Key string.

**`tuple`** (output_control)  tuple(-array) `→` Sequence[Union[int, float, str]]

Tuple value retrieved from the dictionary.

## Example (HDevelop)

```
* ...
get_dict_param (Dict, 'key_exists', ['simple_string','foo','my_image'], \
                KeysPresence)
get_dict_param (Dict, 'key_data_type', ['simple_string','my_image'], \
                KeysType)
get_dict_tuple (Dict, 'simple_string', TupleString)
*
* Access multiple keys, if their tuple all have length 1
get_dict_tuple (Dict, ['key1','key2','key3'], MultipleValues)
```

## Result

If the operation succeeds, `get_dict_tuple` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key), the required key not found in the
dictionary, or other than tuple data associated with given key.

## Possible Predecessors

`set_dict_tuple`

## Possible Successors

`get_dict_tuple`,
`set_dict_tuple`,
`set_dict_tuple_at`

## Alternatives

`get_dict_object`

## See also

`create_dict`,
`set_dict_tuple`,
`set_dict_object`,
`get_dict_object`,
`remove_dict_key`,
`get_dict_param`

## Module

Foundation
