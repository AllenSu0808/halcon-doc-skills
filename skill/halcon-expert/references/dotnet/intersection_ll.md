# IntersectionLl (Operator)

## Name

`IntersectionLl` — Calculate the intersection point of two lines.

## Warning

**`IntersectionLl` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
operator [`IntersectionLines`](intersection_lines.md) of the chapter Tools / Geometry instead.**

## Signature

`static void HOperatorSet.IntersectionLl(HTuple rowA1, HTuple columnA1, HTuple rowA2, HTuple columnA2, HTuple rowB1, HTuple columnB1, HTuple rowB2, HTuple columnB2, out HTuple row, out HTuple column, out HTuple isParallel)`

`static void HMisc.IntersectionLl(HTuple rowA1, HTuple columnA1, HTuple rowA2, HTuple columnA2, HTuple rowB1, HTuple columnB1, HTuple rowB2, HTuple columnB2, out HTuple row, out HTuple column, out HTuple isParallel)`

`static void HMisc.IntersectionLl(double rowA1, double columnA1, double rowA2, double columnA2, double rowB1, double columnB1, double rowB2, double columnB2, out double row, out double column, out int isParallel)`

## Description

The operator `IntersectionLl` calculates the intersection point
of two lines. As input the two points on each line are expected
(*`rowA1`*,*`columnA1`*,
*`rowA2`*,*`columnA2`*) and
(*`rowB1`*,*`columnB1`*,
*`rowB2`*,*`columnB2`*).
The parameters *`row`* and *`column`* return the
result of the calculation.
If the lines are parallel, the values of *`row`* and *`column`*
are undefined and *`isParallel`* is 1. Otherwise, *`isParallel`*
is 0.

## Attention

If the lines are parallel the values of *`row`* and
*`column`* are undefined.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rowA1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the first line.

**`columnA1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the
first line.

**`rowA2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the first line.

**`columnA2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the
first line.

**`rowB1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the second line.

**`columnB1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the
second line.

**`rowB2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the second line.

**`columnB2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the
second line.

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the intersection point.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the intersection point.

**`isParallel`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

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

`IntersectionLl` returns 2 (
H_MSG_TRUE)
.

## Module

Foundation
