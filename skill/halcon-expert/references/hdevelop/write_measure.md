# write_measure (Operator)

## Name

`write_measure` — Write a measure object to a file.

## Signature

`write_measure( : : MeasureHandle, FileName : )`

## Description

`write_measure` writes a measure object that has been
created by, e.g., [`gen_measure_rectangle2`](gen_measure_rectangle2.md)
to the file *`FileName`*. The measure object
is defined by the handle *`MeasureHandle`*. The measure
object can be read with [`read_measure`](read_measure.md). The default
HALCON file extension for a measure object is 'msr'.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MeasureHandle`** (input_control)  measure `→`  (handle)

Measure object handle.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`msr`

## Result

If the parameters are valid, the operator
`write_measure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`,
`gen_measure_arc`

## See also

`read_measure`

## Module

1D Metrology
