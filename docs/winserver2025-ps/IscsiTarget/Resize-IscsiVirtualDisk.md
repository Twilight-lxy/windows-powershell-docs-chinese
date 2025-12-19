---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/resize-iscsivirtualdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resize-IscsiVirtualDisk
---

# 调整 iSCSI 虚拟磁盘的大小

## 摘要
调整 iSCSI 虚拟磁盘的大小。

## 语法

### 路径（默认值）
```
Resize-IscsiVirtualDisk [-Path] <String> [-SizeBytes] <UInt64> [-PassThru] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

### InputObject
```
Resize-IscsiVirtualDisk -InputObject <IscsiVirtualDisk> [-SizeBytes] <UInt64> [-PassThru]
 [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Resize-IscsiVirtualDisk` cmdlet 可以通过扩展或压缩现有的虚拟磁盘来调整其大小。使用 VHDX 格式的虚拟磁盘在命令执行过程中可以保持在线状态。如果该 cmdlet 对正在使用的虚拟磁盘进行缩放（即调整其大小），并且该虚拟磁盘被映射到了 iSCSI 目标设备上，那么发起方（initiator）仍然可以继续访问该虚拟磁盘。不过，发起方不会自动识别出已经调整大小的虚拟磁盘；要使用扩展后的磁盘容量，必须通过 `Resize-Partition` cmdlet 来修改虚拟磁盘上托管的分区（volume）。

只有当启动器端对应的逻辑单元号（LUN）在该LUN上创建了分区时，此cmdlet才能对磁盘进行压缩；压缩过程会缩减LUN中未分配的部分空间。

## 示例

### 示例 1：调整虚拟磁盘的大小
```
PS C:\> Resize-IscsiVirtualDisk -Path "E:\temp\test06.vhdx" -Size 20GB
```

这个命令会将路径为 E:\temp\test06.vhdx 的虚拟磁盘大小调整到 20GB。

## 参数

### -ComputerName
如果此cmdlet在远程计算机上运行，则会指定该远程计算机的名称或IP地址。

指定集群资源组的网络名称，或者如果此cmdlet在集群配置上运行，则指定集群节点的名称。

如果您没有为这个参数指定值，cmdlet 将使用本地计算机。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定与iSCSI虚拟磁盘关联的虚拟硬盘（VHDX）文件的路径。可以使用此参数来筛选iSCSI虚拟磁盘对象。

```yaml
Type: String
Parameter Sets: Path
Aliases: DevicePath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SizeBytes
指定集群资源组的网络名称，或者如果此cmdlet在集群配置上运行，则指定集群节点的名称。

如果您没有为这个参数指定值，cmdlet 将使用本地计算机。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases: Size

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Iscsi.Target Commands.IscsiVirtualDisk

## 输出

### Microsoft.Iscsi.Target Commands.IscsiVirtualDisk

## 备注

## 相关链接

[Checkpoint-IscsiVirtualDisk](./Checkpoint-IscsiVirtualDisk.md)

[Convert-IscsiVirtualDisk](./Convert-IscsiVirtualDisk.md)

[Get-IscsiVirtualDisk](./Get-IscsiVirtualDisk.md)

[导入-iScsiVirtualDisk](./Import-IscsiVirtualDisk.md)

[New-IscsiVirtualDisk](./New-IscsiVirtualDisk.md)

[Remove-IscsiVirtualDisk](./Remove-IscsiVirtualDisk.md)

[ Restore-IscsiVirtualDisk](./Restore-IscsiVirtualDisk.md)

[Set-IscsiVirtualDisk](./Set-IscsiVirtualDisk.md)

