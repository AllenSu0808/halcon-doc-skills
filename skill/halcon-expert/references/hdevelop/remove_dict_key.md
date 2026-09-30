# remove_dict_key (Operator)

## Name

`remove_dict_key` — Remove keys from a dictionary.

## Signature

`remove_dict_key( : : DictHandle, Key : )`

## Description

`remove_dict_key` removes the keys specified in *`Key`* from
the dictionary passed in *`DictHandle`* and releases
all the (tuple or object) data associated with those keys.

If an error occurs while processing one or more keys (in particular
if a key is invalid), the operator attempts to continue removing
as many keys as possible before reporting an appropriate failure.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- DictHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`DictHandle`** (input_control, state is modified)  dict `→`  (handle)

Dictionary handle.

Number of elements:
DictHandle == 1

**`Key`** (input_control)  string(-array) `→`  (string / integer)

Key to remove.

Restriction:
`length(Key) > 0`

## Example (HDevelop)

```
* Remove all keys
get_dict_param (Dict, 'keys', [], Keys)
remove_dict_key (Dict, Keys)
```

## Result

If all the operator parameters are valid, `remove_dict_key` returns
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`create_dict`

## Possible Successors

`get_dict_param`

## See also

`create_dict`,
`set_dict_tuple`,
`get_dict_tuple`,
`set_dict_object`,
`get_dict_object`,
`get_dict_param`

## Module

Foundation
