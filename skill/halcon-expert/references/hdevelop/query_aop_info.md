# query_aop_info (Operator)

## Name

`query_aop_info` — Query indexing structure of AOP information for operators.

## Signature

`query_aop_info( : : OperatorName, IndexName, IndexValue : Name, Value)`

## Description

HALCON supports a mechanism to adapt the behavior of automatic
parallelization of image processing operators (AOP) to the machine's
hardware capability. The
information for this adaption can be obtained by the operator
[`optimize_aop`](optimize_aop.md) and can be partly read and modified by the operators
[`get_aop_info`](get_aop_info.md) and [`set_aop_info`](set_aop_info.md), respectively. To address
specific AOP information the operator's optimization data is indexed within
a 3-ary hierarchy that can be obtained by `query_aop_info`. The
three hierarchy stages are indexed by the operator name, the iconic type,
and a parameter string value denoting a special mode or method supported by
the operator.

If an empty string *''* is passed to *`OperatorName`*,
the parameters *`IndexName`* and *`IndexValue`* are ignored and
all operator names in *`Value`* are returned, for which optimization
data is stored.
*`Name`* contains the index identifier *'operator'* as many
times as operator names are returned. Specifying a single operator
name in *`OperatorName`* and passing an empty string *''* to the
parameters
*`IndexName`* and *`IndexValue`* queries all iconic types
the operator holds optimization data for. *`Value`* contains the type
strings, *`Name`* the index identifier *'iconic_type'*,
respectively. Finally, when specifying a certain
operator in *`OperatorName`* and a specific iconic type by passing the
dimension identifier *'iconic_type'* to *`IndexName`* and
the specific iconic type to *`IndexValue`*, *`Name`* contains
the parameter index identifier *`Value`* holds the parameter string
values supported by the operator. The format of the parameter identifier
string is compound containing the string *parameter*, followed by
a colon separator *:* and a digit, denoting the
parameter index (starting with 1). If the operator does not
support any mode parameter or the operator's parameter values were not
varied during optimization process of [`optimize_aop`](optimize_aop.md) the string
*'parameter:0'* is returned for *`Name`* and *`Value`*
contains an empty string. In case no AOP information is stored for the
specified index, *`Name`* returns an empty string.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`OperatorName`** (input_control)  string `→`  (string / integer)

Operator to get information for

Default:
''

**`IndexName`** (input_control)  string(-array) `→`  (string / integer)

Further specific index

Default:
''

Suggested values:
'', 'iconic_type'

**`IndexValue`** (input_control)  string(-array) `→`  (string / integer)

Further specific address

Number of elements:
IndexName == IndexValue

Default:
''

Suggested values:
'', 'byte', 'int1', 'int2', 'uint2', 'int4', 'int8', 'direction', 'cyclic', 'vector_field', 'complex', 'region', 'xld', 'xld_cont', 'xld_poly'

**`Name`** (output_control)  string-array `→`  (string)

Name of next index stage

**`Value`** (output_control)  string-array `→`  (string)

Values of next index stage

## Result

`query_aop_info` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Module

Foundation
