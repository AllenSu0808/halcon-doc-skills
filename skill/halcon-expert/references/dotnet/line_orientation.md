# LineOrientation (Operator)

## Name

`LineOrientation` — Calculate the orientation of lines.

## Signature

`static void HOperatorSet.LineOrientation(HTuple rowBegin, HTuple colBegin, HTuple rowEnd, HTuple colEnd, out HTuple phi)`

`static HTuple HMisc.LineOrientation(HTuple rowBegin, HTuple colBegin, HTuple rowEnd, HTuple colEnd)`

`static double HMisc.LineOrientation(double rowBegin, double colBegin, double rowEnd, double colEnd)`

## Description

The operator `LineOrientation` returns the orientation
(-pi/2 < *`phi`* <= pi/2) of the given lines. If more
than one line is to be treated the line and column indices can be
passed as tuples. In this case *`phi`* is, of course, also
a tuple and contains the corresponding orientations.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rowBegin`** (input_control)  line.begin.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the starting points of the
input lines.

**`colBegin`** (input_control)  line.begin.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the starting points of the
input lines.

**`rowEnd`** (input_control)  line.end.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the ending points of the
input lines.

**`colEnd`** (input_control)  line.end.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the ending points of the
input lines.

**`phi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of the input lines.

## Result

`LineOrientation` always returns the value 2 (
H_MSG_TRUE)
.

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

`LinePosition`

## See also

`LinePosition`,
`DetectEdgeSegments`

## Module

Foundation
