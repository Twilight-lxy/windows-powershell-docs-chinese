---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/remove-iscsivirtualdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IscsiVirtualDisk
---

# 删除 IscsiVirtualDisk

## 摘要
删除虚拟磁盘对象，但不删除对应的虚拟硬盘（VHD）文件。

## 语法

### DevicePath（默认值）
```
Remove-IscsiVirtualDisk [-Path] <String> [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

### InputObject
```
Remove-IscsiVirtualDisk -InputObject <IscsiVirtualDisk> [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

## 描述
`Remove-IscsiVirtualDisk` 这个 cmdlet 用于删除 iSCSI 虚拟磁盘对象，但不会删除相应的虚拟硬盘（VHD）文件。

## 示例

### 示例 1：删除虚拟磁盘
```
PS C:\> Remove-IscsiVirtualDisk -Path "E:\temp\vhd1.vhdx"
```

这个示例会删除一个虚拟磁盘，其路径为 E:\temp\vhd1.vhdx。

## 参数

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则指定该远程计算机的名称或 IP 地址。

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
从输入管道中接收一个 iSCSI 虚拟磁盘对象。

```yaml
Type: IscsiVirtualDisk
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定与 iSCSI 虚拟磁盘关联的 VHD 文件的路径。可以使用此参数来过滤 iSCSI 虚拟磁盘对象。

```yaml
Type: String
Parameter Sets: DevicePath
Aliases: DevicePath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Iscsi.Target Commands.IscsiVirtualDisk

## 输出

### 无

## 备注

## 相关链接

[Checkpoint-IscsiVirtualDisk](./Checkpoint-IscsiVirtualDisk.md)

[Convert-IscsiVirtualDisk](./Convert-IscsiVirtualDisk.md)

[Get-IscsiVirtualDisk](./Get-IscsiVirtualDisk.md)

[导入 Iscsi 虚拟磁盘](./Import-IscsiVirtualDisk.md)

[New-IscsiVirtualDisk](./New-IscsiVirtualDisk.md)

[ Restore-IscsiVirtualDisk](./Restore-IscsiVirtualDisk.md)

[Set-IscsiVirtualDisk](./Set-IscsiVirtualDisk.md)

