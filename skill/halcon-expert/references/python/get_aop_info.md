# get_aop_info (Operator)

## Name

`get_aop_info` — Return AOP information for operators.

## Signature

`def get_aop_info(operator_name: Union[str, int], index_name: Sequence[str], index_value: Sequence[str], info_name: str) -> Sequence[str]`

`def get_aop_info_s(operator_name: Union[str, int], index_name: Sequence[str], index_value: Sequence[str], info_name: str) -> str`

## Description

HALCON supports a mechanism to optimize the behavior of automatic operator
parallelization (AOP) for a given hardware of a machine. The
information for this optimization can be determined by the operator
[`optimize_aop`](optimize_aop.md) and can also be partly modified by the operator
[`set_aop_info`](set_aop_info.md).

To address specific AOP information, the operator's optimization data
is indexed within
a 3-ary hierarchy that can be obtained by [`query_aop_info`](query_aop_info.md). The
three hierarchy stages are indexed by the operator name, passed in
*`operator_name`*, the iconic type, and
a parameter string value denoting a special mode or method supported by the
indexed operator. The latter two indices are passed by *`index_name`*
and *`index_value`*. *`index_name`* holds the dimension
identifier whereas *`index_value`* holds the index value as returned
in [`query_aop_info`](query_aop_info.md).

`get_aop_info` returns the specific information parts of an operator's
AOP knowledge in *`info_value`* if exactly one index per stage was set.
The scope of information is specified by *`info_name`* and supports
following values:

- ***"max_threads"*** —

  returns the maximum allowed thread number.
  If no optimization data is stored, *`info_value`* contains
  *-1*. In case the specified operator does not support automatic
  parallelization, *1* is returned.
- ***"split_level"*** —

  returns all allowed data
  split levels of the automatic parallelization for this operator, the
  specified iconic type and parameter value. Possible levels are
  *"split_tuple"*, *"split_channel"*,
  *"split_domain"*, and *"split_partial"*. If no split
  level is supported or every level was switched off for the indexed
  operator an empty string *""* is returned. Use
  [`get_operator_info`](get_operator_info.md) to query all split levels generally supported by
  an operator.
- ***"model"*** —

  returns the stored model type. Possible values
  are *"threshold"*, *"linear"*, and *"mlp"*
  (see also the description of operator [`optimize_aop`](optimize_aop.md)). If
  no optimization data is stored, an empty string is returned.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`operator_name`** (input_control)  string `→` Union[str, int]

Operator to get information for

Suggested values:
"mean_image", "opening_circle", "find_shape_model"

**`index_name`** (input_control)  string-array `→` Sequence[str]

Further index stages

Default:
["iconic_type","parameter:0"]

**`index_value`** (input_control)  string-array `→` Sequence[str]

Further index values

Number of elements:
IndexName == IndexValue

Default:
["byte",""]

**`info_name`** (input_control)  string `→` str

Scope of information

Default:
"max_threads"

Suggested values:
"max_threads", "split_level", "model"

**`info_value`** (output_control)  string(-array) `→` Sequence[str]

Value of information

## Result

`get_aop_info` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Module

Foundation
