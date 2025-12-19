---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMClassificationRule.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmclassificationrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmClassificationRule
---

# New-FsrmClassificationRule

## 摘要
创建一条自动分类规则。

## 语法

```
New-FsrmClassificationRule [-Name] <String> [-Description <String>] -Property <String>
 [-PropertyValue <String>] -Namespace <String[]> [-Disabled] [-ReevaluateProperty <RuleReevaluatePropertyEnum>]
 [-Flags <RuleFlagsEnum[]>] [-ContentRegularExpression <String[]>] [-ContentString <String[]>]
 [-ContentStringCaseSensitive <String[]>] -ClassificationMechanism <String> [-Parameters <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmClassificationRule` cmdlet 用于在服务器上创建自动分类规则。每个规则都会设置一个属性的值。默认情况下，规则仅运行一次，并会忽略那些已经具有该属性值的文件。不过，您可以配置规则以便无论属性是否已赋值，都对其进行评估。

## 示例

### 示例 1：创建一个分类规则
```
PS C:\> New-FsrmClassificationRule -Name "Find confidential files" -Namespace @("C:\shares\CtrShare03") -Property "Impact" -PropertyValue "High" -ClassificationMechanism "Content Classifier" -ContentString "Confidential"
```

此命令创建了一条分类规则：如果某个文件包含“Confidential”（机密）这个词，并且该文件尚未具有“Impact”属性，那么该文件的“Impact”值将被标记为“High”（高）。

### 示例 2：创建一个分类规则并覆盖属性值
```
PS C:\> New-FsrmClassificationRule -Name "Find confidential files" -Namespace @("C:\shares\CtrShare03") -Property "Impact" -PropertyValue "High" -ClassificationMechanism "Content Classifier" -ContentString "confidential" -ReevaluateProperty Overwrite
```

此命令创建一条分类规则：如果文件中包含“Confidential”（机密）这个词，则将该文件的“Impact”属性值标记为“High”（高风险），并覆盖原有的“Impact”属性值。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -ClassificationMechanism
指定服务器上可用的一种有效分类机制的名称，该机制用于为属性值分配相应的值。

分类机制由一系列插件提供，这些插件要么随 Windows Server® 2012 自带，要么由您或独立软件供应商（ISV）自行开发。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行。

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

### -ContentRegularExpression
指定一个正则表达式数组，用于模式匹配。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ContentString
指定一个字符串数组，供内容分类器进行搜索。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ContentStringCaseSensitive
指定一个包含大小写敏感字符串的数组，供内容分类器进行搜索。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Description
为分类规则指定一个描述。

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

### -Disabled
表示该分类规则已被禁用。

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

### -Flags
指定一个标志数组，该数组定义了规则可能的状态。此参数的可接受值为：

- ClearAutomaticallyClassifiedProperty.
Integer value 1024.
- ClearManuallyClassifiedProperty.
Integer value 2048.
- Deprecated.
Integer value 4096.

```yaml
Type: RuleFlagsEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: ClearAutomaticallyClassifiedProperty, ClearManuallyClassifiedProperty, Deprecated

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
为分类规则指定一个名称。

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

### -Namespace
指定一个命名空间数组，该规则将应用于这些命名空间中的内容。每个值必须是服务器上定义的 `FolderType` 属性的值（使用格式 “\[文件夹类型属性名称=\<值\>\”)，或者是静态路径。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Parameters
使用格式 `<名称>\>=<值>` 来指定一个字符串数组。文件分类基础设施（File Classification Infrastructure）和其他管理工具会使用这些参数。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Property
指定要设置的分类属性定义的名称。需要在 **FsrmClassificationPropertyDefinition** 对象中指定 “Name” 属性的值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PropertyValue
指定规则将赋予的属性值。您设置的属性值必须是您在 *ClassificationMechanism* 参数中指定的分类机制所支持的有效值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReevaluateProperty
指定规则的评估策略。该参数的可接受值包括：

- Never: Assign values to properties only if that property does not already have a value for the file.
- Overwrite: Reclassify files when the files change and overwrite this property.
- Aggregate: Reclassify files when the files change and aggregate the new value for the property with the existing value.

```yaml
Type: RuleReevaluatePropertyEnum
Parameter Sets: (All)
Aliases:
Accepted values: Never, Aggregate, Overwrite

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-FsrmClassificationPropertyDefinition](./Get-FsrmClassificationPropertyDefinition.md)

[Get-FsrmClassificationRule](./Get-FsrmClassificationRule.md)

[Remove-FsrmClassificationRule](./Remove-FsrmClassificationRule.md)

[Set-FsrmClassificationRule](./Set-FsrmClassificationRule.md)

