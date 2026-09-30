# ReadObject (Operator)

## Name

`ReadObject` — Read an iconic object.

## Signature

`static void HOperatorSet.ReadObject(out HObject objectVal, HTuple fileName)`

`void HObject.ReadObject(string fileName)`

## Description

`ReadObject` reads an iconic object from the file *`fileName`*.
The file must be written in the HALCON Iconic Object format (HOBJ),
which is supported by the operators [`WriteObject`](write_object.md),
[`WriteImage`](write_image.md), and [`WriteRegion`](write_region.md). See [`WriteObject`](write_object.md)
for more information about the HOBJ format.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (output_object)  object(-array) `→` [HObject](HObject.md)

Iconic object.

**`fileName`** (input_control)  filename `→` [HTuple](HTuple.md) (*string*)

Name of file.

File extension:
.`hobj`

## Result

If the parameters are valid, the operator
`ReadObject` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`WriteImage`,
`WriteObject`

## See also

`WriteObject`,
`WriteImage`,
`ReadImage`

## Module

Foundation
