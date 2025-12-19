---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/get-iscsivirtualdisk?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IscsiVirtualDisk
---

# Get-IscsiVirtualDisk

## 摘要
获取iSCSI虚拟磁盘及其相关属性。

## 语法

### 设备（默认值）
```
Get-IscsiVirtualDisk [-ClusterGroupName <String>] [[-Path] <String>] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

### 目标
```
Get-IscsiVirtualDisk [-ClusterGroupName <String>] [-TargetName <String>] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

### 发起人
```
Get-IscsiVirtualDisk [-ClusterGroupName <String>] [-InitiatorId <InitiatorId>] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Get-IscsiVirtualDisk` cmdlet 可以获取 iSCSI 虚拟磁盘及其相关属性。

## 示例

### 示例 1：获取本地服务器上的所有虚拟磁盘
```
PS C:\> Get-IscsiVirtualDisk
```

这个示例会获取本地服务器上的所有虚拟磁盘。

### 示例 2：通过路径获取虚拟磁盘
```
PS C:\> Get-IscsiVirtualDisk -Path "E:\temp\test.vhdx"
```

这个示例获取了本地服务器上路径为 E:\temp\test.vhdx 的虚拟磁盘对象。

### 示例 3：在远程服务器上获取一个虚拟磁盘
```
PS C:\> Get-IscsiVirtualDisk -Path "E:\temp\test.vhdx" -ComputerName "fscluster.contoso.com" -ClusterGroupName "target1Group"
```

这个示例从名为 `fscluster.contoso.com` 的集群服务器上的资源组 `target1Group` 中获取路径为 `E:\temp\test.vhdx` 的虚拟磁盘对象。

### 示例 4：获取与目标关联的虚拟磁盘
```
PS C:\> Get-IscsiVirtualDisk -TargetName "TargetOne"
```

这个示例会获取与本地服务器上名为“TargetOne”的目标相关联的所有虚拟磁盘。

### 示例 5：通过初始值获取虚拟磁盘
```
PS C:\> Get-IscsiVirtualDisk -InitiatorId "IpAddress:10.10.1.1"
```

这个示例获取了本地服务器上所有被IP地址为10.10.1.1的发起者使用的虚拟磁盘。

## 参数

### -ClusterGroupName
指定此 cmdlet 运行的资源组中资源组或网络的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
如果此cmdlet在远程计算机上运行，则指定远程计算机的名称或IP地址。

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

### -InitiatorId
指定用于分配 iSCSI 目标的 iSCSI 启动器标识符（ID）。使用此参数可以过滤出仅能被指定的 iSCSI 启动器访问的 iSCSI 虚拟磁盘对象。该参数的格式为：IdType:Value。可接受的参数值包括：DNSName、IPAddress、IPv6Address、IQN 或 MACAddress。

```yaml
Type: InitiatorId
Parameter Sets: Initiator
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定与iSCSI虚拟磁盘关联的虚拟硬盘（VHD）文件的路径。可以使用此参数来过滤iSCSI虚拟磁盘对象。

```yaml
Type: String
Parameter Sets: Device
Aliases: DevicePath

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定 iSCSI 目标的名称。使用此参数可以过滤出被分配给该特定 iSCSI 目标的 iSCSI 虚拟磁盘对象。

```yaml
Type: String
Parameter Sets: Target
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Iscsi.Target Commands.IscsiVirtualDisk

## 备注

## 相关链接

[Checkpoint-IscsiVirtualDisk](./Checkpoint-IscsiVirtualDisk.md)

[Convert-IscsiVirtualDisk](./Convert-IscsiVirtualDisk.md)

[Import-IscsiVirtualDisk](./Import-IscsiVirtualDisk.md)

[New-IscsiVirtualDisk](./New-IscsiVirtualDisk.md)

[Remove-IscsiVirtualDisk](./Remove-IscsiVirtualDisk.md)

[Restore-IscsiVirtualDisk](./Restore-IscsiVirtualDisk.md)

[Set-IscsiVirtualDisk](./Set-IscsiVirtualDisk.md)

