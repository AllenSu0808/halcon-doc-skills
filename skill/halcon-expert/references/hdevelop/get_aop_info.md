# get_aop_info (Operator)

## Name

`get_aop_info` — Return AOP information for operators.

## Signature

`get_aop_info( : : OperatorName, IndexName, IndexValue, InfoName : InfoValue)`

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
*`OperatorName`*, the iconic type, and
a parameter string value denoting a special mode or method supported by the
indexed operator. The latter two indices are passed by *`IndexName`*
and *`IndexValue`*. *`IndexName`* holds the dimension
identifier whereas *`IndexValue`* holds the index value as returned
in [`query_aop_info`](query_aop_info.md).

`get_aop_info` returns the specific information parts of an operator's
AOP knowledge in *`InfoValue`* if exactly one index per stage was set.
The scope of information is specified by *`InfoName`* and supports
following values:

- ***'max_threads'*** —

  returns the maximum allowed thread number.
  If no optimization data is stored, *`InfoValue`* contains
  *-1*. In case the specified operator does not support automatic
  parallelization, *1* is returned.
- ***'split_level'*** —

  returns all allowed data
  split levels of the automatic parallelization for this operator, the
  specified iconic type and parameter value. Possible levels are
  *'split_tuple'*, *'split_channel'*,
  *'split_domain'*, and *'split_partial'*. If no split
  level is supported or every level was switched off for the indexed
  operator an empty string *''* is returned. Use
  [`get_operator_info`](get_operator_info.md) to query all split levels generally supported by
  an operator.
- ***'model'*** —

  returns the stored model type. Possible values
  are *'threshold'*, *'linear'*, and *'mlp'*
  (see also the description of operator [`optimize_aop`](optimize_aop.md)). If
  no optimization data is stored, an empty string is returned.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`OperatorName`** (input_control)  string `→`  (string / integer)

Operator to get information for

Suggested values:
'mean_image', 'opening_circle', 'find_shape_model'

**`IndexName`** (input_control)  string-array `→`  (string)

Further index stages

Default:
['iconic_type','parameter:0']

**`IndexValue`** (input_control)  string-array `→`  (string)

Further index values

Number of elements:
IndexName == IndexValue

Default:
['byte','']

**`InfoName`** (input_control)  string `→`  (string)

Scope of information

Default:
'max_threads'

Suggested values:
'max_threads', 'split_level', 'model'

**`InfoValue`** (output_control)  string(-array) `→`  (string)

Value of information

## Result

`get_aop_info` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Module

Foundation
