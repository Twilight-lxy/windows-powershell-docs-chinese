---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSDSMSupportedHW.cdxml-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/remove-msdsmsupportedhw?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-MSDSMSupportedHW
---

# 移除对 MSDFSMS 支持的硬件的相关内容

## 摘要
从 MSDSM 支持的硬件列表中删除具有特定供应商 ID 和产品 ID 组合的硬件 ID。

## 语法

### 按供应商产品ID排序（默认设置）
```
Remove-MSDSMSupportedHW [-VendorId] <String[]> [-ProductId] <String[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject (cdxml)
```
Remove-MSDSMSupportedHW -InputObject <CimInstance[]> [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [<CommonParameters>]
```

## 描述
`Remove-MSDSMSSupportedHW` cmdlet 会从微软设备特定模块（Microsoft Device Specific Module，简称 MSDSM）支持的硬件列表中移除具有特定供应商 ID 和产品 ID 组合的硬件标识符。

与MPCLAIM.exe不同，在指定供应商ID和产品ID时，请不要在字段中填充空格。

需要运行 `Update-MPIOClaimedHW` cmdlet 才能使多路径输入/输出（MPIO）的声明过程生效。

## 示例

#### 示例 1：根据供应商 ID 和产品 ID 删除相应的硬件 ID
```
PS C:\> Remove-MSDSMSupportedHW -VendorId "VendorX" -ProductId "ProductY"
```

这个示例将供应商ID（VendorX）和产品ID（ProductY）的组合从MSDSM支持的硬件列表中删除。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets。要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -InputObject
指定该cmdlet的输入内容。您可以使用此参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru
将对象传递给后续的处理流程（即“管道”）。

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

### -ProductId
指定产品ID。

```yaml
Type: String[]
Parameter Sets: ByVendorProductId
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算该命令的最佳限制值。此限制仅适用于当前运行的命令，而不适用于整个会话或计算机本身。

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

### -VendorId
指定供应商ID。

```yaml
Type: String[]
Parameter Sets: ByVendorProductId
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Clear-MSDSMSSupportedHW](./Clear-MSDSMS SupportedHW.md)

[Get-MSDSMSSupportedHW](./Get-MSDSMSSupportedHW.md)

[新支持的硬件设备（适用于 MSDS/MSDM）](./New-MSDSMSSupportedHW.md)

[更新已 claiming 的 MPIO 硬件](./Update-MPIOClaimedHW.md)

