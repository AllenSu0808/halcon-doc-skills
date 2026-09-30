# tuple_histo_range (Operator)

## Name

`tuple_histo_range` — Calculate the value distribution of a tuple within a certain value range.

## Signature

`tuple_histo_range( : : Tuple, Min, Max, NumBins : Histo, BinSize)`

## Description

`tuple_histo_range` calculates the value distribution *`Histo`*
of the *`Tuple`* within the value range [*`Min`*,*`Max`*].
The values for *`Min`* and *`Max`* are
rounded down to the next integer if all entries of the *`Tuple`* are
of type `integer`. The value range is divided into *`NumBins`*
bins of the same size, which is returned in *`BinSize`*. If a value
lies between two bins the value is assigned to the smaller bin.
If the *`Tuple`* has entries of type `real`
$BinSize = \frac{Max-Min}{NumBins}$ ![figure](../assets/e77fbd30d3031e66.svg). If all entries are of type `integer` the size of a bin is
computed with
$BinSize = \frac{Max-Min+1}{NumBins}$ ![figure](../assets/a71e09270487a639.svg).

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

## Attention

If all the data of the *`Tuple`* are of type `integer` the value
of *`BinSize`* may cause the following effects:
For *`BinSize`* > *1* multiple consecutive numbers are
assigned to the same bin. If *`BinSize`* is no integer the numbers
are distributed uneven among the bins, e.g., for
*`BinSize`* = *1.5* the first and second number are assigned
to the first bin, the third number is assigned to the second bin, and the
fourth and fifth number are assigned to the third bin. This becomes
noticeable in several peeks in the histogram *`Histo`*. If
*`BinSize`* < *1* some classes are not assigned by any
number, e.g., for *`BinSize`* = *0.5* the first number is
assigned to the first bin and the second number is assigned to the third bin.
The histogram *`Histo`* shows some gaps, which resembles the
structure of a comb.

If the *`Tuple`* has entries of type `real` and
*`Min`* = *`Max`*, all entries of the corresponding value are
assigned only to the first bin.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  number-array `→`  (real / integer)

Input tuple.

**`Min`** (input_control)  number `→`  (real / integer)

Minimum value.

**`Max`** (input_control)  number `→`  (real / integer)

Maximum value.

Restriction:
`Max >= Min`

**`NumBins`** (input_control)  integer `→`  (integer)

Number of bins.

Restriction:
`NumBins >= 1`

**`Histo`** (output_control)  histogram(-array) `→`  (integer)

Histogram to be calculated.

**`BinSize`** (output_control)  real `→`  (real)

Bin size.

## Result

If the parameters are valid, the operator `tuple_histo_range`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`tuple_min`,
`tuple_max`

## Possible Successors

`create_funct_1d_array`

## See also

`gray_histo`,
`gray_histo_abs`,
`gray_histo_range`

## Module

Foundation
