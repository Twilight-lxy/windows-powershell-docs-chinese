---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 06/21/2023
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vhdsnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VHDSnapshot
---

# Get-VHDSnapshot

## 摘要
获取VHD集中的检查点信息。

## 语法

```
Get-VHDSnapshot [-Path] <String[]> [-GetParentPaths] [-SnapshotId <Guid[]>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [<CommonParameters>]
```

## 描述

`Get-VHDSnapshot` cmdlet 可以获取虚拟硬盘（VHD）集文件中某个检查点的相关信息。

“Checkpoint”取代了之前的术语“Snapshot”。

## 示例

### 示例 1：获取关于检查点的信息

```powershell
Get-VHDSnapshot -Path "Data01.vhds" -SnapshotId 6c87351a-a39a-4581-b231-6d693b26485d
```

该命令从当前工作文件夹中的名为 `Data01.vhds` 的 VHD 集合文件中，获取具有指定 ID 的检查点的相关信息。

## 参数

### -CimSession

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

指定一个或多个运行此命令的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行识别。默认值为本地计算机。可以使用 `localhost` 或点号（`.`）来明确表示本地计算机。

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

### -GetParentPaths

获取所有依赖于此VHD检查点的文件的路径。

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

### -Path

指定一个包含 VHD 配置文件路径的数组，该 cmdlet 从这个数组中获取检查点信息。如果您指定了一个文件名或相对路径，cmdlet 会自动确定相对于当前工作文件夹的完整路径。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -SnapshotId

指定一个由唯一VHD检查点ID组成的数组；此cmdlet会从VHD集合文件中获取这些ID。

```yaml
Type: Guid[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.Vhd POWERShell.VHDSnapshotInfo

此cmdlet返回一个**VHDSnapshotInfo**对象。

## 备注

## 相关链接

[Remove-VHDSnapshot](remove-vhdsnapshot.md)
