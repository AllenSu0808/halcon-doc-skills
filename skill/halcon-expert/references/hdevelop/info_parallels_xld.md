# info_parallels_xld (Operator)

## Name

`info_parallels_xld` — Return information about the gray values of the area enclosed by XLD
parallels.

## Signature

`info_parallels_xld(Parallels, Image : : : QualityMin, QualityMax, GrayMin, GrayMax, StandardMin, StandardMax)`

## Description

`info_parallels_xld` calculates various gray value
features of the area enclosed by the XLD parallels
*`Parallels`*. The input image *`Image`* is used to
get the gray values needed for this. The algorithm used in this
operator is very similar to the one used in
[`mod_parallels_xld`](mod_parallels_xld.md). The operator returns ranges for the
quality factor (*`QualityMin`* and *`QualityMax`*, see
[`gen_parallels_xld`](gen_parallels_xld.md) for the corresponding calculation),
the mean gray value (*`GrayMin`* and *`GrayMax`*), and
the standard deviation with respect to the mean gray value
(*`StandardMin`* and *`StandardMax`*).

This operator serves to determine appropriate thresholds for
[`mod_parallels_xld`](mod_parallels_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Parallels`** (input_object)  xld_para-array `→` object

Input XLD Parallels.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Corresponding gray value image.

**`QualityMin`** (output_control)  real `→`  (real)

Minimum quality factor.

**`QualityMax`** (output_control)  real `→`  (real)

Maximum quality factor.

**`GrayMin`** (output_control)  integer `→`  (integer)

Minimum mean gray value.

**`GrayMax`** (output_control)  integer `→`  (integer)

Maximum mean gray value.

**`StandardMin`** (output_control)  real `→`  (real)

Minimum standard deviation.

**`StandardMax`** (output_control)  real `→`  (real)

Maximum standard deviation.

## Possible Predecessors

`gen_parallels_xld`

## Possible Successors

`mod_parallels_xld`

## See also

`intensity`,
`min_max_gray`

## Module

Foundation
