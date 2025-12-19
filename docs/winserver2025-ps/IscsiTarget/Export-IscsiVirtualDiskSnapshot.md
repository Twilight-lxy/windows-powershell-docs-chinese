---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/export-iscsivirtualdisksnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-IscsiVirtualDiskSnapshot
---

# 导出 IscsiVirtualDiskSnapshot

## 摘要
导出 iSCSI 虚拟磁盘快照。

## 语法

### SnapshotId（默认值）
```
Export-IscsiVirtualDiskSnapshot [-SnapshotId] <String> [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

### InputObject
```
Export-IscsiVirtualDiskSnapshot -InputObject <IscsiVirtualDiskSnapshot> [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Export-IscsiVirtualDiskSnapshot` 这个 cmdlet 用于导出快照。该 cmdlet 会创建一个虚拟磁盘对象，并将快照与该虚拟磁盘对象关联起来。一旦虚拟磁盘对象被添加到目标设备上，发起方（initiator）就可以访问这个快照了。

## 示例

### 示例 1：将快照作为虚拟磁盘公开
```
PS C:\> Export-IscsiVirtualDiskSnapshot -Snapshot "{E9A5BA03-85B9-40CA-85DF-DC1695690B40}"
```

这个示例将一个ID为 {E9A5BA03-85B9-40CA-85DF-DC1695690B40} 的快照作为虚拟磁盘对象进行暴露。要访问该快照，需要将路径为 \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy{41667F16-0FDD-11E1-BA2A-0010184F53D6}\vhd01 的虚拟磁盘分配给某个目标设备。

## 参数

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则会指定远程计算机的名称或 IP 地址。

如果在此cmdlet在集群配置上运行，则会指定集群资源组的网络名称，或者集群节点的名称。

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
指定在连接到远程计算机时所需的凭据信息。

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

### -InputObject
从输入管道中接收一个 iSCSI 虚拟磁盘快照对象。

```yaml
Type: IscsiVirtualDiskSnapshot
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SnapshotId
指定快照的标识符（ID）。

```yaml
Type: String
Parameter Sets: SnapshotId
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Iscsi.Target Commands.VirtualDiskSnapshot

## 输出

### Microsoft.Iscsi.Target Commands.IscsiVirtualDisk

## 备注

## 相关链接

[Dismount-IscsiVirtualDiskSnapshot](./Dismount-IscsiVirtualDiskSnapshot.md)

[Get-IscsiVirtualDiskSnapshot](./Get-IscsiVirtualDiskSnapshot.md)

[Mount-IscsiVirtualDiskSnapshot](./Mount-IscsiVirtualDiskSnapshot.md)

[Remove-IscsiVirtualDiskSnapshot](./Remove-IscsiVirtualDiskSnapshot.md)

[Set-IscsiVirtualDiskSnapshot](./Set-IscsiVirtualDiskSnapshot.md)

