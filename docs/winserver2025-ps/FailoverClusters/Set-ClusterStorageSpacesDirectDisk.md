---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterStorageSpacesDirect.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clusterstoragespacesdirectdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterStorageSpacesDirectDisk
---

# 设置集群存储空间（直接使用磁盘）

## 摘要
配置系统以决定S2D是否可以申请或放弃特定的物理磁盘。

## 语法

```
Set-ClusterStorageSpacesDirectDisk [-CanBeClaimed <Boolean>] [-PhysicalDiskIds <String[]>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Set-ClusterStorageSpacesDirectDisk` cmdlet 用于配置系统，以决定是否允许 Storage Spaces Direct (S2D) 占用特定的物理磁盘。被标记为不被 S2D 占用的磁盘将保持原状，可以继续用于其他用途。

为了避免可能出现的清理操作和警告，我们建议您在启用 S2D 之前运行此 cmdlet。或者，您也可以在启用 S2D 之后再运行此 cmdlet。

## 示例

### 示例 1：配置磁盘以防止被占用

```powershell
$parameters = @{
    CimSession = 'K0619-C1.contoso.com'
    CanBeClaimed = $False
    PhysicalDiskIds = '55CD2E404B75A3FC', '50014EE05950DD7C'
}
Set-ClusterStorageSpacesDirectDisk @parameters
```

此命令配置系统，使得ID为 `55CD2E404B75A3FC` 和 `50014EE05950DD7C` 的物理磁盘不能被S2D程序占用。在这个示例中，**CanBeClaimed** 参数被明确设置为 `$False`；如果省略该参数，则表示指定的物理磁盘可以被S2D程序占用。



这个示例使用了“拆分（splatting）”技术，将 `$Parameters` 变量中的参数值传递给命令。有关 [拆分（Splatting）] 的更多信息，请参阅 [这里](/powershell/module/microsoft.powershell.core/about/about_splatting)。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CanBeClaimed

这表示 S2D 可以获取由 **PhysicalDiskIds** 参数指定的物理磁盘。如果您没有指定此参数，该 cmdlet 表示可以获取所指定的物理磁盘。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession

在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

在运行 cmdlet 之前会提示您进行确认。

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

### -PhysicalDiskIds

指定一个包含物理磁盘唯一ID的数组。该cmdlet用于设置S2D是否要占用这些指定的磁盘。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Disable-ClusterStorageSpacesDirect](./ Disable-ClusterStorageSpacesDirect.md)

[Enable-ClusterStorageSpacesDirect](./Enable-ClusterStorageSpacesDirect.md)

[Get-ClusterStorageSpacesDirect](./Get-ClusterStorageSpacesDirect.md)

[修复-ClusterStorageSpacesDirect](./Repair-ClusterStorageSpacesDirect.md)
