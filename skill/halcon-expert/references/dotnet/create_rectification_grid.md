# CreateRectificationGrid (Operator)

## Name

`CreateRectificationGrid` — Generate a PostScript file, which describes the rectification grid.

## Signature

`static void HOperatorSet.CreateRectificationGrid(HTuple width, HTuple numSquares, HTuple gridFile)`

`static void HMisc.CreateRectificationGrid(double width, int numSquares, string gridFile)`

## Description

`CreateRectificationGrid` generates a checkered pattern with
*`numSquares`* x *`numSquares`* alternating black and white
squares. This pattern is *`width`* meters wide (and high). Around the
pattern there is an inner frame of *0.3* times the width of one
square, which continues the checkered pattern. The pattern is completed by
a solid white outer frame of *0.7* times the width of one square.
In the
center of the pattern there are two circular marks, one black on a white
square and one white on a black square. The radius of both marks
correspond to one third of the side length of the respective enclosing
square.
These marks are used by [`GenGridRectificationMap`](gen_grid_rectification_map.md) to rotate the
detected layout of the grid points into the correct orientation. It is
assumed that the black mark is positioned to the left of the
white mark, when oriented correctly.
The file *`gridFile`* contains the PostScript description of the
rectification grid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`width`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Width of the checkered pattern in meters (without the
two frames).

Default:
0.17

Suggested values:
1.2, 0.8, 0.6, 0.4, 0.2, 0.1

Recommended increment:
0.1

Restriction:
`0.0 < Width`

**`numSquares`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of squares per row and column.

Default:
17

Suggested values:
11, 13, 15, 17, 19, 21, 23, 25, 27

Recommended increment:
2

Restriction:
`2 <= NumSquares`

**`gridFile`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name of the PostScript file.

Default:
"rectification_grid.ps"

File extension:
.`ps`

## Result

[`FindRectificationGrid`](find_rectification_grid.md) returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the file has been written successfully. If necessary,
an exception is raised.

## See also

`FindRectificationGrid`,
`SaddlePointsSubPix`,
`ConnectGridPoints`,
`GenGridRectificationMap`

## Module

Foundation
