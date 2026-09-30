# SelectLinesLongest (Operator)

## Name

`SelectLinesLongest` — Select the longest input lines.

## Warning

**`SelectLinesLongest` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.SelectLinesLongest(HTuple rowBeginIn, HTuple colBeginIn, HTuple rowEndIn, HTuple colEndIn, HTuple num, out HTuple rowBeginOut, out HTuple colBeginOut, out HTuple rowEndOut, out HTuple colEndOut)`

`static void HMisc.SelectLinesLongest(HTuple rowBeginIn, HTuple colBeginIn, HTuple rowEndIn, HTuple colEndIn, int num, out HTuple rowBeginOut, out HTuple colBeginOut, out HTuple rowEndOut, out HTuple colEndOut)`

## Description

The operator `SelectLinesLongest` selects the
*`num`* longest input lines from the input lines described by
the tuples *`rowBeginIn`*, *`colBeginIn`*,
*`rowEndIn`* and *`colEndIn`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rowBeginIn`** (input_control)  line.begin.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the starting points of the
input lines.

**`colBeginIn`** (input_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the starting points of the
input lines.

**`rowEndIn`** (input_control)  line.end.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the ending points of the
input lines.

**`colEndIn`** (input_control)  line.end.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the ending points of the
input lines.

**`num`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

(Maximum) desired number of output lines.

Default:
10

**`rowBeginOut`** (output_control)  line.begin.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the starting points of the
output lines.

**`colBeginOut`** (output_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the starting points of the
output lines.

**`rowEndOut`** (output_control)  line.end.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the ending points of the
output lines.

**`colEndOut`** (output_control)  line.end.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the ending points of the
output lines.

## Result

The operator `SelectLinesLongest` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct. Otherwise an exception is
raised.

## Possible Predecessors

`SobelAmp`,
`EdgesImage`,
`Threshold`,
`HysteresisThreshold`,
`SplitSkeletonRegion`,
`SplitSkeletonLines`

## Possible Successors

`SetLineWidth`,
`DispLine`

## Alternatives

`LineOrientation`,
`LinePosition`,
`SelectLines`,
`PartitionLines`

## See also

`SelectLines`,
`PartitionLines`,
`DetectEdgeSegments`,
`SelectShape`

## Module

Foundation
