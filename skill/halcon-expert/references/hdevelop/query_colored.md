# query_colored (Operator)

## Name

`query_colored` — Query the number of colors for color output.

## Signature

`query_colored( : : : PossibleNumberOfColors)`

## Description

`query_colored` returns all possible parameter values for
[`set_colored`](set_colored.md). [`set_colored`](set_colored.md) defines how many
colors are used for region or graphics output.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`PossibleNumberOfColors`** (output_control)  integer-array `→`  (integer)

Tuple of the possible numbers of colors.

## Example (HDevelop)

```
regiongrowing(Image,Regions,5,5,6,100)
query_colored(Colors)
dev_set_colored(Colors[1])
dev_display (Regions)
```

## Result

`query_colored` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`set_colored`,
`set_color`,
`disp_region`

## Alternatives

`query_color`

## See also

`set_colored`,
`set_color`

## Module

Foundation
