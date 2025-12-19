---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/get-iscsiservertarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IscsiServerTarget
---

# Get-IscsiServerTarget

## 摘要
获取iSCSI目标及其相关属性信息。

## 语法

### 目标（默认值）
```
Get-IscsiServerTarget [-ClusterGroupName <String>] [[-TargetName] <String>] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

### 设备
```
Get-IscsiServerTarget [-ClusterGroupName <String>] [-Path <String>] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

### 发起人
```
Get-IscsiServerTarget [-ClusterGroupName <String>] [-InitiatorId <InitiatorId>] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Get-IscsiServerTarget` cmdlet 用于从本地服务器或指定的计算机获取 iSCSI 目标及其相关属性。

## 示例

### 示例 1：在本地服务器上获取目标数据
```
PS C:\> Get-IscsiServerTarget
```

这个示例用于获取本地服务器上的iSCSI目标资源。

### 示例 2：从远程服务器获取目标信息
```
PS C:\> Get-IscsiServerTarget -ComputerName "fs1.contoso.com"
```

这个示例会获取名为 fs1.contoso.com 的远程服务器上的所有 iSCSI 目标设备。

### 示例 3：获取集群中的目标对象
```
PS C:\> Get-IscsiServerTarget -ComputerName "fscluster.contoso.com" -ClusterGroupName "target1group"
```

这个示例获取了位于名为 fscluster.contoso.com 的集群中的 resourceGroup “target1group” 中的所有 iSCSI 目标。

### 示例 4：通过路径获取目标对象
```
PS C:\> Get-IscsiServerTarget -Path "E:\temp\test.vhdx"
```

这个例子获取了与 VHD 相关联的 iSCSI 目标设备，该设备的路径为 E:\temp\test.vhdx。

### 示例 5：获取分配给发起者的目标
```
PS C:\> Get-IscsiServerTarget -InitiatorId "DNSName:TargetSvr.Contoso.com"
```

这个示例获取了所有被分配给发起者的iSCSI目标对象，这些目标的类型为DNSName，值为TargetSvr.contoso.com。

## 参数

### -ClusterGroupName
指定此cmdlet运行的资源组中对应的资源组或网络的名称。

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

### -InitiatorId
指定 iSCSI 目标所关联的 iSCSI 启动器标识符（IDs）。使用此参数可以过滤出只能被给定 iSCSI 启动器访问的 iSCSI 服务器目标对象。该参数的格式为 `IdType:Value`，允许的值包括：`DNSName`、`IPAddress`、`IPv6Address`、`IQN` 和 `MACAddress`。

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
指定与iSCSI虚拟磁盘关联的虚拟硬盘（VHD）文件的路径。使用此参数可以过滤出与该虚拟磁盘相关联的iSCSI目标对象。

```yaml
Type: String
Parameter Sets: Device
Aliases: DevicePath

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定 iSCSI 目标的名称。使用此参数可以过滤出相应的 iSCSI 目标对象。

```yaml
Type: String
Parameter Sets: Target
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Iscsi.Target Commands.IscsiServerTarget

## 输出

### Microsoft.Iscsi.Target Commands.IscsiServerTarget

## 备注

## 相关链接

[New-IscsiServerTarget](./New-IscsiServerTarget.md)

[Remove-IscsiServerTarget](./Remove-IscsiServerTarget.md)

[Set-IscsiServerTarget](./Set-IscsiServerTarget.md)

