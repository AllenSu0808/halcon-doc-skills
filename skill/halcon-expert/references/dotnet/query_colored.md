# QueryColored (Operator)

## Name

`QueryColored` — Query the number of colors for color output.

## Signature

`static void HOperatorSet.QueryColored(out HTuple possibleNumberOfColors)`

`static HTuple HInfo.QueryColored()`

## Description

`QueryColored` returns all possible parameter values for
[`SetColored`](set_colored.md). [`SetColored`](set_colored.md) defines how many
colors are used for region or graphics output.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`possibleNumberOfColors`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Tuple of the possible numbers of colors.

## Example (HDevelop)

```
regiongrowing(Image,Regions,5,5,6,100)
query_colored(Colors)
dev_set_colored(Colors[1])
dev_display (Regions)
```

## Result

`QueryColored` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`SetColored`,
`SetColor`,
`DispRegion`

## Alternatives

`QueryColor`

## See also

`SetColored`,
`SetColor`

## Module

Foundation
