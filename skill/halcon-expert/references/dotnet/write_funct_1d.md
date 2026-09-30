# WriteFunct1d (Operator)

## Name

`WriteFunct1d` — Write a function to a file.

## Signature

`static void HOperatorSet.WriteFunct1d(HTuple function, HTuple fileName)`

`void HFunction1D.WriteFunct1d(string fileName)`

## Description

The operator `WriteFunct1d` writes the contents of *`function`*
to a file. The data is written in an ASCII format. Therefore, the file can
be exchanged between different architectures (see also
[Tuple / String Operations](toc_tuple_stringoperations.md)).
The data can be read by the operator [`ReadFunct1d`](read_funct_1d.md).
There is no specific extension for this kind of file.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Function to be written.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file to be written.

## Result

If the parameters are correct the operator `WriteFunct1d`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Alternatives

`WriteTuple`,
`FwriteString`

## See also

`ReadFunct1d`,
`WriteImage`,
`WriteRegion`,
`OpenFile`

## Module

Foundation
