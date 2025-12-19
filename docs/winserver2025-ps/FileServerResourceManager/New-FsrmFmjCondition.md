---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMFmjCondition.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmfmjcondition?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmFmjCondition
---

# New-FsrmFmjCondition

## 摘要
创建一个文件管理属性条件对象。

## 语法

```
New-FsrmFmjCondition [-Property] <String> [-Condition] <FmjConditionTypeEnum> [-Value <String>]
 [-DateOffset <Int32>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`New-FsrmFmjCondition` cmdlet 用于创建一个文件管理条件对象。该文件管理条件对象用于定义一种规则，以确定文件管理作业是否应对某个文件执行相应的操作。

## 示例

### 示例 1：创建一个属性条件
```
PS C:\> New-FsrmFmjCondition -Property "PII" -Condition Equal -Value "1"
```

此命令创建了一个属性条件，用于验证某个文件的 PII（个人身份信息）分类属性是否被设置为“true”（即已启用该分类）。

### 示例 2：根据文件分类创建条件
```
PS C:\> New-FsrmFmjCondition -Property "DatePublished" -Condition Equal -Value "File.DateLastModified"
```

该命令根据文件的分类创建一个条件。该命令会检查文件是否具有 `DatePublished` 分类属性（类型为 `DateTime`），并且该属性的值设置为文件的最后修改时间戳。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如使用[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Condition
指定文件管理作业必须匹配的属性条件。此参数的可接受值为：

- Equal
- NotEqual
- GreaterThan
- LessThan
- Contain
- Exist
- NotExist
- StartWith
- EndWith
- ContainedIn
- PrefixOf
- SuffixOf
- MatchesPattern

```yaml
Type: FmjConditionTypeEnum
Parameter Sets: (All)
Aliases:
Accepted values: Equal, NotEqual, GreaterThan, LessThan, Contain, Exist, NotExist, StartWith, EndWith, ContainedIn, PrefixOf, SuffixOf, MatchesPattern

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
Prompts you for confirmation before running the cmdlet.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -DateOffset
Specifies an offset from the *Value* parameter for DateTime values.
The default value is 0.

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Property
Specifies the property to compare for the condition.
Specify one of the following values:

- The name of a classification property definition on the server.
(Do not specify the display name of the property definition.)
- The string File.Name
- The string File.DateCreated
- The string File.DateLastModified
- The string File.DateLastAccessed

The value of this parameter limits the values that other parameters to the cmdlet can accept as follows:

File.Name:

- You can set the *Condition* parameter only to MatchesPattern.
- The *Value* parameter must contain a semi-colon separated list of wildcard patterns.
- You cannot specify the *DateOffset* parameter.

File.DateCreated, File.DateLastModified, or File.DateLastAccessed:

- You can set the *Condition* parameter only to LessThan or Equal.
- If you specify the *DateOffset* parameter, you can set the *Value* parameter to one of the following: File.DateCreated, File.DateLastModified, File.DateLastAccessed, or Date.Now.
- If you do not specify the *DateOffset* parameter, you can set the *Value* parameter to a FileTime value.

The name of a classification property definition whose Type is DateTime:

- You can set the *Condition* parameter to Exist, NotExist, Equal, NotEqual, LessThan, GreaterThan.
- If you specify the *DateOffset* parameter, the *Value* parameter can contain one of the following: File.DateCreated, File.DateLastModified, File.DateLastAccessed, or Date.Now.
- If you do not specify the *DateOffset* parameter, the *Value* parameter can contain a FileTime value.

The name of a classification property definition whose Type is not DateTime:

- You cannot specify the *DateOffset* parameter.
- If the *Condition* parameter is Exist or NotExist, you cannot specify the *Value* parameter.
- If the Type is Integer, you can set the *Condition* parameter to Equal, NotEqual, Exist, NotExist, LessThan, GreaterThan.
- If the Type is String, you can set the *Condition* parameter to Equal, NotEqual, Exist, NotExist, Contains, IsContainedIn, LessThan, GreaterThan, StartsWith, EndsWith, PrefixOf, SuffixOf.
- If the Type is YesNo, you can set the *Condition* parameter to Equal, NotEqual, Exist, NotExist.
- If the Type is OrderedList, you can set the *Condition* parameter to Equal, NotEqual, Exist, NotExist, LessThan, GreaterThan.
- If the Type is SingleChoice, you can set the *Condition* parameter to Equal, NotEqual, Exist, NotExist.
- If the Type is MultiChoice, you can set the *Condition* parameter to Equal, NotEqual, Exist, NotExist, Contains.
- If the Type is MultiString, you can set the *Condition* parameter to Equal, NotEqual, Exist, NotExist, Contains.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
Specifies the maximum number of concurrent operations that can be established to run the cmdlet.
If this parameter is omitted or a value of `0` is entered, then Windows PowerShell® calculates an optimum throttle limit for the cmdlet based on the number of CIM cmdlets that are running on the computer.
The throttle limit applies only to the current cmdlet, not to the session or to the computer.

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Value
Specifies a name of a file condition property value.
Do not specify this parameter if you specify Exists or NotExist for the *Condition* parameter.
If you specify the name of a DateTime property, specify the *DateOffset* parameter.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.PowerShell Cmdletization GeneratedTypes.FmjConditionTypeEnum

### System.Int32

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[Get-FsrmClassificationPropertyDefinition](./Get-FsrmClassificationPropertyDefinition.md)

