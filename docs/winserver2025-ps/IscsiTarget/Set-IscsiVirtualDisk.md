---
description: 使用此主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/set-iscsivirtualdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IscsiVirtualDisk
---

# 设置 IscsiVirtualDisk

## 摘要
修改指定 iSCSI 虚拟磁盘的设置。

## 语法

### DevicePath（默认值）
```
Set-IscsiVirtualDisk [-Path] <String> [-Description <String>] [-PassThru] [-Enable <Boolean>]
 [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

### InputObject
```
Set-IscsiVirtualDisk -InputObject <IscsiVirtualDisk> [-Description <String>] [-PassThru] [-Enable <Boolean>]
 [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Set-IscsiVirtualDisk` cmdlet 用于修改虚拟磁盘的设置；如果指定了 `PassThru` 参数，它还会返回相应的 iSCSI 虚拟磁盘对象。

## 示例

#### 示例 1：更改 VHD 的描述信息
```
PS C:\> Set-IscsiVirtualDisk -Path "E:\Temp\vhd1.vhdx" -Description "disk for data"
```

这个示例将VHD描述更改为“disk”以用于存储数据。

### 示例 2：禁用一个 VHD 文件
```
PS C:\> Set-IscsiVirtualDisk -Path "E:\Temp\vhd1.vhdx" -Enable $False
```

这个示例会禁用路径为 E:\Temp\vhd1.vhdx 的 VHD 文件。

## 参数

### -ComputerName
如果此cmdlet在远程计算机上运行，则会指定远程计算机的名称或IP地址。

如果此cmdlet在集群配置上运行，则会指定集群资源组的网络名称或集群节点的名称。

如果您没有为这个参数指定值，那么该cmdlet会使用本地计算机。

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
指定连接到远程计算机时所需的凭据信息。

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

### -Enable
指定所选的 iSCSI 虚拟磁盘是处于启用状态还是禁用状态。

```yaml
Type: Boolean
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
指定与 iSCSI 虚拟磁盘相关联的虚拟硬盘（VHD）文件的路径。可以使用此参数来过滤 iSCSI 虚拟磁盘对象。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

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

[恢复Iscsi虚拟磁盘](./Restore-IscsiVirtualDisk.md)

