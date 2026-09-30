# mod_parallels_xld (Operator)

## Name

`mod_parallels_xld` — Extract parallel XLD polygons enclosing a homogeneous area.

## Signature

`mod_parallels_xld(Parallels, Image : ModParallels, ExtParallels : Quality, MinGray, MaxGray, MaxStandard : )`

## Description

`mod_parallels_xld` selects XLD parallels enclosing
homogeneous areas from the input parallels *`Parallels`*.
The parameter *`Image`* contains the corresponding gray value
image.

Only parallels having a quality factor larger than
*`Quality`* are examined. The algorithm performs parallel
cross sections one pixel apart, and parallel to the line segments in
the area of overlap between two parallel line segments.

In the first iteration, the mean gray value for each of the lines in
the cross section is calculated. In the second iteration, the
standard deviations of the gray values along each line are computed.

If the mean gray value of an area between parallels lies in the
interval [*`MinGray`*,*`MaxGray`*], and if the mean of
all standard deviations is smaller than the upper threshold
*`MaxStandard`*, the corresponding parallels are returned as
modified parallels in *`ModParallels`*.

In a second step, all polygon segments adjacent to parallels
bordering homogeneous areas are checked for homogeneity. To do so,
a rectangle having the width of the last area enclosed by a
modified parallel is constructed, and checked for homogeneity using
the algorithm described above. This process is continued as long as
there are adjacent polygon segments. The polygons thus found are
returned as extended parallels in *`ExtParallels`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Parallels`** (input_object)  xld_para-array `→` object

Input XLD parallels.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Corresponding gray value image.

**`ModParallels`** (output_object)  xld_mod_para-array `→` object

Modified XLD parallels.

**`ExtParallels`** (output_object)  xld_ext_para-array `→` object

Extended XLD parallels.

**`Quality`** (input_control)  number `→`  (real / integer)

Minimum quality factor (measure of parallelism).

Default:
0.4

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.6

Restriction:
`0.0 <= Quality && Quality <= 1.0`

**`MinGray`** (input_control)  integer `→`  (integer)

Minimum mean gray value.

Default:
160

Suggested values:
80, 100, 120, 140, 160, 180

Restriction:
`0 <= MinGray && MinGray <= 255`

**`MaxGray`** (input_control)  integer `→`  (integer)

Maximum mean gray value.

Default:
220

Suggested values:
140, 160, 180, 200, 220, 240

Restriction:
`0 <= MaxGray && MaxGray <= 255 && MaxGray >= MinGray`

**`MaxStandard`** (input_control)  number `→`  (real / integer)

Maximum allowed standard deviation.

Default:
10.0

Suggested values:
5.0, 10.0, 15.0, 20.0

Restriction:
`MaxStandard >= 0.0`

## Possible Predecessors

`gen_parallels_xld`

## Possible Successors

`max_parallels_xld`

## See also

`info_parallels_xld`

## Module

Foundation
