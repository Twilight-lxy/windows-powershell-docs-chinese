---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/restore-iscsivirtualdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Restore-IscsiVirtualDisk
---

# 恢复 iSCSI 虚拟磁盘

## 摘要
从快照中恢复虚拟磁盘。

## 语法

### SnapshotId（默认值）
```
Restore-IscsiVirtualDisk [-SnapshotId] <String> [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

### InputObject
```
Restore-IscsiVirtualDisk -InputObject <IscsiVirtualDiskSnapshot> [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Restore-IscsiVirtualDisk` 这个 cmdlet 可以使用 iSCSI 虚拟磁盘的快照来恢复该虚拟磁盘。

## 示例

### 示例 1：通过使用快照的ID来恢复该快照
```
PS C:\> Restore-IscsiVirtualDisk -SnapshotId "{E9A5BA03-85B9-40CA-85DF-DC1695690B40}"
```

这个示例用于恢复ID为{E9A5BA03-85B9-40CA-85DF-DC1695690B40}的快照。

### 示例 2：恢复托管在另一台计算机上的快照
```
PS C:\> Restore-IscsiVirtualDisk -SnapshotId "{E9A5BA03-85B9-40CA-85DF-DC1695690B40}" -ComputerName "fs1.contoso.com"
```

这个示例用于恢复一个ID为{E9A5BA03-85B9-40CA-85DF-DC1695690B40}的快照，该快照存储在名为fs1.contoso.com的计算机上。

### 示例 3：使用输入对象来恢复快照
```
PS C:\> Restore-IscsiVirtualDisk -InputObject $vhd1snapshot
```

这个例子使用了 `Get-IscsiVirtualDiskSnapshot` cmdlet 来获取一个快照，然后将该快照对象赋值给名为 `$vhd1snapshot` 的变量，最后将其传递给另一个 cmdlet 以恢复虚拟磁盘。

## 参数

### -ComputerName
如果此cmdlet在远程计算机上运行，则指定该远程计算机的名称或IP地址。

如果此 cmdlet 在集群配置上运行，则会指定集群资源组的网络名称或集群节点的名称。

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
指定在连接到远程计算机时所需的凭据。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Iscsi.Target Commands.IscsiVirtualDiskSnapshot

## 输出

### 无

## 备注

## 相关链接

[Checkpoint-IscsiVirtualDisk](./Checkpoint-IscsiVirtualDisk.md)

[Convert-IscsiVirtualDisk](./Convert-IscsiVirtualDisk.md)

[Get-IscsiVirtualDisk](./Get-IscsiVirtualDisk.md)

[Get-IscsiVirtualDiskSnapshot](./Get-IscsiVirtualDiskSnapshot.md)

[Import-IscsiVirtualDisk](./Import-IscsiVirtualDisk.md)

[New-IscsiVirtualDisk](./New-IscsiVirtualDisk.md)

[Remove-IscsiVirtualDisk](./Remove-IscsiVirtualDisk.md)

[Set-IscsiVirtualDisk](./Set-IscsiVirtualDisk.md)

