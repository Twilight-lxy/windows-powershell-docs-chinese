---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSDSMSupportedHW.cdxml-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/new-msdsmsupportedhw?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-MSDSMSupportedHW
---

# 新支持的硬件（适用于 MSDSMS）

## 摘要
在 MSDSM 支持的硬件列表中，创建一个包含供应商 ID 和产品 ID 组合的硬件 ID。

## 语法

### 按供应商和产品ID排序（默认设置）
```
New-MSDSMSupportedHW [-VendorId] <String> [-ProductId] <String> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 适用范围（ByAllApplicable）
```
New-MSDSMSupportedHW [-AllApplicable] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`New-MSDSMSSupportedHW` cmdlet 用于在支持 Microsoft 设备专用模块（MSDSM）的硬件列表中，创建一个新的硬件标识符（ID），该标识符包含特定的供应商 ID 和产品 ID 组合。

与 MPCLAIM.exe 不同，当您指定供应商 ID 和产品 ID 时，请不要在这些字段中添加空格（即不要使用空格来填充这些字段）。

必须运行 `Update-MPIOClaimedHW` cmdlet，才能使多路径I/O（MPIO）的声明过程生效。

## 示例

### 示例 1：添加硬件 ID
```
PS C:\> New-MSDSMSupportedHW -ProductID "VendorX" -VendorID "ProductY"
```

这个示例将一个硬件标识符添加到 MSDSM（Microsoft System Device Manager）支持的硬件列表中，该标识符由供应商 ID “VendorX” 和产品 ID “ProductY” 组成。

### 示例 2：添加所有适用的硬件 ID
```
PS C:\> New-MSDSMSupportedHW -AllApplicable
```

这个示例会找到所有符合条件的设备，并将相应的硬件标识符添加到 MSDSM 支持的硬件列表中。符合条件的设备是指那些通过光纤通道（Fibre Channel）、iSCSI 或 SAS 协议连接到系统的设备。

## 参数

### -AllApplicable
指定所有通过光纤通道（Fibre Channel）、iSCSI 或 SAS 连接到系统的适用设备都会被添加到 MSDSM 支持的硬件列表中。

```yaml
Type: SwitchParameter
Parameter Sets: ByAllApplicable
Aliases: All

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -ProductId
指定产品ID。

```yaml
Type: String
Parameter Sets: ByVendorProductId
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值为`0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令（cmdlets）的数量来计算该命令的最佳限制值。这个限制仅适用于当前执行的命令本身，而不涉及整个会话或计算机。

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
Type: String
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

[Clear-MSDSMSSupportedHW](./Clear-MSDSMSSupportedHW.md)

[Get-MSDSMSSupportedHW](./Get-MSDSMSSupportedHW.md)

[Remove-MSDSMSSupportedHW](./Remove-MSDSMSSupportedHW.md)

[Update-MPIOClaimedHW](./Update-MPIOClaimedHW.md)

