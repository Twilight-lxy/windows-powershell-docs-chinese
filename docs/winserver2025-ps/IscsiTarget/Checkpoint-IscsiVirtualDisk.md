---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/checkpoint-iscsivirtualdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Checkpoint-IscsiVirtualDisk
---

# 检查点：IscsiVirtualDisk

## 摘要
创建一个虚拟磁盘快照。

## 语法

```
Checkpoint-IscsiVirtualDisk [-Description <String>] [-OriginalPath] <String> [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Checkpoint-IscsiVirtualDisk` 这个 cmdlet 用于创建快照。

## 示例

### 示例 1：创建 VHD 的快照
```
PS C:\> Checkpoint-IscsiVirtualDisk -OriginalPath "D:\VHDs\DB.vhdx"
```

这个示例创建了一个名为 D:\VHDs\db.vhdx 的 VHD 文件的快照。

### 示例 2：为 VHD 创建带有描述的快照
```
PS C:\> Checkpoint-IscsiVirtualDisk -OriginalPath "D:\VHDs\DB.vhdx" -Description "Before database merge" -ComputerName "fssvr.contoso.com"
```

这个示例创建了一个名为 D:\VHDs\db.vhdx 的 VHD 快照，并为该快照提供了描述。此操作是在一台名为 fssvr.contoso.com 的远程计算机上进行的。

## 参数

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则指定远程计算机的名称或 IP 地址。

如果此 cmdlet 在集群配置上运行，则指定集群资源组的网络名称或集群节点的名称。

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

### -Description
用于指定iSCSI虚拟磁盘快照的描述信息。

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

### -OriginalPath
指定与快照所属的iSCSI虚拟磁盘相关联的虚拟硬盘（VHD）文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Path

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Iscsi.Target Commands.IscsiVirtualDiskSnapshot

## 备注

## 相关链接

[Convert-IscsiVirtualDisk](./Convert-IscsiVirtualDisk.md)

[Get-IscsiVirtualDisk](./Get-IscsiVirtualDisk.md)

[Import-IscsiVirtualDisk](./Import-IscsiVirtualDisk.md)

[New-IscsiVirtualDisk](./New-IscsiVirtualDisk.md)

[Remove-IscsiVirtualDisk](./Remove-IscsiVirtualDisk.md)

[恢复Iscsi虚拟磁盘](./Restore-IscsiVirtualDisk.md)

[Set-IscsiVirtualDisk](./Set-IscsiVirtualDisk.md)

