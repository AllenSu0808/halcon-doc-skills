# get_bg_esti_params (Operator)

## Name

`get_bg_esti_params` — Return the parameters of the data set.

## Signature

`get_bg_esti_params( : : BgEstiHandle : Syspar1, Syspar2, GainMode, Gain1, Gain2, AdaptMode, MinDiff, StatNum, ConfidenceC, TimeC)`

## Description

`get_bg_esti_params` returns the parameters of the
data set. The returned parameters are the same as in
[`create_bg_esti`](create_bg_esti.md) and [`set_bg_esti_params`](set_bg_esti_params.md)
(see these for an explanation).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`BgEstiHandle`** (input_control)  bg_estimation `→`  (handle)

ID of the BgEsti data set.

**`Syspar1`** (output_control)  real `→`  (real)

1. system matrix parameter.

**`Syspar2`** (output_control)  real `→`  (real)

2. system matrix parameter.

**`GainMode`** (output_control)  string `→`  (string)

Gain type.

**`Gain1`** (output_control)  real `→`  (real)

Kalman gain / foreground adaptation time.

**`Gain2`** (output_control)  real `→`  (real)

Kalman gain / background adaptation time.

**`AdaptMode`** (output_control)  string `→`  (string)

Threshold adaptation.

**`MinDiff`** (output_control)  real `→`  (real)

Foreground / background threshold.

**`StatNum`** (output_control)  integer `→`  (integer)

Number of statistic data sets.

**`ConfidenceC`** (output_control)  real `→`  (real)

Confidence constant.

**`TimeC`** (output_control)  real `→`  (real)

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

`get_bg_esti_params` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`create_bg_esti`

## Possible Successors

`run_bg_esti`

## See also

`set_bg_esti_params`

## Module

Foundation
