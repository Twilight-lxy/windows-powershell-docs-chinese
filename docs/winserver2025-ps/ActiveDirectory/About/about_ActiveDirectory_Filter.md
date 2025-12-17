---
title: about_ActiveDirectory_Filter
ms.date: 04/22/2013
description: 描述了 Windows PowerShell 的 Active Directory 模块所支持的搜索过滤器的的语法及其行为。
Locale: en-US
schema: 2.0.0
---

# 关于 ActiveDirectoryFilter

## 简要描述

描述了 Windows PowerShell 中 Active Directory 模块支持的搜索过滤器的语法和行为。

## 详细描述

大多数用于操作 Active Directory 的 get-AD* 模块 cmdlet 都使用 Filter 参数来搜索对象。Filter 参数的实现目的是替代 LDAP 过滤器的功能，并增加了对 PowerShell 变量、丰富数据类型的支持，改进了错误检查机制，同时还采用了扩展版的 PowerShell 表达式语言（Active Directory Extended Form of PowerShell Expression Language）。


- Support for LDAP Filter Syntax

通过 `LDAPFilter` 参数可以支持 LDAP 过滤语法。您可以在本主题的“过滤示例”部分找到 LDAP 过滤器的示例，以及新的 Active Directory 模块中的过滤器示例。


- Search Breadth and Depth

您通过过滤器驱动的搜索的范围和深度可以通过两个 Active Directory 模块cmdlet参数来修改：**SearchBase** 和 **SearchScope**。

在 Active Directory 提供者的上下文中，如果未指定 **SearchBase** 参数，**SearchBase** 将默认为当前路径。当不在 Active Directory 提供者下运行时，**SearchBase** 将默认为服务器的 **DefaultNamingContext**。

`SearchScope` 参数的默认值为 `Subtree`，该值属于枚举类型 `ADSearchScope`。

有关更多信息，请参阅任何 `Get-AD*` cmdlet 中的 **SearchBase** 和 **SearchScope** 参数描述。

- Search Result Behavior

Active Directory模块在返回搜索结果时的行为会受到两个cmdlet参数的影响：**ResultPageSize** 和 **ResultSetSize**。

`ResultSetSize` 控制返回的对象的最大数量。

`ResultPageSize` 指定了每页返回的信息中对象的最大数量。

有关更多信息，请参阅任何 `Get-AD*` cmdlet 中的 **ResultPageSize** 和 **ResultSetSize** 参数描述。


- Timeout Behavior

以下语句指定了 Active Directory 模块中的超时条件，并描述了针对这些超时情况可以采取的措施。

所有操作的默认Active Directory模块超时时间为2分钟。

对于搜索操作，Active Directory模块使用分页控制机制，并且每次页面搜索的超时时间为2分钟。

> [!注意] > 由于搜索过程可能涉及多次向服务器发起页面请求，因此整个搜索时间可能会超过2分钟。

一个 **TimeoutException** 错误表示发生了超时现象。

在进行搜索操作时，如果您遇到了 **TimeoutException** 错误，可以选择使用更小的页面大小。您可以通过设置 **ResultPageSize** 参数来调整页面大小。

如果尝试了这些更改后仍然出现 **TimeoutException** 错误，请参考本主题中“优化过滤器”部分的指导来优化您的过滤器。


- Optimizing Filters

你可以按照这些指导原则来改进搜索过滤器的功能。

  - Avoid using the **Recursive** parameter as it intensifies resource usage of
    the search operation.
  - Avoid using bitwise AND operators and bitwise OR operators. For more
    information, see the Supported Operators section of this topic.
  - Avoid using the logical NOT operator.
  - Break down your search into multiple queries with narrower conditions.

有关过滤器语法和用法的完整描述，请参阅本主题中的“过滤器语法”部分。


## 过滤器示例

以下部分展示了在常见查询中如何使用过滤器的许多示例。

### 示例 1 - 获取所有条目：

- LDAP Filter Equivalent: `(objectClass=*)`

```powershell
Get-ADObject -Filter 'ObjectClass -like "*"'
```

### 示例 2 - 获取在常用名称中包含“bob”的条目

- LDAP Filter Equivalent: `(cn=*bob*)`

```powershell
Get-ADObject -Filter 'CN -like "*bob*"'
```

### 示例 3 - 获取密码错误次数超过五次的条目

- LDAP Filter Equivalent: `(&(!badpwdcount<=5)(badpwdcount=*))`

