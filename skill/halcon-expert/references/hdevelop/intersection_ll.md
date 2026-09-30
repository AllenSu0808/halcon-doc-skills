# intersection_ll (Operator)

## Name

`intersection_ll` — Calculate the intersection point of two lines.

## Warning

**`intersection_ll` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
operator [`intersection_lines`](intersection_lines.md) of the chapter Tools / Geometry instead.**

## Signature

`intersection_ll( : : RowA1, ColumnA1, RowA2, ColumnA2, RowB1, ColumnB1, RowB2, ColumnB2 : Row, Column, IsParallel)`

## Description

The operator `intersection_ll` calculates the intersection point
of two lines. As input the two points on each line are expected
(*`RowA1`*,*`ColumnA1`*,
*`RowA2`*,*`ColumnA2`*) and
(*`RowB1`*,*`ColumnB1`*,
*`RowB2`*,*`ColumnB2`*).
The parameters *`Row`* and *`Column`* return the
result of the calculation.
If the lines are parallel, the values of *`Row`* and *`Column`*
are undefined and *`IsParallel`* is 1. Otherwise, *`IsParallel`*
is 0.

## Attention

If the lines are parallel the values of *`Row`* and
*`Column`* are undefined.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`RowA1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point of the first line.

**`ColumnA1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the
first line.

**`RowA2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the first line.

**`ColumnA2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the
first line.

**`RowB1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point of the second line.

**`ColumnB1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the
second line.

**`RowB2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the second line.

**`ColumnB2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the
second line.

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the intersection point.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of the intersection point.

**`IsParallel`** (output_control)  number(-array) `→`  (integer)

Are the two lines parallel?

## Example (HDevelop)

```
dev_set_color ('black')
RowLine1 := 350
ColLine1 := 250
RowLine2 := 300
ColLine2 := 300
Rows := 300
Columns := 50
disp_line (WindowHandle, RowLine1, ColLine1, RowLine2, ColLine2)
n := 0
for Rows := 40 to 200 by 4
  dev_set_color ('red')
  disp_line (WindowHandle, Rows, Columns, Rows+n, Columns+n)
  intersection_ll (Rows, Columns, Rows+n, Columns+n, RowLine1, ColLine1, \
                   RowLine2, ColLine2, Row, Column, IsParallel)
  dev_set_color ('blue')
  disp_line (WindowHandle, Row, Column-2, Row, Column+2)
  disp_line (WindowHandle, Row-2, Column, Row+2, Column)
  n := n+8
endfor
```

## Result

`intersection_ll` returns 2 (
H_MSG_TRUE)
.

## Module

Foundation
