---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/mount-iscsivirtualdisksnapshot?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Mount-IscsiVirtualDiskSnapshot
---

#挂载Iscsi虚拟磁盘快照

## 摘要
在本地创建一个快照。

## 语法

### SnapshotId（默认值）
```
Mount-IscsiVirtualDiskSnapshot [-SnapshotId] <String> [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

### InputObject
```
Mount-IscsiVirtualDiskSnapshot -InputObject <IscsiVirtualDiskSnapshot> [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
注意：此cmdlet已被弃用，可能在未来的版本中被移除。我们建议您不要使用此cmdlet。

`Mount-IscsiVirtualDiskSnapshot` 这个 cmdlet 可以在本地挂载快照。该 cmdlet 仅适用于虚拟磁盘 1.0（VHD）格式的快照。

在本地挂载快照后，该快照会作为磁盘显示在本地计算机上。可以使用 `diskmgmt.msc` 或相应的 PowerShell cmdlet 将该磁盘设置为可访问状态（即使其在线可用）。

## 示例

### 示例 1：使用 ID 挂载快照
```
PS C:\> Mount-IscsiVirtualDiskSnapshot -SnapshotId "{E9A5BA03-85B9-40CA-85DF-DC1695690B40}"
```

这个示例将ID为{E9A5BA03-85B9-40CA-85DF-DC1695690B40}的快照 mounting（挂载）到本地服务器上，备份服务器可以访问该快照来进行数据备份。

### 示例 2：通过名称挂载快照
```
PS C:\> Mount-IscsiVirtualDiskSnapshot -InputObject $VhdSnapshot
```

这个示例将存储在名为 $VhdSnapshot 的变量中的 Snapshot 对象挂载到本地服务器上，备份服务器可以访问该对象以执行备份操作。

## 参数

### -ComputerName
如果此cmdlet在远程计算机上运行，则指定远程计算机的名称或IP地址。

指定集群资源组的网络名称，或者如果该cmdlet在集群配置上运行，则指定集群节点的名称。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Iscsi TargetCommands.IscsiVirtualDiskSnapshot

## 输出

### 无

## 备注

## 相关链接

[Dismount-IscsiVirtualDiskSnapshot](./Dismount-IscsiVirtualDiskSnapshot.md)

[Export-IscsiVirtualDiskSnapshot](./Export-IscsiVirtualDiskSnapshot.md)

[Get-IscsiVirtualDiskSnapshot](./Get-IscsiVirtualDiskSnapshot.md)

[删除Iscsi虚拟磁盘快照](./Delete-IscsiVirtualDiskSnapshot.md)

[Set-IscsiVirtualDiskSnapshot](./Set-IscsiVirtualDiskSnapshot.md)

