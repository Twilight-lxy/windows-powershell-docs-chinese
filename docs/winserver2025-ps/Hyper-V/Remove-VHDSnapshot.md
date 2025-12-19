---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/21/2023
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vhdsnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VHDSnapshot
---

# 删除 VHDS 快照

## 摘要
从VHD集合文件中删除一个检查点。

## 语法

### 路径（默认值）

```
Remove-VHDSnapshot [-Path] <String[]> [-PersistReferencePoint] -SnapshotId <Guid[]> [-AsJob]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VHDSnapshot

```
Remove-VHDSnapshot [-PersistReferencePoint] [-VHDSnapshot] <VHDSnapshotInfo[]> [-AsJob]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Remove-VHDSnapshot` cmdlet 用于从虚拟硬盘（VHD）集文件中删除某个虚拟硬盘（VHD）的检查点。

“Checkpoint”取代了之前的术语“snapshot”。

## 示例

#### 示例 1：删除检查点

```powershell
Remove-VHDSnapshot -Path "Data01.vhds" -SnapshotId 6c87351a-a39a-4581-b231-6d693b26485d
```

此命令会从名为`Data01.vhds`的VHD集合文件中删除具有指定ID的检查点。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。

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

在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如，使用[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName

指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全 Qualified 域名来进行识别。默认值是本地计算机。可以使用 `localhost` 或点（`.`）来明确指出本地计算机。

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

### -Credential

指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定一组VHD设置文件的路径数组。此cmdlet会从这些参数指定的文件中删除检查点。如果您指定了一个文件名或相对路径，cmdlet会自动确定相对于当前工作文件夹的完整路径。

```yaml
Type: String[]
Parameter Sets: Path
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PersistReferencePoint

表示此 cmdlet 在删除检查点后仍会保留一个仅用于 RCT（Remote Copy Test）的参考点。

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

### -SnapshotId

指定一个包含唯一VHD检查点ID的数组，该cmdlet会将这些检查点从VHD集合文件中删除。

```yaml
Type: Guid[]
Parameter Sets: Path
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VHDSnapshot

指定一个VHD检查点数组，该cmdlet会从VHD集合文件中删除这些检查点。

```yaml
Type: VHDSnapshotInfo[]
Parameter Sets: VHDSnapshot
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Vhd.PowerShell.VHDSnapshotInfo[]

## 输出

### Microsoft.Vhd.PowerShell.VHDSnapshotInfo[]

## 备注

## 相关链接

[Get-VHDSnapshot](get-vhdsnapshot.md)
