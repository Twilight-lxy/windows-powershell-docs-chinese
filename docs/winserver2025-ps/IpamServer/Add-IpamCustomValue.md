---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamCustomValue.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/add-ipamcustomvalue?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-IpamCustomValue
---

# Add-IpamCustomValue

## 摘要
向 IPAM 中的自定义字段添加一个值。

## 语法

```
Add-IpamCustomValue [-Name] <String> [-Value] <String> [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-IpamCustomValue` cmdlet 用于向 IP 地址管理（IPAM）中的自定义字段添加值。您可以向内置字段或用户定义的自定义字段添加值。

## 示例

### 示例 1：添加自定义值
```
PS C:\> Add-IpamCustomValue -Name "Divisions" -Value "DivMain01"
```

此命令将自定义值“DivMain01”添加到名为“Divisions”的用户自定义字段中。

### 示例 2：向用户自定义的自定义字段添加一个自定义值
```
PS C:\> Add-IpamCustomValue -Name "Divisions" -Value "DivMain01" -PassThru
Value                  Category             CustomField
------------------------------------------------------------
DivMain01              UserDefined          Divisions
```

此命令将自定义值“DivMain01”添加到名为“Divisions”的用户定义的自定义字段中。该命令包含了“PassThru”参数，因此会将结果显示在控制台上。

### 示例 3：为内置的自定义字段添加一个自定义值
```
PS C:\> Add-IpamCustomValue -Name "ServiceInstance" -Value "vmm1.contoso.com" -PassThru
Value                  Category             CustomField
------------------------------------------------------------
vmm1.contoso.com       UserDefined          ServiceInstance
```

此命令将自定义值 `vmm1.contoso.com` 添加到名为 `ServiceInstance` 的内置自定义字段中。该命令包含了 `*PassThru*` 参数，因此会将结果显示在控制台上。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
在运行该 cmdlet 之前，会提示您进行确认。

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

### -Name
用于指定自定义字段的名称。该 cmdlet 会将您为 *Value* 参数指定的值添加到该自定义字段中。您可以指定本地化的服务器名称，或内置的多值自定义字段的非本地化名称。

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
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
指定可以同时执行该cmdlet的最大操作数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。该限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

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
指定一个要添加到自定义字段中的值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该 cmdlet 会发生什么情况。但实际上并未运行该 cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Windows.IpamCommands.IpamCustomValue
此 cmdlet 返回一个对象，其中包含一个 IPAM 自定义值。

## 备注

## 相关链接

[Remove-IpamCustomValue](./Remove-IpamCustomValue.md)

[ Rename-IpamCustomValue](./Rename-IpamCustomValue.md)

[Add-IpamCustomField](./Add-IpamCustomField.md)

[Get-IpamCustomField](./Get-IpamCustomField.md)

