# TupleHistoRange (Operator)

## Name

`TupleHistoRange` — Calculate the value distribution of a tuple within a certain value range.

## Signature

`static void HOperatorSet.TupleHistoRange(HTuple tuple, HTuple min, HTuple max, HTuple numBins, out HTuple histo, out HTuple binSize)`

`HTuple HTuple.TupleHistoRange(HTuple min, HTuple max, HTuple numBins, out HTuple binSize)`

## Description

`TupleHistoRange` calculates the value distribution *`histo`*
of the *`tuple`* within the value range [*`min`*,*`max`*].
The values for *`min`* and *`max`* are
rounded down to the next integer if all entries of the *`tuple`* are
of type `integer`. The value range is divided into *`numBins`*
bins of the same size, which is returned in *`binSize`*. If a value
lies between two bins the value is assigned to the smaller bin.
If the *`tuple`* has entries of type `real`
$BinSize = \frac{Max-Min}{NumBins}$ ![figure](../assets/e77fbd30d3031e66.svg). If all entries are of type `integer` the size of a bin is
computed with
$BinSize = \frac{Max-Min+1}{NumBins}$ ![figure](../assets/a71e09270487a639.svg).

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

## Attention

If all the data of the *`tuple`* are of type `integer` the value
of *`binSize`* may cause the following effects:
For *`binSize`* > *1* multiple consecutive numbers are
assigned to the same bin. If *`binSize`* is no integer the numbers
are distributed uneven among the bins, e.g., for
*`binSize`* = *1.5* the first and second number are assigned
to the first bin, the third number is assigned to the second bin, and the
fourth and fifth number are assigned to the third bin. This becomes
noticeable in several peeks in the histogram *`histo`*. If
*`binSize`* < *1* some classes are not assigned by any
number, e.g., for *`binSize`* = *0.5* the first number is
assigned to the first bin and the second number is assigned to the third bin.
The histogram *`histo`* shows some gaps, which resembles the
structure of a comb.

If the *`tuple`* has entries of type `real` and
*`min`* = *`max`*, all entries of the corresponding value are
assigned only to the first bin.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`min`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum value.

**`max`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum value.

Restriction:
`Max >= Min`

**`numBins`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of bins.

Restriction:
`NumBins >= 1`

**`histo`** (output_control)  histogram(-array) `→` [HTuple](HTuple.md) (*int* / long)

Histogram to be calculated.

**`binSize`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Bin size.

## Result

If the parameters are valid, the operator `TupleHistoRange`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`TupleMin`,
`TupleMax`

## Possible Successors

`CreateFunct1dArray`

## See also

`GrayHisto`,
`GrayHistoAbs`,
`GrayHistoRange`

## Module

Foundation
