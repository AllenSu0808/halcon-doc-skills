# create_rectification_grid (Operator)

## Name

`create_rectification_grid` — Generate a PostScript file, which describes the rectification grid.

## Signature

`create_rectification_grid( : : Width, NumSquares, GridFile : )`

## Description

`create_rectification_grid` generates a checkered pattern with
*`NumSquares`* x *`NumSquares`* alternating black and white
squares. This pattern is *`Width`* meters wide (and high). Around the
pattern there is an inner frame of *0.3* times the width of one
square, which continues the checkered pattern. The pattern is completed by
a solid white outer frame of *0.7* times the width of one square.
In the
center of the pattern there are two circular marks, one black on a white
square and one white on a black square. The radius of both marks
correspond to one third of the side length of the respective enclosing
square.
These marks are used by [`gen_grid_rectification_map`](gen_grid_rectification_map.md) to rotate the
detected layout of the grid points into the correct orientation. It is
assumed that the black mark is positioned to the left of the
white mark, when oriented correctly.
The file *`GridFile`* contains the PostScript description of the
rectification grid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Width`** (input_control)  real `→`  (real)

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

**`NumSquares`** (input_control)  integer `→`  (integer)

Number of squares per row and column.

Default:
17

Suggested values:
11, 13, 15, 17, 19, 21, 23, 25, 27

Recommended increment:
2

Restriction:
`2 <= NumSquares`

**`GridFile`** (input_control)  filename.write `→`  (string)

File name of the PostScript file.

Default:
'rectification_grid.ps'

File extension:
.`ps`

## Result

[`find_rectification_grid`](find_rectification_grid.md) returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the file has been written successfully. If necessary,
an exception is raised.

## See also

`find_rectification_grid`,
`saddle_points_sub_pix`,
`connect_grid_points`,
`gen_grid_rectification_map`

## Module

Foundation
