# GetBgEstiParams (Operator)

## Name

`GetBgEstiParams` — Return the parameters of the data set.

## Signature

`static void HOperatorSet.GetBgEstiParams(HTuple bgEstiHandle, out HTuple syspar1, out HTuple syspar2, out HTuple gainMode, out HTuple gain1, out HTuple gain2, out HTuple adaptMode, out HTuple minDiff, out HTuple statNum, out HTuple confidenceC, out HTuple timeC)`

`double HBgEsti.GetBgEstiParams(out double syspar2, out string gainMode, out double gain1, out double gain2, out string adaptMode, out double minDiff, out int statNum, out double confidenceC, out double timeC)`

## Description

`GetBgEstiParams` returns the parameters of the
data set. The returned parameters are the same as in
[`CreateBgEsti`](create_bg_esti.md) and [`SetBgEstiParams`](set_bg_esti_params.md)
(see these for an explanation).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`bgEstiHandle`** (input_control)  bg_estimation `→` [HBgEsti](HBgEsti.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the BgEsti data set.

**`syspar1`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

1. system matrix parameter.

**`syspar2`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

2. system matrix parameter.

**`gainMode`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Gain type.

**`gain1`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Kalman gain / foreground adaptation time.

**`gain2`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Kalman gain / background adaptation time.

**`adaptMode`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Threshold adaptation.

**`minDiff`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Foreground / background threshold.

**`statNum`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of statistic data sets.

**`confidenceC`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Confidence constant.

**`timeC`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Constant for decay time.

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
* Display the foreground region:
dev_display (ForegroundRegion1)
* Read the next image in sequence:
read_image(Image1,'xing/xing001')
* Estimate the background:
run_bg_esti(Image1,ForegroundRegion2,BgEstiHandle)
* Display the foreground region:
dev_display (ForegroundRegion2)
* etc.
* Change only the gain parameter in dataset:
get_bg_esti_params(BgEstiHandle, Syspar1, Syspar2, \
                   GainMode, Gain1, Gain2, AdaptMode,\
                   MinDiff, StatNum, ConfidenceC, TimeC)
set_bg_esti_params(BgEstiHandle, Syspar1, Syspar2, \
                   GainMode, 0.004, 0.08, AdaptMode,\
                   MinDiff, StatNum, ConfidenceC, TimeC)
* Read the next image in sequence:
read_image(Image3,'xing/xing003')
* Estimate the background:
run_bg_esti(Image3,ForegroundRegion3,BgEstiHandle)
* Display the foreground region:
dev_display(ForegroundRegion3)
* etc
```

## Result

`GetBgEstiParams` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`CreateBgEsti`

## Possible Successors

`RunBgEsti`

## See also

`SetBgEstiParams`

## Module

Foundation
