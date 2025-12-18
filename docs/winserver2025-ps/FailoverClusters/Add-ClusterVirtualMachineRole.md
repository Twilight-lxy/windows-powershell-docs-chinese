---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustervirtualmachinerole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterVirtualMachineRole
---

# 添加集群虚拟机角色

## 摘要
创建一个集群化的虚拟机，即这种虚拟机在需要时可以切换到故障转移集群中的另一台服务器上继续运行。

## 语法

```
Add-ClusterVirtualMachineRole [-Name <String>] [[-VMName] <String>] [-VirtualMachine <String>]
 [-VMId <Guid>] [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterVirtualMachineRole` cmdlet 用于创建一个集群化的虚拟机，这种虚拟机在需要时可以自动切换到故障转移集群中的另一台服务器上。

通过创建集群化的虚拟机，您可以在一台物理服务器上整合多台服务器，而不会导致该服务器成为单点故障。如果这台服务器或集群节点发生故障，或者需要定期维护，那么另一台节点会通过一种称为“故障转移”（failover）的过程来接管对这些虚拟机的管理。集群化虚拟机的虚拟硬盘（VHD）文件必须存储在该虚拟机所使用的集群磁盘上。

> [!注意] > > - 该 cmdlet 无法在没有服务器计算机上的凭据安全服务提供程序（CredSSP）身份验证的情况下远程运行。  
> > - 该 cmdlet 会在用户的临时文件夹下生成一个 `.TMP` 文件，且此 cmdlet 生成的 `.TMP` 文件数量不能超过 65535 个；否则会收到 “文件已存在” 的异常提示。有关更多信息，请访问：  
> https://techcommunity.microsoft.com/t5/ITOps-Talk-Blog/TQA-Add-ClusterVirtualMachineRole-fails-with-the-error-quot-The/ba-p/713344

## 示例

### 示例 1

```powershell
Add-ClusterVirtualMachineRole -VirtualMachine VM1
```

这个示例将 `VM1` 配置为集群虚拟机，并为其分配一个默认名称。

### 示例 2

```powershell
Add-ClusterVirtualMachineRole -VirtualMachine VM1 -Name "MainServer1"
```

这个示例将 `VM1` 配置为集群虚拟机，并为其分配名称 `MainServer1`。

### 示例 3

```powershell
Get-VM -Name *print* | Add-ClusterVirtualMachineRole
```

这个示例查询与通配符 `*print*` 匹配的虚拟机，并将它们配置为集群式虚拟机。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -InputObject

指定用于创建高可用性虚拟机的集群。

```yaml
Type: PSObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name

指定要创建的高可用虚拟机的名称。

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

### -VMId

指定虚拟机的标识符（ID）。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VMName

指定要实现高可用性的虚拟机的名称。可以使用 **VirtualMachine** 参数或 **VMName** 参数来指定虚拟机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VirtualMachine

指定要实现高可用性的虚拟机的名称。可以使用 **VirtualMachine** 参数或 **VMName** 参数来指定虚拟机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: VM

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FAILoverClusters.PowerShell Cluster

## 输出

### MicrosoftFailoverClusters.PowerShell.ClusterGroup

## 备注

## 相关链接

[Move-ClusterVirtualMachineRole](./Move-ClusterVirtualMachineRole.md)

[更新集群虚拟机配置](./Update-ClusterVirtualMachineConfiguration.md)

[Get-VM](../Hyper-V/Get-VM.md)
