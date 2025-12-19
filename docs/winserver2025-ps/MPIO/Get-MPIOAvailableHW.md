---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MPIOAvailableHW.cdxml-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/get-mpioavailablehw?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MPIOAvailableHW
---

# Get-MPIOAvailableHW

## 摘要
列出系统中可通过MSDSM进行管理的、适用于MPIO（多路径I/O）的设备。

## 语法

```
Get-MPIOAvailableHW [[-VendorId] <String[]>] [[-ProductId] <String[]>] [-BusType <BusType[]>]
 [-IsMultipathed <Boolean[]>] [-IsSPC3Supported <Boolean[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-MPIOAvailableHW` cmdlet 可以列出系统中可用的硬件设备，这些设备可以通过微软的设备特定模块（Microsoft Device Specific Module，简称 MSDSM）来管理，以实现多路径输入/输出（Multipath I/O，简称 MPIO）功能。

要将某个设备添加到 MSDSM 支持的硬件列表中，请使用此 cmdlet 输出的设备供应商标识符（ID）和产品 ID 作为 **New-MSDSMSSupportedHW** cmdlet 的输入参数。

## 示例

#### 示例 1：获取支持多路径连接的设备
```
PS C:\> Get-MPIOAvailableHW
```

这个示例返回一个列表，其中包含了当前连接到系统的支持多路径功能的设备。

### 示例 2：为某种总线类型获取支持多路径连接的设备
```
PS C:\> Get-MPIOAvailableHW -BusType iSCSI
```

这个示例返回了一个列表，其中包含了当前通过 iSCSI 连接到系统的、支持多路径功能的设备。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlet；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -BusType
指定设备通过哪种总线类型连接到系统。该参数的允许取值为：iSCSI、SAS 和 FibreChannel。

```yaml
Type: BusType[]
Parameter Sets: (All)
Aliases:
Accepted values: FibreChannel, iSCSI, SAS

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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

### -IsMultipathed
指定该设备当前已通过 Microsoft MPIO 启用了多路径功能。

```yaml
Type: Boolean[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IsSPC3Supported
指定设备的支持规范是 T10 SPC3 还是后续版本。

```yaml
Type: Boolean[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ProductId
指定设备的产品ID。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的命令（cmdlet）的最大数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM命令的数量来计算该命令的最佳并发限制。这个并发限制仅适用于当前执行的命令，而不适用于整个会话或整个计算机。

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
指定设备的供应商ID。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[新支持的硬件设备（适用于MSDSMS）](./New-MSDSMSSupportedHW.md)

