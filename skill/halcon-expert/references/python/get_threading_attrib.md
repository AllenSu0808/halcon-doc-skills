# get_threading_attrib (Operator)

## Name

`get_threading_attrib` — Query the attributes of a threading / synchronization object.

## Signature

`def get_threading_attrib(threading_handle: int) -> Tuple[Sequence[str], Sequence[str], Sequence[Union[int, float, str]]]`

## Description

`get_threading_attrib` determines the type of threading object passed
to *`threading_handle`* and the attributes the threading object was
created with.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`threading_handle`** (input_control)  number `→` int

Threading object.

**`threading_class`** (output_control)  string-array `→` Sequence[str]

Class name of threading object.

**`attrib_name`** (output_control)  string-array `→` Sequence[str]

Name of an attribute.

**`attrib_value`** (output_control)  number-array `→` Sequence[Union[int, float, str]]

Value of the attribute.

## Result

If the threading handle is valid, the operator `get_threading_attrib`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`create_mutex`,
`create_event`,
`create_condition`,
`create_barrier`

## See also

`create_mutex`,
`create_event`,
`create_condition`,
`create_barrier`

## Module

Foundation
