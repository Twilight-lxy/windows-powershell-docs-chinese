---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/get-iscsivirtualdisksnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IscsiVirtualDiskSnapshot
---

# 获取 iScsiVirtualDiskSnapshot

## 摘要
获取快照的属性信息。

## 语法

### 设备（默认值）
```
Get-IscsiVirtualDiskSnapshot [[-OriginalPath] <String>] [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

### SnapshotId
```
Get-IscsiVirtualDiskSnapshot [-SnapshotId <String>] [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

## 描述
`Get-IscsiVirtualDiskSnapshot` cmdlet 可用于获取 iSCSI 虚拟磁盘上快照的属性信息。

## 示例

### 示例 1：获取所有虚拟磁盘快照
```
PS C:\> Get-IscsiVirtualDiskSnapshot
```

这个示例会获取本地服务器上所有的虚拟磁盘快照。

### 示例 2：通过 ID 获取虚拟磁盘快照
```
PS C:\> Get-IscsiVirtualDiskSnapshot -SnapshotId "{E9A5BA03-85B9-40CA-85DF-DC1695690B40}"
```

这个示例从本地服务器中获取所有ID为{E9A5BA03-85B9-40CA-85DF-DC1695690B40}的虚拟磁盘快照。

### 示例 3：获取虚拟磁盘的快照
```
PS C:\> Get-IscsiVirtualDiskSnapshot -Path "E:\temp\test.vhdx"
```

这个示例获取了为虚拟磁盘 E:\temp\test.vhdx 所创建的快照。

## 参数

### -ComputerName
如果此cmdlet在远程计算机上运行，则指定远程计算机的名称或IP地址。

如果此 cmdlet 在集群配置上运行，则会指定集群资源组的网络名称，或者集群节点的名称。

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

### -Credential
指定在连接到远程计算机时所需的身份凭证。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -OriginalPath
指定与快照所属的iSCSI虚拟磁盘相关联的虚拟硬盘（VHD）文件的路径。

```yaml
Type: String
Parameter Sets: Device
Aliases: Path

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SnapshotId
指定快照的标识符（ID）。

```yaml
Type: String
Parameter Sets: SnapshotId
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Iscsi.Target Commands.IscsiVirtualDisk

## 输出

### Microsoft.Iscsi.Target Commands.IscsiVirtualDiskSnapshot

## 备注

## 相关链接

[Dismount-IscsiVirtualDiskSnapshot](./Dismount-IscsiVirtualDiskSnapshot.md)

[Export-IscsiVirtualDiskSnapshot](./Export-IscsiVirtualDiskSnapshot.md)

[Mount-IscsiVirtualDiskSnapshot](./Mount-IscsiVirtualDiskSnapshot.md)

[Remove-IscsiVirtualDiskSnapshot](./Remove-IscsiVirtualDiskSnapshot.md)

[Set-IscsiVirtualDiskSnapshot](./Set-IscsiVirtualDiskSnapshot.md)

