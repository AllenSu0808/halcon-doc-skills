# set_dict_tuple_at (Operator)

## Name

`set_dict_tuple_at` — Assignment of one or several values to one or several tuple elements
in a dictionary

## Signature

`set_dict_tuple_at( : : DictHandle, Key, Index, Value : )`

## Description

`set_dict_tuple_at` assigns a single value to one or several
elements of a tuple, or it assigns a number of values elementwise to the
specified elements of a tuple that is stored in *`DictHandle`*
under the key *`Key`*.
The operator allows to efficiently replace parts of a tuple stored
in a dictionary without first reading the previous values from the
dictionary.

If the dictionary does not yet contain a tuple under the given key,
or if the given key maps to an iconic value, a new tuple is created
and stored under the given key. In the latter case, the iconic
object previously stored under that key is removed from the dictionary.

If the passed indices are out of the current range of the tuple stored
in the dictionary, the tuple length is increased and the new values are
initialized to a default value.

The *`Key`* has to be a string or an integer.
Strings are treated case sensitive.
The *`Index`* parameter can be any expression that evaluates to any
number of positive integer values.
The *`Value`* parameter must evaluate to exactly one value or to
the same number of indices that are provided via the *`Index`*
parameter.:

The tuple data for the given key can be retrieved again from the dictionary
using [`get_dict_tuple`](get_dict_tuple.md).

## Attention

Note that if *`Value`* contains any handles, only the handle values
are copied by the operation, not the resources behind those handles.

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

**`Key`** (input_control)  string `→`  (string / integer)

Key string.

Number of elements:
Key == 1

Restriction:
`length(Key) > 0`

**`Index`** (input_control)  integer-array `→`  (integer)

Indices of the elements that have to be replaced by the new
value(s).

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6

Minimum increment:
1

**`Value`** (input_control)  tuple-array `→`  (string / integer / real / handle)

Value(s) that is to be assigned.

## Example (HDevelop)

```
Dict := dict{}
Dict.some_key := 27

set_dict_tuple_at (Dict, 'some_key', 1, 5)
* Dict.some_key is now [27, 5]

* Alternative TRIAS syntax
Dict.some_key[0] := 66
* Dict.some_key is now [66, 5]
```

## Result

If the operation succeeds, `set_dict_tuple_at` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters or resource allocation error.

## Possible Predecessors

`create_dict`

## Possible Successors

`set_dict_tuple`,
`get_dict_tuple`

## Alternatives

`set_dict_tuple`

## See also

`create_dict`,
`set_dict_tuple`,
`get_dict_tuple`,
`set_dict_object`,
`get_dict_object`,
`get_dict_param`,
`remove_dict_key`

## Module

Foundation
