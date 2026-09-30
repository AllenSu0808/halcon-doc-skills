# tuple_histo_range (Operator)

## Name

`tuple_histo_range` — Calculate the value distribution of a tuple within a certain value range.

## Signature

`def tuple_histo_range(tuple: Sequence[Union[float, int]], min: Union[float, int], max: Union[float, int], num_bins: int) -> Tuple[Sequence[int], float]`

`def tuple_histo_range_s(tuple: Sequence[Union[float, int]], min: Union[float, int], max: Union[float, int], num_bins: int) -> Tuple[int, float]`

## Description

`tuple_histo_range` calculates the value distribution *`histo`*
of the *`tuple`* within the value range [*`min`*,*`max`*].
The values for *`min`* and *`max`* are
rounded down to the next integer if all entries of the *`tuple`* are
of type `integer`. The value range is divided into *`num_bins`*
bins of the same size, which is returned in *`bin_size`*. If a value
lies between two bins the value is assigned to the smaller bin.
If the *`tuple`* has entries of type `real`
$BinSize = \frac{Max-Min}{NumBins}$ ![figure](../assets/e77fbd30d3031e66.svg). If all entries are of type `integer` the size of a bin is
computed with
$BinSize = \frac{Max-Min+1}{NumBins}$ ![figure](../assets/a71e09270487a639.svg).

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

## Attention

If all the data of the *`tuple`* are of type `integer` the value
of *`bin_size`* may cause the following effects:
For *`bin_size`* > *1* multiple consecutive numbers are
assigned to the same bin. If *`bin_size`* is no integer the numbers
are distributed uneven among the bins, e.g., for
*`bin_size`* = *1.5* the first and second number are assigned
to the first bin, the third number is assigned to the second bin, and the
fourth and fifth number are assigned to the third bin. This becomes
noticeable in several peeks in the histogram *`histo`*. If
*`bin_size`* < *1* some classes are not assigned by any
number, e.g., for *`bin_size`* = *0.5* the first number is
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

**`tuple`** (input_control)  number-array `→` Sequence[Union[float, int]]

Input tuple.

**`min`** (input_control)  number `→` Union[float, int]

Minimum value.

**`max`** (input_control)  number `→` Union[float, int]

Maximum value.

Restriction:
`Max >= Min`

**`num_bins`** (input_control)  integer `→` int

Number of bins.

Restriction:
`NumBins >= 1`

**`histo`** (output_control)  histogram(-array) `→` Sequence[int]

Histogram to be calculated.

**`bin_size`** (output_control)  real `→` float

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
