---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/remove-iscsivirtualdisktargetmapping?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IscsiVirtualDiskTargetMapping
---

# 删除 IscsiVirtualDiskTargetMapping

## 摘要
删除指定的 iSCSI 虚拟磁盘与指定的 iSCSI 目标之间的关联（即解除它们之间的绑定）。

## 语法

```
Remove-IscsiVirtualDiskTargetMapping [-TargetName] <String> [-Path] <String> [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Remove-IscsiVirtualDiskTargetMapping` cmdlet 用于移除虚拟磁盘与 iSCSI 目标之间的关联。关联被移除后，该虚拟磁盘将无法再被 iSCSI 发起程序访问。

## 示例

### 示例 1：将虚拟磁盘与目标设备分离
```
PS C:\> Remove-IscsiVirtualDiskTargetMapping -TargetName "TargetOne" -Path "E:\temp\vhd1.vhdx"
```

这个示例将位于 E:\temp\vhd1.vhdx 的虚拟磁盘从名为 “TargetOne” 的目标设备中解绑（即断开两者之间的关联）。在使用该虚拟磁盘之前，需要先使用 `Add-IscsiVirtualDiskTargetMapping` 命令将其重新分配到一个 iSCSI 目标设备上，以便后续的 iSCSI 发起者能够对其进行访问。

## 参数

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

### -Path
指定与 iSCSI 虚拟磁盘关联的虚拟硬盘（VHD）文件的路径。可以使用此参数来过滤 iSCSI 虚拟磁盘对象。

```yaml
Type: String
Parameter Sets: (All)
Aliases: DevicePath

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定 iSCSI 目标的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

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

### 无

## 备注

## 相关链接

[Add-IscsiVirtualDiskTargetMapping](./Add-IscsiVirtualDiskTargetMapping.md)