```powershell
Get-ADUser -Filter 'badpwdcount -ge 5'
```

### 示例 4 – 获取所有具有电子邮件属性的用户

- LDAP Filter Equivalent: `(&(objectClass=user)(email=*))`

```powershell
Get-ADUser -filter 'email -like "*"'
```

或者

```powershell
Get-ADObject -filter 'email -like "*" -and ObjectClass -eq "user"'
```

### 示例 5 - 获取所有具有电子邮件属性（email）且姓氏（surname）等于“smith”的用户记录：

- LDAP Filter Equivalent: `(&(sn=smith)(objectClass=user)(email=*))`

```powershell
Get-ADUser -Filter 'Email -like "*" -and SurName -eq "smith"'
```

或者

```powershell
Get-ADUser -Filter 'Email -like "*" -and sn -eq "smith"'
```


### 示例 6 – 获取所有名字以 “andy” 开头且具有相同名称的用户记录，以及名字为 “steve” 或 “margaret”的用户记录

- LDAP Filter Equivalent: `(&(objectClass=user) | (cn=andy*)(cn=steve)(cn=margaret))`

```powershell
Get-ADUser -Filter 'CN -like "andy*" -or CN -eq "steve" -or CN -eq "margaret"'
```


这个示例展示了更复杂的逻辑，并说明了如何通过括号来实现优先级控制。

```powershell
Get-ADObject -Filter 'objectClass -eq "user" -and (CN -like "andy*" -or CN -eq "steve" -or CN -eq "margaret")'
```

### 示例 7 – 获取所有没有电子邮件属性的条目

- LDAP Filter Equivalent: `(!(email=*))`

```powershell
Get-ADUser -Filter '-not Email -like "*"'
```

或者

```powershell
Get-ADUser -Filter 'Email -notlike "*"'
```

### 示例 8 - 获取所有自 2007 年 1 月 1 日以来未登录过的用户

- LDAP Filter Equivalent: `(&(lastlogon<=X)(objectClass=user))` where X is
  number of 100-nanosecond slices since Jan 1st 1601

```powershell
$date = new-object System.DateTime -ArgumentList @(2007,1,1,0,0,0)
Get-ADUser -Filter '-not LastLogon -le $date'
```

### 示例 9 - 获取在过去 5 天内登录过的所有用户

- LDAP Filter Equivalent:

  ```
  (&(lastLogon>=128812906535515110)
    (objectClass=user)(!(objectClass=computer)))
  ```

```powershell
$date = (get-date) - (new-timespan -days 5)
Get-ADUser -Filter 'lastLogon -gt $date'
```

### Example 10 - Search for group objects that have the ADS_GROUP_TYPE_SECURITY_ENABLED flag set

- LDAP Filter Equivalent:
  `(&(objectCategory=group)(groupType:1.2.840.113556.1.4.803:=2147483648))`

以下示例查询字符串用于搜索那些设置了 `ADS_GROUP_TYPE_security_ENABLED` 标志的组对象。请注意，用于比较的值是 `ADS_GROUP_TYPE SECURITYEnabled` 的十进制表示（0x80000000 = 2147483648）。

```powershell
Get-ADGroup -filter 'groupType -band 0x80000000'
```

### 示例 11 – 查找某个对象的起源信息

- LDAP Filter Equivalent:
  `(memberof:1.2.840.113556.1.4.1941:=(cn=Group1,OU=groupsOU,DC=x)))`

`LDAP_MATCHING_RULE_INCHAIN` 是一个用于匹配的规则 OID（Object Identifier），其设计目的是提供一种方法来查找某个对象的“祖先”关系（即该对象所属的层级结构）。许多使用 Active Directory 和 AD LDS 的应用程序通常处理的是具有父子关系的层次化数据。在过去，这些应用程序会通过执行“传递性组扩展”（transitive group expansion）操作来确定对象的组成员身份，这一过程会消耗大量网络带宽。为了判断某个对象是否属于某个组，应用程序需要多次进行网络请求（往返通信），以确认是否能够沿着层级链一直访问到该组的根节点。

这样一个查询的例子是用来检查用户“user1”是否属于组“group1”。用户“user1”可能不是组“group1”的直接成员，它可能是某个其他组的成员，而那个其他组又是组“group1”的成员。

您可以将基础（base）设置为用户的 DN（Distinguished Name），范围（scope）也设置为“base”，然后使用以下查询：

