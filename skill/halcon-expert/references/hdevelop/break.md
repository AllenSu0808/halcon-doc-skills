# break (Operator)

## Name

`break` — Terminate loop execution or leave a [`switch`](switch.md) block.

## Signature

`break( : : : )`

## Description

`break` terminates the smallest enclosing [`for`](for.md), [`while`](while.md),
or [`repeat`](repeat.md)..[`until`](until.md) loop.
In addition, the `break` statement is used to leave a [`switch`](switch.md)
block, in particular at the end of a [`case`](case.md) branch.
The program execution is continued at the program line following the
corresponding block.

`break` statements that are not enclosed by a loop or [`switch`](switch.md)
block are invalid.

## Example (HDevelop)

```
read_image (Image, 'monkey')
threshold (Image, Region, 160, 180)
connection (Region, Regions)
Number := |Regions|
AllRegionsValid := 1
* check if for all regions area <=30
for i := 1 to Number by 1
  select_obj (Regions, ObjectSelected, i)
  area_center (ObjectSelected, Area, Row, Column)
  if (Area > 30)
    AllRegionsValid := 0
    break
  endif
endfor
```

## Result

`break` (as an operator) always returns 2 (
H_MSG_TRUE)
.

## Alternatives

`continue`

## See also

`for`,
`while`,
`repeat`,
`until`,
`switch`,
`case`

## Module

Foundation
