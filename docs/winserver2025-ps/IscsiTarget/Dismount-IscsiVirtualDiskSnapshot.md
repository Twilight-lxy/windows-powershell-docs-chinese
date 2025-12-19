---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/dismount-iscsivirtualdisksnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Dismount-IscsiVirtualDiskSnapshot
---

# 卸载 IscsiVirtualDiskSnapshot

## 摘要
卸载快照。

## 语法

### SnapshotId（默认值）
```
Dismount-IscsiVirtualDiskSnapshot [-SnapshotId] <String> [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

### InputObject
```
Dismount-IscsiVirtualDiskSnapshot -InputObject <IscsiVirtualDiskSnapshot> [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
注意：此cmdlet已被弃用，未来版本中可能会被移除。建议不要使用该cmdlet。

`Dismount-IscsiVirtualDiskSnapshot` 这个 cmdlet 用于卸载快照。卸载后，该快照将无法被访问。此 cmdlet 仅适用于虚拟磁盘 1.0（VHD）格式的快照。

## 示例

### 示例 1：卸载所有快照
```
PS C:\> Get-IscsiVirtualDiskSnapshot | Dismount-IscsiVirtualDiskSnapshot
```

这个示例会获取所有的快照数据，并将它们卸载（即从系统中移除）。

## 参数

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则会指定远程计算机的名称或 IP 地址。

如果此cmdlet在集群配置上运行，则会指定集群资源组的网络名称或集群节点的名称。

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
从输入管道中接收一个iSCSI虚拟磁盘快照对象。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Iscsi.Targetcommands.IscsiVirtualDiskSnapshot

## 输出

### 无

## 备注

## 相关链接

[Export-IscsiVirtualDiskSnapshot](./Export-IscsiVirtualDiskSnapshot.md)

[Get-IscsiVirtualDiskSnapshot](./Get-IscsiVirtualDiskSnapshot.md)

[Mount-IscsiVirtualDiskSnapshot](./Mount-IscsiVirtualDiskSnapshot.md)

[删除Iscsi虚拟磁盘快照](./Remove-IscsiVirtualDiskSnapshot.md)

[Set-IscsiVirtualDiskSnapshot](./Set-IscsiVirtualDiskSnapshot.md)