```powershell
Get-ADUser -Filter 'memberOf -RecursiveMatch "CN=Administrators, CN=Builtin,DC=Fabrikam,DC=com"' -SearchBase "CN=Administrator,CN=Users,DC=Fabrikam,DC=com"
```

## 过滤器语法

以下语法描述使用了巴克斯-诺尔（Backus-Naur）形式来展示用于 `Filter` 参数的 PowerShell 表达式语言。

```Syntax
<filter>  ::= "{" <FilterComponentList> "}"

<FilterComponentList> ::= <FilterComponent> |
  <FilterComponent> <JoinOperator> <FilterComponent> |
  <NotOperator>  <FilterComponent>

<FilterComponent> ::= <attr> <FilterOperator> <value> |
  "(" <FilterComponent> ")"

<FilterOperator> ::= "-eq" | "-le" | "-ge" | "-ne" | "-lt" | "-gt" |
  "-approx" | "-bor" | "-band" | "-recursivematch" | "-like" |
  "-notlike"

<JoinOperator> ::= "-and" | "-or"

<NotOperator> ::= "-not"

<attr> ::= <PropertyName> | <LDAPDisplayName of the attribute>

<value>::= < this value will be compared to the object data for
  attribute <ATTR> using the specified filter operator
```


## 支持的操作符

下表展示了常用的搜索过滤器操作符。

|     Operator      |              Description               |      LDAP Equivalent       |
| ----------------- | -------------------------------------- | -------------------------- |
| `-eq`             | Equal to. Wildcards not supported.     | =                          |
| `-ne`             | Not equal to. Wildcards not supported. | !x = y                     |
| `-approx`         | Approximately equal to                 | ~=                         |
| `-le`             | Lexicographically less than            | <=                         |
|                   | or equal to                            |                            |
| `-lt`             | Lexicographically less than            | !x >= y                    |
| `-ge`             | Lexicographically greater              | >=                         |
|                   | than or equal to                       |                            |
| `-gt`             | Lexicographically greater than         | !x <= y                    |
|                   |                                        |                            |
| `-and`            | AND                                    | &                          |
| `-or`             | OR                                     |                            |
| `-not`            | NOT                                    | !                          |
| `-bor`            | Bitwise OR                             | :1.2.840.113556.1.4.804:=  |
| `-band`           | Bitwise AND                            | :1.2.840.113556.1.4.803:=  |
| `-recursivematch` | Use LDAP_MATCHING_RULE_IN_CHAIN        | :1.2.840.113556.1.4.1941:= |
| `-like`           | Similar to `-eq` and supports          | =                          |
|                   | wildcard comparison. The only          |                            |
|                   | wildcard character supported is: `*`   |                            |
| `-notlike`        | Not like. Supports wild                | !x = y                     |
|                   | card comparison.                       |                            |

> [!注意] > 除了“*”之外，PowerShell中的通配符（如“?”）不支持**Filter**参数语法。

### 运算符优先级

以下列表显示了过滤器中运算符的优先级，从高到低排列。

- Highest precedence: `-eq`, `-ge`, `-le`, `-approx`, `-band`, `-bor`,
  `-recursivematch`, `-ne`, `-like`, `-not`, `-and`
- Lowest precedence: `-or`

### 特殊字符

在 AD 过滤器字符串数据中（即被双引号或单引号括起来的数据），应使用以下转义序列来表示特殊字符。

| ASCII Character |             Escape sequence substitute              |
| --------------- | --------------------------------------------------- |
| `"`             | `` `" ``  (This escape sequence is only required if |
|                 | STRING data is enclosed in double quotes.)          |
| `'`             | `''`  (This escape sequence is only required if     |
|                 | STRING data is enclosed in single quotes.)          |
| NUL             | `\00` (This is a standard LDAP escape sequence.)    |
| `\`             | `\5c` (This is a standard LDAP escape sequence.)    |

### LDAP特殊字符

ADFilter解析器会自动将STRING数据中出现的所有以下字符（即用“”或‘’括起来的数据）转换为其LDAP转义序列。最终用户无需了解这些LDAP转义序列。

| ASCII Character |           Escape sequence substitute            |
| --------------- | ----------------------------------------------- |
| `*`             | `\2a`  (Character `*` will only be converted in |
|                 | -eq and -ne comparisons Users should use        |
|                 | -like and -notlike operators for wildcard       |
|                 | comparison.)                                    |
| `(`             | `\28`                                           |
| `)`             | `\29`                                           |
| `/`             | `\2f`                                           |
