---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/new-iscsiservertarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-IscsiServerTarget
---

# 新的iSCSI服务器目标

## 摘要
创建一个新的 iSCSI 目标对象，并指定其名称。

## 语法

```
New-IscsiServerTarget [-TargetName] <String> [-InitiatorIds <InitiatorId[]>] [-ClusterGroupName <String>]
 [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`New-IscsiServerTarget` cmdlet 用于创建一个具有指定名称的 iSCSI 目标对象。创建该目标对象后，可以将该目标分配给某个 iSCSI 启动器，并将虚拟磁盘与该目标关联起来。

## 示例

### 示例 1：在本地服务器上创建一个目标（target）
```
PS C:\> New-IscsiServerTarget -TargetName "T1"
```

这个示例在本地服务器上创建了一个名为T1的目标。

### 示例 2：创建一个目标并分配发起者
```
PS C:\> New-IscsiServerTarget -TargetName "T1" -InitiatorId @("IPAddress:10.10.1.1","IPAddress:10.10.1.2")
```

这个示例创建了一个名为T1的目标，并将其分配给两个发起者，它们的IP地址分别是10.10.1.1和10.10.1.2。

### 示例 3：在集群上创建一个目标
```
PS C:\> New-IscsiServerTarget -TargetName "T1" -ComputerName "fscluster.contoso.com" -ClusterGroupName "Group1"
```

此示例在名为fscluster.contoso.com的集群上，创建了一个目标（target），该目标的名称为T1，并且位于名为Group1的集群组中。

## 参数

### -ClusterGroupName
指定应在此cmdlet运行的资源组或该资源组中的网络名称。

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
如果此cmdlet在远程计算机上运行，则会指定远程计算机的名称或IP地址。

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

### -InitiatorIds
指定要分配iSCSI目标的iSCSI发起方标识符（ID）。该参数的格式为“IdType:Value”。该参数的可接受值包括：DNSName、IPAddress、IPv6Address、IQN或MACAddress。

```yaml
Type: InitiatorId[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定iSCSI目标的名称。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

```cpp
### Microsoft.Iscsi.Target Commands.iSCSIServerTarget
```

## 备注

## 相关链接

[Get-IscsiServerTarget](./Get-IscsiServerTarget.md)

[Remove-IscsiServerTarget](./Remove-IscsiServerTarget.md)

[Set-IscsiServerTarget](./Set-IscsiServerTarget.md)

