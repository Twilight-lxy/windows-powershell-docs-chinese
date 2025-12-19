---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSDSMSupportedHW.cdxml-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/get-msdsmsupportedhw?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-MSDSMSupportedHW
---

# 获取 Microsoft Distributed Systems Management Service (MSDSS) 支持的硬件

## 摘要
列出 MSDSM 支持的硬件列表中的硬件 ID。

## 语法

```
Get-MSDSMSupportedHW [[-VendorId] <String[]>] [[-ProductId] <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-MSDSMSupportedHW` cmdlet 会列出在微软设备特定模块（Microsoft Device Specific Module，简称 MSDSM）支持的硬件列表中的硬件标识符（IDs）。

当您指定 *VendorID* 和 *ProductID* 参数时，不需要像处理 MPCLAIM.EXE 时那样在参数值末尾添加空格。

## 示例

### 示例 1：获取硬件 ID
```
PS C:\> Get-MSDSMSupportedHW
```

这个示例从 MSDSM 支持的硬件列表中获取所有的硬件 ID。

### 示例 2：根据供应商 ID 获取硬件 ID
```
PS C:\> Get-MSDSMSupportedHW -VendorId "VendorX"
```

这个示例会从MSDSM支持的硬件列表中获取所有厂商ID为“VendorX”的硬件的相关信息（包括这些硬件的ID）。

### 示例 3：获取某个产品ID对应的硬件ID
```
PS C:\> Get-MSDSMSupportedHW -ProductId "ProductY"
```

这个示例从 MSDSM 支持的硬件列表中获取所有产品 ID 为 “ProductY” 的硬件的 ID。

### 示例 4：获取硬件ID、供应商ID和产品ID
```
PS C:\> Get-MSDSMSupportedHW -VendorId "VendorX" -ProductId "ProductY"
```

这个示例从MSDSM支持的硬件列表中获取所有硬件ID，这些硬件的供应商ID为VendorX、产品ID为ProductY。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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
指定该cmdlet用于获取硬件ID的产品ID。

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
该参数用于指定可以同时执行此 cmdlet 的最大操作数量。如果省略了此参数或输入了 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算一个最优的操作限制值。此操作限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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
指定此cmdlet获取硬件ID的供应商ID。

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

[Clear-MSDSMSSupportedHW](./Clear-MSDSMSupportedHW.md)

[新支持的硬件设备（符合 MSDSMS 标准）](./New-MSDSMSSupportedHW.md)

[Remove-MSDSMSSupportedHW](./Remove-MSDSMSSupportedHW.md)

