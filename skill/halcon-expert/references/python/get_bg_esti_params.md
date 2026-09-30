# get_bg_esti_params (Operator)

## Name

`get_bg_esti_params` — Return the parameters of the data set.

## Signature

`def get_bg_esti_params(bg_esti_handle: HHandle) -> Tuple[float, float, str, float, float, str, float, int, float, float]`

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

**`bg_esti_handle`** (input_control)  bg_estimation `→` HHandle

ID of the BgEsti data set.

**`syspar_1`** (output_control)  real `→` float

1. system matrix parameter.

**`syspar_2`** (output_control)  real `→` float

2. system matrix parameter.

**`gain_mode`** (output_control)  string `→` str

Gain type.

**`gain_1`** (output_control)  real `→` float

Kalman gain / foreground adaptation time.

**`gain_2`** (output_control)  real `→` float

Kalman gain / background adaptation time.

**`adapt_mode`** (output_control)  string `→` str

Threshold adaptation.

**`min_diff`** (output_control)  real `→` float

Foreground / background threshold.

**`stat_num`** (output_control)  integer `→` int

Number of statistic data sets.

**`confidence_c`** (output_control)  real `→` float

Confidence constant.

**`time_c`** (output_control)  real `→` float

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
