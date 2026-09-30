# CloseBgEsti (Operator)

## Name

`CloseBgEsti` — Delete the background estimation data set.

## Signature

`static void HOperatorSet.CloseBgEsti(HTuple bgEstiHandle)`

`void HBgEsti.CloseBgEsti()`

## Description

`CloseBgEsti` deletes the background estimation data set and
releases all used memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- bgEstiHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`bgEstiHandle`** (input_control, state is modified)  bg_estimation `→` [HBgEsti](HBgEsti.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the BgEsti data set.

## Example (HDevelop)

```
* Read image for initialization:
read_image (InitImage, 'xing/init')
* Initialize BgEsti dataset with
* fixed gains and threshold adaption:
create_bg_esti(InitImage,0.7,0.7,'fixed',0.002,0.02, \
               'on',7.0,10,3.25,15.0,BgEstiHandle)
* Read the next image in sequence:
read_image(Image0, 'xing/xing001')
* Estimate the background:
run_bg_esti(Image0,ForegroundRegion1,BgEstiHandle)
* Display the foreground region:
dev_display (ForegroundRegion1)
* Read the next image in sequence:
read_image(Image1, 'xing/xing002')
* Estimate the background:
run_bg_esti(Image1,ForegroundRegion2,BgEstiHandle)
* Display the foreground region:
dev_display (ForegroundRegion2)
* etc.
* - End of background estimation -
* Close the dataset:
close_bg_esti(BgEstiHandle)
```

## Result

`CloseBgEsti` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`RunBgEsti`

## See also

`CreateBgEsti`

## Module

Foundation
