# get_threading_attrib (Operator)

## Name

`get_threading_attrib` — Query the attributes of a threading / synchronization object.

## Signature

`get_threading_attrib( : : ThreadingHandle : ThreadingClass, AttribName, AttribValue)`

## Description

`get_threading_attrib` determines the type of threading object passed
to *`ThreadingHandle`* and the attributes the threading object was
created with.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ThreadingHandle`** (input_control)  number `→`  (integer)

Threading object.

**`ThreadingClass`** (output_control)  string-array `→`  (string)

Class name of threading object.

**`AttribName`** (output_control)  string-array `→`  (string)

Name of an attribute.

**`AttribValue`** (output_control)  number-array `→`  (string / integer / real)

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
