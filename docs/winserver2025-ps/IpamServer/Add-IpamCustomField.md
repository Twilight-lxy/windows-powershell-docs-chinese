---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCustomField.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/add-ipamcustomfield?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IpamCustomField
---

# Add-IpamCustomField

## 摘要
向 IPAM 添加一个自由格式或多值的自定义字段。

## 语法

```
Add-IpamCustomField [-Name] <String> [-MultiValue] [-Value <String[]>] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-IpamCustomField` cmdlet 用于向 IP 地址管理（IPAM）系统中添加自定义字段。需要为该自定义字段指定一个名称。默认情况下，自定义字段的格式是自由的（即可以输入任意类型的值）。如果希望该自定义字段支持多值输入，请使用 `MultiValue` 参数进行设置。

## 示例

### 示例 1：添加自定义字段
```
PS C:\> Add-IpamCustomField -Name "CustomField01" -PassThru
Name                  Category               Multivalue        CustomValue
---------------------------------------------------------------------------------
CustomField01         UserDefined            False
```

此命令会在 IPAM 服务器上添加一个名为 “CustomField01” 的自定义字段，并返回该自定义字段对象。默认情况下，这个自定义字段是自由格式的（即可以输入任意类型的数据）。

### 示例 2：添加一个多值自定义字段
```
PS C:\> Add-IpamCustomField -Name "CustomMVField02" -MultiValue -PassThru
Name                  Category               Multivalue        CustomValue
---------------------------------------------------------------------------------
CustomMVField02       UserDefined            True
```

这个命令会在IPAM服务器上添加一个名为CustomMVField02的多值自定义字段，并返回该自定义字段对象。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，也可以输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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
在运行该cmdlet之前，会提示您进行确认。

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

### -MultiValue
表示该自定义字段允许多个值。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
为自定义字段指定一个名称。

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

### -PassThru
返回一个对象，表示您正在操作的项。默认情况下，此cmdlet不会生成任何输出。

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

### -ThrottleLimit
该参数用于指定可以同时执行的命令操作的最大数量。如果省略此参数或输入值为 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳限制值（即并发操作的最大数量）。这个限制仅适用于当前的命令本身，而不适用于整个会话或整个计算机。

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
为自定义字段指定一个值数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: CustomValueName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Windows.IpamCommands.IpamCustomField
此cmdlet返回一个对象，其中包含一个IPAM自定义字段。

## 备注

## 相关链接

[Add-IpamCustomValue](./Add-IpamCustomValue.md)

[Get-IpamCustomField](./Get-IpamCustomField.md)

[Remove-IpamCustomField](./Remove-IpamCustomField.md)

[ Rename-IpamCustomField](./Rename-IpamCustomField.md)

