---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/import-iscsivirtualdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-IscsiVirtualDisk
---

# 导入 IscsiVirtualDisk

## 摘要
使用现有的虚拟硬盘（VHD）文件来添加一个iSCSI虚拟磁盘对象。

## 语法

```
Import-IscsiVirtualDisk [-Description <String>] [-Path] <String> [-PassThru] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Import-IscsiVirtualDisk` cmdlet 使用现有的虚拟硬盘（VHD）文件来创建一个 iSCSI 虚拟磁盘对象。该 cmdlet 可以导入 VHD 和 VHDX 格式的虚拟磁盘；而 `New-IscsiVirtualDisk` cmdlet 仅能创建 VHDX 格式的虚拟磁盘。

## 示例

### 示例 1：为 VHD 文件创建一个虚拟磁盘
```
PS C:\> Import-IscsiVirtualDisk -Path "E:\Temp\test.vhd" -Description "Migrated from fs1"
```

这个示例为位于 E:\Temp\test.vhd 的现有 VHD 文件创建了一个虚拟磁盘对象，并将该虚拟磁盘对象的描述设置为 “从 fs1 迁移而来”。

## 参数

### -ComputerName
如果此cmdlet在远程计算机上运行，则会指定该远程计算机的名称或IP地址。

如果此cmdlet在集群配置上运行，则指定集群资源组的网络名称，或者集群节点的名称。

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
指定在连接远程计算机时所需的凭据信息。

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
用于指定iSCSI虚拟磁盘的描述信息。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
指定与 iSCSI 虚拟磁盘关联的 VHD 文件的路径。可以使用此参数来过滤 iSCSI 虚拟磁盘对象。

```yaml
Type: String
Parameter Sets: (All)
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

### 无

## 输出

### Microsoft.Iscsi.Target Commands.IscsiVirtualDisk

## 备注

## 相关链接

[Checkpoint-IscsiVirtualDisk](./Checkpoint-IscsiVirtualDisk.md)

[Convert-IscsiVirtualDisk](./Convert-IscsiVirtualDisk.md)

[Get-IscsiVirtualDisk](./Get-IscsiVirtualDisk.md)

[New-IscsiVirtualDisk](./New-IscsiVirtualDisk.md)

[Remove-IscsiVirtualDisk](./Remove-IscsiVirtualDisk.md)

[恢复Iscsi虚拟磁盘](./Restore-IscsiVirtualDisk.md)

[Set-IscsiVirtualDisk](./Set-IscsiVirtualDisk.md)

