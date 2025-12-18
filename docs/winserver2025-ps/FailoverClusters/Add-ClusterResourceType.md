---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clusterresourcetype?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterResourceType
---

# 添加集群资源类型

## 摘要
向故障转移集群添加一种资源类型，并指定与该资源类型相关联的信息（例如要使用的动态链接库（DLL））。

## 语法

```
Add-ClusterResourceType [-Name] <String> [-Dll] <String> [[-DisplayName] <String>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterResourceType` cmdlet 可以将一种资源类型添加到故障转移集群中，并指定与该资源类型相关联的信息，例如要使用的动态链接库（DLL）。

故障转移集群软件为最常见的资源类型提供了相应的资源DLL文件。通过使用微软平台软件开发工具包（Microsoft Platform Software Development Kit，简称SDK）中提供的应用程序编程接口（Application Programming Interface，API），其他供应商也可以为其他类型的资源添加支持功能。

> [!注意] > 如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）的身份验证机制，就无法远程运行此cmdlet。

## 示例

### 示例 1

```powershell
Add-ClusterResourceType -Name ResType3 -InputObject C:\res3.dll
```

这个示例使用位于提供资源DLL文件路径`C:\`下的`res3.dll`，在本地集群上创建了`ResType3`。

### 示例 2

```powershell
Add-ClusterResourceType -Name ResType4 -InputObject C:\res4.dll -DisplayName "Resource Type 4"
```

这个示例使用位于指定资源DLL文件路径（`C:\`）下的`res4.dll`，在本地集群上创建了`ResType4`。该资源类型的显示名称为“Resource Type 4”。

## 参数

### -Cluster

指定用于运行此 cmdlet 的集群的名称。如果该参数的输入值为`.` 或被省略，则 cmdlet 将在本地集群上运行。

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

### -DisplayName

指定资源类型的显示名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Dll

指定资源类型的DLL文件路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定用于注册新资源类型的集群。

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

指定要注册的集群资源类型的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShell.Cluster

## 输出

### MicrosoftFailoverClusters.PowShellClusterResourceType

## 备注

## 相关链接

[Get-ClusterResourceType](./Get-ClusterResourceType.md)

[Remove-ClusterResourceType](./Remove-ClusterResourceType.md)
