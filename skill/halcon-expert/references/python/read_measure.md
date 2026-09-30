# read_measure (Operator)

## Name

`read_measure` — Read a measure object from a file.

## Signature

`def read_measure(file_name: str) -> HHandle`

## Description

`read_measure` reads a measure object, which has
been written with [`write_measure`](write_measure.md) from
the file *`file_name`*. The default HALCON file
extension for a measure object is 'msr'. The values
contained in the read measure object are stored in a measure object
with the handle *`measure_handle`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`msr`

**`measure_handle`** (output_control)  measure `→` HHandle

Measure object handle.

## Result

If the parameters are valid, the operator
`read_measure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`measure_pos`,
`measure_pairs`

## See also

`write_measure`

## Module

1D Metrology
