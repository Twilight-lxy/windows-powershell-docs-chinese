---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMClassificationPropertyDefinition.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmclassificationpropertydefinition?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmClassificationPropertyDefinition
---

# 新的FsrmClassificationProperty定义

## 摘要
创建一个分类属性定义。

## 语法

```
New-FsrmClassificationPropertyDefinition [-Name] <String> [-DisplayName <String>] [-Description <String>]
 -Type <PropertyDefinitionTypeEnum> [-PossibleValue <CimInstance[]>] [-Parameters <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmClassificationPropertyDefinition` cmdlet 在服务器上创建一个分类属性定义。创建属性定义的目的是为了指定用于对文件进行分类的属性；一个或多个分类规则可以关联到该属性。File Server Resource Manager (FSRM) 服务器将属性定义的数量限制为 100 个。

## 示例

### 示例 1：创建一个“YesNo”分类属性定义
```
PS C:\> New-FsrmClassificationPropertyDefinition -Name "ClassProp01" -DisplayName "Central Level Definitions" -Type YesNo
```

这个命令创建了一个名为“ClassProp01”的YesNo分类属性定义，其显示名称为“Central Level Definitions”。

### 示例 2：创建一个有序列表分类属性定义
```
PS C:\> New-FsrmClassificationPropertyDefinition -Name "Impact" -Type OrderedList -PossibleValue @("High","Moderate","Low")
```

此命令创建了一个名为“Impact”的`OrderedList`分类属性定义，并指定了该属性可能取的值。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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

### -Description
为属性定义指定一个描述性说明。

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

### -DisplayName
为该属性指定一个可选的名称。

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

### -Name
为该属性指定一个名称。

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

### -Parameters
使用 `<名称>\>=<值>` 的格式指定一个字符串数组。文件分类系统（File Classification Infrastructure）和其他管理工具会使用这些参数。

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

### -PossibleValue
用于指定一组属性值。默认值为空列表。您可以使用 **New-FsrmClassificationPropertyValue** cmdlet 来为某个分类属性创建可能的值。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -Type
指定分类属性定义的类型。此参数的可接受值为：

- OrderedList
- MultiChoice
- SingleChoice
- String
- MultiString
- Integer
- YesNo
- DateTime

```yaml
Type: PropertyDefinitionTypeEnum
Parameter Sets: (All)
Aliases:
Accepted values: OrderedList, MultiChoice, SingleChoice, String, MultiString, Integer, YesNo, DateTime

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

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
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### System.String

### Microsoft.PowerShell.Cmdletization.GeneratedTypes.PropertyDefinitionTypeEnum

### System.String[]

## 输出

### System.Object
## 备注

## 相关链接

[Get-FsrmClassificationPropertyDefinition](./Get-FsrmClassificationPropertyDefinition.md)

[New-FsrmClassificationPropertyValue](./New-FsrmClassificationPropertyValue.md)

[Remove-FsrmClassificationPropertyDefinition](./Remove-FsrmClassificationPropertyDefinition.md)

[Set-FsrmClassificationPropertyDefinition](./Set-FsrmClassificationPropertyDefinition.md)

[更新-FsrmClassificationPropertyDefinition](./Update-FsrmClassificationPropertyDefinition.md)

