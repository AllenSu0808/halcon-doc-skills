# give_bg_esti (Operator)

## Name

`give_bg_esti` — Return the estimated background image.

## Signature

`give_bg_esti( : BackgroundImage : BgEstiHandle : )`

## Description

`give_bg_esti` returns the estimated background image of
the current BgEsti data set. The background image has the same type
and size as the initialization image passed in
[`create_bg_esti`](create_bg_esti.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`BackgroundImage`** (output_object)  image `→` object (byte / real)

Estimated background image of the current data set.

**`BgEstiHandle`** (input_control)  bg_estimation `→`  (handle)

ID of the BgEsti data set.

## Example (HDevelop)

```
* Read image for initialization:
read_image(InitImage,'xing/init')
* Initialize BgEsti dataset with
* fixed gains and threshold adaption:
create_bg_esti(InitImage,0.7,0.7,'fixed',0.002,0.02, \
               'on',7.0,10,3.25,15.0,BgEstiHandle)
* Read the next image in sequence:
read_image(Image0,'xing/xing000')
* Estimate the background:
run_bg_esti(Image0,ForegroundRegion1,BgEstiHandle)
* Give the background image from the aktive dataset:
give_bg_esti(BgImage,BgEstiHandle)
* Display the background image:
dev_display(BgImage)
```

## Result

`give_bg_esti` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`run_bg_esti`

## Possible Successors

`run_bg_esti`,
`create_bg_esti`,
`update_bg_esti`

## See also

`run_bg_esti`,
`update_bg_esti`,
`create_bg_esti`

## Module

Foundation
